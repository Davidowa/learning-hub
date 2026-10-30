using TMPro;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.XR.Interaction.Toolkit.Samples.StarterAssets;
public sealed class ComfortOptionsLab : MonoBehaviour
{
    [SerializeField] ControllerInputActionManager leftController;
    [SerializeField] ControllerInputActionManager rightController;
    [SerializeField] Toggle moveToggle;
    [SerializeField] Toggle turnToggle;
    [SerializeField] TMP_Text statusText;
    bool continuousMove;
    bool continuousTurn;
    void Start()
    {
        if (leftController == null || rightController == null ||
            moveToggle == null || turnToggle == null || statusText == null)
        {
            Debug.LogError("Completa las cinco referencias del menu.", this);
            enabled = false;
            return;
        }
        RestoreDefaults();
    }
    public void SetContinuousMove(bool value)
    {
        if (!enabled) return;
        continuousMove = value;
        ApplyModes();
    }
    public void SetContinuousTurn(bool value)
    {
        if (!enabled) return;
        continuousTurn = value;
        ApplyModes();
    }
    public void RestoreDefaults()
    {
        continuousMove = false;
        continuousTurn = false;
        moveToggle.SetIsOnWithoutNotify(false);
        turnToggle.SetIsOnWithoutNotify(false);
        ApplyModes();
    }
    void ApplyModes()
    {
        leftController.smoothMotionEnabled = continuousMove;
        rightController.smoothMotionEnabled = continuousMove;
        leftController.smoothTurnEnabled = continuousTurn;
        rightController.smoothTurnEnabled = continuousTurn;
        statusText.text = (continuousMove ? "Movimiento continuo" : "Teletransporte")
            + " / " + (continuousTurn ? "Giro continuo" : "Snap turn");
    }
    public void QuitApplication()
    {
        Debug.Log("Solicitud de salida de la aplicacion.", this);
        Application.Quit();
    }
}
