import SwiftUI

@main
struct BitacoraApp: App {
    var body: some Scene {
        WindowGroup { ContentView() }
    }
}

struct ContentView: View {
    var body: some View { Text("Hola, Bitácora") }
}

#Preview { ContentView() }
