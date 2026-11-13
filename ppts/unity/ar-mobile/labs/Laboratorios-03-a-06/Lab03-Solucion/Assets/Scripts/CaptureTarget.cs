using UnityEngine;

namespace MarkerCapture
{
    public sealed class CaptureTarget : MonoBehaviour
    {
        CaptureRegistry registry;
        public GameObject cube;
        public GameObject capturedSphere;
        public GameObject visuals;

        public string ImageId { get; private set; }
        public bool IsTracking { get; private set; }
        public bool IsCaptured => registry != null && registry.IsCaptured(ImageId);

        public void Initialize(CaptureRegistry registry, string imageId)
        {
            this.registry = registry;
            ImageId = imageId;
            if(visuals==null||cube==null||capturedSphere==null)
                throw new System.InvalidOperationException("Completa las referencias del prefab Objetivo.");
            Refresh();
            SetTracking(false);
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

