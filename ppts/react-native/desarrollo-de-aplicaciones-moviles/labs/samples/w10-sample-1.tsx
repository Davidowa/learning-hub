const [permission, requestPermission] = useCameraPermissions();
const camera = useRef<CameraView>(null);

if (!permission) return null;          // aún cargando
if (!permission.granted) {
  return <Button title="Permitir cámara"
                 onPress={requestPermission} />;
}
return <CameraView ref={camera} style={{ flex: 1 }} />;
