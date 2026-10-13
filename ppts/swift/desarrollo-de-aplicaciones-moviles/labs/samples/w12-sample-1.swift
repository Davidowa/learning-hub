.onOpenURL { url in
    // bitacora://report/<uuid>
    guard url.scheme == "bitacora",
          url.host() == "report",
          let id = UUID(uuidString: url.lastPathComponent)
    else { return }
    path.append(id)
}
