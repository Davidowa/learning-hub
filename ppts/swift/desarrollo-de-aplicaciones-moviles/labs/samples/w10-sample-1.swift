@State private var item: PhotosPickerItem?

PhotosPicker("Adjuntar foto", selection: $item,
             matching: .images)
    .onChange(of: item) { _, newItem in
        Task {
            guard let data = try? await newItem?
                .loadTransferable(type: Data.self)
            else { return }
            store.attachPhoto(data, to: report)
        }
    }
