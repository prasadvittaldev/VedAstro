def test_log_request(tmp_path, monkeypatch):
    db = tmp_path / "log.db"
    monkeypatch.setenv("VEDASTRO_DB", str(db))
    from importlib import reload

    import vedastro_api.api_logger as logger
    import vedastro_api.sqlite_db as sqlite_db

    reload(sqlite_db)
    reload(logger)
    logger.log_request("/test", 200)
    assert logger.fetch_logs() == [{"endpoint": "/test", "status_code": 200}]
