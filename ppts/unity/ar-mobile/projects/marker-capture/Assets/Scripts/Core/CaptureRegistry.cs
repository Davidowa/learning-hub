using System;

namespace MarkerCapture
{
    public interface ICaptureStore
    {
        bool Read(string key);
        void Write(string key, bool captured);
    }

    // The reference image identifies the capture; a tracking instance does not.
    public sealed class CaptureRegistry
    {
        public const string Prefix = "marker-capture.v1.";
        readonly ICaptureStore store;

        public CaptureRegistry(ICaptureStore store)
        {
            this.store = store ?? throw new ArgumentNullException(nameof(store));
        }

        static string Key(string imageId)
        {
            if (string.IsNullOrWhiteSpace(imageId))
                throw new ArgumentException("La imagen necesita un identificador.", nameof(imageId));
            return Prefix + imageId;
        }

        public bool IsCaptured(string imageId) => store.Read(Key(imageId));

        public bool TryCapture(string imageId)
        {
            string key = Key(imageId);
            if (store.Read(key)) return false;
            store.Write(key, true);
            return true;
        }

        public void Reset(string imageId) => store.Write(Key(imageId), false);
    }
}
