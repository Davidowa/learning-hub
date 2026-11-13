using UnityEngine;

[CreateAssetMenu(menuName="Laboratorios/Contenido",fileName="ContenidoLab")]
public sealed class LabContent : ScriptableObject
{
    [Tooltip("Prefab centrado, escala 1. El controlador lo muestra a 20 cm.")]
    public GameObject contentA;
    public GameObject contentB;
    public GameObject indicator;
    public GameObject captureTarget;
    public GameObject projectile;
    public GameObject arucoVisual;
    public Material selectedMaterial;
}
