"""Package Unity 6.3 source projects using an official XRI 3.3.2 package.

The editor setup builds and saves each authoring scene on first import. Generated
projects and ZIPs live outside the repository; no Unity installation is assumed.
"""
from pathlib import Path
import argparse
import hashlib
import json
import shutil
import uuid
import zipfile

KIT = Path(__file__).resolve().parent
LABS = KIT.parent
VERSIONS = {
    'com.unity.inputsystem': '1.11.2',
    'com.unity.xr.interaction.toolkit': '3.3.2',
    'com.unity.xr.openxr': '1.16.1',
    'com.unity.xr.core-utils': '2.5.1',
    'com.unity.xr.management': '4.5.3',
    'com.unity.render-pipelines.universal': '17.3.0',
    'com.unity.ugui': '2.0.0',
    'com.unity.modules.audio': '1.0.0',
    'com.unity.modules.imgui': '1.0.0',
    'com.unity.modules.physics': '1.0.0',
    'com.unity.modules.ui': '1.0.0',
    'com.unity.modules.uielements': '1.0.0',
    'com.unity.modules.xr': '1.0.0',
    'com.unity.modules.androidjni': '1.0.0',
}
TITLES = {0:'Primer montaje XR y torquimetro',1:'Presencia escala y seguimiento',2:'Interaccion y retroalimentacion',
          3:'Locomocion y orientacion espacial',4:'Opcional - Cibermareo y comodidad'}


def guid(name):
    return uuid.uuid5(uuid.NAMESPACE_URL, 'learning-hub-vr/'+name).hex


def own_metas(root):
    for p in sorted((root/'Assets').rglob('*')):
        meta = p.with_name(p.name+'.meta')
        if p.suffix == '.meta' or meta.exists():
            continue
        identity = guid(str(p.relative_to(root)))
        if p.is_dir():
            meta.write_text(f'fileFormatVersion: 2\nguid: {identity}\nfolderAsset: yes\nDefaultImporter:\n  externalObjects: {{}}\n')
        elif p.suffix == '.cs':
            meta.write_text(f'fileFormatVersion: 2\nguid: {identity}\nMonoImporter:\n  externalObjects: {{}}\n  serializedVersion: 2\n  defaultReferences: []\n  executionOrder: 0\n  icon: {{instanceID: 0}}\n  userData: \n  assetBundleName: \n  assetBundleVariant: \n')
        else:
            meta.write_text(f'fileFormatVersion: 2\nguid: {identity}\nDefaultImporter:\n  externalObjects: {{}}\n')


def package(xri, output, selected_lab=None):
    package_info = json.loads((xri/'package.json').read_text())
    if package_info['name'] != 'com.unity.xr.interaction.toolkit' or package_info['version'] != '3.3.2':
        raise ValueError('Use el paquete oficial XRI 3.3.2.')
    output.mkdir(parents=True, exist_ok=True)
    for lab,title in TITLES.items():
        if selected_lab is not None and lab != selected_lab:
            continue
        code = f'VR-C0{lab}'
        scene_name = code + ('-Opcional' if lab == 4 else '')
        root = output/(code+' - Proyecto Unity 6.3 URP')
        if root.exists():
            raise FileExistsError(f'No se sobrescribe un proyecto existente: {root}')
        for folder in ['Assets/Editor','Assets/Scripts','Assets/Scenes','Packages','ProjectSettings','Documentacion','Licencias']:
            (root/folder).mkdir(parents=True,exist_ok=True)
        for sample in ['Starter Assets','XR Interaction Simulator']:
            dest = root/'Assets/Samples/XR Interaction Toolkit/3.3.2'/sample
            shutil.copytree(xri/'Samples~'/sample,dest)
        for source in (LABS/'scripts').glob('*.cs'):
            shutil.copy2(source,root/'Assets/Scripts'/source.name)
        for source in KIT.glob('*.cs'):
            (root/'Assets/Editor'/source.name).write_text(source.read_text().replace('__LAB__',str(lab)).replace('__SCENE__',scene_name))
        (root/'Packages/manifest.json').write_text(json.dumps({'dependencies':VERSIONS},indent=2)+'\n')
        (root/'ProjectSettings/ProjectVersion.txt').write_text('m_EditorVersion: 6000.3.27f1\nm_EditorVersionWithRevision: 6000.3.27f1 (672d562a42a7)\n')
        (root/'ProjectSettings/ProjectSettings.asset').write_text(f'''%YAML 1.1
%TAG !u! tag:unity3d.com,2011:
--- !u!129 &1
PlayerSettings:
  m_ObjectHideFlags: 0
  serializedVersion: 28
  companyName: Learning Hub
  productName: Laboratorio {code}
  bundleVersion: 1.0
  activeInputHandler: 1
  applicationIdentifier:
    Android: edu.learninghub.vrc0{lab}
  AndroidMinSdkVersion: 29
  AndroidTargetSdkVersion: 0
  AndroidTargetArchitectures: 2
  scriptingBackend:
    Android: 1
''')
        (root/'ProjectSettings/EditorBuildSettings.asset').write_text('''%YAML 1.1
%TAG !u! tag:unity3d.com,2011:
--- !u!1045 &1
EditorBuildSettings:
  m_ObjectHideFlags: 0
  serializedVersion: 2
  m_Scenes: []
  m_configObjects: {}
''')
        pdf = next((LABS/'output/pdf').glob(code+'*.pdf'))
        shutil.copy2(pdf,root/'Documentacion'/pdf.name)
        source = next(LABS.glob(code+'*.es.md'))
        shutil.copy2(source,root/'Documentacion'/source.name)
        for name in ['LICENSE.md','Third Party Notices.md','ThirdPartyNotices.md']:
            if (xri/name).exists():shutil.copy2(xri/name,root/'Licencias'/name)
        (root/'Licencias/PROCEDENCIA.md').write_text('''# Procedencia de los recursos

Los dos samples proceden del paquete oficial com.unity.xr.interaction.toolkit 3.3.2 publicado por Unity. Se conservaron los assets, sus archivos .meta y las licencias disponibles del paquete. Su uso sigue sujeto a esas licencias y depende de Unity.

Los paquetes de Unity se descargan desde sus registros al abrir el proyecto. Los recursos esenciales de TextMeshPro se importan desde la instalación de UGUI mediante la API del Editor, sin servicios de conversión externos.
''')
        readme = f'''# {code}: {title.replace('Opcional - ', '')}

Este ZIP contiene un proyecto fuente de Unity 6.3 con URP para Meta Quest 3S. Incluye los scripts del laboratorio, los samples oficiales de XRI 3.3.2, la guía y un asistente del Editor que construye y guarda la escena. No contiene un APK ni una compilación ya probada.

## Abrir y preparar

1. Extrae todo el ZIP en una carpeta nueva. En Unity Hub usa Add > Add project from disk y selecciona la carpeta que contiene Assets, Packages y ProjectSettings.
2. Abre con Unity 6.3 LTS. La referencia es 6000.3.27f1; instala Android Build Support, Android SDK & NDK Tools y OpenJDK en ese Editor.
3. Espera la resolución de paquetes y la compilación. El asistente importa TMP Essential Resources si faltan, configura URP y OpenXR para Android, construye la escena y la guarda como Assets/Scenes/{scene_name}.unity. La escena se genera en ese primer arranque, no está prerenderizada dentro del ZIP.
4. Si no termina, revisa Console. Después de resolver el error, usa Tools > Learning Hub VR > Preparar proyecto. La opción reconstruye la escena de ejemplo y pide confirmar cuando ya existe una preparación; guarda una copia de tus modificaciones.
5. Abre la escena generada y verifica la jerarquía. El proyecto usa un XR Interaction Simulator marcado EditorOnly. No actives además la instancia automática del simulador, porque aparecerían dos. Ese objeto se excluye de la compilación para el visor.
6. En XR Plug-in Management > Project Validation revisa Android. Aplica el Fix de Starter Assets para nombrar Teleport a Interaction Layer 31 si se solicita. Se usa ese bit para las superficies y los rayos de teletransporte.
7. Pulsa Play y da foco a Game. Usa la ayuda del simulador. Compara la configuración con los pasos de la guía en Documentacion. Los objetos y los eventos se crean como objetos editables de la escena, no solamente durante Play.

## Probar en Quest 3S

Selecciona Meta Quest en File > Build Profiles y cambia a esa plataforma. El asistente configura Android con OpenXR 1.16.1, Meta Quest Support, Oculus Touch Controller Profile, Vulkan, IL2CPP y ARM64. Revisa los overrides del perfil, la lista de escenas y Project Validation antes de Build And Run. La lista debe tener solo la escena {scene_name}. Autoriza la depuración USB en el visor y utiliza un cable de datos.

La guía explica las comprobaciones y los resultados esperados. La simulación del Editor no verifica seguimiento físico ni comodidad. {'Este laboratorio es opcional y no requiere activar movimiento continuo en el visor.' if lab==4 else 'Registra por separado simulación, resultados físicos y pruebas pendientes.'}

## Contenido y límites

El asistente utiliza URP 17.3.0, XRI 3.3.2, OpenXR 1.16.1 y Unity UI 2.0.0. El montaje es independiente: este proyecto ya incluye {'el banco y el torquímetro con agarre y diagnóstico XR' if lab==0 else 'las interacciones y la sala base' if lab>=2 else 'la sala base'}. {'Incluye también los destinos y el panel XR.' if lab>=3 else ''}

Se revisaron el inventario del ZIP, la sintaxis de los scripts y las APIs utilizadas frente al código oficial. No se ejecutó Unity ni se probó un Quest 3S durante la preparación. La importación, la compilación de Unity y la prueba del APK siguen pendientes; informa cualquier error de Console con la versión del Editor.

Conserva Assets, Packages y ProjectSettings. Library, Temp, Logs y Obj se generan localmente y no se incluyen.
'''
        (root/'LEEME.md').write_text(readme)
        own_metas(root)
        archive=output/f'Laboratorio {code} - {title} - Proyecto Unity 6.3 URP.zip'
        with zipfile.ZipFile(archive,'w',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
            for f in sorted(root.rglob('*')):
                if f.is_file():z.write(f,f.relative_to(output))
        with zipfile.ZipFile(archive) as z:
            if z.testzip() is not None:raise ValueError('ZIP corrupto')
        print(archive, archive.stat().st_size,hashlib.sha256(archive.read_bytes()).hexdigest())


if __name__=='__main__':
    args=argparse.ArgumentParser()
    args.add_argument('--xri-package',type=Path,required=True)
    args.add_argument('--output-dir',type=Path,required=True)
    args.add_argument('--lab',type=int,choices=range(5))
    a=args.parse_args();package(a.xri_package,a.output_dir,a.lab)
