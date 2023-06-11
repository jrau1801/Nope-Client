import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QVBoxLayout, QPushButton


class MainMenu(QWidget):
    """
    !!!UNFINISHED!!!
    Graphical User Interface for the main menu
    !!!UNFINISHED!!!
    """
    def __init__(self):
        """
        Initializes window and components
        """
        super().__init__()
        self.disconnect_button = None
        self.textarea = None
        self.initUI()

    def initUI(self):
        """
        Adds components to window
        :return: nothing
        """
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
        """
        Disconnects from server
        :return:
        """
        self.close()

    def append_text(self, text):
        """
        Adds text to textarea
        :param text: text to add
        :return: nothing
        """
        self.textarea.append(text)

    def clear_text(self):
        """
        Clears the text from textarea
        :return: nothing
        """
        self.textarea.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = MainMenu()
    sys.exit(app.exec_())
