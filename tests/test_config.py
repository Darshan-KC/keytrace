import os
import sys
import importlib.util

CONFIG_PATH = os.path.join(os.path.dirname(__file__), "..", "config", "config.py")
spec = importlib.util.spec_from_file_location("config", CONFIG_PATH)
config_module = importlib.util.module_from_spec(spec)
sys.modules["config"] = config_module
spec.loader.exec_module(config_module)

def test_config_has_required_settings():
    assert hasattr(config_module, "LOG_DIR")
    assert hasattr(config_module, "LOG_FILE_PREFIX")
    assert hasattr(config_module, "FLUSH_INTERVAL")
    assert isinstance(config_module.FLUSH_INTERVAL, int)