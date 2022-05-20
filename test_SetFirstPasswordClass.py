import unittest
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5 import uic, Qt
from PyQt5.QtWidgets import QDialog
from PyQt5.QtTest import QTest
from PyQt5.QtCore import Qt


class SetFirstPassword(QDialog):
    """
    This is a demo class for setting the first password of the application.

    This class loads the ui file in order to generate the interface for setting the first
    password.

    """

    def __init__(self):
        """
        The constructor for setFirstPassword class.

        """

        super(SetFirstPassword, self).__init__()
        uic.loadUi("setFirstPasswordPage.ui", self)
        self.goBack.clicked.connect(self.goToMainSettings)
        self.setPwd.clicked.connect(self.setPassword)

    def goToMainSettings(self):
        """
        The function to go back to the main settings page.

        """

        print("Go to main settings button pressed")

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
                self.label_4.setText("Password successfully saved")

            else:
                self.label_4.setText("The passwords do not match. Please try again.")


class TestGUI(unittest.TestCase):
    """
    This is a class for testing the widgets of the set first password interface.

    This class loads the ui file in order to generate the interface and tests the different features
    the user may use on this interface.

    """

    def test1(self):
        """
        The function to test what happens when the two passwords are the same.

        """

        app = QApplication(sys.argv)
        testObject = SetFirstPassword()

        QTest.keyClicks(testObject.pwd1, "helloworld")
        QTest.keyClicks(testObject.pwd2, "helloworld")
        QTest.mouseClick(testObject.setPwd, Qt.LeftButton)
        self.assertEqual(testObject.label_4.text(), "Password successfully saved")

    def test2(self):
        """
        The function to test what happens when the two passwords entered are different and what
        happens when user clicks go back.

        """

        app = QApplication(sys.argv)
        testObject = SetFirstPassword()

        QTest.keyClicks(testObject.pwd1, "helloworld")
        QTest.keyClicks(testObject.pwd2, "apple")
        QTest.mouseClick(testObject.setPwd, Qt.LeftButton)
        self.assertEqual(testObject.label_4.text(), "The passwords do not match. Please try again.")
        QTest.mouseClick(testObject.goBack, Qt.LeftButton)

    def test3(self):
        """
        The function to test what happens when the fields are left blank.

        """

        app = QApplication(sys.argv)
        testObject = SetFirstPassword()

        QTest.keyClicks(testObject.pwd1, "")
        QTest.keyClicks(testObject.pwd2, "")
        QTest.mouseClick(testObject.setPwd, Qt.LeftButton)
        self.assertEqual(testObject.label_4.text(), "The password cannot be left blank. Please try again.")
        QTest.mouseClick(testObject.goBack, Qt.LeftButton)


if __name__ == "__main__":
    unittest.main()