namespace QrPlace
{
    public static class QrPayload
    {
        public static bool TryGetShape(string text,out ShapeKind kind)
        {
            kind=ShapeKind.Cube;
            if(text=="AR:CUBO")return true;
            if(text=="AR:ESFERA"){kind=ShapeKind.Sphere;return true;}
            return false;
        }
    }
}
