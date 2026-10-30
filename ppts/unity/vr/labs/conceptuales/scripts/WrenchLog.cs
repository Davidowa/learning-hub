using UnityEngine;
using UnityEngine.XR.Interaction.Toolkit;

public sealed class WrenchLog : MonoBehaviour
{
    public void Held(SelectEnterEventArgs args)
    {
        string interactor = args.interactorObject.transform.name;
        Debug.Log($"VR-C00 | Torquimetro tomado por {interactor}");
    }
}
