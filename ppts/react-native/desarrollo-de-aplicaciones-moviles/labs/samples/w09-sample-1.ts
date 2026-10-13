async function migrate(db: SQLiteDatabase) {
  await db.withTransactionAsync(async () => {
    const row = await db.getFirstAsync<{
      user_version: number
    }>('PRAGMA user_version');
    let version = row?.user_version ?? 0;
    if (version < 1) {
      await db.execAsync(`CREATE TABLE report (
        id TEXT PRIMARY KEY, title TEXT NOT NULL,
        status TEXT NOT NULL)`);
      version = 1;
    }
    if (version < 2) {
      await db.execAsync(
        'ALTER TABLE report ADD COLUMN photo TEXT');
      version = 2;
    }
    await db.execAsync(`PRAGMA user_version = ${version}`);
  });
}
