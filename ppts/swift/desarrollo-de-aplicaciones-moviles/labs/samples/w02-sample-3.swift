import Testing
@testable import Bitacora

@Test func pendingKeepsOnlyUnsynced() {
    let rs = [Report(title: "Fuga", status: .pending),
              Report(title: "Lámpara", status: .synced)]
    #expect(pending(rs).map(\.title) == ["Fuga"])
}
