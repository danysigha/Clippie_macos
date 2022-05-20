from PyQt5 import uic
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog


class MainSetting(QDialog):
    """
    This is a class for the main settings page.

    This class loads the ui file in order to generate the interface for the main
    settings page and grants access to the different pages that are accountable
    for the other features and settings the user can change.

    Attributes
    parent (QMainWindow): the MainWindow object to be used to access the main window
    dataAccessObject (dao): the dao object used to communicate with database
    widget (QStackedWidget) : the stacked widget of all the screens for moving from one screen
                               to another

    """

    def __init__(self, parent, dataAccessObject, widget):
        """
        The constructor for mainSetting class.

        Parameters:
        parent (QMainWindow): the MainWindow object to be used to access the main window
        dataAccessObject (dao): the dao object used to communicate with database
        widget (QStackedWidget) : the stacked widget of all the screens for moving from one screen
                               to another

        """

        super(MainSetting, self).__init__()
        uic.loadUi("mainSettingsPage.ui", self)
        self._parent = parent
        self.widget = widget
        self.dao = dataAccessObject
        self.password.clicked.connect(self.goToPasswordPage)
        self.goBack.clicked.connect(self.goToMainWindow)
        self.reset.clicked.connect(self.goToResetPage)
        self.show()

    def goToPasswordPage(self):
        """
        The function to go to the Password Page either to set or change password based
        on current password state.

        """

        if self.dao.getPasswordState():
            self.widget.setCurrentIndex(self.widget.currentIndex() + 2)

        else:
            self.widget.setCurrentIndex(self.widget.currentIndex() + 1)

    def goToResetPage(self):
        """
        The function to go to the reset application page.

        """

        self.widget.setCurrentIndex(self.widget.currentIndex() + 3)

    def goToMainWindow(self):
        """
        The function to go back to the main window.

        """

        self.widget.close()
        self._parent.show()


class SetFirstPassword(QDialog):
    """
    This is a class for setting the first password of the application.

    This class loads the ui file in order to generate the interface for setting the first
    password.

    Attributes
    parent (QMainWindow): the MainWindow object to be used to access the main window
    dataAccessObject (dao): the dao object used to communicate with database
    widget (QStackedWidget) : the stacked widget of all the screens for moving from one screen
                               to another

    """

    def __init__(self, dataAccessObject, widget):
        """
        The constructor for setFirstPassword class.

        Parameters:
        parent (QMainWindow): the MainWindow object to be used to access the main window
        dataAccessObject (dao): the dao object used to communicate with database
        widget (QStackedWidget) : the stacked widget of all the screens for moving from one screen
                               to another

        """

        super(SetFirstPassword, self).__init__()
        uic.loadUi("setFirstPasswordPage.ui", self)
        self.dao = dataAccessObject
        self.widget = widget
        self.pwd1.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pwd2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.goBack.clicked.connect(self.goToMainSettings)
        self.setPwd.clicked.connect(self.setPassword)

    def goToMainSettings(self):
        """
        The function to go back to the main settings page.

        """

        self.widget.setCurrentIndex(self.widget.currentIndex() - 1)
        self.label_4.clear()

    def setPassword(self):
        """
        The function to set the password and send it to database.

        """

        pwd1 = self.pwd1.text()
        pwd2 = self.pwd2.text()

        if pwd1 == "" or pwd2 == "":
            self.label_4.setText("The password cannot be left blank. Please try again.")

        else:
            if pwd1 == pwd2:
                self.dao.setPassword(pwd1)
                self.label_4.setText("Password successfully saved")
                print(pwd1)

            else:
                self.label_4.setText("The passwords do not match. Please try again.")

            self.pwd1.clear()
            self.pwd2.clear()


class ResetApplication(QDialog):
    """
    This is a class for resetting the whole application and erasing the database.

    This class loads the ui file in order to generate the interface for resetting
    the application.

    Attributes
    parent (QMainWindow): the MainWindow object to be used to access the main window
    dataAccessObject (dao): the dao object used to communicate with database
    widget (QStackedWidget) : the stacked widget of all the screens for moving from one screen
                               to another

    """

    def __init__(self, dataAccessObject, widget, parent):
        """
        The constructor for resetApplication class.

        Parameters:
        parent (QMainWindow): the MainWindow object to be used to access the main window
        dataAccessObject (dao): the dao object used to communicate with database
        widget (QStackedWidget) : the stacked widget of all the screens for moving from one screen
                               to another

        """

        super(ResetApplication, self).__init__()
        uic.loadUi("resetApplicationPage.ui", self)
        self.dao = dataAccessObject
        self.widget = widget
        self.parent = parent
        self.goBack.clicked.connect(self.goToMainSettings)
        self.reset.clicked.connect(self.resetDatabase)

    def goToMainSettings(self):
        """
        The function to go back to the main settings page.

        """

        self.widget.setCurrentIndex(self.widget.currentIndex() - 3)

    def resetDatabase(self):
        """
        The function to go erase everything in the database and reset application.

        """

        self.dao.resetDb()
        self.widget.close()
        self.parent.close()


class ChangePasswordPage(QDialog):
    """
    This is a class for changing the current password, disabling the password,
    and sending temporary password.

    This class loads the ui file in order to generate the interface for changing
    the current password, disabling password, and sending temporary password.

    Attributes
    parent (QMainWindow): the MainWindow object to be used to access the main window
    dataAccessObject (dao): the dao object used to communicate with database
    widget (QStackedWidget) : the stacked widget of all the screens for moving from one screen
                               to another

    """

    def __init__(self, dataAccessObject, widget):
        """
        The constructor for changePasswordPage class.

        Parameters:
        parent (QMainWindow): the MainWindow object to be used to access the main window
        dataAccessObject (dao): the dao object used to communicate with database
        widget (QStackedWidget) : the stacked widget of all the screens for moving from one screen
                               to another

        """

        super(ChangePasswordPage, self).__init__()
        uic.loadUi("changePasswordPage.ui", self)
        self.dao = dataAccessObject
        self.widget = widget
        self.goBack.clicked.connect(self.goToMainSettings)
        self.forgotPwd.clicked.connect(self.sendToEmail)
        self.setPwd.clicked.connect(self.setPassword)
        self.disablePwd.clicked.connect(self.turnOffPasswordPage)
        self.oldpwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pwd1.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pwd2.setEchoMode(QtWidgets.QLineEdit.Password)

    def goToMainSettings(self):
        """
        The function to go back to the main settings page.

        """

        self.widget.setCurrentIndex(self.widget.currentIndex() - 2)
        self.label_4.clear()

    def setPassword(self):
        """
        The function to change the password in database.

        """

        oldpwd = self.oldpwd.text()
        pwd1 = self.pwd1.text()
        pwd2 = self.pwd2.text()

        if oldpwd == "" or pwd1 == "" or pwd2 == "":
            self.label_4.setText("At least one field was left blank. Please try again.")

        else:

            if pwd1 == pwd2 and self.dao.changePassword(oldpwd, pwd1):
                self.label_4.setText("Password successfully saved")

            elif pwd1 == pwd2 and not self.dao.changePassword(oldpwd, pwd1):
                self.label_4.setText("The current password entered is incorrect. Please try again.")

            elif pwd1 != pwd2 and self.dao.changePassword(oldpwd, pwd1):
                self.label_4.setText("The new passwords do not match. Please try again.")

            else:
                self.label_4.setText("One or more input has been incorrect. Please try again.")

        self.oldpwd.clear()
        self.pwd1.clear()
        self.pwd2.clear()

    def sendToEmail(self):
        """
        The function to send the temporary password to user email.

        """

        self.dao.sendEmail()
        self.label_4.setText("A temporary password was sent to the email on file. Please check your email.")

    def turnOffPasswordPage(self):
        """
        The function to go to the disable password page.

        """

        self.widget.setCurrentIndex(self.widget.currentIndex() + 2)


class DisablePasswordPage(QDialog):
    """
    This is a class for disabling the password

    This class loads the ui file in order to generate the interface for disabling the password.

    Attributes
    parent (QMainWindow): the MainWindow object to be used to access the main window
    dataAccessObject (dao): the dao object used to communicate with database
    widget (QStackedWidget) : the stacked widget of all the screens for moving from one screen
                               to another

    """

    def __init__(self, dataAccessObject, widget):
        """
        The constructor for disablePassword class.

        Parameters:
        parent (QMainWindow): the MainWindow object to be used to access the main window
        data_access_object (dao): the dao object used to communicate with database
        widget (QStackedWidget) : the stacked widget of all the screens for moving from one screen
                               to another

        """

        super(DisablePasswordPage, self).__init__()
        uic.loadUi("disablePasswordPage.ui", self)
        self.widget = widget
        self.dao = dataAccessObject
        self.enter.clicked.connect(self.turnOffPassword)
        self.backOnePage.clicked.connect(self.goBack)
        self.passwordEntered.setEchoMode(QtWidgets.QLineEdit.Password)

    def turnOffPassword(self):
        """
        The function to go disable the password.

        """

        pwd = self.passwordEntered.text()
        if pwd == "":
            self.returnedText.setText("You have not entered a password. Please try again.")
        else:
            if self.dao.passwordIsValid(pwd):
                self.dao.setPasswordState(0)
                self.widget.setCurrentIndex(self.widget.currentIndex() - 4)
            else:
                self.returnedText.setText("The current password entered is incorrect. Please try again.")
                self.passwordEntered.clear()

    def goBack(self):
        """
        The function to go back to the change password page.

        """

        self.widget.setCurrentIndex(self.widget.currentIndex() - 2)
