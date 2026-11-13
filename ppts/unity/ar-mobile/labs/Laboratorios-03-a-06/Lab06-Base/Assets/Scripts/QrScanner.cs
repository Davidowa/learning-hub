using System;
using CodeMarkerExamples;
using UnityEngine;
using UnityEngine.XR.ARFoundation;

namespace QrPlace
{
    public sealed class QrScanner : MonoBehaviour
    {
        readonly PureQrDecoder decoder=new();
        CpuGrayCamera cameraReader;
        Action<string> onDecoded;
        public string Status => cameraReader != null ? cameraReader.Status : "Preparando lector...";
        public bool ScanEnabled {get=>cameraReader!=null&&cameraReader.enabled;set{if(cameraReader!=null)cameraReader.enabled=value;}}
        public void Initialize(ARCameraManager manager,Action<string> callback)
        {
            onDecoded=callback;cameraReader=gameObject.AddComponent<CpuGrayCamera>();
            cameraReader.Initialize(manager);cameraReader.FrameReady+=OnImage;
        }
        void OnImage(GrayCameraFrame frame)
        {
            string text=decoder.Decode(frame.Pixels,frame.Width,frame.Height);
            if(text!=null)onDecoded?.Invoke(text);
        }
        void OnDestroy(){if(cameraReader!=null)cameraReader.FrameReady-=OnImage;}
    }
}
