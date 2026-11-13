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

namespace MarkerlessPlace
{
    public sealed class PlacementBootstrap : MonoBehaviour
    {
        public const int SurfaceLayer = 8;
        public const int ObjectLayer = 9;
        const float ViewDistance = 1000f;
        public LabSceneReferences scene;
        public LabContent content;
        public LabUI ui;
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
        bool ready;
        bool placing;
        bool showSurfaces = true;
        string error;
        string notice;
        float noticeUntil;

        IEnumerator Start()
        {
            if(scene==null||content==null||ui==null)
            { Debug.LogError("Completa Scene, Content y UI en el controlador Laboratorio.");yield break; }
            Screen.sleepTimeout = SleepTimeout.NeverSleep;
            RenderSettings.ambientLight = new Color(0.65f, 0.65f, 0.65f);
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



        void StartSimulation()
        {
            viewCamera=scene.Activate(true);
            simulatedSurfaces.AddRange(scene.simulationWorld.GetComponentsInChildren<Renderer>());
        }



        void StartAR()
        {
            viewCamera=scene.Activate(false);
            planes=scene.planes;raycasts=scene.raycasts;anchors=scene.anchors;
            planes.trackablesChanged.AddListener(OnPlanesChanged);
        }

        void MakePreview()
        {
            preview=Instantiate(content.indicator);preview.name="Indicador de superficie";preview.SetActive(false);
        }

        void OnPlanesChanged(ARTrackablesChangedEventArgs<ARPlane> changes)
        {
            foreach(var plane in changes.added)
            {
                var visualizer=plane.GetComponent<ARPlaneMeshVisualizer>();
                if(visualizer!=null)visualizer.enabled=showSurfaces;
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
            if (pressed)
            {
                if (!OverUI(point)) HandleTap(point);
            }
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
                item.Initialize(id, kind, anchor,content);
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

        void Choose(ShapeKind kind)
        {
            ClearSelection();
            inventory.Choose(kind);
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
        bool OverUI(Vector2 point)=>LabUI.BlocksWorld(point);

        public void DeleteButton()=>DeleteSelection();
        public void SurfacesButton()=>ToggleSurfaces();
        public void ChooseA(){ClearSelection();inventory.Choose(ShapeKind.Cube);}
        public void ChooseB(){ClearSelection();inventory.Choose(ShapeKind.Sphere);}
        void LateUpdate()
        {
            if(ui==null)return;
            string status=error;
            if(status==null&&!ready)status="Preparando cámara...";
            if(status==null&&!TrackingReady)status="Mueve lentamente el celular por una superficie iluminada con detalle.";
            if(status==null&&Time.unscaledTime<noticeUntil)status=notice;
            if(status==null)status="Elige contenido A/B y toca una superficie. Toca una figura para seleccionarla.";
            ui.Message(status+"\nObjetos: "+inventory.Items.Count);
            ui.State(ui.primary,"Contenido A",ready&&!placing);ui.State(ui.secondary,"Contenido B",ready&&!placing);
            ui.State(ui.tertiary,"Eliminar selección",ready&&!placing&&inventory.SelectedId.HasValue);
            ui.State(ui.quaternary,showSurfaces?"Ocultar superficies":"Mostrar superficies",ready);
        }

        void OnDestroy()
        {
            if (planes != null) planes.trackablesChanged.RemoveListener(OnPlanesChanged);
        }
    }
}

