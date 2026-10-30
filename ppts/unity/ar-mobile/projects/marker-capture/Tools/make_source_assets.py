"""Regenerate the original test marker, Unity metadata and bootstrap scene."""
from pathlib import Path
import random
import uuid
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
RESOURCE = ROOT / 'Assets/Resources'
RESOURCE.mkdir(parents=True, exist_ok=True)
rng = random.Random(1456)
image = Image.new('RGB', (1024, 1024), 'white')
draw = ImageDraw.Draw(image)
draw.rectangle((24, 24, 999, 999), outline='#122735', width=20)
# Asymmetric, non-repeating geometry gives the tracker corners at several scales.
for i in range(185):
    x, y = rng.randint(65, 950), rng.randint(195, 890)
    size = rng.randint(10, 52)
    color = rng.choice(['#132a38', '#172a39', '#8d2e22', '#19383a', '#425137'])
    if i % 3 == 0:
        draw.ellipse((x-size,y-size,x+size,y+size), outline=color, width=rng.randint(5,14))
    elif i % 3 == 1:
        draw.polygon([(x-size,y+size),(x,y-size),(x+size,y+size)], fill=color)
    else:
        draw.rectangle((x-size,y-size,x+size,y+size), fill=color)
        draw.line((x-size,y,x+size,y),fill='white',width=5)
font_path = '/System/Library/Fonts/Supplemental/Arial Bold.ttf'
try:
    title_font=ImageFont.truetype(font_path,76)
    small_font=ImageFont.truetype(font_path,37)
except OSError:
    title_font=ImageFont.load_default(size=76)
    small_font=ImageFont.load_default(size=37)
draw.rectangle((55,55,970,173),fill='white')
draw.text((72,65),'CAPTURA AR / 01',font=title_font,fill='#122735')
draw.rectangle((55,895,970,968),fill='white')
draw.text((73,906),'BLANCO  |  IMAGEN DE PRUEBA',font=small_font,fill='#122735')
image.save(RESOURCE/'Marker.png')

def guid(path):
    return uuid.uuid5(uuid.NAMESPACE_URL,'learninghub/ar-capture/'+path.as_posix()).hex

for path in sorted((ROOT/'Assets').rglob('*.cs')):
    rel=path.relative_to(ROOT)
    path.with_suffix(path.suffix+'.meta').write_text(
        'fileFormatVersion: 2\nguid: '+guid(rel)+'\nMonoImporter:\n'
        '  externalObjects: {}\n  serializedVersion: 2\n  defaultReferences: []\n'
        '  executionOrder: 0\n  icon: {instanceID: 0}\n  userData: \n'
        '  assetBundleName: \n  assetBundleVariant: \n')
script_guid=guid(Path('Assets/Scripts/CaptureBootstrap.cs'))
scene=ROOT/'Assets/Scenes/Capture.unity'
scene.write_text('''%YAML 1.1
%TAG !u! tag:unity3d.com,2011:
--- !u!1 &1000
GameObject:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {fileID: 0}
  m_PrefabInstance: {fileID: 0}
  m_PrefabAsset: {fileID: 0}
  serializedVersion: 6
  m_Component:
  - component: {fileID: 1001}
  - component: {fileID: 1002}
  m_Layer: 0
  m_Name: Captura AR
  m_TagString: Untagged
  m_Icon: {fileID: 0}
  m_NavMeshLayer: 0
  m_StaticEditorFlags: 0
  m_IsActive: 1
--- !u!4 &1001
Transform:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {fileID: 0}
  m_PrefabInstance: {fileID: 0}
  m_PrefabAsset: {fileID: 0}
  m_GameObject: {fileID: 1000}
  serializedVersion: 2
  m_LocalRotation: {x: 0, y: 0, z: 0, w: 1}
  m_LocalPosition: {x: 0, y: 0, z: 0}
  m_LocalScale: {x: 1, y: 1, z: 1}
  m_ConstrainProportionsScale: 0
  m_Children: []
  m_Father: {fileID: 0}
  m_LocalEulerAnglesHint: {x: 0, y: 0, z: 0}
--- !u!114 &1002
MonoBehaviour:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {fileID: 0}
  m_PrefabInstance: {fileID: 0}
  m_PrefabAsset: {fileID: 0}
  m_GameObject: {fileID: 1000}
  m_Enabled: 1
  m_EditorHideFlags: 0
  m_Script: {fileID: 11500000, guid: '''+script_guid+''', type: 3}
  m_Name: 
  m_EditorClassIdentifier: 
  simulateInEditor: 1
--- !u!1660057539 &9223372036854775807
SceneRoots:
  m_ObjectHideFlags: 0
  m_Roots:
  - {fileID: 1001}
''')
scene.with_suffix('.unity.meta').write_text('fileFormatVersion: 2\nguid: '+guid(Path('Assets/Scenes/Capture.unity'))+'\nDefaultImporter:\n  externalObjects: {}\n  userData: \n  assetBundleName: \n  assetBundleVariant: \n')
print(RESOURCE/'Marker.png')
print(scene)
