import unittest
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5 import uic, Qt
from PyQt5.QtWidgets import QDialog
from PyQt5.QtTest import QTest
from PyQt5.QtCore import Qt


class MainSetting(QDialog):
    """
    This is a demo class for the main settings page.

    This class loads the ui file in order to generate the interface for the main
    settings page and grants access to the different pages that are accountable
    for the other features and settings the user can change.

    """

    def __init__(self):
        """
        The constructor for mainSetting class.

        """

        super(MainSetting, self).__init__()
        uic.loadUi("mainSettingsPage.ui", self)
        self.password.clicked.connect(self.goToPasswordPage)
        self.goBack.clicked.connect(self.goToMainWindow)
        self.reset.clicked.connect(self.goToResetPage)
        self.show()

    def goToPasswordPage(self):
        """
        The function to go to the Password Page either to set or change password based
        on current password state.

        """

        print("Go to password page button pressed. ")

    def goToMainWindow(self):
        """
        The function to go back to the main window.

        """

        print("Go to main window button pressed. ")

    def goToResetPage(self):
        """
        The function to go to the reset application page.

        """

        print("Reset application button pressed. ")


class TestGUI(unittest.TestCase):
    """
    This is a class for testing the widgets of the main settings interface.

    This class loads the ui file in order to generate the interface and tests the different features
    the user may use on this interface.

    """

    def testWidgets(self):
        """
        The function to test what happens when the user presses each button.

        """

        app = QApplication(sys.argv)
        testObject = MainSetting()

        QTest.mouseClick(testObject.password, Qt.LeftButton)
        QTest.mouseClick(testObject.goBack, Qt.LeftButton)
        QTest.mouseClick(testObject.reset, Qt.LeftButton)


if __name__ == "__main__":
    unittest.main()
