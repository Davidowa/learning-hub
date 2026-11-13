using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.EventSystems;

public sealed class LabUI : MonoBehaviour
{
    public Text status;
    public Button primary,secondary,tertiary,quaternary,simulation;
    public RectTransform[] cornerDots;
    public void Message(string text) { if(status!=null)status.text=text; }
    public void State(Button button,string label,bool enabled=true)
    {
        if(button==null)return;
        button.interactable=enabled;
        var text=button.GetComponentInChildren<Text>();if(text!=null)text.text=label;
    }
    public static bool BlocksWorld(Vector2 point)
    {
        if(EventSystem.current==null)return false;
        var hits=new List<RaycastResult>();
        EventSystem.current.RaycastAll(new PointerEventData(EventSystem.current){position=point},hits);
        return hits.Count>0;
    }
    public void Corners(Vector2[] viewport)
    {
        if(cornerDots==null)return;
        for(int i=0;i<cornerDots.Length;i++)
        {
            var dot=cornerDots[i];if(dot==null)continue;
            bool show=viewport!=null&&i<viewport.Length;dot.gameObject.SetActive(show);
            if(show){dot.anchorMin=dot.anchorMax=viewport[i];dot.anchoredPosition=Vector2.zero;}
        }
    }
}
