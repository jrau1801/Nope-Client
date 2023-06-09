import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout, QCheckBox
from events import *
from main import *


class LoginForm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Create username label and entry
        username_label = QLabel('Username:')
        self.username_entry = QLineEdit()

        # Create password label and entry
        password_label = QLabel('Password:')
        self.password_entry = QLineEdit()
        self.password_entry.setEchoMode(QLineEdit.Password)

        # Create checkbox for showing/hiding password
        self.show_password_check = QCheckBox('Show Password')
        self.show_password_check.stateChanged.connect(self.show_password)

        # Create login button
        login_button = QPushButton('Login')
        login_button.clicked.connect(lambda: login(self.username_entry.text(), self.password_entry.text()))

        # Add all widgets to layout
        hbox1 = QHBoxLayout()
        hbox1.addWidget(username_label)
        hbox1.addWidget(self.username_entry)

        hbox2 = QHBoxLayout()
        hbox2.addWidget(password_label)
        hbox2.addWidget(self.password_entry)

        hbox3 = QHBoxLayout()
        hbox3.addWidget(self.show_password_check)

        hbox4 = QHBoxLayout()
        hbox4.addWidget(login_button)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)
        vbox.addLayout(hbox4)

        self.setLayout(vbox)

        # Set window properties
        self.setGeometry(500, 300, 600, 300)
        self.setWindowTitle('Login Form')
        self.show()

    def show_password(self, state):
        if state == 2:
            self.password_entry.setEchoMode(QLineEdit.Normal)
        else:
            self.password_entry.setEchoMode(QLineEdit.Password)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    login_form = LoginForm()
    sys.exit(app.exec_())
