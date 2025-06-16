from PySide6.QtWidgets import (QPushButton, QVBoxLayout, QWidget, QApplication, QMainWindow)
from PySide6.QtCore import QCoreApplication
from PySide6.QtUiTools import QUiLoader
import os
import sys
import signal
import requests
import subprocess , time

GIT_RAW_URL = "https://raw.githubusercontent.com/chawala1408/update/refs/heads/main/test_update.py"
LOCAL_UPDATE_FILE = "test_update2.py"

def download_update():
    try:
        print("⬇️  Downloading latest version of test_update.py...")
        response = requests.get(GIT_RAW_URL)
        response.raise_for_status()
        with open(LOCAL_UPDATE_FILE, "w", encoding="utf-8") as f:
            f.write(response.text)
        print("✅ Update downloaded successfully.")
        return True
    except Exception as e:
        print("❌ Failed to download update:", e)
        return False
    
def update():
    print("Update function called", flush=True)  # <-- สำคัญมากdownload_update()
    if download_update():
        print("🚀 Running updated version...")
        subprocess.Popen(["update.bat"], shell=True)
        sys.stdout.flush()  # เพิ่มอีกเผื่อไว้
        time.sleep(1)

        # ปิดตัว
        QCoreApplication.quit()
        os.kill(os.getpid(), signal.SIGTERM)
    else:
        print("⚠️ Update download failed. Keeping old version.")
    

app = QApplication([])

load = QUiLoader()
UI = os.path.join(os.path.dirname(__file__), 'main.ui')

if not os.path.exists(UI):
    print(f"UI file not found: {UI}")
    sys.exit(1)

window = load.load(UI)
if not window:
    print("Failed to load the UI file.")
    sys.exit(1)

window.setWindowTitle("Test Update")
window.resize(150, 90)

# 🟢 ตรงนี้ต้องระบุว่าเราหา QPushButton ที่ชื่อ "pushButton"
button = window.findChild(QPushButton, "pushButton")
if button:
    button.clicked.connect(update)

else:
    print("Button not found!")

if __name__ == "__main__":
    window.show()
    sys.exit(app.exec())

