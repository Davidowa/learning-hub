using UnityEngine;

namespace ImageTrackingExamples
{
    public sealed class ImageContentPreview : MonoBehaviour
    {
        [SerializeField] GameObject[] prefabs;
        [SerializeField] Texture2D[] markers;
        GameObject[] content;
        bool[] tracked;

        void Start()
        {
            var cameraObject = new GameObject("Cámara de vista previa", typeof(Camera), typeof(AudioListener));
            var camera = cameraObject.GetComponent<Camera>();
            camera.transform.position = new Vector3(0f, 0.26f, -0.35f);
            camera.transform.LookAt(new Vector3(0f, 0f, 0.35f));
            camera.nearClipPlane = 0.01f;
            camera.farClipPlane = 15f;
            camera.clearFlags = CameraClearFlags.SolidColor;
            camera.backgroundColor = new Color(0.08f, 0.1f, 0.13f);
            cameraObject.AddComponent<EditorWalkCamera>();
            var light = new GameObject("Luz", typeof(Light)).GetComponent<Light>();
            light.type = LightType.Directional;
            light.intensity = 1f;
            light.transform.rotation = Quaternion.Euler(45f, -30f, 0f);
            RenderSettings.ambientLight = Color.gray;
            content = new GameObject[prefabs.Length];
            tracked = new bool[prefabs.Length];
            for (int i = 0; i < prefabs.Length; i++)
            {
                var root = new GameObject("Imagen de vista previa " + i);
                root.transform.position = new Vector3((i - (prefabs.Length - 1) * 0.5f) * 0.22f, 0f, 0.35f);
                var card = GameObject.CreatePrimitive(PrimitiveType.Quad);
                card.transform.SetParent(root.transform, false);
                card.transform.localRotation = Quaternion.Euler(90f, 0f, 0f);
                card.transform.localScale = Vector3.one * 0.16f;
                card.GetComponent<Collider>().enabled = false;
                var material = new Material(Shader.Find("Universal Render Pipeline/Unlit"));
                material.SetTexture("_BaseMap", markers[i]);
                card.GetComponent<Renderer>().material = material;
                content[i] = Instantiate(prefabs[i], root.transform, false);
                content[i].SetActive(false);
            }
        }

        void OnGUI()
        {
            float scale = Mathf.Clamp(Screen.width / 680f, 0.8f, 2f);
            GUI.matrix = Matrix4x4.Scale(new Vector3(scale, scale, 1f));
            float width = Screen.width / scale;
            GUI.skin.box.fontSize = 17;
            GUI.skin.box.wordWrap = true;
            GUI.skin.button.fontSize = 17;
            GUI.Box(new Rect(12, 12, width - 24, 76),
                "Vista previa sin cámara real. Los botones simulan estados; no prueban ARCore.\nWASD: recorrer. Q/E: altura. Botón derecho: girar.");
            if (content == null) return;
            for (int i = 0; i < content.Length; i++)
            {
                string name = i == 0 ? "cubo" : "esfera";
                if (GUI.Button(new Rect(16 + i * (width - 40) / 2, 102, (width - 48) / 2, 52),
                    (tracked[i] ? "Simular Limited: " : "Simular Tracking: ") + name))
                {
                    tracked[i] = !tracked[i];
                    content[i].SetActive(tracked[i]);
                }
            }
        }
    }
}
