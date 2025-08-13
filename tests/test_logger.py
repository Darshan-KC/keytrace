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