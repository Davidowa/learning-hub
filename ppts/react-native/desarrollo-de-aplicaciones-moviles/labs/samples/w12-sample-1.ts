const Trigger = Notifications.SchedulableTriggerInputTypes;

await Notifications.scheduleNotificationAsync({
  content: {
    title: 'Reporte pendiente',
    body: report.title,
    data: { url: `bitacora://report/${report.id}` },
  },
  trigger: { type: Trigger.TIME_INTERVAL, seconds: 3600 },
});
