# KeyTrace - Educational Keylogger

**KeyTrace** is a Python-based keylogger project built **strictly for educational purposes only**.  
It demonstrates concepts like keyboard event capture, buffered logging, background execution, and cross-platform support.

---

## ⚠️ Disclaimer

This project is intended **ONLY for ethical, educational, and research purposes**.  
Do not use it for malicious activity. Misuse can lead to legal consequences.

---

## 📂 Project Structure

```
.
├── config
│   └── config.py          # Configuration (log paths, flush intervals)
├── core
│   ├── logger.py          # Main keylogging logic (buffer, flush, formatting)
│   └── credentials.json   # Placeholder for optional features
├── logs/                  # Logs stored here (daily log files)
├── main.py                # Entry point (normal/silent mode)
├── run_hidden.py          # Cross-platform background launcher
├── start_keylogger.bat    # Windows startup script
├── start_keylogger.sh     # Linux/macOS startup script
├── requirements.txt       # Python dependencies
├── tests/                 # Unit tests (pytest)
└── venv/                  # Virtual environment (ignored in git)
```

---

## 🚀 Features

- Cross-platform (Windows, Linux, macOS)
- Thread-safe buffered logging
- Configurable flush interval & buffer size
- Special key formatting (`[Enter]`, `[Backspace]`, etc.)
- Daily log files with timestamps
- Run in **normal mode** or **silent mode**
- Background execution with `.bat` / `.sh` launchers
- Unit tests included (`pytest`)

---

## 🔧 Setup

1. Clone this repo:
   ```bash
   git clone https://github.com/Darshan-KC/keytrace.git
   cd keytrace
   ```

2. Create virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/macOS
   venv\Scripts\activate    # Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## ▶️ Usage

Run in normal mode (shows console output):
```bash
python main.py
```

Run in silent mode (no console output):
```bash
python main.py --silent
```

Run in hidden/background mode:
```bash
python run_hidden.py
```

Windows startup (hidden):
```bat
start_keylogger.bat
```

Linux/macOS startup (hidden):
```bash
./start_keylogger.sh
```

---

## 🧪 Running Tests

This project includes unit tests. Run with:
```bash
pytest tests/
```

---

## 📜 License

This project is released under the MIT License.  
Use responsibly and only for **educational purposes**.