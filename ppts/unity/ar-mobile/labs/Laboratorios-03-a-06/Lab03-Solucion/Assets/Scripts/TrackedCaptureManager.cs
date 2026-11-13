using System;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.XR.ARFoundation;
using UnityEngine.XR.ARSubsystems;

namespace MarkerCapture
{
    public sealed class TrackedCaptureManager : MonoBehaviour
    {
        ARTrackedImageManager images;
        CaptureRegistry registry;
        GameObject targetPrefab;
        readonly Dictionary<TrackableId, CaptureTarget> spawned = new();
        public IEnumerable<CaptureTarget> Targets => spawned.Values;

        public void Initialize(ARTrackedImageManager manager, CaptureRegistry captureRegistry,GameObject prefab)
        {
            images = manager;targetPrefab=prefab;
            registry = captureRegistry;
            images.trackablesChanged.AddListener(OnChanged);
        }

        void OnDestroy()
        {
            if (images != null) images.trackablesChanged.RemoveListener(OnChanged);
        }

        void OnChanged(ARTrackablesChangedEventArgs<ARTrackedImage> changes)
        {
            foreach (var image in changes.added) Apply(image);
            foreach (var image in changes.updated) Apply(image);
            foreach (var pair in changes.removed)
            {
                if (!spawned.TryGetValue(pair.Key, out var target)) continue;
                if (target != null) Destroy(target.gameObject);
                spawned.Remove(pair.Key);
            }
        }

        void Apply(ARTrackedImage image)
        {
            if (!spawned.TryGetValue(image.trackableId, out var target))
            {
                // Wait for reference metadata when a provider reports the pose first.
                if (image.referenceImage.guid == Guid.Empty) return;
                var go = Instantiate(targetPrefab);
                go.transform.SetParent(image.transform, false);
                target = go.GetComponent<CaptureTarget>();
                target.Initialize(registry, image.referenceImage.guid.ToString("N"));
                spawned.Add(image.trackableId, target);
            }
            target.SetTracking(image.trackingState == TrackingState.Tracking);
        }
    }
}
