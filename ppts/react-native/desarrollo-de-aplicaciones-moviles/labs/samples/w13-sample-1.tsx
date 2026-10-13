<Pressable
  onPress={confirmDelete}
  accessibilityRole="button"
  accessibilityLabel={t('report.delete', { title: r.title })}
  hitSlop={8}
>
  <Ionicons name="trash" size={24} />
</Pressable>
