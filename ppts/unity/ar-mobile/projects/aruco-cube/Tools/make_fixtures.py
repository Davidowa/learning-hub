from pathlib import Path
import cv2,numpy as np,json,importlib.metadata
p=Path(__file__).resolve().parents[1]
(p/'Assets/Resources').mkdir(parents=True,exist_ok=True)
f=p/'Validation/Fixtures';f.mkdir(parents=True,exist_ok=True)
d=cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_50)
marker=cv2.aruco.generateImageMarker(d,23,600,borderBits=1)
cv2.imwrite(str(p/'Assets/Resources/Aruco23.png'),marker)
(p/'Marcadores').mkdir(exist_ok=True)
cv2.imwrite(str(p/'Marcadores/ArUco23-con-margen.png'),cv2.copyMakeBorder(marker,100,100,100,100,cv2.BORDER_CONSTANT,value=255))
bits=''.join(str(int(marker[(y+1)*100+50,(x+1)*100+50]>127)) for y in range(4) for x in range(4))
s=p/'Assets/Scripts/Core/Aruco23Detector.cs';s.write_text(s.read_text().replace('__BITS__',bits))
fixtures=[]
def add(name,src,quad,positive,canonical=None):
 matrix=cv2.getPerspectiveTransform(np.float32([[0,0],[599,0],[599,599],[0,599]]),np.float32(quad))
 im=cv2.warpPerspective(src,matrix,(640,480),borderValue=255)
 if name=='blur':im=cv2.GaussianBlur(im,(3,3),.7)
 if name=='low_light':im=(im.astype(float)*.5+20).astype(np.uint8)
 if name=='noise':
  rng=np.random.default_rng(77);im=np.clip(im.astype(float)+rng.normal(0,8,im.shape),0,255).astype(np.uint8)
 if name=='occluded':cv2.rectangle(im,(200,110),(335,230),255,-1)
 im.tofile(f/(name+'.gray'));cv2.imwrite(str(f/(name+'.png')),im)
 fixtures.append({'name':name,'width':640,'height':480,'positive':positive,'corners':canonical or quad})
base=[[210,120],[430,120],[430,340],[210,340]]
add('front',marker,base,True)
for k in (1,2,3):
 src=np.rot90(marker,-k).copy()
 # Source marker canonical top-left after k clockwise rotations lies at image-corner k.
 add('rot'+str(k),src,base,True,[base[(i+k)%4] for i in range(4)])
add('perspective',marker,[[195,115],[421,135],[398,338],[217,318]],True)
add('tilted',marker,[[175,165],[395,100],[458,305],[249,372]],True)
for name in ('blur','low_light','noise'):add(name,marker,base,True)
add('unknown',cv2.aruco.generateImageMarker(d,24,600,borderBits=1),base,False)
add('mirrored',np.fliplr(marker).copy(),base,False)
add('occluded',marker,base,False)
np.full((480,640),255,np.uint8).tofile(f/'blank.gray');fixtures.append({'name':'blank','width':640,'height':480,'positive':False,'corners':base})
(f/'cases.json').write_text(json.dumps(fixtures,indent=2)+'\n')
(p/'Tools').mkdir(exist_ok=True)
(p/'Tools/marker-version.txt').write_text('opencv-python-headless '+importlib.metadata.version('opencv-python-headless')+' / OpenCV '+cv2.__version__+'\nDICT_4X4_50 ID23 / white=1: '+bits+'\n')
print(len(fixtures),'fixtures; marker',bits,cv2.__version__)
