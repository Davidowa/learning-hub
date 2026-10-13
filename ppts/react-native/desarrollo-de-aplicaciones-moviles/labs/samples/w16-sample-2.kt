class PowerModule : Module() {
  override fun definition() = ModuleDefinition {
    Name("Power")
    Function("isLowPowerMode") {
      val ctx = appContext.reactContext
        ?: return@Function false
      val pm = ctx.getSystemService(Context.POWER_SERVICE)
        as PowerManager
      pm.isPowerSaveMode
    }
  }
}
