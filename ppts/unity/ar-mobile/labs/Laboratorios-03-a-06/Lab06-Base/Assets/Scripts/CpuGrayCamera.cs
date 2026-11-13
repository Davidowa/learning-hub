using System;
using Unity.Collections;
using UnityEngine;
using UnityEngine.XR.ARFoundation;
using UnityEngine.XR.ARSubsystems;

namespace CodeMarkerExamples
{
    public sealed class GrayCameraFrame
    {
        public byte[] Pixels;
        public int Width,Height;
        public Matrix4x4 Display;
        public bool HasDisplay;
    }

    public sealed class CpuGrayCamera : MonoBehaviour
    {
        ARCameraManager manager;
        Matrix4x4 display;
        bool hasDisplay,subscribed;
        float nextFrame;
        public string Status {get;private set;}="Esperando imagen CPU de la cámara.";
        public event Action<GrayCameraFrame> FrameReady;

        public void Initialize(ARCameraManager cameraManager)
        {
            if(manager!=null&&subscribed)manager.frameReceived-=OnFrame;
            manager=cameraManager;subscribed=false;Register();
        }
        void OnEnable()=>Register();
        void Register(){if(manager!=null&&!subscribed){manager.frameReceived+=OnFrame;subscribed=true;}}
        void OnDisable(){if(manager!=null&&subscribed)manager.frameReceived-=OnFrame;subscribed=false;hasDisplay=false;}
        void OnFrame(ARCameraFrameEventArgs frame){if(frame.displayMatrix.HasValue){display=frame.displayMatrix.Value;hasDisplay=true;}}

        void Update()
        {
            if(manager==null||Time.unscaledTime<nextFrame)return;
            nextFrame=Time.unscaledTime+.2f;
            if(!manager.TryAcquireLatestCpuImage(out var image)){Status="Sin imagen CPU disponible. Espera a que inicie la cámara.";return;}
            using(image)
            {
                if(!image.FormatSupported(TextureFormat.R8)){Status="Este proveedor no convierte la cámara a R8.";return;}
                float ratio=Mathf.Min(1f,640f/Mathf.Max(image.width,image.height));
                int width=Mathf.Max(24,Mathf.RoundToInt(image.width*ratio));
                int height=Mathf.Max(24,Mathf.RoundToInt(image.height*ratio));
                var conversion=new XRCpuImage.ConversionParams
                {
                    inputRect=new RectInt(0,0,image.width,image.height),
                    outputDimensions=new Vector2Int(width,height),outputFormat=TextureFormat.R8,
                    transformation=XRCpuImage.Transformation.None
                };
                try
                {
                    using var bytes=new NativeArray<byte>(image.GetConvertedDataSize(conversion),Allocator.Temp);
                    image.Convert(conversion,new NativeSlice<byte>(bytes));
                    Status="Imagen CPU: "+width+" × "+height+".";
                    FrameReady?.Invoke(new GrayCameraFrame {Pixels=bytes.ToArray(),Width=width,Height=height,Display=display,HasDisplay=hasDisplay});
                }
                catch(Exception ex){Status="No se procesó la imagen CPU: "+ex.Message;Debug.LogException(ex);}
            }
        }

        public static byte[] FromTexture(Texture2D texture)
        {
            var pixels=texture.GetPixels32();var gray=new byte[pixels.Length];
            for(int y=0;y<texture.height;y++)for(int x=0;x<texture.width;x++)
            {
                var pixel=pixels[(texture.height-1-y)*texture.width+x];
                gray[y*texture.width+x]=(byte)((77*pixel.r+150*pixel.g+29*pixel.b)>>8);
            }
            return gray;
        }
    }
}
