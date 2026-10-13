useEffect(() => {
  const sub = AppState.addEventListener('change', state => {
    log(`${new Date().toISOString()} ${state}`);
  });
  return () => sub.remove();
}, []);
