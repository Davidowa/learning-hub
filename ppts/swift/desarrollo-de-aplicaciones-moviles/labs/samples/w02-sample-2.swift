func pending(_ reports: [Report]) -> [Report] {
    reports.filter { $0.status == .pending }
}
