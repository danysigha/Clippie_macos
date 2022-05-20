import unittest
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5 import uic, Qt
from PyQt5.QtWidgets import QDialog
from PyQt5.QtTest import QTest
from PyQt5.QtCore import Qt


class NewUser(QDialog):
    """
    This is a demo class for the new user interface.

    This class loads the ui file in order to generate the interface for the new user to enter
    their email for future use.

    """

    def __init__(self):
        """
        The constructor for the newUser class.

        """

        super(NewUser, self).__init__()
        uic.loadUi("newUserPage.ui", self)
        self.enter.clicked.connect(self.goToMainWindow)
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
            if email1 == email2:
                print("Main window entered.")

            else:
                self.prompt.setText("Emails do not match, please try again.")


class TestGUI(unittest.TestCase):
    """
    This is a class for testing the widgets of the new user interface.

    This class loads the ui file in order to generate the interface and tests the different features
    the user may use on this interface.

    """

    def test1(self):
        """
        The function to test what happens when the same emails are entered by user.

        """

        app = QApplication(sys.argv)
        testObject = NewUser()

        QTest.keyClicks(testObject.pwd1, "apple")
        QTest.keyClicks(testObject.pwd2, "apple")
        QTest.mouseClick(testObject.enter, Qt.LeftButton)

    def test2(self):
        """
        The function to test what happens when different emails are entered by user.

        """
        app = QApplication(sys.argv)
        testObject = NewUser()

        QTest.keyClicks(testObject.pwd1, "apple")
        QTest.keyClicks(testObject.pwd2, "banana")
        QTest.mouseClick(testObject.enter, Qt.LeftButton)
        self.assertEqual(testObject.prompt.text(), "Emails do not match, please try again.")

    def test3(self):
        """
        The function to test what happens when the email fields are left blank.

        """

        app = QApplication(sys.argv)
        testObject = NewUser()

        QTest.keyClicks(testObject.pwd1, "")
        QTest.keyClicks(testObject.pwd2, "")
        QTest.mouseClick(testObject.enter, Qt.LeftButton)
        self.assertEqual(testObject.prompt.text(), "At least one field was left blank. Please try again.")


if __name__ == "__main__":
    unittest.main()
