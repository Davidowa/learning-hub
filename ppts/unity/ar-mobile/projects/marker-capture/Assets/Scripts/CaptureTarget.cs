using UnityEngine;

namespace MarkerCapture
{
    public sealed class CaptureTarget : MonoBehaviour
    {
        CaptureRegistry registry;
        GameObject cube;
        GameObject capturedSphere;
        GameObject visuals;

        public string ImageId { get; private set; }
        public bool IsTracking { get; private set; }
        public bool IsCaptured => registry != null && registry.IsCaptured(ImageId);

        public void Initialize(CaptureRegistry registry, string imageId)
        {
            this.registry = registry;
            ImageId = imageId;
            visuals = new GameObject("Contenido visible");
            visuals.transform.SetParent(transform, false);
            cube = MakeShape(PrimitiveType.Cube, "Cubo por capturar", 0.06f, "CubeMaterial");
            capturedSphere = MakeShape(PrimitiveType.Sphere, "Captura verde", 0.055f, "CapturedMaterial");
            capturedSphere.GetComponent<Collider>().enabled = false;
            Refresh();
            SetTracking(false);
        }

        GameObject MakeShape(PrimitiveType type, string objectName, float diameter, string material)
        {
            var shape = GameObject.CreatePrimitive(type);
            shape.name = objectName;
            shape.transform.SetParent(visuals.transform, false);
            shape.transform.localScale = Vector3.one * diameter;
            shape.transform.localPosition = Vector3.up * (diameter * 0.5f);
            shape.GetComponent<Renderer>().sharedMaterial = Resources.Load<Material>(material);
            return shape;
        }

        public void SetTracking(bool tracking)
        {
            IsTracking = tracking;
            if (visuals != null) visuals.SetActive(tracking);
        }

        public bool TryCapture()
        {
            if (!IsTracking || !registry.TryCapture(ImageId)) return false;
            Refresh();
            return true;
        }

        public void ResetCapture()
        {
            registry.Reset(ImageId);
            Refresh();
        }

        void Refresh()
        {
            bool captured = IsCaptured;
            // Disable the whole cube so tracking updates cannot revive its renderer.
            cube.SetActive(!captured);
            capturedSphere.SetActive(captured);
        }
    }
}
