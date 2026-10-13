test('save is disabled until the title is valid', () => {
  render(<NewReport onSave={jest.fn()} />);
  const save = screen.getByRole('button', { name: 'Guardar' });
  expect(save).toBeDisabled();

  fireEvent.changeText(
    screen.getByPlaceholderText('¿Qué observaste?'), 'Fuga');
  expect(save).toBeEnabled();
});
