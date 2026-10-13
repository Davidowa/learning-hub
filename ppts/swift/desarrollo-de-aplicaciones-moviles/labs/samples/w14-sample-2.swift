func testCreateReport() throws {
    let app = XCUIApplication()
    app.launch()
    app.buttons["Nuevo reporte"].tap()
    let field = app.textFields["¿Qué observaste?"]
    field.tap()
    field.typeText("Fuga")
    app.buttons["Guardar"].tap()
    XCTAssertTrue(app.staticTexts["Fuga"].exists)
}
