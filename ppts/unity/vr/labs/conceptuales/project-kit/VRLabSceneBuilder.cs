using System;
using System.Linq;
using TMPro;
using Unity.XR.CoreUtils;
using UnityEditor;
using UnityEditor.Events;
using UnityEditor.SceneManagement;
using UnityEngine;
using UnityEngine.EventSystems;
using UnityEngine.Rendering;
using UnityEngine.UI;
using UnityEngine.XR.Interaction.Toolkit;
using UnityEngine.XR.Interaction.Toolkit.Interactables;
using UnityEngine.XR.Interaction.Toolkit.Locomotion.Teleportation;
using UnityEngine.XR.Interaction.Toolkit.Locomotion.Turning;
using UnityEngine.XR.Interaction.Toolkit.Samples.StarterAssets;
using UnityEngine.XR.Interaction.Toolkit.UI;

public static class VRLabSceneBuilder
{
    const string Samples = "Assets/Samples/XR Interaction Toolkit/3.3.2/";
    static TMP_FontAsset font;
    static Transform environment;
    static XRInteractionManager manager;
    static GameObject rig;
    static Camera camera;
    static Material gray, pale, orange, dark;
    static readonly InteractionLayerMask TeleportMask = (InteractionLayerMask)(1 << 31);

    public static void Build(int lab, string scenePath)
    {
        var scene = EditorSceneManager.NewScene(NewSceneSetup.EmptyScene, NewSceneMode.Single);
        font = AssetDatabase.LoadAssetAtPath<TMP_FontAsset>(
            "Assets/TextMesh Pro/Resources/Fonts & Materials/LiberationSans SDF.asset");
        if (font == null) throw new InvalidOperationException("Falta LiberationSans SDF. Importa TMP Essential Resources.");
        gray = MaterialAsset("PisoGris", new Color(0.36f, 0.38f, 0.4f));
        pale = MaterialAsset("MesaClara", new Color(0.76f, 0.77f, 0.79f));
        orange = MaterialAsset("CuboNaranja", new Color(0.91f, 0.47f, 0.12f));
        dark = MaterialAsset("TextoOscuro", new Color(0.08f, 0.09f, 0.1f));
        var sun = new GameObject("Directional Light").AddComponent<Light>();
        sun.type = LightType.Directional;
        sun.intensity = 1.1f;
        sun.transform.rotation = Quaternion.Euler(45, -30, 0);
        RenderSettings.ambientMode = AmbientMode.Flat;
        RenderSettings.ambientLight = new Color(0.55f, 0.55f, 0.55f);
        manager = new GameObject("XR Interaction Manager").AddComponent<XRInteractionManager>();
        var prefab = AssetDatabase.LoadAssetAtPath<GameObject>(Samples + "Starter Assets/Prefabs/XR Origin (XR Rig).prefab");
        if (prefab == null) throw new InvalidOperationException("Falta el prefab XR Origin de Starter Assets 3.3.2.");
        rig = (GameObject)PrefabUtility.InstantiatePrefab(prefab);
        rig.transform.SetPositionAndRotation(Vector3.zero, Quaternion.identity);
        rig.transform.localScale = Vector3.one;
        var origin = rig.GetComponent<XROrigin>();
        origin.RequestedTrackingOriginMode = XROrigin.TrackingOriginMode.Floor;
        camera = origin.Camera;
        foreach (var controller in rig.GetComponentsInChildren<ControllerInputActionManager>(true))
        {
            controller.smoothMotionEnabled = false;
            controller.smoothTurnEnabled = false;
        }
        var locomotion = rig.transform.Find("Locomotion");
        if (locomotion == null) throw new InvalidOperationException("El prefab no contiene Locomotion.");
        locomotion.gameObject.SetActive(lab >= 3);
        foreach (var turn in rig.GetComponentsInChildren<SnapTurnProvider>(true)) turn.turnAmount = 45;
        environment = new GameObject("Entorno").transform;
        if (lab == 0)
        {
            IntroBench();
            Simulator();
            EditorSceneManager.SaveScene(scene, scenePath);
            Selection.activeGameObject = rig;
            SceneView.lastActiveSceneView?.Frame(new Bounds(new Vector3(0,1,1.2f), Vector3.one*4), false);
            return;
        }
        var floor = Cube("Piso", lab >= 3 ? new Vector3(0,-0.05f,2) : new Vector3(0,-0.05f,1),
            lab >= 3 ? new Vector3(6,0.1f,6) : new Vector3(4,0.1f,4), gray);
        Vector3 tablePosition = lab >= 3 ? new Vector3(1.5f,0.7f,2) : new Vector3(0,0.7f,1.2f);
        Cube("SuperficieMesa", tablePosition, new Vector3(1.2f,0.1f,0.6f), pale);
        Cube("ReferenciaAltura", new Vector3(-1.2f,0.5f,1.2f), new Vector3(0.05f,1,0.05f), pale);
        Text3D("Medida1m", "1 metro", new Vector3(-1.2f,1.12f,1.15f), environment, 0.24f);
        var tool = Cube(lab == 1 ? "CuboMedida" : "Herramienta", tablePosition + new Vector3(0,0.15f,0), Vector3.one*0.2f, orange);
        if (lab >= 2) Interaction(tool, tablePosition);
        if (lab >= 3)
        {
            Teleportation(floor);
            Instructions();
        }
        if (lab == 4) Preferences();
        Simulator();
        EditorSceneManager.SaveScene(scene, scenePath);
        Selection.activeGameObject = rig;
        SceneView.lastActiveSceneView?.Frame(new Bounds(new Vector3(0,1,1.5f), Vector3.one*6), false);
    }

    static Material MaterialAsset(string name, Color color)
    {
        string path = "Assets/Settings/" + name + ".mat";
        var material = AssetDatabase.LoadAssetAtPath<Material>(path);
        if (material == null)
        {
            var shader = Shader.Find("Universal Render Pipeline/Lit");
            if (shader == null) throw new InvalidOperationException("Falta el shader URP/Lit.");
            material = new Material(shader);
            AssetDatabase.CreateAsset(material, path);
        }
        material.color = color;
        EditorUtility.SetDirty(material);
        return material;
    }

    static void IntroBench()
    {
        Cube("Piso", new Vector3(0,-0.05f,1), new Vector3(4,0.1f,4), gray);
        var bench = new GameObject("Banco").transform;
        bench.SetParent(environment, false);
        var table = Cube("Mesa", new Vector3(0,0.9f,1.2f), new Vector3(1.6f,0.05f,0.8f), pale);
        table.transform.SetParent(bench, true);
        var motor = Cube("Motor", new Vector3(-0.55f,1.13f,1.2f), new Vector3(0.5f,0.4f,0.4f), dark);
        motor.transform.SetParent(bench, true);
        var tool = Cube("Torquimetro", new Vector3(0.25f,0.94f,1.2f), new Vector3(0.3f,0.03f,0.04f), orange);
        tool.transform.SetParent(bench, true);
        var rb = tool.AddComponent<Rigidbody>();
        rb.mass = 0.5f;
        rb.useGravity = true;
        rb.isKinematic = false;
        rb.interpolation = RigidbodyInterpolation.Interpolate;
        rb.collisionDetectionMode = CollisionDetectionMode.ContinuousDynamic;
        var grab = tool.AddComponent<XRGrabInteractable>();
        grab.interactionManager = manager;
        grab.interactionLayers = (InteractionLayerMask)1;
        grab.selectMode = InteractableSelectMode.Single;
        grab.movementType = XRBaseInteractable.MovementType.Kinematic;
        grab.throwOnDetach = false;
        grab.colliders.Clear();
        grab.colliders.Add(tool.GetComponent<Collider>());
        var log = tool.AddComponent<WrenchLog>();
        UnityEventTools.AddPersistentListener(grab.selectEntered, log.Held);
        new GameObject("DiagnosticoXR").AddComponent<DeviceReport>();
    }

    static GameObject Cube(string name, Vector3 position, Vector3 scale, Material material)
    {
        var obj = GameObject.CreatePrimitive(PrimitiveType.Cube);
        obj.name = name;
        obj.transform.SetParent(environment, false);
        obj.transform.position = position;
        obj.transform.localScale = scale;
        obj.GetComponent<Renderer>().sharedMaterial = material;
        return obj;
    }

    static TextMeshPro Text3D(string name, string text, Vector3 position, Transform parent, float height = 0.16f)
    {
        var obj = new GameObject(name);
        obj.transform.SetParent(parent, false);
        obj.transform.position = position;
        // Child labels of the scaled cube must keep their text size in world units.
        Vector3 p = parent.lossyScale;
        obj.transform.localScale = new Vector3(1/p.x,1/p.y,1/p.z);
        var label = obj.AddComponent<TextMeshPro>();
        label.font = font;
        label.text = text;
        label.fontSize = 2.5f;
        label.alignment = TextAlignmentOptions.Center;
        label.color = Color.white;
        label.rectTransform.sizeDelta = new Vector2(1.6f, height);
        return label;
    }

    static void Assign(UnityEngine.Object component, string property, UnityEngine.Object value)
    {
        var serialized = new SerializedObject(component);
        var field = serialized.FindProperty(property);
        if (field == null) throw new InvalidOperationException("No existe el campo " + property);
        field.objectReferenceValue = value;
        serialized.ApplyModifiedPropertiesWithoutUndo();
    }

    static void Interaction(GameObject tool, Vector3 table)
    {
        var rb = tool.AddComponent<Rigidbody>();
        rb.useGravity = true;
        rb.interpolation = RigidbodyInterpolation.Interpolate;
        rb.collisionDetectionMode = CollisionDetectionMode.ContinuousDynamic;
        var grab = tool.AddComponent<XRGrabInteractable>();
        grab.interactionManager = manager;
        grab.interactionLayers = (InteractionLayerMask)1;
        grab.selectMode = InteractableSelectMode.Single;
        grab.movementType = XRBaseInteractable.MovementType.Kinematic;
        grab.throwOnDetach = false;
        grab.colliders.Clear();
        grab.colliders.Add(tool.GetComponent<Collider>());
        var hover = Text3D("AvisoTomar", "TOMAR", tool.transform.position + Vector3.up*0.25f, tool.transform);
        hover.gameObject.SetActive(false);
        UnityEventTools.AddBoolPersistentListener(grab.firstHoverEntered, hover.gameObject.SetActive, true);
        UnityEventTools.AddBoolPersistentListener(grab.lastHoverExited, hover.gameObject.SetActive, false);
        var switchObj = Cube("Interruptor", table + new Vector3(0.4f,0.11f,0), Vector3.one*0.12f, pale);
        var simple = switchObj.AddComponent<XRSimpleInteractable>();
        simple.interactionManager = manager;
        simple.interactionLayers = (InteractionLayerMask)1;
        simple.selectMode = InteractableSelectMode.Single;
        simple.colliders.Clear();
        simple.colliders.Add(switchObj.GetComponent<Collider>());
        Text3D("InstruccionInterruptor", "SELECCIONAR: ENCENDER/APAGAR", table + new Vector3(0.25f,0.62f,0), environment);
        var light = new GameObject("LuzLaboratorio").AddComponent<Light>();
        light.transform.SetParent(environment, false);
        light.transform.position = table + Vector3.up;
        light.type = LightType.Point;
        light.range = 3;
        light.intensity = 3;
        light.shadows = LightShadows.None;
        var on = Text3D("EstadoEncendido", "ENCENDIDA", table + new Vector3(0.35f,0.4f,-0.1f), environment);
        var off = Text3D("EstadoApagado", "APAGADA", table + new Vector3(0.35f,0.4f,-0.1f), environment);
        on.gameObject.SetActive(false);
        light.enabled = false;
        var logic = new GameObject("ControlLampara").AddComponent<LightSwitchLab>();
        Assign(logic, "targetLight", light);
        Assign(logic, "onLabel", on.gameObject);
        Assign(logic, "offLabel", off.gameObject);
        UnityEventTools.AddVoidPersistentListener(simple.selectEntered, logic.ToggleLamp);
    }

    static void Teleportation(GameObject floor)
    {
        var provider = rig.GetComponentInChildren<TeleportationProvider>(true);
        if (provider == null) throw new InvalidOperationException("Falta Teleportation Provider en el prefab.");
        var area = floor.AddComponent<TeleportationArea>();
        area.interactionManager = manager;
        area.interactionLayers = TeleportMask;
        area.teleportationProvider = provider;
        area.teleportTrigger = BaseTeleportationInteractable.TeleportTrigger.OnSelectExited;
        area.matchOrientation = MatchOrientation.WorldSpaceUp;
        area.matchDirectionalInput = false;
        area.colliders.Clear();
        area.colliders.Add(floor.GetComponent<Collider>());
        string[] names = { "Inicio", "HerramientaDestino", "Revision" };
        Vector3[] positions = { new Vector3(-1.5f,0,0),new Vector3(1.5f,0,1),new Vector3(0,0,3.8f) };
        for (int i=0;i<names.Length;i++)
        {
            var root = new GameObject(names[i]);
            root.transform.SetParent(environment, false);
            root.transform.position = positions[i];
            root.transform.rotation = Quaternion.Euler(0,i==2 ? 180 : 0,0);
            var disc = GameObject.CreatePrimitive(PrimitiveType.Cylinder);
            disc.name = "Disco";
            disc.transform.SetParent(root.transform, false);
            disc.transform.localPosition = new Vector3(0,0.01f,0);
            disc.transform.localScale = new Vector3(0.6f,0.01f,0.6f);
            disc.GetComponent<Renderer>().sharedMaterial = orange;
            var arrival = new GameObject("PuntoLlegada").transform;
            arrival.SetParent(root.transform, false);
            var anchor = root.AddComponent<TeleportationAnchor>();
            anchor.interactionManager = manager;
            anchor.interactionLayers = TeleportMask;
            anchor.teleportationProvider = provider;
            anchor.teleportAnchorTransform = arrival;
            anchor.teleportTrigger = BaseTeleportationInteractable.TeleportTrigger.OnSelectExited;
            anchor.matchOrientation = MatchOrientation.TargetUpAndForward;
            anchor.colliders.Clear();
        anchor.colliders.Add(disc.GetComponent<Collider>());
            Text3D("Nombre", names[i], positions[i]+new Vector3(0,0.25f,0), environment);
            var arrow = Cube("Direccion"+i, positions[i]+root.transform.forward*0.45f+Vector3.up*0.02f,
                new Vector3(0.1f,0.02f,0.3f), pale);
            arrow.transform.rotation = root.transform.rotation;
        }
    }

    static RectTransform Rect(string name, Transform parent, Vector2 position, Vector2 size)
    {
        var obj = new GameObject(name, typeof(RectTransform));
        var rect = obj.GetComponent<RectTransform>();
        rect.SetParent(parent, false);
        rect.anchorMin = rect.anchorMax = rect.pivot = new Vector2(0.5f,0.5f);
        rect.anchoredPosition = position;
        rect.sizeDelta = size;
        return rect;
    }

    static Canvas Canvas(string name, Vector3 position, float height)
    {
        if (UnityEngine.Object.FindFirstObjectByType<EventSystem>() == null)
        {
            var events = new GameObject("EventSystem");
            events.AddComponent<EventSystem>();
            events.AddComponent<XRUIInputModule>();
        }
        var rect = Rect(name, environment, Vector2.zero, new Vector2(800,height));
        rect.position = position;
        rect.localScale = Vector3.one*0.002f;
        var canvas = rect.gameObject.AddComponent<Canvas>();
        canvas.renderMode = RenderMode.WorldSpace;
        canvas.worldCamera = camera;
        rect.gameObject.AddComponent<CanvasScaler>();
        rect.gameObject.AddComponent<TrackedDeviceGraphicRaycaster>();
        return canvas;
    }

    static TextMeshProUGUI UIText(string name, Transform parent, string content, Vector2 position, Vector2 size)
    {
        var rect = Rect(name, parent, position, size);
        var text = rect.gameObject.AddComponent<TextMeshProUGUI>();
        text.font = font;
        text.text = content;
        text.fontSize = 30;
        text.color = Color.white;
        text.alignment = TextAlignmentOptions.Center;
        text.raycastTarget = false;
        return text;
    }

    static Button Button(string name, Transform parent, string content, Vector2 position, Vector2 size)
    {
        var rect = Rect(name, parent, position, size);
        var image = rect.gameObject.AddComponent<Image>();
        image.color = new Color(0.18f,0.2f,0.22f);
        var button = rect.gameObject.AddComponent<Button>();
        button.targetGraphic = image;
        UIText("Label", rect, content, Vector2.zero, size-new Vector2(16,8));
        return button;
    }

    static void Instructions()
    {
        var canvas = Canvas("InstruccionesXR", new Vector3(-1.5f,1.3f,1.5f),450);
        var show = Button("MostrarAyuda",canvas.transform,"MOSTRAR INSTRUCCIONES",new Vector2(0,130),new Vector2(650,90));
        var panel = Rect("Ayuda",canvas.transform,new Vector2(0,-70),new Vector2(700,220));
        panel.gameObject.AddComponent<Image>().color = new Color(0.1f,0.12f,0.14f);
        UIText("Texto",panel,"Apunta al disco. Joystick adelante y soltar para viajar. Lados para girar.",
            new Vector2(0,35),new Vector2(660,130));
        var hide = Button("CerrarAyuda",panel,"CERRAR",new Vector2(0,-75),new Vector2(200,60));
        UnityEventTools.AddBoolPersistentListener(show.onClick,panel.gameObject.SetActive,true);
        UnityEventTools.AddBoolPersistentListener(hide.onClick,panel.gameObject.SetActive,false);
        panel.gameObject.SetActive(false);
    }

    static Toggle Toggle(string name, Transform parent, string content, Vector2 position)
    {
        var rect = Rect(name,parent,position,new Vector2(650,70));
        var image = rect.gameObject.AddComponent<Image>();
        image.color = new Color(0.15f,0.17f,0.19f);
        var toggle = rect.gameObject.AddComponent<Toggle>();
        toggle.targetGraphic = image;
        var check = Rect("Check",rect,new Vector2(-280,0),new Vector2(42,42));
        var graphic = check.gameObject.AddComponent<Image>();
        graphic.color = new Color(0.95f,0.55f,0.12f);
        toggle.graphic = graphic;
        UIText("Label",rect,content,new Vector2(30,0),new Vector2(550,60));
        toggle.isOn = false;
        return toggle;
    }

    static void Preferences()
    {
        var canvas = Canvas("PreferenciasXR",new Vector3(0,1.3f,1.5f),600);
        var move = Toggle("MovimientoContinuo",canvas.transform,"MOVIMIENTO CONTINUO",new Vector2(0,170));
        var turn = Toggle("GiroContinuo",canvas.transform,"GIRO CONTINUO",new Vector2(0,80));
        var restore = Button("Restaurar",canvas.transform,"VOLVER A TELETRANSPORTE Y SNAP",new Vector2(0,-20),new Vector2(650,70));
        var quit = Button("Salir",canvas.transform,"SALIR DE LA APP",new Vector2(0,-110),new Vector2(650,70));
        var status = UIText("EstadoPreferencias",canvas.transform,"Teletransporte / Snap turn",new Vector2(0,-220),new Vector2(700,100));
        var logic = new GameObject("ControlComodidad").AddComponent<ComfortOptionsLab>();
        var controllers = rig.GetComponentsInChildren<ControllerInputActionManager>(true);
        var left = controllers.First(c => c.gameObject.name.Contains("Left"));
        var right = controllers.First(c => c.gameObject.name.Contains("Right"));
        Assign(logic,"leftController",left);
        Assign(logic,"rightController",right);
        Assign(logic,"moveToggle",move);
        Assign(logic,"turnToggle",turn);
        Assign(logic,"statusText",status);
        UnityEventTools.AddPersistentListener(move.onValueChanged,logic.SetContinuousMove);
        UnityEventTools.AddPersistentListener(turn.onValueChanged,logic.SetContinuousTurn);
        UnityEventTools.AddPersistentListener(restore.onClick,logic.RestoreDefaults);
        UnityEventTools.AddPersistentListener(quit.onClick,logic.QuitApplication);
    }

    static void Simulator()
    {
        var prefab = AssetDatabase.LoadAssetAtPath<GameObject>(Samples+"XR Interaction Simulator/XR Interaction Simulator.prefab");
        if (prefab == null) throw new InvalidOperationException("Falta XR Interaction Simulator 3.3.2.");
        var simulator = (GameObject)PrefabUtility.InstantiatePrefab(prefab);
        simulator.name = "XR Interaction Simulator (EditorOnly)";
        simulator.tag = "EditorOnly";
    }
}
