import ExpoModulesCore

public class PowerModule: Module {
  public func definition() -> ModuleDefinition {
    Name("Power")
    Function("isLowPowerMode") {
      ProcessInfo.processInfo.isLowPowerModeEnabled
    }
  }
}
