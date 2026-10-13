import Foundation

enum Status: Hashable { case draft, pending, synced }

struct Report: Identifiable, Hashable {
    let id = UUID()
    var title: String
    var status: Status
    var note: String?
    var createdAt = Date()
}

let a = Report(title: "Fuga", status: .draft)
var b = a                 // copia: struct es valor
b.title = "Lámpara"
print(a.title)            // Fuga
