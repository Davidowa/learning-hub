struct ReportRow: View {
    let report: Report

    var body: some View {
        HStack(spacing: 12) {
            Image(systemName: "doc.text")
            VStack(alignment: .leading) {
                Text(report.title).font(.headline)
                Text(report.createdAt, style: .date)
                    .foregroundStyle(.secondary)
            }
        }
    }
}
