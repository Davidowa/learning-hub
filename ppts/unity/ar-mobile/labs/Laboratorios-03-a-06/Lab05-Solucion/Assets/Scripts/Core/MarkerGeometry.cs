using System;

namespace ArucoExample
{
    public readonly struct P2
    {
        public readonly double X, Y;
        public P2(double x, double y) { X = x; Y = y; }
        public static P2 operator +(P2 a, P2 b) => new(a.X+b.X,a.Y+b.Y);
        public static P2 operator -(P2 a, P2 b) => new(a.X-b.X,a.Y-b.Y);
        public static P2 operator *(P2 a, double s) => new(a.X*s,a.Y*s);
        public double Length => Math.Sqrt(X*X+Y*Y);
    }

    public readonly struct P3
    {
        public readonly double X, Y, Z;
        public P3(double x,double y,double z) { X=x;Y=y;Z=z; }
        public static P3 operator +(P3 a,P3 b) => new(a.X+b.X,a.Y+b.Y,a.Z+b.Z);
        public static P3 operator -(P3 a,P3 b) => new(a.X-b.X,a.Y-b.Y,a.Z-b.Z);
        public static P3 operator *(P3 a,double s) => new(a.X*s,a.Y*s,a.Z*s);
        public double Length => Math.Sqrt(X*X+Y*Y+Z*Z);
        public P3 Unit => this*(1.0/Length);
        public static double Dot(P3 a,P3 b) => a.X*b.X+a.Y*b.Y+a.Z*b.Z;
        public static P3 Cross(P3 a,P3 b) => new(a.Y*b.Z-a.Z*b.Y,a.Z*b.X-a.X*b.Z,a.X*b.Y-a.Y*b.X);
    }

    public static class Homography
    {
        public static readonly P2[] UnitSquare = {
            new(-.5,-.5),new(.5,-.5),new(.5,.5),new(-.5,.5)
        };

        public static bool TryFit(P2[] from,P2[] to,out double[] h)
        {
            h=null;
            if(from==null||to==null||from.Length!=4||to.Length!=4)return false;
            var a=new double[8,9];
            for(int i=0;i<4;i++)
            {
                double x=from[i].X,y=from[i].Y,u=to[i].X,v=to[i].Y;
                int r=2*i;
                a[r,0]=x;a[r,1]=y;a[r,2]=1;a[r,6]=-u*x;a[r,7]=-u*y;a[r,8]=u;
                a[r+1,3]=x;a[r+1,4]=y;a[r+1,5]=1;a[r+1,6]=-v*x;a[r+1,7]=-v*y;a[r+1,8]=v;
            }
            for(int col=0;col<8;col++)
            {
                int pivot=col;
                for(int r=col+1;r<8;r++)if(Math.Abs(a[r,col])>Math.Abs(a[pivot,col]))pivot=r;
                if(Math.Abs(a[pivot,col])<1e-11)return false;
                for(int j=col;j<9;j++){double temp=a[col,j];a[col,j]=a[pivot,j];a[pivot,j]=temp;}
                double divisor=a[col,col];for(int j=col;j<9;j++)a[col,j]/=divisor;
                for(int r=0;r<8;r++)if(r!=col)
                {
                    double factor=a[r,col];for(int j=col;j<9;j++)a[r,j]-=factor*a[col,j];
                }
            }
            h=new double[9];for(int i=0;i<8;i++)h[i]=a[i,8];h[8]=1;
            return true;
        }

        public static P2 Project(double[] h,P2 p)
        {
            double w=h[6]*p.X+h[7]*p.Y+h[8];
            return new((h[0]*p.X+h[1]*p.Y+h[2])/w,(h[3]*p.X+h[4]*p.Y+h[5])/w);
        }
    }

    public readonly struct MarkerPose
    {
        // Camera coordinates: X right, Y down, Z forward. Marker axes: X right, Y down.
        public readonly P3 Right, Down, Translation;
        public readonly double ReprojectionError;
        public MarkerPose(P3 right,P3 down,P3 translation,double error)
        {Right=right;Down=down;Translation=translation;ReprojectionError=error;}
    }

    public static class PlanarPose
    {
        public static bool TrySolve(P2[] normalizedCameraCorners,double sideMeters,out MarkerPose pose)
        {
            pose=default;
            if(!(sideMeters>0)||!Homography.TryFit(Homography.UnitSquare,normalizedCameraCorners,out var h))return false;
            var a=new P3(h[0],h[3],h[6]);var b=new P3(h[1],h[4],h[7]);
            var c=new P3(h[2],h[5],h[8]);
            if(a.Length<1e-10||b.Length<1e-10)return false;
            double ratio=a.Length/b.Length;
            if(ratio<.65||ratio>1.55||Math.Abs(P3.Dot(a.Unit,b.Unit))>.4)return false;
            double scale=2/(a.Length+b.Length);
            var right=a.Unit;
            var remainder=b-right*P3.Dot(b,right);
            if(remainder.Length<1e-10)return false;
            var down=remainder.Unit;var t=c*(scale*sideMeters);
            if(t.Z<=.03||t.Z>5)return false;
            double error=0;
            for(int i=0;i<4;i++)
            {
                var p=t+right*(Homography.UnitSquare[i].X*sideMeters)+down*(Homography.UnitSquare[i].Y*sideMeters);
                if(p.Z<=.01)return false;
                error+=(new P2(p.X/p.Z,p.Y/p.Z)-normalizedCameraCorners[i]).Length;
            }
            error/=4;
            if(double.IsNaN(error)||error>.035)return false;
            pose=new MarkerPose(right,down,t,error);return true;
        }
    }
}

namespace ArucoExample
{
    public static class UvTransform
    {
        // Inverse of the provider's row-vector display mapping: raw = [viewport.x viewport.y 1] * M.
        public static bool TryInverse(double a,double b,double c,double d,double e,double f,P2 raw,out P2 viewport)
        {
            viewport=default;double det=a*e-b*d;if(Math.Abs(det)<1e-10)return false;
            double u=raw.X-c,v=raw.Y-f;viewport=new P2((e*u-b*v)/det,(-d*u+a*v)/det);return true;
        }
    }
}
