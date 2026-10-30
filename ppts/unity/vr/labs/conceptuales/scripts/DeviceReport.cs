using UnityEngine;
using UnityEngine.XR;

public sealed class DeviceReport : MonoBehaviour
{
    void Start()
    {
        Debug.Log($"VR-C00 | platform={Application.platform}");
        Debug.Log($"VR-C00 | graphics={SystemInfo.graphicsDeviceType}");
        Debug.Log($"VR-C00 | editor={Application.isEditor}");
        Debug.Log($"VR-C00 | xrEnabled={XRSettings.enabled}");
    }
}
