useEffect(() => {
  Accelerometer.setUpdateInterval(100);   // ms
  const sub = Accelerometer.addListener(({ x, y, z }) => {
    const rad = Math.atan2(y, Math.hypot(x, z));
    setTilt(lowPass(rad * 180 / Math.PI));
  });
  return () => sub.remove();
}, []);
