import unittest
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5 import uic, Qt, QtWidgets
from PyQt5.QtWidgets import QDialog
from PyQt5.QtTest import QTest
from PyQt5.QtCore import Qt


class DisablePasswordPage(QDialog):
    """
    This is a demo class for disabling the password

    This class loads the ui file in order to generate the interface for disabling the password.


    """

    def __init__(self):
        """
        The constructor for disablePassword class.

        """

        super(DisablePasswordPage, self).__init__()
        uic.loadUi("disablePasswordPage.ui", self)
        self.enter.clicked.connect(self.turnOffPassword)
        self.backOnePage.clicked.connect(self.goBack)
        self.passwordEntered.setEchoMode(QtWidgets.QLineEdit.Password)

    def turnOffPassword(self):
        """
        The function to  disable the password.

        """
        pwd = self.passwordEntered.text()
        if pwd == "":
            self.returnedText.setText("You have not entered a password. Please try again.")
        else:
            if pwd == "apple":
                print("Password disabled.")
            else:
                self.returnedText.setText("The current password entered is incorrect. Please try again.")

    def goBack(self):
        """
        The function to go back to the change password page.

        """

        print("Go back button pressed")


class TestGUI(unittest.TestCase):
    """
    This is a class for testing the widgets of the disable password interface.

    This class loads the ui file in order to generate the interface and tests the different features
    the user may use on this interface.

    """

    def testWidgets(self):
        """
        The function to test what happens when the current password entered is incorrect or when
        user chooses to click go back.

        """

        app = QApplication(sys.argv)
        testObject = DisablePasswordPage()

        QTest.keyClicks(testObject.passwordEntered, "helloworld")
        QTest.mouseClick(testObject.enter, Qt.LeftButton)
        self.assertEqual(testObject.returnedText.text(), "The current password entered is incorrect. Please try again.")
        QTest.mouseClick(testObject.backOnePage, Qt.LeftButton)

    def test2(self):
        """
        The function to test what happens when the current password entered is correct.

        """

        app = QApplication(sys.argv)
        testObject = DisablePasswordPage()
        QTest.keyClicks(testObject.passwordEntered, "apple")
        QTest.mouseClick(testObject.enter, Qt.LeftButton)

    def test3(self):
        """
        The function to test what happens when nothing is inputted for password.

        """

        app = QApplication(sys.argv)
        testObject = DisablePasswordPage()
        QTest.keyClicks(testObject.passwordEntered, "")
        QTest.mouseClick(testObject.enter, Qt.LeftButton)
        self.assertEqual(testObject.returnedText.text(), "You have not entered a password. Please try again.")


if __name__ == "__main__":
    unittest.main()
