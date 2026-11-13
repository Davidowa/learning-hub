using System.Collections;
#if UNITY_ANDROID
using UnityEngine.Android;
#endif
using UnityEngine;
using UnityEngine.InputSystem;
using UnityEngine.InputSystem.XR;
using UnityEngine.XR.ARFoundation;
using Unity.XR.CoreUtils;
using CodeMarkerExamples;

namespace ArucoExample
{
    public sealed class ArucoBootstrap : MonoBehaviour
    {
        public LabSceneReferences scene;
        public LabContent content;
        public LabUI ui;
        [SerializeField] bool simulateInEditor=true;
        [SerializeField] float markerSideMeters=.10f;
        [SerializeField] bool flipCpuImageY;
        readonly Aruco23Detector detector=new();
        Camera viewCamera;
        CpuGrayCamera reader;
        GameObject cube;
        Texture2D simulationTexture;
        byte[] simulationPixels;
        bool simulated,lostSimulation,showCorners=true,hasTarget;
        float nextSimulation,lastSeen=-100,lastDetection=-100;
        Vector3 targetPosition;
        Quaternion targetRotation;
        P2[] viewportCorners;
        string status="Preparando cámara...";

        IEnumerator Start()
        {
            if(scene==null||content==null||ui==null){Debug.LogError("Completa Scene, Content y UI en Laboratorio.");yield break;}
            simulated=Application.isEditor&&simulateInEditor;
            Screen.sleepTimeout=SleepTimeout.NeverSleep;
            RenderSettings.ambientLight=new Color(.65f,.65f,.65f);
            cube=Instantiate(content.arucoVisual);cube.name="Contenido sobre ArUco23";
            
            cube.transform.localScale=Vector3.one*.05f;cube.SetActive(false);
            if(simulated) { StartSimulation(); yield break; }
#if UNITY_ANDROID && !UNITY_EDITOR
            if(!Permission.HasUserAuthorizedPermission(Permission.Camera))
            {
                bool answered=false;
                var callbacks=new PermissionCallbacks();
                callbacks.PermissionGranted += _ => answered=true;
                callbacks.PermissionDenied += _ => answered=true;
                Permission.RequestUserPermission(Permission.Camera,callbacks);
                yield return new WaitUntil(()=>answered);
                if(!Permission.HasUserAuthorizedPermission(Permission.Camera))
                { status="Activa el permiso de cámara en Android y vuelve a abrir la app."; yield break; }
            }
#endif
            StartAR();
        }



        void StartAR()
        {
            viewCamera=scene.Activate(false);
            reader=viewCamera.GetComponent<CpuGrayCamera>();reader.Initialize(viewCamera.GetComponent<ARCameraManager>());reader.FrameReady+=Process;
        }

        void StartSimulation()
        {
            viewCamera=scene.Activate(true);viewCamera.aspect=4f/3f;
            simulationTexture=Resources.Load<Texture2D>("SimulationFrame");
            if(simulationTexture==null){status="Falta SimulationFrame.png.";return;}
            simulationPixels=CpuGrayCamera.FromTexture(simulationTexture);
        }

        void Update()
        {
            if(cube==null)return;
            if(simulated&&simulationPixels!=null&&Time.unscaledTime>=nextSimulation)
            {
                nextSimulation=Time.unscaledTime+.2f;
                if(!lostSimulation)Process(new GrayCameraFrame {Pixels=simulationPixels,Width=simulationTexture.width,Height=simulationTexture.height,HasDisplay=true,Display=Matrix4x4.identity});
                else {status="Simulación: marcador oculto.";viewportCorners=null;}
            }
            bool visible=hasTarget&&Time.unscaledTime-lastSeen<.35f&&(simulated||ARSession.state==ARSessionState.SessionTracking);
            cube.SetActive(visible);
            if(visible)
            {
                float blend=1-Mathf.Exp(-22*Time.unscaledDeltaTime);
                cube.transform.position=Vector3.Lerp(cube.transform.position,targetPosition,blend);
                cube.transform.rotation=Quaternion.Slerp(cube.transform.rotation,targetRotation,blend);
            }
        }

        void Process(GrayCameraFrame frame)
        {
            var found=detector.Detect(frame.Pixels,frame.Width,frame.Height);
            if(found==null){status="No se reconoce DICT_4X4_50, ID 23. Muestra el borde completo.";viewportCorners=null;return;}
            if(!frame.HasDisplay){status="ID 23 detectado. Falta la matriz de visualización del proveedor.";return;}
            if(!simulated&&ARSession.state!=ARSessionState.SessionTracking){status="ID 23 detectado; rastreo AR limitado.";return;}
            var normalized=new P2[4];var viewport=new P2[4];
            for(int i=0;i<4;i++)
            {
                double u=found.Corners[i].X/(frame.Width-1),v=found.Corners[i].Y/(frame.Height-1);
                if(simulated||flipCpuImageY)v=1-v;
                var m=frame.Display;
                if(!UvTransform.TryInverse(m.m00,m.m10,m.m20,m.m01,m.m11,m.m21,new P2(u,v),out viewport[i]))
                {status="No se pudo convertir la imagen CPU al visor.";return;}
                var ray=viewCamera.ViewportPointToRay(new Vector3((float)viewport[i].X,(float)viewport[i].Y,0));
                var direction=viewCamera.transform.InverseTransformDirection(ray.direction);
                if(direction.z<=.01f)return;
                normalized[i]=new P2(direction.x/direction.z,-direction.y/direction.z);
            }
            viewportCorners=viewport;lastDetection=Time.unscaledTime;
            if(!PlanarPose.TrySolve(normalized,markerSideMeters,out var pose))
            {status="ID 23 detectado, pero la pose no es válida. Acércate y reduce la inclinación.";return;}
            var outward=P3.Cross(pose.Right,pose.Down)*-1;
            var forward=pose.Down*-1;
            var rotation=Quaternion.LookRotation(ToUnity(forward),ToUnity(outward));
            targetRotation=viewCamera.transform.rotation*rotation;
            targetPosition=viewCamera.transform.TransformPoint(ToUnity(pose.Translation))+targetRotation*Vector3.up*.025f;
            if(!hasTarget||Time.unscaledTime-lastSeen>=.35f)cube.transform.SetPositionAndRotation(targetPosition,targetRotation);
            hasTarget=true;lastSeen=Time.unscaledTime;
            status="ID 23 reconocido • lado "+(markerSideMeters*100).ToString("F1")+" cm • distancia "+pose.Translation.Z.ToString("F2")+" m";
        }

        static Vector3 ToUnity(P3 p)=>new((float)p.X,(float)-p.Y,(float)p.Z);
        void OnDestroy(){if(reader!=null)reader.FrameReady-=Process;}
        public void CornersButton()=>showCorners=!showCorners;
        public void FlipButton(){flipCpuImageY=!flipCpuImageY;lastSeen=-100;}
        public void TrackingButton()=>lostSimulation=!lostSimulation;
        void LateUpdate()
        {
            if(ui==null)return;
            ui.Message(status+"\n"+(simulated?"Simulación con imagen estática":reader!=null?reader.Status:""));
            ui.State(ui.primary,showCorners?"Ocultar puntos":"Mostrar puntos");
            ui.State(ui.secondary,"Invertir Y: "+(flipCpuImageY?"sí":"no"),!simulated);
            if(ui.simulation!=null)ui.simulation.gameObject.SetActive(simulated);
            ui.State(ui.simulation,lostSimulation?"Volver a detectar":"Simular pérdida");
            Vector2[] points=null;
            if(showCorners&&viewportCorners!=null&&Time.unscaledTime-lastDetection<.5f)
            {points=new Vector2[4];for(int i=0;i<4;i++)points[i]=new Vector2((float)viewportCorners[i].X,(float)viewportCorners[i].Y);}
            ui.Corners(points);
        }
    }
}
