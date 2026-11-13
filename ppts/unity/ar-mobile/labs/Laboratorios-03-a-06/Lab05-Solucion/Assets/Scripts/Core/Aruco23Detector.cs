using System;
using System.Collections.Generic;

namespace ArucoExample
{
    public sealed class Aruco23Detection
    {
        public P2[] Corners;
        public int Id => 23;
        public double Area;
    }

    // Educational subset: one genuine DICT_4X4_50 marker (ID 23), exact decoding, four rotations.
    // The marker pattern is generated with OpenCV; the detector below is managed C#.
    public sealed class Aruco23Detector
    {
        public const string CanonicalBits = "1101110110000010";
        byte[] binary;
        int[] labels, queue, integral;
        int width,height;

        public Aruco23Detection Detect(byte[] gray,int w,int h)
        {
            if(gray==null||w<24||h<24||gray.Length!=w*h)throw new ArgumentException("Invalid grayscale image.");
            width=w;height=h;int length=w*h;
            if(binary==null||binary.Length!=length)
            {binary=new byte[length];labels=new int[length];queue=new int[length];integral=new int[(w+1)*(h+1)];}
            Array.Clear(labels,0,length);Array.Clear(integral,0,integral.Length);
            for(int y=0;y<h;y++)
            {
                int row=0;
                for(int x=0;x<w;x++){row+=gray[y*w+x];integral[(y+1)*(w+1)+x+1]=integral[y*(w+1)+x+1]+row;}
            }
            const int radius=12;
            for(int y=0;y<h;y++)for(int x=0;x<w;x++)
            {
                int l=Math.Max(0,x-radius),r=Math.Min(w,x+radius+1),t=Math.Max(0,y-radius),b=Math.Min(h,y+radius+1);
                int sum=integral[b*(w+1)+r]-integral[t*(w+1)+r]-integral[b*(w+1)+l]+integral[t*(w+1)+l];
                int mean=sum/((r-l)*(b-t));binary[y*w+x]=(byte)(gray[y*w+x]<mean-7?1:0);
            }
            Aruco23Detection best=null;int label=0;
            for(int seed=0;seed<length;seed++)
            {
                if(binary[seed]==0||labels[seed]!=0)continue;
                label++;int read=0,write=1;queue[0]=seed;labels[seed]=label;
                int minX=w,minY=h,maxX=0,maxY=0;var boundary=new List<P2>();
                while(read<write)
                {
                    int p=queue[read++],x=p%w,y=p/w;
                    minX=Math.Min(minX,x);maxX=Math.Max(maxX,x);minY=Math.Min(minY,y);maxY=Math.Max(maxY,y);
                    bool edge=false;
                    for(int d=0;d<4;d++)
                    {
                        int nx=x+(d==0?-1:d==1?1:0),ny=y+(d==2?-1:d==3?1:0);
                        if(nx<0||nx>=w||ny<0||ny>=h){edge=true;continue;}
                        int q=ny*w+nx;
                        if(binary[q]==0){edge=true;continue;}
                        if(labels[q]==0){labels[q]=label;queue[write++]=q;}
                    }
                    if(edge)boundary.Add(new P2(x,y));
                }
                if(write<65||maxX-minX<24||maxY-minY<24||minX==0||minY==0||maxX==w-1||maxY==h-1)continue;
                var hull=Hull(boundary);if(hull.Count<4)continue;
                while(hull.Count>4)
                {
                    int remove=0;double smallest=double.MaxValue;
                    for(int i=0;i<hull.Count;i++)
                    {
                        double area=Math.Abs(Cross(hull[(i+hull.Count-1)%hull.Count],hull[i],hull[(i+1)%hull.Count]));
                        if(area<smallest){smallest=area;remove=i;}
                    }
                    hull.RemoveAt(remove);
                }
                double areaQuad=Area(hull);
                if(areaQuad<500||areaQuad>w*h*.9)continue;
                double minSide=double.MaxValue,maxSide=0;
                for(int i=0;i<4;i++){double side=(hull[i]-hull[(i+1)%4]).Length;minSide=Math.Min(minSide,side);maxSide=Math.Max(maxSide,side);}
                if(minSide<20||minSide/maxSide<.25)continue;
                P2[] quad=hull.ToArray();
                if(!Homography.TryFit(Homography.UnitSquare,quad,out var transform))continue;
                if(!Decode(gray,transform,out int rotations))continue;
                var canonical=new P2[4];
                // Rotating sampled cells clockwise makes new top-left the old bottom-left.
                for(int i=0;i<4;i++)canonical[i]=quad[(i-rotations+8)%4];
                if(best==null||areaQuad>best.Area)best=new Aruco23Detection {Corners=canonical,Area=areaQuad};
            }
            return best;
        }

        bool Decode(byte[] gray,double[] h,out int rotations)
        {
            rotations=0;var means=new double[36];double dark=255,light=0;
            for(int y=0;y<6;y++)for(int x=0;x<6;x++)
            {
                double sum=0;
                foreach(double dy in new[]{-.15,0,.15})foreach(double dx in new[]{-.15,0,.15})
                {
                    var p=Homography.Project(h,new P2((x+.5+dx)/6-.5,(y+.5+dy)/6-.5));
                    int px=(int)Math.Round(p.X),py=(int)Math.Round(p.Y);
                    if(px<0||px>=width||py<0||py>=height)return false;
                    sum+=gray[py*width+px];
                }
                means[y*6+x]=sum/9;dark=Math.Min(dark,means[y*6+x]);light=Math.Max(light,means[y*6+x]);
            }
            if(light-dark<45)return false;
            double threshold=(dark+light)*.5;
            for(int y=0;y<6;y++)for(int x=0;x<6;x++)
                if((x==0||x==5||y==0||y==5)&&means[y*6+x]>threshold)return false;
            var cells=new bool[4,4];for(int y=0;y<4;y++)for(int x=0;x<4;x++)cells[y,x]=means[(y+1)*6+x+1]>threshold;
            for(int rotation=0;rotation<4;rotation++)
            {
                bool matches=true;
                for(int y=0;y<4;y++)for(int x=0;x<4;x++)if(cells[y,x]!=(CanonicalBits[y*4+x]=='1'))matches=false;
                if(matches){rotations=rotation;return true;}
                var rotated=new bool[4,4];for(int y=0;y<4;y++)for(int x=0;x<4;x++)rotated[y,x]=cells[3-x,y];cells=rotated;
            }
            return false;
        }

        static double Cross(P2 a,P2 b,P2 c)=>(b.X-a.X)*(c.Y-a.Y)-(b.Y-a.Y)*(c.X-a.X);
        static double Area(List<P2> p){double v=0;for(int i=0;i<p.Count;i++){var a=p[i];var b=p[(i+1)%p.Count];v+=a.X*b.Y-a.Y*b.X;}return Math.Abs(v)*.5;}
        static List<P2> Hull(List<P2> points)
        {
            points.Sort((a,b)=>a.X==b.X?a.Y.CompareTo(b.Y):a.X.CompareTo(b.X));
            var result=new List<P2>();
            foreach(var p in points){while(result.Count>=2&&Cross(result[result.Count-2],result[result.Count-1],p)<=0)result.RemoveAt(result.Count-1);result.Add(p);}
            int lower=result.Count;
            for(int i=points.Count-2;i>=0;i--){var p=points[i];while(result.Count>lower&&Cross(result[result.Count-2],result[result.Count-1],p)<=0)result.RemoveAt(result.Count-1);result.Add(p);}
            if(result.Count>1)result.RemoveAt(result.Count-1);return result;
        }
    }
}
