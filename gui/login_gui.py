import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout, QCheckBox
from main import *
from register_gui import RegistrationForm


class LoginForm(QWidget):
    """
    Graphical User Interface for logging in
    """
    def __init__(self):
        """
        Initializes window and components
        """
        super().__init__()
        self.show_password_check = None
        self.password_entry = None
        self.username_entry = None
        self.registration_form = None
        self.initUI()

    def initUI(self):
        """
        Adds components to window
        :return: nothing
        """
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
        login_button.clicked.connect(self.handle_login)

        # Create registration button
        registration_button = QPushButton('Register')
        registration_button.clicked.connect(self.open_registration_form)

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
        hbox4.addWidget(registration_button)

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
        """
        Show password toggle
        :param state: shown or not shown
        :return: nothing
        """
        if state == 2:
            self.password_entry.setEchoMode(QLineEdit.Normal)
        else:
            self.password_entry.setEchoMode(QLineEdit.Password)

    def handle_login(self):
        """
        Handles functionality of login-button
        :return: nothing
        """
        login_successful = login(self.username_entry.text(), self.password_entry.text())

        if login_successful:
            # Perform actions for successful login
            self.close()  # Close the login window
            tournament_menu()
        else:
            # Perform actions for failed login
            print("Login failed")

    def open_registration_form(self):
        """
        Opens the registration gui if register-button is clicked
        :return: nothing
        """
        self.close()
        self.username_entry.clear()
        self.username_entry.clear()
        self.registration_form = RegistrationForm(self)
        self.registration_form.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    login_form = LoginForm()
    sys.exit(app.exec_())
