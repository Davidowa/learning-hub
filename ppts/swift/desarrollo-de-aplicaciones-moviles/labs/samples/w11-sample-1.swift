.task {
    do {
        let updates = CLLocationUpdate.liveUpdates()
        for try await update in updates {
            guard let loc = update.location else { continue }
            draft.coordinate = loc.coordinate
            break        // una lectura basta para el reporte
        }
    } catch {
        draft.locationError = error
    }
}
