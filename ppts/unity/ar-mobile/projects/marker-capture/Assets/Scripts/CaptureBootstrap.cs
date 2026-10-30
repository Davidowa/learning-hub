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
        [SerializeField] bool simulateInEditor = true;
        Camera viewCamera;
        CaptureRegistry registry;
        CaptureTarget simulatedTarget;
        TrackedCaptureManager tracked;
        bool simulatedTracking = true;
        bool ready;
        string error;
        float nextLaunch;

        IEnumerable<CaptureTarget> Targets => simulatedTarget != null
            ? new[] { simulatedTarget }
            : tracked != null ? tracked.Targets : Enumerable.Empty<CaptureTarget>();

        IEnumerator Start()
        {
            registry = new CaptureRegistry(new PlayerPrefsCaptureStore());
            if (Resources.Load<Material>("CubeMaterial") == null)
            {
                error = "Ejecuta Tools > AR Capture > Preparar proyecto antes de Play.";
                yield break;
            }

            Screen.sleepTimeout = SleepTimeout.NeverSleep;
            RenderSettings.ambientLight = new Color(0.65f, 0.65f, 0.65f);
            var light = new GameObject("Luz de las figuras").AddComponent<Light>();
            light.type = LightType.Directional;
            light.intensity = 0.9f;
            light.transform.rotation = Quaternion.Euler(45f, -35f, 0f);

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

        Camera MakeCamera(Transform parent)
        {
            var go = new GameObject("AR Camera", typeof(Camera), typeof(AudioListener));
            if (parent != null) go.transform.SetParent(parent, false);
            go.tag = "MainCamera";
            var camera = go.GetComponent<Camera>();
            camera.clearFlags = CameraClearFlags.SolidColor;
            camera.backgroundColor = new Color(0.07f, 0.09f, 0.12f);
            camera.nearClipPlane = 0.01f;
            camera.farClipPlane = 20f;
            return camera;
        }

        void StartSimulation()
        {
            viewCamera = MakeCamera(null);
            var target = new GameObject("Marcador simulado");
            target.transform.position = new Vector3(0f, 0f, 0.65f);
            target.transform.rotation = Quaternion.Euler(-90f, 0f, 0f);
            simulatedTarget = target.AddComponent<CaptureTarget>();
            // A separate key keeps desktop practice captures out of the AR state.
            simulatedTarget.Initialize(registry, "editor-simulation");
            simulatedTarget.SetTracking(true);

            var card = GameObject.CreatePrimitive(PrimitiveType.Quad);
            card.name = "Imagen de prueba simulada";
            card.transform.SetParent(target.transform, false);
            card.transform.localRotation = Quaternion.Euler(90f, 0f, 0f);
            card.transform.localScale = Vector3.one * 0.16f;
            card.GetComponent<Collider>().enabled = false;
            card.GetComponent<Renderer>().sharedMaterial = Resources.Load<Material>("MarkerMaterial");
        }

        void StartAR()
        {
            var library = Resources.Load<XRReferenceImageLibrary>("MarkerLibrary");
            if (library == null || library.count == 0)
            {
                error = "Falta MarkerLibrary. Ejecuta Tools > AR Capture > Preparar proyecto.";
                return;
            }

            new GameObject("AR Session", typeof(ARSession), typeof(ARInputManager));
            var root = new GameObject("XR Origin");
            root.SetActive(false);
            var origin = root.AddComponent<XROrigin>();
            var offset = new GameObject("Camera Offset");
            offset.transform.SetParent(root.transform, false);
            viewCamera = MakeCamera(offset.transform);
            viewCamera.gameObject.AddComponent<ARCameraManager>();
            viewCamera.gameObject.AddComponent<ARCameraBackground>();

            var pose = viewCamera.gameObject.AddComponent<TrackedPoseDriver>();
            var position = new InputAction("Position", binding: "<XRHMD>/centerEyePosition",
                expectedControlType: "Vector3");
            position.AddBinding("<HandheldARInputDevice>/devicePosition");
            var rotation = new InputAction("Rotation", binding: "<XRHMD>/centerEyeRotation",
                expectedControlType: "Quaternion");
            rotation.AddBinding("<HandheldARInputDevice>/deviceRotation");
            pose.positionInput = new InputActionProperty(position);
            pose.rotationInput = new InputActionProperty(rotation);
            origin.Camera = viewCamera;
            origin.CameraFloorOffsetObject = offset;
            origin.CameraYOffset = 0f;

            var manager = root.AddComponent<ARTrackedImageManager>();
            manager.referenceLibrary = library;
            manager.requestedMaxNumberOfMovingImages = 1;
            tracked = root.AddComponent<TrackedCaptureManager>();
            tracked.Initialize(manager, registry);
            root.SetActive(true);
            ready = true;
        }

        bool CanLaunch => ready && viewCamera != null && Time.time >= nextLaunch
            && Targets.Any(t => t != null && t.IsTracking && !t.IsCaptured);

        void Launch()
        {
            if (!CanLaunch) return;
            CaptureProjectile.Launch(viewCamera);
            nextLaunch = Time.time + 0.4f;
        }

        void Update()
        {
            if (Keyboard.current != null && Keyboard.current.spaceKey.wasPressedThisFrame) Launch();
        }

        void OnGUI()
        {
            float scale = Mathf.Clamp(Screen.width / 540f, 0.8f, 3f);
            GUI.matrix = Matrix4x4.Scale(new Vector3(scale, scale, 1f));
            float width = Screen.width / scale;
            float height = Screen.height / scale;
            bool compact = height < 480f;
            GUI.skin.label.fontSize = 18;
            GUI.skin.button.fontSize = 20;
            GUI.skin.box.fontSize = 18;
            GUI.skin.box.wordWrap = true;
            GUI.skin.box.alignment = TextAnchor.MiddleCenter;
            string status = error;
            if (status == null && !ready) status = "Preparando cámara...";
            if (status == null && simulatedTarget == null && ARSession.state == ARSessionState.Unsupported)
                status = "Este celular no admite ARCore.";
            if (status == null)
            {
                var visible = Targets.FirstOrDefault(t => t != null && t.IsTracking);
                status = visible == null ? "Busca el marcador con la cámara."
                    : visible.IsCaptured ? "Capturado: el marcador conserva la esfera verde."
                    : "Apunta al cubo con la mira y presiona Lanzar.";
            }
            GUI.Box(new Rect(12, 12, width - 24, compact ? 60 : 90), status);
            GUI.skin.label.alignment = TextAnchor.MiddleCenter;
            GUI.Label(new Rect(width / 2f - 20f, height / 2f - 20f, 40, 40), "+");

            GUI.enabled = CanLaunch;
            var launchRect = compact
                ? new Rect(16, height - 66, (width - 48) / 2, 50)
                : new Rect(16, height - 150, width - 32, 58);
            if (GUI.Button(launchRect, "Lanzar")) Launch();
            GUI.enabled = ready && Targets.Any(t => t != null && t.IsTracking);
            var resetRect = compact
                ? new Rect(width / 2 + 8, height - 66, (width - 48) / 2, 50)
                : new Rect(16, height - 78, width - 32, 54);
            if (GUI.Button(resetRect, compact ? "Reiniciar" : "Reiniciar captura visible"))
            {
                foreach (var ball in FindObjectsByType<CaptureProjectile>(FindObjectsSortMode.None))
                    Destroy(ball.gameObject);
                foreach (var target in Targets.Where(t => t != null && t.IsTracking)) target.ResetCapture();
            }
            GUI.enabled = true;
            if (simulatedTarget != null && GUI.Button(new Rect(16, compact ? 78 : 112, width - 32, compact ? 32 : 45),
                simulatedTracking ? "Simular pérdida de rastreo" : "Volver a detectar marcador"))
            {
                simulatedTracking = !simulatedTracking;
                simulatedTarget.SetTracking(simulatedTracking);
            }
        }
    }
}
