@Environment(\.horizontalSizeClass) private var size

var body: some View {
    if size == .regular {
        NavigationSplitView {
            ReportList()
        } detail: {
            ReportDetailPlaceholder()
        }
    } else {
        NavigationStack { ReportList() }
    }
}
