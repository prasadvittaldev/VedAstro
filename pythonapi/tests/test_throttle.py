def test_throttle_limits(tmp_path, monkeypatch):
    db = tmp_path / "throttle.db"
    monkeypatch.setenv("VEDASTRO_DB", str(db))
    from importlib import reload

    import vedastro_api.sqlite_db as sqlite_db
    import vedastro_api.throttle_manager as tm

    reload(sqlite_db)
    reload(tm)
    assert tm.is_allowed("1.1.1.1", 1, 60) is True
    assert tm.is_allowed("1.1.1.1", 1, 60) is False
