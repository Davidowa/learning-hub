using UnityEngine;

namespace MarkerCapture
{
    public sealed class CaptureProjectile : MonoBehaviour
    {
        const float Radius = 0.02f;
        const float Speed = 0.8f;
        Vector3 direction;
        float age;

        public static void Launch(Camera camera,GameObject prefab)
        {
            var ball=Instantiate(prefab,camera.transform.position+camera.transform.forward*.07f,Quaternion.identity);
            ball.GetComponent<CaptureProjectile>().direction=camera.transform.forward.normalized;
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

