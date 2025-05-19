def check_pipeline_status():
    print("📡 Simulating pipeline failure check...")
    mock_pipeline_failure = {
        "status": "failed",
        "commit_sha": "abc123def",
        "log_url": "logs/fixtures/sample_log.txt",
        "code_context": {
            "file": "app.py",
            "line": 42,
            "snippet": "def process_order(order_id):\n    return order_id + 1"
        }
    }
    return mock_pipeline_failure