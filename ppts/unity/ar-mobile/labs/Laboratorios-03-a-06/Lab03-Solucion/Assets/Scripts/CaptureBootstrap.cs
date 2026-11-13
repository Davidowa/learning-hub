using System.Collections;
using System.Collections.Generic;
using System.Linq;
using Unity.XR.CoreUtils;
using UnityEngine;
using UnityEngine.InputSystem;
using UnityEngine.InputSystem.XR;
using UnityEngine.XR.ARFoundation;
using UnityEngine.XR.ARSubsystems;
#if UNITY_ANDROID
using UnityEngine.Android;
#endif

namespace MarkerCapture
{
    public sealed class CaptureBootstrap : MonoBehaviour
    {
        public LabSceneReferences scene;
        public LabContent content;
        public LabUI ui;
        [SerializeField] bool simulateInEditor = true;
        Camera viewCamera;
        CaptureRegistry registry;
        CaptureTarget simulatedTarget;
        TrackedCaptureManager tracked;
        bool simulatedTracking = true;
        bool ready;
        string error;
        float nextLaunch;
        string launchNotice;
        float launchNoticeUntil;

        IEnumerable<CaptureTarget> Targets => simulatedTarget != null
            ? new[] { simulatedTarget }
            : tracked != null ? tracked.Targets : Enumerable.Empty<CaptureTarget>();

        IEnumerator Start()
        {
            registry = new CaptureRegistry(new PlayerPrefsCaptureStore());
            if(scene==null||content==null||ui==null)
            { Debug.LogError("Completa Scene, Content y UI en el controlador Laboratorio.");yield break; }

            Screen.sleepTimeout = SleepTimeout.NeverSleep;
            RenderSettings.ambientLight = new Color(0.65f, 0.65f, 0.65f);

            if (Application.isEditor && simulateInEditor)
            {
                StartSimulation();
                ready = true;
                yield break;
            }

#if UNITY_ANDROID && !UNITY_EDITOR
            if (!Permission.HasUserAuthorizedPermission(Permission.Camera))
            {
                bool answered = false;
                var callbacks = new PermissionCallbacks();
                callbacks.PermissionGranted += _ => answered = true;
                callbacks.PermissionDenied += _ => answered = true;
                Permission.RequestUserPermission(Permission.Camera, callbacks);
                yield return new WaitUntil(() => answered);
                if (!Permission.HasUserAuthorizedPermission(Permission.Camera))
                {
                    error = "Activa el permiso de cámara en los ajustes de Android y vuelve a abrir la app.";
                    yield break;
                }
            }
#endif
            StartAR();
        }



        void StartSimulation()
        {
            viewCamera=scene.Activate(true);
            simulatedTarget=Instantiate(content.captureTarget,scene.simulatedMarker).GetComponent<CaptureTarget>();
            simulatedTarget.Initialize(registry,"editor-simulation");simulatedTarget.SetTracking(true);
        }

        void StartAR()
        {
            if(scene.trackedImages==null||scene.trackedImages.referenceLibrary==null)
            { error="Asigna MarkerLibrary en AR Tracked Image Manager.";return; }
            viewCamera=scene.Activate(false);
            tracked=scene.trackedImages.gameObject.GetComponent<TrackedCaptureManager>();
            tracked.Initialize(scene.trackedImages,registry,content.captureTarget);
            ready=true;
        }

        bool CanLaunch => ready && viewCamera != null && Time.time >= nextLaunch
            && Targets.Any(t => t != null && t.IsTracking && !t.IsCaptured);

        void Launch()
        {
            if (!CanLaunch) return;
            CaptureProjectile.Launch(viewCamera,content.projectile);
            nextLaunch = Time.time + 0.4f;
            launchNotice = "Esfera azul lanzada. Mantén la mira sobre el cubo.";
            launchNoticeUntil = Time.unscaledTime + 1.5f;
        }

        void Update()
        {
            if(Keyboard.current!=null&&Keyboard.current.spaceKey.wasPressedThisFrame)Launch();
        }
        public void LaunchButton()=>Launch();
        public void ResetButton()=>ResetVisibleCapture();
        public void TrackingButton()
        {
            if(simulatedTarget==null)return;
            simulatedTracking=!simulatedTracking;simulatedTarget.SetTracking(simulatedTracking);
        }

        static Rect LaunchRect(float width, float height, bool compact) => compact
            ? new Rect(16, height - 66, (width - 48) / 2, 50)
            : new Rect(16, height - 150, width - 32, 58);

        static Rect ResetRect(float width, float height, bool compact) => compact
            ? new Rect(width / 2 + 8, height - 66, (width - 48) / 2, 50)
            : new Rect(16, height - 78, width - 32, 54);

        void ResetVisibleCapture()
        {
            if (!ready) return;
            foreach (var ball in FindObjectsByType<CaptureProjectile>(FindObjectsSortMode.None))
                Destroy(ball.gameObject);
            foreach (var target in Targets.Where(t => t != null && t.IsTracking)) target.ResetCapture();
            launchNoticeUntil = 0;
        }

        void LateUpdate()
        {
            if(ui==null)return;
            var visible=Targets.FirstOrDefault(t=>t!=null&&t.IsTracking);
            string message=error??(!ready?"Preparando cámara...":visible==null?"Busca el marcador con la cámara.":visible.IsCaptured?"Capturado: esfera verde.":Time.unscaledTime<launchNoticeUntil?launchNotice:"Centra la mira sobre el objetivo y pulsa Lanzar.");
            ui.Message(message);ui.State(ui.primary,"Lanzar",CanLaunch);
            ui.State(ui.secondary,"Reiniciar captura",ready&&visible!=null);
            if(ui.simulation!=null)ui.simulation.gameObject.SetActive(simulatedTarget!=null);
            ui.State(ui.simulation,simulatedTracking?"Simular pérdida":"Volver a detectar");
        }
    }
}
