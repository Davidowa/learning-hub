useEffect(() => {
  const ctrl = new AbortController();
  setState({ kind: 'loading' });
  fetchCategories(ctrl.signal)
    .then(data => {
      if (!ctrl.signal.aborted) {
        setState(data.length ? { kind: 'ok', data }
                             : { kind: 'empty' });
      }
    })
    .catch(error => {
      if (!ctrl.signal.aborted) {
        setState({ kind: 'error', error });
      }
    });
  return () => ctrl.abort();
}, []);
