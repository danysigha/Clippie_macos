import unittest
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5 import uic, Qt
from PyQt5.QtWidgets import QDialog
from PyQt5.QtTest import QTest
from PyQt5.QtCore import Qt


class ResetApplication(QDialog):
    """
    This is a demo class for resetting the whole application and erasing the database.

    This class loads the ui file in order to generate the interface for resetting
    the application.

    """

    def __init__(self):
        """
        The constructor for resetApplication class.

        """

        super(ResetApplication, self).__init__()
        uic.loadUi("resetApplicationPage.ui", self)
        self.goBack.clicked.connect(self.goToMainSettings)
        self.reset.clicked.connect(self.resetDatabase)

    def goToMainSettings(self):
        """
        The function to go back to the main settings page.

        """

        print("Go to main window button pressed. ")

    def resetDatabase(self):
        """
        The function to erase everything in the database and reset application.

        """

        print("Reset application button pressed. ")


class TestGUI(unittest.TestCase):
    """
    This is a class for testing the widgets of the reset application interface.

    This class loads the ui file in order to generate the interface and tests the different features
    the user may use on this interface.

    """

    def testWidgets(self):
        """
        The function to test what happens when goBack and reset buttons are pressed.

        """

        app = QApplication(sys.argv)
        testObject = ResetApplication()

        QTest.mouseClick(testObject.goBack, Qt.LeftButton)
        QTest.mouseClick(testObject.reset, Qt.LeftButton)


if __name__ == "__main__":
    unittest.main()
