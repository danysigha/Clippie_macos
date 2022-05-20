import unittest
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5 import uic, Qt
from PyQt5.QtWidgets import QDialog
from PyQt5.QtTest import QTest
from PyQt5.QtCore import Qt


class WelcomeScreen(QDialog):
    """
    This is a demo class for the first welcome screen.

    This class loads the ui file in order to generate the interface for the first welcome
    screen. It determines what screen to show next when the enter button is clicked based
    on whether there's a new user or returning user.

    """

    def __init__(self):
        """
        The constructor for welcomeScreen class.

        """

        super(WelcomeScreen, self).__init__()
        uic.loadUi("welcomescreen.ui", self)
        self.login.clicked.connect(self.goToNextPage)
        self.show()

    def goToNextPage(self):
        """
        The function to go to the next page based on the conditions met.

        """

        print("Next page is opened.")


class TestGUI(unittest.TestCase):
    """
    This is a class for testing the widgets of the welcome screen interface.

    This class loads the ui file in order to generate the interface and tests the different features
    the user may use on this interface.

    """

    def testWidgets(self):
        """
        The function to test the functionality of the enter button.

        """

        app = QApplication(sys.argv)
        testObject = WelcomeScreen()

        QTest.mouseClick(testObject.login, Qt.LeftButton)


if __name__ == "__main__":
    unittest.main()