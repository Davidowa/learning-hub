using UnityEngine;

public sealed class LightSwitchLab : MonoBehaviour
{
    [SerializeField] Light targetLight;
    [SerializeField] GameObject onLabel;
    [SerializeField] GameObject offLabel;
    bool isOn;

    void Start()
    {
        if (targetLight == null || onLabel == null || offLabel == null)
        {
            Debug.LogError("Asigna luz y las dos etiquetas.", this);
            enabled = false;
            return;
        }
        ApplyState();
    }

    public void ToggleLamp()
    {
        if (!enabled || targetLight == null) return;
        isOn = !isOn;
        ApplyState();
    }

    void ApplyState()
    {
        targetLight.enabled = isOn;
        onLabel.SetActive(isOn);
        offLabel.SetActive(!isOn);
        Debug.Log(isOn ? "Lampara encendida" : "Lampara apagada", this);
    }
}
