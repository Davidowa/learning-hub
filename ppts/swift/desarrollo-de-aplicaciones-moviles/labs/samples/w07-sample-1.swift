@Observable
final class ReportStore {
    private(set) var reports: [Report] = []
    private let repo: ReportRepository

    init(repo: ReportRepository) { self.repo = repo }

    func add(_ report: Report) {
        reports.append(report)
        repo.save(report)
    }
}
