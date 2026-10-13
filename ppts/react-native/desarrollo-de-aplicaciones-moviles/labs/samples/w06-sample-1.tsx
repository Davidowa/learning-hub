<FlatList
  data={reports}
  keyExtractor={r => r.id}
  renderItem={({ item }) => (
    <Link href={`/report/${item.id}`} asChild>
      <Pressable>
        <ReportCard title={item.title}
                    category={item.category} />
      </Pressable>
    </Link>
  )}
/>
// app/report/[id].tsx
const { id } = useLocalSearchParams<{ id: string }>();
