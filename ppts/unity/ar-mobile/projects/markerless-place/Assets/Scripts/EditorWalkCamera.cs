using UnityEngine;
using UnityEngine.InputSystem;

namespace MarkerlessPlace
{
    public sealed class EditorWalkCamera : MonoBehaviour
    {
        float yaw;
        float pitch;

        void Start()
        {
            yaw = transform.eulerAngles.y;
            pitch = transform.eulerAngles.x;
        }

        void Update()
        {
            if (Keyboard.current == null) return;
            var keyboard = Keyboard.current;
            Vector3 input = new Vector3(
                (keyboard.dKey.isPressed ? 1 : 0) - (keyboard.aKey.isPressed ? 1 : 0),
                (keyboard.eKey.isPressed ? 1 : 0) - (keyboard.qKey.isPressed ? 1 : 0),
                (keyboard.wKey.isPressed ? 1 : 0) - (keyboard.sKey.isPressed ? 1 : 0));
            var forward = Vector3.ProjectOnPlane(transform.forward, Vector3.up).normalized;
            var right = Vector3.ProjectOnPlane(transform.right, Vector3.up).normalized;
            transform.position += (right * input.x + Vector3.up * input.y + forward * input.z)
                * (keyboard.leftShiftKey.isPressed ? 3f : 1.2f) * Time.deltaTime;
            if (Mouse.current == null || !Mouse.current.rightButton.isPressed) return;
            var delta = Mouse.current.delta.ReadValue();
            yaw += delta.x * 0.12f;
            pitch = Mathf.Clamp(pitch - delta.y * 0.12f, -80f, 80f);
            transform.rotation = Quaternion.Euler(pitch, yaw, 0f);
        }
    }
}
