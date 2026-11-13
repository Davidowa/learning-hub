using System;
using System.Collections.Generic;
using ZXing;
using ZXing.Common;

namespace QrPlace
{
    public sealed class PureQrDecoder
    {
        readonly BarcodeReaderGeneric reader=new()
        {
            AutoRotate=true,
            Options=new DecodingOptions {TryHarder=true,PossibleFormats=new List<BarcodeFormat>{BarcodeFormat.QR_CODE}}
        };
        public string Decode(byte[] gray,int width,int height)
        {
            if(gray==null||width<1||height<1||gray.Length!=width*height)throw new ArgumentException("Invalid grayscale image.");
            var source=new RGBLuminanceSource(gray,width,height,RGBLuminanceSource.BitmapFormat.Gray8);
            return reader.Decode(source)?.Text;
        }
    }
}
