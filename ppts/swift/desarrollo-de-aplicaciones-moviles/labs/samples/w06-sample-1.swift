NavigationStack {
    List(reports) { report in
        NavigationLink(value: report) {
            ReportRow(report: report)
        }
    }
    .navigationTitle("Reportes")
    .navigationDestination(for: Report.self) { report in
        ReportDetail(report: report)
    }
}
