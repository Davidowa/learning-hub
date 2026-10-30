using System;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.XR.ARFoundation;
using UnityEngine.XR.ARSubsystems;

public sealed class ImageContentController : MonoBehaviour
{
    [Serializable]
    public sealed class ImageBinding
    {
        public string imageName;
        public GameObject prefab;
    }

    [SerializeField] ARTrackedImageManager images;
    [SerializeField] ImageBinding[] bindings;
    readonly Dictionary<TrackableId, GameObject> spawned = new();

    void OnEnable()
    {
        if (images == null || bindings == null || bindings.Length == 0)
        {
            Debug.LogError("Asigna Images y al menos una entrada en Bindings.", this);
            enabled = false;
            return;
        }
        images.trackablesChanged.AddListener(OnChanged);
        foreach (var image in images.trackables) Apply(image);
    }

    void OnDisable()
    {
        if (images != null)
            images.trackablesChanged.RemoveListener(OnChanged);
        foreach (var content in spawned.Values)
            if (content != null) Destroy(content);
        spawned.Clear();
    }

    void OnChanged(ARTrackablesChangedEventArgs<ARTrackedImage> changes)
    {
        foreach (var image in changes.added) Apply(image);
        foreach (var image in changes.updated) Apply(image);
        foreach (var pair in changes.removed)
        {
            if (!spawned.TryGetValue(pair.Key, out var content)) continue;
            if (content != null) Destroy(content);
            spawned.Remove(pair.Key);
        }
    }

    GameObject FindPrefab(string imageName)
    {
        foreach (var binding in bindings)
        {
            if (binding != null && binding.imageName == imageName)
                return binding.prefab;
        }
        return null;
    }

    void Apply(ARTrackedImage image)
    {
        if (image == null) return;
        bool tracked = image.trackingState == TrackingState.Tracking;
        if (!spawned.TryGetValue(image.trackableId, out var content)
            || content == null)
        {
            if (!tracked) return;
            var prefab = FindPrefab(image.referenceImage.name);
            if (prefab == null) return;
            content = Instantiate(prefab, image.transform, false);
            content.transform.localPosition = Vector3.zero;
            content.transform.localRotation = Quaternion.identity;
            content.transform.localScale = Vector3.one;
            spawned[image.trackableId] = content;
        }
        content.SetActive(tracked);
    }
}
