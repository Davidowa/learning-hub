using UnityEngine;

namespace MarkerCapture
{
    public sealed class CaptureProjectile : MonoBehaviour
    {
        const float Radius = 0.0125f;
        const float Speed = 1.5f;
        Vector3 direction;
        float age;

        public static void Launch(Camera camera)
        {
            var ball = GameObject.CreatePrimitive(PrimitiveType.Sphere);
            ball.name = "Esfera lanzada";
            ball.transform.localScale = Vector3.one * (Radius * 2f);
            ball.transform.position = camera.transform.position + camera.transform.forward * 0.07f;
            ball.GetComponent<Renderer>().sharedMaterial = Resources.Load<Material>("ProjectileMaterial");
            // The sweep below detects hits; the projectile must not hit itself.
            ball.GetComponent<Collider>().enabled = false;
            ball.AddComponent<CaptureProjectile>().direction = camera.transform.forward.normalized;
        }

        void Update()
        {
            age += Time.deltaTime;
            if (age > 3f)
            {
                Destroy(gameObject);
                return;
            }

            float distance = Speed * Time.deltaTime;
            Physics.SyncTransforms();
            // Sweep the whole step so a small cube cannot be skipped between frames.
            var hits = Physics.SphereCastAll(transform.position, Radius, direction, distance,
                Physics.DefaultRaycastLayers, QueryTriggerInteraction.Ignore);
            System.Array.Sort(hits, (a, b) => a.distance.CompareTo(b.distance));
            foreach (var hit in hits)
            {
                var target = hit.collider.GetComponentInParent<CaptureTarget>();
                if (target == null || !target.TryCapture()) continue;
                Destroy(gameObject);
                return;
            }

            transform.position += direction * distance;
        }
    }
}
