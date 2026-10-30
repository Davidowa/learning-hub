using System;
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

namespace QrPlace
{
    public sealed class QrPlacementBootstrap : MonoBehaviour
    {
        public const int SurfaceLayer = 8;
        public const int ObjectLayer = 9;
        const float ViewDistance = 1000f;
        [SerializeField] bool simulateInEditor = true;
        readonly PlacementRegistry inventory = new();
        readonly Dictionary<int, PlacedShape> placed = new();
        readonly List<ARRaycastHit> planeHits = new();
        readonly List<Renderer> simulatedSurfaces = new();
        Camera viewCamera;
        ARPlaneManager planes;
        ARRaycastManager raycasts;
        ARAnchorManager anchors;
        GameObject preview;
        bool simulated;
        bool qrReady;
        QrScanner scanner;
        bool ready;
        bool placing;
        bool showSurfaces = true;
        string error;
        string notice;
        float noticeUntil;

        IEnumerator Start()
        {
            if (Resources.Load<Material>("CubeMaterial") == null)
            {
                error = "Ejecuta Tools > AR QR > Preparar proyecto antes de Play.";
                yield break;
            }
            Screen.sleepTimeout = SleepTimeout.NeverSleep;
            RenderSettings.ambientLight = new Color(0.65f, 0.65f, 0.65f);
            var light = new GameObject("Luz de las figuras").AddComponent<Light>();
            light.type = LightType.Directional;
            light.intensity = 0.85f;
            light.transform.rotation = Quaternion.Euler(45f, -30f, 0f);
            simulated = Application.isEditor && simulateInEditor;
            if (simulated)
            {
                StartSimulation();
                MakePreview();
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
                    error = "Activa el permiso de cámara en Android y vuelve a abrir la app.";
                    yield break;
                }
            }
#endif
            StartAR();
            MakePreview();
            ready = true;
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
            camera.farClipPlane = ViewDistance;
            return camera;
        }

        void StartSimulation()
        {
            viewCamera = MakeCamera(null);
            viewCamera.transform.SetPositionAndRotation(new Vector3(0, 1.6f, -2f), Quaternion.Euler(27f, 0, 0));
            viewCamera.gameObject.AddComponent<EditorWalkCamera>();
            MakeSimulatedSurface(PrimitiveType.Plane, "Piso simulado", Vector3.zero,
                new Vector3(2f, 1f, 2f));
            MakeSimulatedSurface(PrimitiveType.Cube, "Pared simulada", new Vector3(0, 1.5f, 5),
                new Vector3(10f, 3f, 0.05f));
        }

        void MakeSimulatedSurface(PrimitiveType type, string objectName, Vector3 position, Vector3 scale)
        {
            var go = GameObject.CreatePrimitive(type);
            go.name = objectName;
            go.layer = SurfaceLayer;
            go.transform.position = position;
            go.transform.localScale = scale;
            var renderer = go.GetComponent<Renderer>();
            renderer.sharedMaterial = Resources.Load<Material>("SimulationMaterial");
            simulatedSurfaces.Add(renderer);
        }

        void StartAR()
        {
            new GameObject("AR Session", typeof(ARSession), typeof(ARInputManager));
            var root = new GameObject("XR Origin");
            root.SetActive(false);
            var origin = root.AddComponent<XROrigin>();
            var offset = new GameObject("Camera Offset");
            offset.transform.SetParent(root.transform, false);
            viewCamera = MakeCamera(offset.transform);
            var cameraManager = viewCamera.gameObject.AddComponent<ARCameraManager>();
            scanner = viewCamera.gameObject.AddComponent<QrScanner>();
            scanner.Initialize(cameraManager, ReadQr);
            viewCamera.gameObject.AddComponent<ARCameraBackground>();
            var driver = viewCamera.gameObject.AddComponent<TrackedPoseDriver>();
            var position = new InputAction("Position", binding: "<XRHMD>/centerEyePosition",
                expectedControlType: "Vector3");
            position.AddBinding("<HandheldARInputDevice>/devicePosition");
            var rotation = new InputAction("Rotation", binding: "<XRHMD>/centerEyeRotation",
                expectedControlType: "Quaternion");
            rotation.AddBinding("<HandheldARInputDevice>/deviceRotation");
            driver.positionInput = new InputActionProperty(position);
            driver.rotationInput = new InputActionProperty(rotation);
            origin.Camera = viewCamera;
            origin.CameraFloorOffsetObject = offset;
            origin.CameraYOffset = 0f;
            planes = root.AddComponent<ARPlaneManager>();
            planes.requestedDetectionMode = PlaneDetectionMode.Horizontal | PlaneDetectionMode.Vertical;
            planes.trackablesChanged.AddListener(OnPlanesChanged);
            raycasts = root.AddComponent<ARRaycastManager>();
            anchors = root.AddComponent<ARAnchorManager>();
            root.SetActive(true);
        }

        void MakePreview()
        {
            preview = GameObject.CreatePrimitive(PrimitiveType.Cylinder);
            preview.name = "Indicador de superficie";
            preview.layer = 2;
            preview.transform.localScale = new Vector3(0.10f, 0.001f, 0.10f);
            preview.GetComponent<Collider>().enabled = false;
            preview.GetComponent<Renderer>().sharedMaterial = Resources.Load<Material>("PreviewMaterial");
            preview.SetActive(false);
        }

        void OnPlanesChanged(ARTrackablesChangedEventArgs<ARPlane> changes)
        {
            foreach (var plane in changes.added)
            {
                plane.gameObject.AddComponent<MeshFilter>();
                var renderer = plane.gameObject.AddComponent<MeshRenderer>();
                renderer.sharedMaterial = Resources.Load<Material>("PlaneMaterial");
                var visualizer = plane.gameObject.AddComponent<ARPlaneMeshVisualizer>();
                visualizer.enabled = showSurfaces;
            }
        }

        bool TrackingReady => simulated || ARSession.state == ARSessionState.SessionTracking;

        bool TrySurface(Vector2 screenPoint, out Pose pose, out ARPlane plane)
        {
            pose = default;
            plane = null;
            if (!ready || !TrackingReady || viewCamera == null) return false;
            if (simulated)
            {
                if (!Physics.Raycast(viewCamera.ScreenPointToRay(screenPoint), out var hit,
                        ViewDistance, 1 << SurfaceLayer)) return false;
                pose = new Pose(hit.point, Quaternion.FromToRotation(Vector3.up, hit.normal));
                return true;
            }
            if (!raycasts.Raycast(screenPoint, planeHits, TrackableType.PlaneWithinPolygon)) return false;
            foreach (var hit in planeHits)
            {
                var candidate = planes.GetPlane(hit.trackableId);
                if (candidate == null || candidate.trackingState != TrackingState.Tracking) continue;
                pose = hit.pose;
                plane = candidate;
                return true;
            }
            return false;
        }

        void Update()
        {
            if (!ready) return;
            Physics.SyncTransforms();
            foreach (var pair in placed.ToArray())
            {
                if (pair.Value == null)
                {
                    inventory.Remove(pair.Key);
                    placed.Remove(pair.Key);
                    continue;
                }
                pair.Value.RefreshTracking();
            }
            if (TrySurface(new Vector2(Screen.width / 2f, Screen.height / 2f), out var pose, out _))
            {
                preview.transform.SetPositionAndRotation(pose.position + pose.rotation * Vector3.up * 0.003f, pose.rotation);
                preview.SetActive(true);
            }
            else preview.SetActive(false);

            bool pressed = false;
            Vector2 point = default;
            if (Touchscreen.current != null && Touchscreen.current.primaryTouch.press.wasPressedThisFrame)
            {
                point = Touchscreen.current.primaryTouch.position.ReadValue();
                pressed = true;
            }
            else if (Mouse.current != null && Mouse.current.leftButton.wasPressedThisFrame)
            {
                point = Mouse.current.position.ReadValue();
                pressed = true;
            }
            if (pressed && !OverUI(point)) HandleTap(point);
        }

        void HandleTap(Vector2 point)
        {
            if (!TrackingReady || placing) return;
            if (Physics.Raycast(viewCamera.ScreenPointToRay(point), out var hit, ViewDistance, 1 << ObjectLayer))
            {
                var item = hit.collider.GetComponentInParent<PlacedShape>();
                if (item != null)
                {
                    if (inventory.SelectedId == item.Id) ClearSelection();
                    else
                    {
                        ClearSelection();
                        inventory.Select(item.Id);
                        item.SetSelected(true);
                    }
                }
                return;
            }
            if (!qrReady) { Notify("Primero lee un QR de cubo o esfera."); return; }
            if (TrySurface(point, out var pose, out var plane)) Place(pose, plane, inventory.CurrentShape);
            else Notify("Mueve lentamente el celular para detectar esa superficie.");
        }

        async void Place(Pose pose, ARPlane plane, ShapeKind kind)
        {
            placing = true;
            GameObject root = null;
            bool registered = false;
            int? allocatedId = null;
            try
            {
                ARAnchor anchor = null;
                if (simulated)
                {
                    root = new GameObject("Anclaje simulado");
                    root.transform.SetPositionAndRotation(pose.position, pose.rotation);
                }
                else
                {
                    if (anchors == null || anchors.subsystem == null)
                    {
                        Notify("El rastreo todavía no está listo para crear un anclaje.");
                        return;
                    }
                    if (plane != null) anchor = anchors.AttachAnchor(plane, pose);
                    if (anchor == null)
                    {
                        var result = await anchors.TryAddAnchorAsync(pose);
                        if (result.status.IsSuccess()) anchor = result.value;
                    }
                    if (anchor == null)
                    {
                        Notify("No se pudo fijar la figura. Escanea la zona e inténtalo otra vez.");
                        return;
                    }
                    root = anchor.gameObject;
                    if (this == null || !isActiveAndEnabled || !TrackingReady)
                    {
                        Destroy(root);
                        return;
                    }
                }
                ClearSelection();
                int id = inventory.Add(kind);
                allocatedId = id;
                var item = root.AddComponent<PlacedShape>();
                item.Initialize(id, kind, anchor);
                placed.Add(id, item);
                registered = true;
                Notify(kind == ShapeKind.Cube ? "Cubo colocado." : "Esfera colocada.");
            }
            catch (Exception exception)
            {
                Debug.LogException(exception);
                if (this != null) Notify("No se pudo colocar la figura. Revisa el rastreo e inténtalo de nuevo.");
            }
            finally
            {
                if (!registered && root != null) Destroy(root);
                if (!registered && allocatedId.HasValue) inventory.Remove(allocatedId.Value);
                if (this != null) placing = false;
            }
        }

        void ClearSelection()
        {
            if (inventory.SelectedId.HasValue && placed.TryGetValue(inventory.SelectedId.Value, out var item)
                && item != null) item.SetSelected(false);
            inventory.Deselect();
        }

        void ReadQr(string text)
        {
            if (qrReady) return;
            if (!QrPayload.TryGetShape(text, out var kind))
            { Notify("QR sin contenido AR configurado. Usa AR:CUBO o AR:ESFERA."); return; }
            ClearSelection(); inventory.Choose(kind); qrReady = true;
            if (scanner != null) scanner.ScanEnabled = false;
            Notify(kind == ShapeKind.Cube ? "QR de cubo leído. Toca una superficie." : "QR de esfera leído. Toca una superficie.");
        }

        void ReadExample(string resource)
        {
            qrReady = false;
            var texture = Resources.Load<Texture2D>(resource);
            if (texture == null) { Notify("Falta el QR de ejemplo."); return; }
            string text = new PureQrDecoder().Decode(CodeMarkerExamples.CpuGrayCamera.FromTexture(texture), texture.width, texture.height);
            if (text == null) Notify("No se pudo leer el QR de ejemplo."); else ReadQr(text);
        }

        void ScanAgain()
        {
            qrReady = false;
            if (scanner != null) scanner.ScanEnabled = true;
            Notify("Muestra AR:CUBO o AR:ESFERA completos y con margen blanco.");
        }

        void DeleteSelection()
        {
            int? id = inventory.RemoveSelected();
            if (!id.HasValue || !placed.TryGetValue(id.Value, out var item)) return;
            placed.Remove(id.Value);
            if (item == null) return;
            if (item.Anchor != null && anchors != null && anchors.enabled && anchors.subsystem != null)
                anchors.TryRemoveAnchor(item.Anchor);
            Destroy(item.gameObject);
            Notify("Figura eliminada.");
        }

        void ToggleSurfaces()
        {
            showSurfaces = !showSurfaces;
            foreach (var renderer in simulatedSurfaces) renderer.enabled = showSurfaces;
            if (planes == null) return;
            foreach (var plane in planes.trackables)
            {
                var visualizer = plane.GetComponent<ARPlaneMeshVisualizer>();
                if (visualizer != null) visualizer.enabled = showSurfaces;
            }
        }

        void Notify(string message)
        {
            notice = message;
            noticeUntil = Time.unscaledTime + 3f;
        }

        float UIScale => Mathf.Clamp(Screen.width / 540f, 0.8f, 3f);
        bool CompactUI => Screen.height / UIScale < 430f;
        bool OverUI(Vector2 point)
        {
            float scale = UIScale;
            var guiPoint = new Vector2(point.x / scale, (Screen.height - point.y) / scale);
            float footer = CompactUI ? 106f : 144f;
            return new Rect(0, 0, Screen.width / scale, CompactUI ? 64 : 94).Contains(guiPoint)
                || new Rect(0, Screen.height / scale - footer, Screen.width / scale, footer).Contains(guiPoint);
        }

        void OnGUI()
        {
            float scale = UIScale;
            float width = Screen.width / scale;
            float height = Screen.height / scale;
            GUI.matrix = Matrix4x4.Scale(new Vector3(scale, scale, 1));
            bool compact = CompactUI;
            GUI.skin.box.fontSize = compact ? 14 : 17;
            GUI.skin.box.wordWrap = true;
            GUI.skin.box.alignment = TextAnchor.MiddleCenter;
            GUI.skin.button.fontSize = compact ? 16 : 19;
            string status = error;
            if (status == null && !ready) status = "Preparando cámara...";
            if (status == null && !TrackingReady) status = ARSession.state == ARSessionState.Unsupported
                ? "Este celular no admite ARCore."
                : "Rastreo limitado. Enfoca una zona iluminada con detalle.";
            if (status == null && placing) status = "Fijando la figura...";
            if (status == null && Time.unscaledTime < noticeUntil) status = notice;
            if (status == null) status = inventory.SelectedId.HasValue
                ? "Figura seleccionada. Presiona Eliminar o vuelve a tocarla para deseleccionar."
                : qrReady ? "Toca una superficie para colocar. Toca una figura para seleccionarla." : "Muestra un QR: AR:CUBO o AR:ESFERA.";
            GUI.Box(new Rect(12, 8, width - 24, compact ? 52 : 78), status + "\nObjetos: " + inventory.Items.Count + (!simulated && !qrReady && scanner != null ? " • " + scanner.Status : ""));
            GUI.enabled = ready && !placing;
            float half = (width - 48) / 2;
            GUI.backgroundColor = inventory.CurrentShape == ShapeKind.Cube ? new Color(1f, 0.65f, 0.3f) : Color.white;
            if (GUI.Button(new Rect(16, height - (compact ? 100 : 134), half, compact ? 40 : 54), simulated ? "Leer QR cubo" : qrReady ? inventory.CurrentShape == ShapeKind.Cube ? "QR: cubo" : "QR: esfera" : "Buscando QR...")) { if (simulated) ReadExample("QrCube"); }
            GUI.backgroundColor = inventory.CurrentShape == ShapeKind.Sphere ? new Color(0.4f, 0.75f, 1f) : Color.white;
            if (GUI.Button(new Rect(width / 2 + 8, height - (compact ? 100 : 134), half, compact ? 40 : 54), simulated ? "Leer QR esfera" : "Leer otro QR")) { if (simulated) ReadExample("QrSphere"); else ScanAgain(); }
            GUI.backgroundColor = Color.white;
            GUI.enabled = ready && !placing && inventory.SelectedId.HasValue;
            if (GUI.Button(new Rect(16, height - (compact ? 52 : 66), half, compact ? 40 : 50),
                compact ? "Eliminar" : "Eliminar selección")) DeleteSelection();
            GUI.enabled = ready;
            if (GUI.Button(new Rect(width / 2 + 8, height - (compact ? 52 : 66), half, compact ? 40 : 50),
                showSurfaces ? "Ocultar superficies" : "Mostrar superficies")) ToggleSurfaces();
            GUI.enabled = true;
        }

        void OnDestroy()
        {
            if (planes != null) planes.trackablesChanged.RemoveListener(OnPlanesChanged);
        }
    }
}
