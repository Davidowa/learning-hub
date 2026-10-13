struct Category: Decodable, Identifiable {
    let id: String
    let label: String
}

func fetchCategories() async throws -> [Category] {
    let url = API.base.appending(path: "categories")
    let (data, resp) = try await URLSession.shared
        .data(from: url)
    guard (resp as? HTTPURLResponse)?.statusCode == 200
    else { throw URLError(.badServerResponse) }
    return try JSONDecoder()
        .decode([Category].self, from: data)
}
