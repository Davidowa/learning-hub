@Model
final class Report {
    var title: String
    var status: String = "pending"
    var createdAt: Date = Date.now
    var photoPath: String?

    init(title: String) { self.title = title }
}

@Query(sort: \Report.createdAt, order: .reverse)
private var reports: [Report]
