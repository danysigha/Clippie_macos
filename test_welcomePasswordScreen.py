import unittest
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5 import uic, Qt
from PyQt5.QtWidgets import QDialog
from PyQt5.QtTest import QTest
from PyQt5.QtCore import Qt


class WelcomeScreenPasswordPage(QDialog):
    """
    This is a demo class for the login page.

    This class loads the ui file in order to generate the interface for entering the
    password in order for the user to log in and access the main window.

    """

    def __init__(self):
        """
        The constructor for welcomeScreenPasswordPage class.

        """

        super(WelcomeScreenPasswordPage, self).__init__()
        uic.loadUi("welcomescreenPasswordPage.ui", self)
        self.login.clicked.connect(self.goToNextPage)
        self.forgotPwd.clicked.connect(self.sendToEmail)
        self.show()

    def goToNextPage(self):
        """
        The function to go to either go to the main window if password entered is correct
        or to stay on current page until correct password is entered.

        """

        if self.passwordEntered.text() == "":
            self.prompt.setText("Password field was left blank. Please try again.")

        else:
            if self.passwordEntered.text() == "apple":
                print("Correct password inputted")

            else:
                self.prompt.setText("Incorrect password. Please try again.")

    def sendToEmail(self):
        """
        The function to go to send a temporary password to email on file.

        """

        self.prompt.setText("A temporary password was sent to the email on file. Please check your email.")


class TestGUI(unittest.TestCase):
    """
    This is a class for testing the widgets of the welcome password screen interface.

    This class loads the ui file in order to generate the interface and tests the different features
    the user may use on this interface.

    """

    def test1(self):
        """
        The function to test what happens when the user enters a correct password.

        """

        app = QApplication(sys.argv)
        testObject = WelcomeScreenPasswordPage()

        QTest.keyClicks(testObject.passwordEntered, "apple")
        QTest.mouseClick(testObject.login, Qt.LeftButton)

    def test2(self):
        """
        The function to test what happens when the user enters an incorrect password.

        """

        app = QApplication(sys.argv)
        testObject = WelcomeScreenPasswordPage()

        QTest.keyClicks(testObject.passwordEntered, "banana")
        QTest.mouseClick(testObject.login, Qt.LeftButton)
        self.assertEqual(testObject.prompt.text(), "Incorrect password. Please try again.")

    def test3(self):
        """
        The function to test what happens when the user presses the forgot password button.

        """

        app = QApplication(sys.argv)
        testObject = WelcomeScreenPasswordPage()
        QTest.mouseClick(testObject.forgotPwd, Qt.LeftButton)
        self.assertEqual(testObject.prompt.text(),
                         "A temporary password was sent to the email on file. Please check your email.")
    def test4(self):
        """
        The function to test what happens when the password field is left blank.

        """

        app = QApplication(sys.argv)
        testObject = WelcomeScreenPasswordPage()

        QTest.keyClicks(testObject.passwordEntered, "")
        QTest.mouseClick(testObject.login, Qt.LeftButton)
        self.assertEqual(testObject.prompt.text(), "Password field was left blank. Please try again.")

if __name__ == "__main__":
    unittest.main()