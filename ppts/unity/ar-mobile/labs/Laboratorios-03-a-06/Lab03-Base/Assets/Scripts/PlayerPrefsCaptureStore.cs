using UnityEngine;

namespace MarkerCapture
{
    public sealed class PlayerPrefsCaptureStore : ICaptureStore
    {
        public bool Read(string key) => PlayerPrefs.GetInt(key, 0) == 1;

        public void Write(string key, bool captured)
        {
            if (captured) PlayerPrefs.SetInt(key, 1);
            else PlayerPrefs.DeleteKey(key);
            // Save immediately, including when Android later terminates the app.
            PlayerPrefs.Save();
        }
    }
}
