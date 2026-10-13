struct ToolPilot {
    let minimumSuccessRate: Double

    func shouldStop(_ successRate: Double) -> Bool {
        successRate < minimumSuccessRate
    }
}
