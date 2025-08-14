import os
import tempfile
import threading
import time
from core.logger import KeyLogger

def test_log_creation_and_write():
    tmp_dir = tempfile.mkdtemp()
    logger = KeyLogger(log_dir=tmp_dir)

    logger.log_key("TestKey1")
    logger.flush_logs()
    
    log_files = os.listdir(tmp_dir)
    assert len(log_files) == 1
    with open(os.path.join(tmp_dir, log_files[0]), "r") as f:
        contents = f.read()
    assert "TestKey1" in contents

def test_thread_safe_logging():
    tmp_dir = tempfile.mkdtemp()
    logger = KeyLogger(log_dir=tmp_dir)

    def write_keys():
        for i in range(50):
            logger.log_key(f"Key-{i}")

    threads = [threading.Thread(target=write_keys) for _ in range(5)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    logger.flush_logs()
    log_files = os.listdir(tmp_dir)
    with open(os.path.join(tmp_dir, log_files[0]), "r") as f:
        data = f.read()

    assert data.count("Key-") >= 250  # 5 threads * 50 keys