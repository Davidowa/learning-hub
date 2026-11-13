using UnityEngine;
using UnityEngine.XR.ARFoundation;

public sealed class LabSceneReferences : MonoBehaviour
{
    public GameObject arOrigin;
    public GameObject arSession;
    public Camera arCamera;
    public GameObject simulationWorld;
    public Camera simulationCamera;
    public ARTrackedImageManager trackedImages;
    public ARPlaneManager planes;
    public ARRaycastManager raycasts;
    public ARAnchorManager anchors;
    public Transform simulatedMarker;
    public Camera Activate(bool simulation)
    {
        if(arOrigin==null||arSession==null||arCamera==null||simulationWorld==null||simulationCamera==null)
            throw new System.InvalidOperationException("Faltan referencias de escena. Completa Lab Scene References según la guía.");
        arOrigin.SetActive(!simulation); arSession.SetActive(!simulation);
        simulationWorld.SetActive(simulation);
        return simulation ? simulationCamera : arCamera;
    }
}
