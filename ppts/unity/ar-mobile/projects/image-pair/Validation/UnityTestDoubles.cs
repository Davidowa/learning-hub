// Local doubles exercise controller logic. They do not implement or validate Unity/ARCore.
namespace UnityEngine
{
    [AttributeUsage(AttributeTargets.Field)] public sealed class SerializeField : Attribute { }
    public class Object
    {
        public bool destroyed;
        public static bool operator ==(Object a, Object b) => ReferenceEquals(a,b) ||
            ((ReferenceEquals(a,null) || a.destroyed) && (ReferenceEquals(b,null) || b.destroyed));
        public static bool operator !=(Object a, Object b) => !(a == b);
        public override bool Equals(object other) => ReferenceEquals(this,other);
        public override int GetHashCode() => System.Runtime.CompilerServices.RuntimeHelpers.GetHashCode(this);
        public static void Destroy(Object value) { if (!ReferenceEquals(value,null)) value.destroyed = true; }
        public static GameObject Instantiate(GameObject original, Transform parent, bool worldPositionStays)
            => new(original.name) { transform = new Transform { parent = parent,
                localPosition = new(2,3,4), localScale = new(4,4,4), localRotation = new(1,2,3,4) } };
    }
    public class MonoBehaviour : Object { public bool enabled = true; }
    public record struct Vector3(float x,float y,float z)
    {
        public static Vector3 zero => new(0,0,0);
        public static Vector3 one => new(1,1,1);
    }
    public record struct Quaternion(float x,float y,float z,float w)
    { public static Quaternion identity => new(0,0,0,1); }
    public sealed class Transform
    {
        public Transform parent;
        public Vector3 localPosition;
        public Vector3 localScale;
        public Quaternion localRotation;
    }
    public sealed class GameObject : Object
    {
        public string name;
        public Transform transform = new();
        public bool activeSelf = true;
        public GameObject(string name) { this.name = name; }
        public void SetActive(bool value) { activeSelf = value; }
    }
    public static class Debug
    {
        public static int Errors;
        public static void LogError(string message, Object context) => Errors++;
    }
}
namespace UnityEngine.XR.ARSubsystems
{
    public record struct TrackableId(ulong value);
    public enum TrackingState { None, Limited, Tracking }
    public struct XRReferenceImage { public string name; }
}
namespace UnityEngine.XR.ARFoundation
{
    using UnityEngine;
    using UnityEngine.XR.ARSubsystems;
    public sealed class FakeEvent<T>
    {
        readonly List<Action<T>> listeners = new();
        public int Count => listeners.Count;
        public void AddListener(Action<T> listener) => listeners.Add(listener);
        public void RemoveListener(Action<T> listener) => listeners.Remove(listener);
        public void Invoke(T value) { foreach (var listener in listeners.ToArray()) listener(value); }
    }
    public sealed class ARTrackedImageManager : Object
    {
        public FakeEvent<ARTrackablesChangedEventArgs<ARTrackedImage>> trackablesChanged = new();
        public List<ARTrackedImage> trackables = new();
    }
    public sealed class ARTrackedImage : Object
    {
        public TrackableId trackableId;
        public XRReferenceImage referenceImage;
        public TrackingState trackingState;
        public Transform transform = new();
    }
    public sealed class ARTrackablesChangedEventArgs<T>
    {
        public List<T> added = new();
        public List<T> updated = new();
        public List<KeyValuePair<TrackableId,T>> removed = new();
    }
}
