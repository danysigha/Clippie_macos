from PyQt5 import uic
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QLabel, QTextEdit, QPushButton, QLineEdit, QComboBox


class WelcomeScreen(QDialog):
    """
    This is a class for the first welcome screen.

    This class loads the ui file in order to generate the interface for the first welcome
    screen. It determines what screen to show next when the enter button is clicked based
    on whether there's a new user or returning user.

    Attributes
    parent (QMainWindow): the MainWindow object to be used to access the main window
    dataAccessObject (dao): the dao object used to communicate with database
    widget (QStackedWidget) : the stacked widget of all the screens for moving from one screen
                               to another

    """

    def __init__(self, dataAccessObject, widget, MainWindow):
        """
        The constructor for welcomeScreen class.

        Parameters:
        parent (QMainWindow): the MainWindow object to be used to access the main window
        dataAccessObject (dao): the dao object used to communicate with database
        widget (QStackedWidget) : the stacked widget of all the screens for moving from one screen
                               to another

        """

        super(WelcomeScreen, self).__init__()
        uic.loadUi("welcomescreen.ui", self)
        self.MainWindow = MainWindow
        self.widget = widget
        self.dao = dataAccessObject
        self.login.clicked.connect(self.goToNextPage)
        self.show()

    def goToNextPage(self):
        """
        The function to go to the next page based on the conditions met.

        """

        if self.dao.getUserStatus() != 0:
            if self.dao.getPasswordState() == True:
                self.widget.setCurrentIndex(self.widget.currentIndex() + 2)

            else:
                self.widget.close()
                self.MainWindow.show()

        else:
            self.widget.setCurrentIndex(self.widget.currentIndex() + 1)


class WelcomeScreenPasswordPage(QDialog):
    """
    This is a class for the login page.

    This class loads the ui file in order to generate the interface for entering the
    password in order for the user to log in and access the main window.

    Attributes
    parent (QMainWindow): the MainWindow object to be used to access the main window
    dataAccessObject (dao): the dao object used to communicate with database
    widget (QStackedWidget) : the stacked widget of all the screens for moving from one screen
                               to another

    """

    def __init__(self, dataAccessObject, widget, MainWindow):
        """
        The constructor for welcomeScreenPasswordPage class.

        Parameters:
        parent (QMainWindow): the MainWindow object to be used to access the main window
        dataAccessObject (dao): the dao object used to communicate with database
        widget (QStackedWidget) : the stacked widget of all the screens for moving from one screen
                               to another
        """
        super(WelcomeScreenPasswordPage, self).__init__()
        uic.loadUi("welcomescreenPasswordPage.ui", self)
        self.dao = dataAccessObject
        self.widget = widget
        self.MainWindow = MainWindow
        self.passwordEntered.setEchoMode(QtWidgets.QLineEdit.Password)
        self.login.clicked.connect(self.goToNextPage)
        self.forgotPwd.clicked.connect(self.sendToEmail)
        self.show()

    def goToNextPage(self):
        """
        The function to go to either go to the main window if password entered is correct
        or to stay on current page until correct password is entered.

        """

        self.passwordEntered.setEchoMode(QtWidgets.QLineEdit.Password)
        pwd = self.passwordEntered.text()

        if pwd == "":
            self.prompt.setText("Password field was left blank. Please try again.")
        else:
            if self.dao.passwordIsValid(pwd):
                self.widget.close()
                self.MainWindow.show()

            else:
                self.prompt.setText("Incorrect password. Please try again.")
                self.passwordEntered.clear()

    def sendToEmail(self):
        """
        The function to go to send a temporary password to email on file.

        """

        self.dao.sendEmail()
        self.prompt.setText("A temporary password was sent to the email on file. Please check your email.")


class NewUser(QDialog):
    """
    This is a class for the new user interface.

    This class loads the ui file in order to generate the interface for the new user to enter
    their email for future use.

    Attributes
    parent (QMainWindow): the MainWindow object to be used to access the main window
    dataAccessObject (dao): the dao object used to communicate with database
    widget (QStackedWidget) : the stacked widget of all the screens for moving from one screen
                               to another

    """

    def __init__(self, dataAccessObject, widget, MainWindow):
        """
        The constructor for the newUser class.

        Parameters:
        parent (QMainWindow): the MainWindow object to be used to access the main window
        dataAccessObject (dao): the dao object used to communicate with database
        widget (QStackedWidget) : the stacked widget of all the screens for moving from one screen
                                   to another

        """

        super(NewUser, self).__init__()
        uic.loadUi("newUserPage.ui", self)
        self.dao = dataAccessObject
        self.widget = widget
        self.enter.clicked.connect(self.goToMainWindow)
        self.MainWindow = MainWindow
        self.show()

    def goToMainWindow(self):
        """
        The function to save email entered by new user to database and move to main window.

        """

        email1 = self.pwd1.text()
        email2 = self.pwd2.text()

        if email1 == "" or email2 == "":
            self.prompt.setText("At least one field was left blank. Please try again.")
        else:
            if (email1 == email2):
                self.dao.createUser(email1)
                self.widget.close()
                self.MainWindow.show()

            else:
                self.prompt.setText("Emails do not match, please try again.")
                self.pwd1.clear()
                self.pwd2.clear()
