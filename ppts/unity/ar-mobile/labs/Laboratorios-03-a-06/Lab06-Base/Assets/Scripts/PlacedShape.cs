using UnityEngine;
using UnityEngine.XR.ARFoundation;
using UnityEngine.XR.ARSubsystems;
namespace QrPlace
{
 public sealed class PlacedShape:MonoBehaviour
 {
  GameObject visual;Renderer[] renderers;Material[][] normal;Material selected;
  public int Id{get;private set;}public ARAnchor Anchor{get;private set;}
  public void Initialize(int id,ShapeKind kind,ARAnchor anchor,LabContent content)
  {
   Id=id;Anchor=anchor;selected=content.selectedMaterial;
   visual=Instantiate(kind==ShapeKind.Cube?content.contentA:content.contentB,transform);
   visual.transform.localPosition=Vector3.up*.1f;visual.transform.localRotation=Quaternion.identity;
   visual.transform.localScale=Vector3.one*.2f;
   foreach(var child in visual.GetComponentsInChildren<Transform>(true))child.gameObject.layer=9;
   renderers=visual.GetComponentsInChildren<Renderer>(true);normal=new Material[renderers.Length][];
   for(int i=0;i<renderers.Length;i++)normal[i]=renderers[i].sharedMaterials;
  }
  public void SetSelected(bool value)
  {
   for(int i=0;i<renderers.Length;i++)
   {
    var mats=(Material[])normal[i].Clone();if(value)for(int j=0;j<mats.Length;j++)mats[j]=selected;
    renderers[i].sharedMaterials=mats;
   }
  }
  public void RefreshTracking(){if(visual!=null)visual.SetActive(Anchor==null||Anchor.trackingState==TrackingState.Tracking);}
 }
}
