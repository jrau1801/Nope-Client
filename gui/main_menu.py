import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QVBoxLayout, QPushButton


class MainMenu(QWidget):
    def __init__(self):
        super().__init__()
        self.disconnect_button = None
        self.textarea = None
        self.initUI()

    def initUI(self):
        # Create a QTextEdit widget for the textarea and set it as non-editable
        self.textarea = QTextEdit()
        self.textarea.setReadOnly(True)

        # Create a QPushButton for the disconnect button
        self.disconnect_button = QPushButton('Disconnect')
        self.disconnect_button.clicked.connect(self.disconnect)

        # Create a QVBoxLayout and add the widgets
        layout = QVBoxLayout()
        layout.addWidget(self.textarea)
        layout.addWidget(self.disconnect_button)

        self.setLayout(layout)

        # Set window properties
        self.setWindowTitle('GUI with Textarea and Disconnect Button')
        self.setGeometry(300, 300, 400, 300)
        self.show()

    def disconnect(self):
        # Perform actions when the disconnect button is clicked
        self.close()

    def append_text(self, text):
        self.textarea.append(text)

    def clear_text(self):
        self.textarea.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = MainMenu()
    sys.exit(app.exec_())
