import Foundation

enum Status: Hashable { case draft, pending, synced }

struct Report: Identifiable, Hashable {
    let id = UUID()
    var title: String
    var status: Status
    var note: String?
    var createdAt = Date()
}

func pending(_ reports: [Report]) -> [Report] {
    reports.filter { $0.status == .pending }
}
func isValidTitle(_ title: String) -> Bool {
    title.trimmingCharacters(in: .whitespacesAndNewlines)
        .count >= 3
}

let a = Report(title: "Fuga", status: .draft)
var b = a
b.title = "Lamp"
assert(a.title == "Fuga")
assert(b.title == "Lamp")
assert(isValidTitle("   ") == false)
assert(isValidTitle("ab") == false)
assert(isValidTitle("Fuga") == true)
let records = [Report(title: "A", status: .pending),
               Report(title: "B", status: .synced)]
assert(pending(records).map(\.title) == ["A"])
print("6 Swift domain checks passed")
