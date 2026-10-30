using System;
using System.Collections.Generic;
using System.Collections.ObjectModel;

namespace QrPlace
{
    public enum ShapeKind { Cube, Sphere }

    // Session inventory. Spatial poses belong to AR anchors, not this inventory.
    public sealed class PlacementRegistry
    {
        readonly Dictionary<int, ShapeKind> items = new();
        readonly ReadOnlyDictionary<int, ShapeKind> view;
        int nextId = 1;
        public ShapeKind CurrentShape { get; private set; } = ShapeKind.Cube;
        public int? SelectedId { get; private set; }
        public IReadOnlyDictionary<int, ShapeKind> Items => view;

        public PlacementRegistry() => view = new ReadOnlyDictionary<int, ShapeKind>(items);

        public void Choose(ShapeKind kind)
        {
            if (!Enum.IsDefined(typeof(ShapeKind), kind))
                throw new ArgumentOutOfRangeException(nameof(kind));
            CurrentShape = kind;
        }

        public int Add(ShapeKind kind)
        {
            if (!Enum.IsDefined(typeof(ShapeKind), kind))
                throw new ArgumentOutOfRangeException(nameof(kind));
            int id = nextId;
            nextId = checked(nextId + 1);
            items.Add(id, kind);
            SelectedId = null;
            return id;
        }

        public bool Select(int id)
        {
            if (!items.ContainsKey(id)) return false;
            SelectedId = id;
            return true;
        }

        public void Deselect() => SelectedId = null;

        public bool Remove(int id)
        {
            if (!items.Remove(id)) return false;
            if (SelectedId == id) SelectedId = null;
            return true;
        }

        public int? RemoveSelected()
        {
            int? id = SelectedId;
            if (id.HasValue) Remove(id.Value);
            return id;
        }
    }
}
