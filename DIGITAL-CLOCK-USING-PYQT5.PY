"""
Digital Clock Application using PyQt5--

This application creates a digital clock with the following features:
- Displays current time in 12-hour format (HH:MM:SS AM/PM)
- Updates every second
- Uses a custom digital font (DS-DIGIT.TTF)
- Black background with white text
- Centered display
- Window size: 500x200 pixels

Requirements:
- PyQt5
- DS-DIGIT.TTF font file in the same directory
"""

import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton,
                            QWidget, QVBoxLayout, QLabel)
from PyQt5.QtCore import QTimer, QTime, Qt
from PyQt5.QtGui import QFont, QFontDatabase

class DigitalClock(QWidget):
    def __init__(self): 
        super().__init__()
        # Initialize UI components
        self.time_label = QLabel(self)
        self.timer = QTimer(self)
        self.initUI()

    def initUI(self):
        # Set window properties
        self.setWindowTitle("Digital Clock")
        self.setGeometry(700, 200, 500, 200)
        self.setStyleSheet("background-color: black;")
        
        # Create and set up layout
        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)

        # Configure time label
        self.time_label.setAlignment(Qt.AlignCenter)
        self.time_label.setStyleSheet("font-size: 100px; color: white;")
        
        # Load and set custom digital font
        font_id = QFontDatabase.addApplicationFont("DS-DIGIT.TTF")
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        my_font = QFont(font_family, 150)
        self.time_label.setFont(my_font)

        # Initialize and start the timer
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)  # Update every 1000ms (1 second)
        self.update_time()  # Initial update

    def update_time(self):
        # Update the displayed time
        current_time = QTime.currentTime().toString("hh:mm:ss A")
        self.time_label.setText(current_time)

def main():
    # Create and run the application
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()