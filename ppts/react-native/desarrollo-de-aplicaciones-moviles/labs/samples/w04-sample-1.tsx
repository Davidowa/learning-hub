type Props = { title: string; category: string };

export function ReportCard({ title, category }: Props) {
  return (
    <View style={styles.card}>
      <Text style={styles.title}>{title}</Text>
      <Text style={styles.chip}>{category}</Text>
    </View>
  );
}
