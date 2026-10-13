func isValidTitle(_ title: String) -> Bool {
    title.trimmingCharacters(in: .whitespacesAndNewlines)
        .count >= 3
}
