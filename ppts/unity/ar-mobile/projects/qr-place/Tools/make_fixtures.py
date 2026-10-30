from pathlib import Path
import json,qrcode,cv2,numpy as np
from PIL import Image
root=Path(__file__).resolve().parents[1];out=root/'Validation/Fixtures';out.mkdir(parents=True,exist_ok=True)
cases=[]
for label,payload in [('Cube','AR:CUBO'),('Sphere','AR:ESFERA'),('Unknown','https://example.com')]:
 qr=qrcode.QRCode(version=None,error_correction=qrcode.constants.ERROR_CORRECT_Q,box_size=16,border=4);qr.add_data(payload);qr.make(fit=True)
 image=qr.make_image(fill_color='black',back_color='white').convert('L')
 if label!='Unknown':
  image.save(root/f'Assets/Resources/Qr{label}.png');image.save(root/f'Marcadores/QR-{label.lower()}.png')
 array=np.array(image);n=len(array)
 for rotation in ([0,1,2,3] if label!='Unknown' else [0]):
  rotated=np.rot90(array,rotation).copy();quad=np.float32([[160,80],[480,80],[480,400],[160,400]])
  h=cv2.getPerspectiveTransform(np.float32([[0,0],[n-1,0],[n-1,n-1],[0,n-1]]),quad)
  frame=cv2.warpPerspective(rotated,h,(640,480),borderValue=255)
  name=f'{label.lower()}-r{rotation}';(out/f'{name}.gray').write_bytes(frame.tobytes());Image.fromarray(frame).save(out/f'{name}.png');cases.append(dict(name=name,payload=payload))
  if rotation==0 and label!='Unknown':
   quad=np.float32([[170,90],[480,120],[460,390],[150,360]])
   h=cv2.getPerspectiveTransform(np.float32([[0,0],[n-1,0],[n-1,n-1],[0,n-1]]),quad)
   frame=cv2.warpPerspective(array,h,(640,480),borderValue=255);frame=cv2.GaussianBlur(frame,(3,3),.6)
   name=f'{label.lower()}-perspective';(out/f'{name}.gray').write_bytes(frame.tobytes());Image.fromarray(frame).save(out/f'{name}.png');cases.append(dict(name=name,payload=payload))
(out/'blank.gray').write_bytes(bytes([255])*640*480);cases.append(dict(name='blank',payload=None))
(out/'cases.json').write_text(json.dumps(cases,indent=2))
print('Generated',len(cases),'QR cases.')
