@Test(arguments: ["", "   ", "ab"])
func shortTitlesAreInvalid(title: String) {
    #expect(isValidTitle(title) == false)
}

