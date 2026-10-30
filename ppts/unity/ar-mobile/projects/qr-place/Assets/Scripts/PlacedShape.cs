using UnityEngine;
using UnityEngine.XR.ARFoundation;
using UnityEngine.XR.ARSubsystems;

namespace QrPlace
{
    public sealed class PlacedShape : MonoBehaviour
    {
        Renderer visualRenderer;
        Material normalMaterial;
        GameObject visual;
        public int Id { get; private set; }
        public ARAnchor Anchor { get; private set; }

        public void Initialize(int id, ShapeKind kind, ARAnchor anchor)
        {
            Id = id;
            Anchor = anchor;
            float size = 0.20f;
            visual = GameObject.CreatePrimitive(kind == ShapeKind.Cube ? PrimitiveType.Cube : PrimitiveType.Sphere);
            visual.name = kind == ShapeKind.Cube ? "Cubo de 20 cm" : "Esfera de 20 cm";
            visual.layer = PlacementBootstrap.ObjectLayer;
            visual.transform.SetParent(transform, false);
            visual.transform.localPosition = Vector3.up * (size * 0.5f);
            visual.transform.localScale = Vector3.one * size;
            visualRenderer = visual.GetComponent<Renderer>();
            normalMaterial = Resources.Load<Material>(kind == ShapeKind.Cube ? "CubeMaterial" : "SphereMaterial");
            SetSelected(false);
        }

        public void SetSelected(bool selected)
        {
            if (visualRenderer != null)
                visualRenderer.sharedMaterial = selected
                    ? Resources.Load<Material>("SelectedMaterial") : normalMaterial;
        }

        public void RefreshTracking()
        {
            // Hiding a temporarily untracked shape does not delete its anchor or inventory entry.
            if (visual != null)
                visual.SetActive(Anchor == null || Anchor.trackingState == TrackingState.Tracking);
        }
    }
}
