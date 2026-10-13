@main
struct BitacoraApp: App {
    @Environment(\.scenePhase) private var phase

    var body: some Scene {
        WindowGroup { ContentView() }
            .onChange(of: phase) { _, newPhase in
                print(newPhase)
            }
    }
}
