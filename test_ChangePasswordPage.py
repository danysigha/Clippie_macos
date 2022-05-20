import unittest
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5 import uic, Qt, QtWidgets
from PyQt5.QtWidgets import QDialog
from PyQt5.QtTest import QTest
from PyQt5.QtCore import Qt


class ChangePasswordPage(QDialog):
    """
    This is a demo class for changing the current password, disabling the password,
    and sending temporary password.

    This class loads the ui file in order to generate the interface for changing
    the current password, disabling password, and sending temporary password.

    """

    def __init__(self):
        """
        The constructor for changePasswordPage class.

        """

        super(ChangePasswordPage, self).__init__()
        uic.loadUi("changePasswordPage.ui", self)
        self.goBack.clicked.connect(self.goToMainSettings)
        self.forgotPwd.clicked.connect(self.sendToEmail)
        self.setPwd.clicked.connect(self.setPassword)
        self.disablePwd.clicked.connect(self.turnOffPasswordPage)

    def goToMainSettings(self):
        """
        The function to go back to the main settings page.

        """

        print("Go to main settings button pressed")

    def sendToEmail(self):
        """
        The function to send the temporary password to user email.

        """

        print("Forgot password button pressed")

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
            if pwd1 == pwd2 and oldpwd == "apple":
                self.label_4.setText("Password successfully saved")

            elif pwd1 == pwd2 and oldpwd != "apple":
                self.label_4.setText("The current password entered is incorrect. Please try again.")

            elif pwd1 != pwd2 and oldpwd == "apple":
                self.label_4.setText("The new passwords do not match. Please try again.")

            else:
                self.label_4.setText("One or more input has been incorrect. Please try again.")

    def turnOffPasswordPage(self):
        """
        The function to go to the disable password page.

        """

        print("Go to turn off password button pressed")


class TestGUI(unittest.TestCase):
    """
    This is a class for testing the widgets of the change password interface.

    This class loads the ui file in order to generate the interface and tests the different features
    the user may use on this interface.

    """

    def testWidgets(self):
        """
        The function to test what happens when the user enters a correct current password and same
        new passwords. It also tests the functionalities of the forgot password button and disable
        password button.

        """

        app = QApplication(sys.argv)
        testObject = ChangePasswordPage()
        QTest.keyClicks(testObject.pwd1, "helloworld")
        QTest.keyClicks(testObject.pwd2, "helloworld")
        QTest.keyClicks(testObject.oldpwd, "apple")
        QTest.mouseClick(testObject.setPwd, Qt.LeftButton)
        self.assertEqual(testObject.label_4.text(), "Password successfully saved")
        QTest.mouseClick(testObject.forgotPwd, Qt.LeftButton)
        QTest.mouseClick(testObject.disablePwd, Qt.LeftButton)

    def test2(self):
        """
        The function to test what happens when the current password is incorrect but the new passwords
        are the same.

        """

        app = QApplication(sys.argv)
        testObject = ChangePasswordPage()
        QTest.keyClicks(testObject.pwd1, "helloworld")
        QTest.keyClicks(testObject.pwd2, "helloworld")
        QTest.keyClicks(testObject.oldpwd, "banana")
        QTest.mouseClick(testObject.setPwd, Qt.LeftButton)
        self.assertEqual(testObject.label_4.text(), "The current password entered is incorrect. Please try again.")

    def test3(self):
        """
        The function to test what happens when current password is current but new passwords are
        not the same

        """

        app = QApplication(sys.argv)
        testObject = ChangePasswordPage()
        QTest.keyClicks(testObject.pwd1, "helloworld")
        QTest.keyClicks(testObject.pwd2, "helloearth")
        QTest.keyClicks(testObject.oldpwd, "apple")
        QTest.mouseClick(testObject.setPwd, Qt.LeftButton)
        self.assertEqual(testObject.label_4.text(), "The new passwords do not match. Please try again.")

    def test4(self):
        """
        The function to test what happens when the current password is incorrect and new passwords
        are not the same.

        """

        app = QApplication(sys.argv)
        testObject = ChangePasswordPage()
        QTest.keyClicks(testObject.pwd1, "helloworld")
        QTest.keyClicks(testObject.pwd2, "apple")
        QTest.keyClicks(testObject.oldpwd, "banana")
        QTest.mouseClick(testObject.setPwd, Qt.LeftButton)
        self.assertEqual(testObject.label_4.text(), "One or more input has been incorrect. Please try again.")

    def test5(self):
        """
        The function to test what happens when the fields are left blank.

        """

        app = QApplication(sys.argv)
        testObject = ChangePasswordPage()
        QTest.keyClicks(testObject.pwd1, "")
        QTest.keyClicks(testObject.pwd2, "")
        QTest.keyClicks(testObject.oldpwd, "")
        QTest.mouseClick(testObject.setPwd, Qt.LeftButton)
        self.assertEqual(testObject.label_4.text(), "At least one field was left blank. Please try again.")


if __name__ == "__main__":
    unittest.main()