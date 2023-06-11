from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout, QCheckBox
from events import registration


class RegistrationForm(QWidget):
    """
    Graphical User Interface for registration
    """
    def __init__(self, login_form):
        """
        Initializes window and components
        """
        super().__init__()
        self.first_name_entry = None
        self.last_name_entry = None
        self.username_entry = None
        self.password_entry = None
        self.show_password_check = None
        self.login_form = login_form
        self.initUI()

    def initUI(self):
        """
        Adds components to window
        :return: nothing
        """
        first_name_label = QLabel('First Name:')
        self.first_name_entry = QLineEdit()

        # Create last name label and entry
        last_name_label = QLabel('Last Name:')
        self.last_name_entry = QLineEdit()

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

        # Create register button
        register_button = QPushButton('Register')
        register_button.clicked.connect(self.handle_registration)

        # Create back button
        back_button = QPushButton('Back')
        back_button.clicked.connect(self.go_back)

        # Add all widgets to layout
        hbox1 = QHBoxLayout()
        hbox1.addWidget(first_name_label)
        hbox1.addWidget(self.first_name_entry)

        hbox2 = QHBoxLayout()
        hbox2.addWidget(last_name_label)
        hbox2.addWidget(self.last_name_entry)

        hbox3 = QHBoxLayout()
        hbox3.addWidget(username_label)
        hbox3.addWidget(self.username_entry)

        hbox4 = QHBoxLayout()
        hbox4.addWidget(password_label)
        hbox4.addWidget(self.password_entry)

        hbox5 = QHBoxLayout()
        hbox5.addWidget(self.show_password_check)

        hbox6 = QHBoxLayout()
        hbox6.addWidget(register_button)

        hbox7 = QHBoxLayout()
        hbox7.addWidget(back_button)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)
        vbox.addLayout(hbox4)
        vbox.addLayout(hbox5)
        vbox.addLayout(hbox6)
        vbox.addLayout(hbox7)

        self.setLayout(vbox)

        # Set window properties
        self.setGeometry(500, 300, 600, 300)
        self.setWindowTitle('Registration Form')
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

    def handle_registration(self):
        """
        Handles the registration if the button is clicked
        :return: nothing
        """
        # Get the values entered in the registration form
        first_name = self.first_name_entry.text()
        last_name = self.last_name_entry.text()
        username = self.username_entry.text()
        password = self.password_entry.text()

        if registration(username, password, first_name, last_name):
            print("Registration Successful")
        else:
            print("Registration Failed")

    def go_back(self):
        """
        Go back to Login-form
        :return: nothing
        """
        self.close()
        self.login_form.show()
