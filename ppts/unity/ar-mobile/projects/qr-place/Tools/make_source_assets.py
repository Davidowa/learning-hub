"""Generate stable Unity metadata and the bootstrap scene without opening Unity."""
from pathlib import Path
import uuid

ROOT=Path(__file__).resolve().parents[1]
def guid(path):
    return uuid.uuid5(uuid.NAMESPACE_URL,'learninghub/qr-place/'+path.as_posix()).hex
for path in sorted((ROOT/'Assets').rglob('*.cs')):
    path.with_suffix(path.suffix+'.meta').write_text(
        'fileFormatVersion: 2\nguid: '+guid(path.relative_to(ROOT))+'\nMonoImporter:\n'
        '  externalObjects: {}\n  serializedVersion: 2\n  defaultReferences: []\n'
        '  executionOrder: 0\n  icon: {instanceID: 0}\n  userData: \n'
        '  assetBundleName: \n  assetBundleVariant: \n')
script=guid(Path('Assets/Scripts/QrPlacementBootstrap.cs'))
scene=ROOT/'Assets/Scenes/QrPlacement.unity'
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
  m_Name: QR AR
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
  m_Script: {fileID: 11500000, guid: '''+script+''', type: 3}
  m_Name: 
  m_EditorClassIdentifier: 
  simulateInEditor: 1
--- !u!1660057539 &9223372036854775807
SceneRoots:
  m_ObjectHideFlags: 0
  m_Roots:
  - {fileID: 1001}
''')
scene.with_suffix('.unity.meta').write_text('fileFormatVersion: 2\nguid: '+guid(Path('Assets/Scenes/QrPlacement.unity'))+'\nDefaultImporter:\n  externalObjects: {}\n  userData: \n  assetBundleName: \n  assetBundleVariant: \n')
print(scene)

# Stable metadata for directories and non-script source assets. Unity configures textures on first import.
for path in sorted((ROOT/'Assets').rglob('*')):
    if path.suffix in ('.meta', '.png', '.dll') or path.with_suffix(path.suffix+'.meta').exists(): continue
    path.with_suffix(path.suffix+'.meta').write_text('fileFormatVersion: 2\nguid: '+guid(path.relative_to(ROOT))+'\n'+('folderAsset: yes\n' if path.is_dir() else '')+'DefaultImporter:\n  externalObjects: {}\n  userData: \n  assetBundleName: \n  assetBundleVariant: \n')
