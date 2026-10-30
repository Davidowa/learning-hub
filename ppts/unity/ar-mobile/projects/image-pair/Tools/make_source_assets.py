"""Regenerate reference images, metadata, materials, prefabs, libraries and source scenes."""
from pathlib import Path
import json,random,uuid,struct
from PIL import Image, ImageDraw, ImageFont
ROOT=Path(__file__).resolve().parents[1]
CONFIG=json.loads((ROOT/'Tools/project.json').read_text())
N=CONFIG['practice'];NAMES=['cubo'] if N==1 else ['cubo','esfera']

def guid(path):
 return uuid.uuid5(uuid.NAMESPACE_URL,'learninghub/'+CONFIG['slug']+'/'+str(path)).hex

def write(path,text):
 p=ROOT/path;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(text)

def meta(path,kind='DefaultImporter'):
 write(str(path)+'.meta','fileFormatVersion: 2\nguid: '+guid(path)+'\n'+kind+':\n  externalObjects: {}\n  userData: \n  assetBundleName: \n  assetBundleVariant: \n')

def script_meta(path):
 write(str(path)+'.meta','fileFormatVersion: 2\nguid: '+guid(path)+'\nMonoImporter:\n  externalObjects: {}\n  serializedVersion: 2\n  defaultReferences: []\n  executionOrder: 0\n  icon: {instanceID: 0}\n  userData: \n  assetBundleName: \n  assetBundleVariant: \n')

HEADER='%YAML 1.1\n%TAG !u! tag:unity3d.com,2011:\n'

def go(fid,name,components):
 return f'''--- !u!1 &{fid}
GameObject:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {{fileID: 0}}
  m_PrefabInstance: {{fileID: 0}}
  m_PrefabAsset: {{fileID: 0}}
  serializedVersion: 6
  m_Component:
'''+''.join(f'  - component: {{fileID: {x}}}\n' for x in components)+f'''  m_Layer: 0
  m_Name: {name}
  m_TagString: {'MainCamera' if name=='AR Camera' else 'Untagged'}
  m_Icon: {{fileID: 0}}
  m_NavMeshLayer: 0
  m_StaticEditorFlags: 0
  m_IsActive: 1
'''

def transform(fid,obj,parent=0,children=(),pos=(0,0,0),scale=(1,1,1)):
 return f'''--- !u!4 &{fid}
Transform:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {{fileID: 0}}
  m_PrefabInstance: {{fileID: 0}}
  m_PrefabAsset: {{fileID: 0}}
  m_GameObject: {{fileID: {obj}}}
  serializedVersion: 2
  m_LocalRotation: {{x: 0, y: 0, z: 0, w: 1}}
  m_LocalPosition: {{x: {pos[0]}, y: {pos[1]}, z: {pos[2]}}}
  m_LocalScale: {{x: {scale[0]}, y: {scale[1]}, z: {scale[2]}}}
  m_ConstrainProportionsScale: 0
  m_Children:{' []' if not children else ''}
'''+''.join(f'  - {{fileID: {x}}}\n' for x in children)+f'''  m_Father: {{fileID: {parent}}}
  m_LocalEulerAnglesHint: {{x: 0, y: 0, z: 0}}
'''

def mono(fid,obj,script,fields=''):
 return f'''--- !u!114 &{fid}
MonoBehaviour:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {{fileID: 0}}
  m_PrefabInstance: {{fileID: 0}}
  m_PrefabAsset: {{fileID: 0}}
  m_GameObject: {{fileID: {obj}}}
  m_Enabled: 1
  m_EditorHideFlags: 0
  m_Script: {{fileID: 11500000, guid: {script}, type: 3}}
  m_Name: 
  m_EditorClassIdentifier: 
'''+fields

# Stable package script GUIDs taken from official AR Foundation and XR Core Utils metadata.
SCRIPTS={'session':'3859a92a05d4f5d418cb6ca605290e74','input':'fa850fbd5b8aded44846f96e35f1a9f5','origin':'e0cb9aa70a22847b5925ee5f067c10a9','manager':'4dea56a9eaadd1c439095de4f9a371cb','camera':'4966719baa26e4b0e8231a24d9bd491a','background':'816b289ef451e094f9ae174fb4cf8db0','library':'848409ee8ba454f42a5ddff137688a27'}

for path in sorted((ROOT/'Assets').rglob('*.cs')):script_meta(path.relative_to(ROOT).as_posix())
for name in NAMES:
 rng=random.Random(4738 if name=='cubo' else 9217)
 im=Image.new('RGB',(1024,1024),'#faf9f3');d=ImageDraw.Draw(im)
 palette=['#182932','#753a21','#304933','#273d5a','#3a242d'] if name=='cubo' else ['#123f4b','#463541','#5f331e','#29361d','#2b334d']
 d.rectangle((18,18,1005,1005),outline=palette[0],width=16)
 for i in range(240):
  x=rng.randint(55,969); y=rng.randint(190,927);size=rng.randint(9,35);color=rng.choice(palette)
  if i%4==0:d.ellipse((x-size,y-size,x+size,y+size),outline=color,width=rng.randint(5,12))
  elif i%4==1:d.polygon([(x-size,y+size),(x+size,y-size),(x+size,y+size)],fill=color)
  elif i%4==2:d.rectangle((x-size,y-size,x+size,y+size),fill=color)
  else:d.line([(x-size,y-size),(x+size,y+size),(x-size,y+size)],fill=color,width=8)
 fontpath='/System/Library/Fonts/Supplemental/Arial Bold.ttf'
 try:font=ImageFont.truetype(fontpath,90)
 except OSError:font=ImageFont.load_default(size=90)
 d.rectangle((42,42,982,166),fill='#faf9f3');d.text((65,53),name.upper()+' / AR',font=font,fill=palette[0])
 path=f'Assets/Blancos/{name}.png';im.save(ROOT/path)
 write(path+'.meta','fileFormatVersion: 2\nguid: '+guid(path)+'''\nTextureImporter:
  serializedVersion: 13
  mipmaps:
    enableMipMap: 0
  isReadable: 1
  textureType: 0
  textureShape: 1
  maxTextureSize: 1024
  textureCompression: 0
  sRGBTexture: 1
  alphaIsTransparency: 0
  userData: 
  assetBundleName: 
  assetBundleVariant: 
''')
 color=(1,.4,.08) if name=='cubo' else (.15,.55,1)
 mat=f'Assets/Materials/{name}.mat'
 write(mat,HEADER+f'''--- !u!21 &2100000
Material:
  serializedVersion: 8
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {{fileID: 0}}
  m_PrefabInstance: {{fileID: 0}}
  m_PrefabAsset: {{fileID: 0}}
  m_Name: {name}
  m_Shader: {{fileID: 4800000, guid: 933532a4fcc9baf4fa0491de14d08ed7, type: 3}}
  m_Parent: {{fileID: 0}}
  m_ValidKeywords: []
  m_InvalidKeywords: []
  m_LightmapFlags: 4
  m_EnableInstancingVariants: 0
  m_DoubleSidedGI: 0
  m_CustomRenderQueue: -1
  stringTagMap: {{}}
  disabledShaderPasses: []
  m_SavedProperties:
    serializedVersion: 3
    m_TexEnvs: []
    m_Ints: []
    m_Floats:
    - _Surface: 0
    - _Metallic: 0
    - _Smoothness: 0.35
    m_Colors:
    - _BaseColor: {{r: {color[0]}, g: {color[1]}, b: {color[2]}, a: 1}}
    - _Color: {{r: {color[0]}, g: {color[1]}, b: {color[2]}, a: 1}}
''');meta(mat,'NativeFormatImporter')
 prefab=f'Assets/Prefabs/Contenido{name.title()}.prefab';mesh=10202 if name=='cubo' else 10207
 text=HEADER+go(100000,'Contenido'+name.title(),[400000])+transform(400000,100000,children=[400001])+go(100001,name.title(),[400001,3300000,2300000])+transform(400001,100001,400000,pos=(0,.025,0),scale=(.05,.05,.05))
 text+=f'''--- !u!33 &3300000
MeshFilter:
  m_ObjectHideFlags: 0
  m_GameObject: {{fileID: 100001}}
  m_Mesh: {{fileID: {mesh}, guid: 0000000000000000e000000000000000, type: 0}}
--- !u!23 &2300000
MeshRenderer:
  m_ObjectHideFlags: 0
  m_GameObject: {{fileID: 100001}}
  m_Enabled: 1
  m_CastShadows: 1
  m_ReceiveShadows: 1
  m_LightProbeUsage: 1
  m_ReflectionProbeUsage: 1
  m_RenderingLayerMask: 1
  m_Materials:
  - {{fileID: 2100000, guid: {guid(mat)}, type: 2}}
  m_SortingLayerID: 0
  m_SortingOrder: 0
'''
 write(prefab,text);meta(prefab,'PrefabImporter')

def guid_parts(value):
 b=uuid.UUID(hex=value).bytes_le
 return int.from_bytes(b[:8],'little'),int.from_bytes(b[8:],'little')
libpath='Assets/Resources/'+CONFIG['library']+'.asset'
lo,hi=guid_parts(guid(libpath))
text=HEADER+mono(11400000,0,SCRIPTS['library'],f'  m_GuidLow: {lo}\n  m_GuidHigh: {hi}\n  m_DataStore:\n    m_Storage: []\n  m_Images:\n')
for name in NAMES:
 low,high=guid_parts(guid('reference/'+name));tlow,thigh=guid_parts(guid(f'Assets/Blancos/{name}.png'))
 text+=f'''  - m_SerializedGuid:
      m_GuidLow: {low}
      m_GuidHigh: {high}
    m_SerializedTextureGuid:
      m_GuidLow: {tlow}
      m_GuidHigh: {thigh}
    m_Size: {{x: 0.16, y: 0.16}}
    m_SpecifySize: 1
    m_Name: {name}
    m_Texture: {{fileID: 2800000, guid: {guid(f'Assets/Blancos/{name}.png')}, type: 3}}
'''
text=text.replace('  m_Name: \n', '  m_Name: '+CONFIG['library']+'\n', 1)
write(libpath,text);meta(libpath,'NativeFormatImporter')
scene=HEADER+go(1000,'AR Session',[1001,1002,1003])+transform(1001,1000)+mono(1002,1000,SCRIPTS['session'],'  m_AttemptUpdate: 1\n  m_MatchFrameRate: 1\n  m_TrackingMode: 2\n')+mono(1003,1000,SCRIPTS['input'])
scene+=go(2000,'XR Origin',[2001,2002,2003,2004])+transform(2001,2000,children=[3001])+mono(2002,2000,SCRIPTS['origin'],'  m_Camera: {fileID: 4002}\n  m_OriginBaseGameObject: {fileID: 2000}\n  m_CameraFloorOffsetObject: {fileID: 3000}\n  m_RequestedTrackingOriginMode: 1\n  m_CameraYOffset: 0\n')
scene+=mono(2003,2000,SCRIPTS['manager'],f'  m_SerializedLibrary: {{fileID: 11400000, guid: {guid(libpath)}, type: 2}}\n  m_MaxNumberOfMovingImages: {N}\n  m_TrackedImagePrefab: {{fileID: 0}}\n')
fields='  images: {fileID: 2003}\n  bindings:\n'
for name in NAMES:fields+=f'  - imageName: {name}\n    prefab: {{fileID: 100000, guid: {guid(f"Assets/Prefabs/Contenido{name.title()}.prefab")}, type: 3}}\n'
scene+=mono(2004,2000,guid('Assets/Scripts/ImageContentController.cs'),fields)
scene+=go(3000,'Camera Offset',[3001])+transform(3001,3000,2001,children=[4001])+go(4000,'AR Camera',[4001,4002,4003,4004,4005])+transform(4001,4000,3001)
scene+='''--- !u!20 &4002
Camera:
  m_ObjectHideFlags: 0
  m_GameObject: {fileID: 4000}
  m_Enabled: 1
  serializedVersion: 2
  m_ClearFlags: 2
  m_BackGroundColor: {r: 0.07, g: 0.09, b: 0.12, a: 1}
  m_projectionMatrixMode: 1
  m_GateFitMode: 2
  m_FOVAxisMode: 0
  m_NormalizedViewPortRect:
    serializedVersion: 2
    x: 0
    y: 0
    width: 1
    height: 1
  near clip plane: 0.01
  far clip plane: 20
  field of view: 60
  orthographic: 0
  orthographic size: 5
  m_Depth: -1
  m_CullingMask:
    serializedVersion: 2
    m_Bits: 4294967295
  m_RenderingPath: -1
  m_TargetTexture: {fileID: 0}
  m_TargetDisplay: 0
  m_TargetEye: 3
  m_HDR: 0
  m_AllowMSAA: 1
  m_AllowDynamicResolution: 0
  m_OcclusionCulling: 1
--- !u!81 &4003
AudioListener:
  m_ObjectHideFlags: 0
  m_GameObject: {fileID: 4000}
  m_Enabled: 1
'''
scene+=mono(4004,4000,SCRIPTS['camera'],'  m_AutoFocus: 1\n  m_LightEstimation: 0\n  m_FacingDirection: 1\n')+mono(4005,4000,SCRIPTS['background'])
# The Editor setup adds and serializes Input System pose bindings on first import.
scene+=go(5000,'Luz direccional',[5001,5002])+transform(5001,5000)+'''--- !u!108 &5002
Light:
  m_ObjectHideFlags: 0
  m_GameObject: {fileID: 5000}
  m_Enabled: 1
  serializedVersion: 11
  m_Type: 1
  m_Color: {r: 1, g: 0.97, b: 0.93, a: 1}
  m_Intensity: 1
  m_Range: 10
  m_CullingMask:
    serializedVersion: 2
    m_Bits: 4294967295
'''
scene+='''--- !u!1660057539 &9223372036854775807
SceneRoots:
  m_ObjectHideFlags: 0
  m_Roots:
  - {fileID: 1001}
  - {fileID: 2001}
  - {fileID: 5001}
'''
scenepath=f'Assets/Scenes/Practica{N}AR.unity';write(scenepath,scene);meta(scenepath)
previewpath='Assets/Scenes/VistaPrevia.unity'
fields='  prefabs:\n'+''.join(f'  - {{fileID: 100000, guid: {guid(f"Assets/Prefabs/Contenido{name.title()}.prefab")}, type: 3}}\n' for name in NAMES)+'  markers:\n'+''.join(f'  - {{fileID: 2800000, guid: {guid(f"Assets/Blancos/{name}.png")}, type: 3}}\n' for name in NAMES)
text=HEADER+go(1000,'Vista previa de contenido',[1001,1002])+transform(1001,1000)+mono(1002,1000,guid('Assets/Scripts/ImageContentPreview.cs'),fields)+'''--- !u!1660057539 &9223372036854775807
SceneRoots:
  m_ObjectHideFlags: 0
  m_Roots:
  - {fileID: 1001}
'''
write(previewpath,text);meta(previewpath)
write('ProjectSettings/EditorBuildSettings.asset',HEADER+f'''--- !u!1045 &1
EditorBuildSettings:
  m_ObjectHideFlags: 0
  serializedVersion: 2
  m_Scenes:
  - enabled: 1
    path: {scenepath}
    guid: {guid(scenepath)}
  m_configObjects: {{}}
''')
print(f'Práctica {N}: {len(NAMES)} imágenes, prefabs y biblioteca; escena AR y vista previa.')
