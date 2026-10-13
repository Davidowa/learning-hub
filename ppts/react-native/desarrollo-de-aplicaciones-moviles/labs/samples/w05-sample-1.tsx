export function NewReport({ onSave }: Props) {
  const [title, setTitle] = useState('');
  const valid = isValidTitle(title);

  return (
    <View style={{ gap: 12 }}>
      <TextInput value={title} onChangeText={setTitle}
                 placeholder="¿Qué observaste?" />
      <Button title="Guardar" disabled={!valid}
              onPress={() => onSave(title.trim())} />
    </View>
  );
}
