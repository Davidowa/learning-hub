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

        void Start()
        {
            var material=Resources.Load<Material>("CubeMaterial");
            if(material==null){status="Ejecuta Tools > AR ArUco > Preparar proyecto.";return;}
            simulated=Application.isEditor&&simulateInEditor;
            Screen.sleepTimeout=SleepTimeout.NeverSleep;
            RenderSettings.ambientLight=new Color(.65f,.65f,.65f);
            var light=new GameObject("Luz",typeof(Light)).GetComponent<Light>();
            light.type=LightType.Directional;light.transform.rotation=Quaternion.Euler(40,-30,0);
            cube=GameObject.CreatePrimitive(PrimitiveType.Cube);cube.name="Cubo sobre ArUco23";
            cube.GetComponent<Renderer>().sharedMaterial=material;cube.GetComponent<Collider>().enabled=false;
            cube.transform.localScale=Vector3.one*.05f;cube.SetActive(false);
            if(simulated)StartSimulation();else StartAR();
        }

        Camera MakeCamera(Transform parent)
        {
            var go=new GameObject("AR Camera",typeof(Camera),typeof(AudioListener));
            if(parent!=null)go.transform.SetParent(parent,false);
            go.tag="MainCamera";var camera=go.GetComponent<Camera>();
            camera.nearClipPlane=.01f;camera.farClipPlane=20f;
            camera.clearFlags=CameraClearFlags.SolidColor;camera.backgroundColor=Color.gray;
            return camera;
        }

        void StartAR()
        {
            new GameObject("AR Session",typeof(ARSession),typeof(ARInputManager));
            var root=new GameObject("XR Origin");root.SetActive(false);
            var origin=root.AddComponent<XROrigin>();var offset=new GameObject("Camera Offset");
            offset.transform.SetParent(root.transform,false);viewCamera=MakeCamera(offset.transform);
            var manager=viewCamera.gameObject.AddComponent<ARCameraManager>();
            viewCamera.gameObject.AddComponent<ARCameraBackground>();
            var driver=viewCamera.gameObject.AddComponent<TrackedPoseDriver>();
            var position=new InputAction("Position",InputActionType.Value,"<XRHMD>/centerEyePosition",expectedControlType:"Vector3");
            position.AddBinding("<HandheldARInputDevice>/devicePosition");
            var rotation=new InputAction("Rotation",InputActionType.Value,"<XRHMD>/centerEyeRotation",expectedControlType:"Quaternion");
            rotation.AddBinding("<HandheldARInputDevice>/deviceRotation");
            var tracking=new InputAction("Tracking State",InputActionType.Value,"<XRHMD>/trackingState",expectedControlType:"Integer");
            tracking.AddBinding("<HandheldARInputDevice>/trackingState");
            driver.positionInput=new InputActionProperty(position);driver.rotationInput=new InputActionProperty(rotation);
            driver.trackingStateInput=new InputActionProperty(tracking);
            origin.Camera=viewCamera;origin.CameraFloorOffsetObject=offset;origin.CameraYOffset=0;
            reader=viewCamera.gameObject.AddComponent<CpuGrayCamera>();reader.Initialize(manager);reader.FrameReady+=Process;
            root.SetActive(true);
        }

        void StartSimulation()
        {
            viewCamera=MakeCamera(null);viewCamera.fieldOfView=60;viewCamera.aspect=4f/3f;
            simulationTexture=Resources.Load<Texture2D>("SimulationFrame");
            if(simulationTexture==null){status="Falta SimulationFrame.png.";return;}
            simulationPixels=CpuGrayCamera.FromTexture(simulationTexture);
            float focal=480f/(2*Mathf.Tan(30*Mathf.Deg2Rad));float depth=focal*.1f/220f;
            var card=GameObject.CreatePrimitive(PrimitiveType.Quad);card.name="Imagen de prueba estática";
            card.transform.position=new Vector3(0,0,depth);
            float height=2*depth*Mathf.Tan(30*Mathf.Deg2Rad);
            card.transform.localScale=new Vector3(height*4/3,height,1);
            card.GetComponent<Collider>().enabled=false;
            var mat=new Material(Shader.Find("Universal Render Pipeline/Unlit"));mat.mainTexture=simulationTexture;
            card.GetComponent<Renderer>().material=mat;
        }

        void Update()
        {
            if(cube==null)return;
            if(simulated&&simulationPixels!=null&&Time.unscaledTime>=nextSimulation)
            {
                nextSimulation=Time.unscaledTime+.2f;
                if(!lostSimulation)Process(new GrayCameraFrame {Pixels=simulationPixels,Width=640,Height=480,HasDisplay=true,Display=Matrix4x4.identity});
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
        void OnGUI()
        {
            float scale=Mathf.Clamp(Screen.width/650f,.8f,3f);GUI.matrix=Matrix4x4.Scale(new Vector3(scale,scale,1));
            float width=Screen.width/scale;GUI.skin.box.fontSize=16;GUI.skin.box.wordWrap=true;GUI.skin.button.fontSize=17;
            string source=simulated?"Simulación con imagen estática; no cámara real.":reader!=null?reader.Status:"";
            GUI.Box(new Rect(12,12,width-24,96),status+"\n"+source);
            if(GUI.Button(new Rect(16,118,width-32,42),showCorners?"Ocultar puntos de diagnóstico":"Mostrar puntos de diagnóstico"))showCorners=!showCorners;
            if(simulated)
            {
                if(GUI.Button(new Rect(16,170,width-32,42),lostSimulation?"Volver a detectar":"Simular pérdida"))lostSimulation=!lostSimulation;
            }
            else if(GUI.Button(new Rect(16,170,width-32,42),"Invertir Y de la imagen CPU: "+(flipCpuImageY?"sí":"no")))
            {flipCpuImageY=!flipCpuImageY;lastSeen=-100;}
            if(showCorners&&viewportCorners!=null&&Time.unscaledTime-lastDetection<.5f)
            {
                GUI.color=Color.green;
                foreach(var p in viewportCorners)
                {
                    var point=viewCamera.ViewportToScreenPoint(new Vector3((float)p.X,(float)p.Y,0));
                    GUI.DrawTexture(new Rect(point.x/scale-5,(Screen.height-point.y)/scale-5,10,10),Texture2D.whiteTexture);
                }
                GUI.color=Color.white;
            }
        }
    }
}
