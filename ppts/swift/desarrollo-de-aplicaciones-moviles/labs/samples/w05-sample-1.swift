struct NewReportView: View {
    @State private var title = ""
    var onSave: (String) -> Void

    var body: some View {
        Form {
            TextField("¿Qué observaste?", text: $title)
            Button("Guardar") {
                onSave(title.trimmingCharacters(
                    in: .whitespacesAndNewlines))
            }
                .disabled(!isValidTitle(title))
        }
    }
}
