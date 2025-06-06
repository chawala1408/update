from PySide6.QtWidgets import (QPushButton, QVBoxLayout, QWidget, QApplication, QMainWindow)
from PySide6.QtCore import QCoreApplication
from PySide6.QtUiTools import QUiLoader
import os
import sys
import signal

def update():
    print("Update function called")
    os.kill(os.getpid(), signal.SIGTERM)
    QCoreApplication.quit()

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
