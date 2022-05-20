import unittest
from PyQt5.QtTest import QTest
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, \
    QLineEdit, QFrame, QGridLayout, QDesktopWidget, QScrollArea
from PyQt5 import uic
from PyQt5.QtCore import Qt
import sys


class MainWindow(QMainWindow):
    """
            This is a class to display the main user interface of the clipboard manager.

            Attributes:
                gridLayout2 (QGridlayout class instance): A grid like structure to display cards.
                menu (QGridlayout class instance): A grid like structure to display menu options.
                settingsButton (QPushButton class instance): A button that displays the settings page.
                leftMenuFrame (QFrame class instance): A frame that contains the menu.
                sideBarButton (QPushButton class instance): A button that displays the settings page.
                allCards (QPushButton class instance): A button that displays all the cards.
                favoriteCards (QPushButton class instance): A button that displays cards which were added to favorites.
                textCards (QPushButton class instance): A button that displays cards which contain text.
                image_cards (QPushButton class instance): A button that displays cards which contain images.
                linkCards (QPushButton class instance): A button that displays cards which contain links.
                searchButton (QPushButton class instance): A button that displays cards that match the search term.
                searchBar (QLineEdit class instance): A textbox where search terms can be entered.
                uic (Qt utility): utility that generates the C++ code that creates the user interface.

        """

    def __init__(self):
        """
        The constructor for the MainWindow class.

        """

        super(MainWindow, self).__init__()
        uic.loadUi("main_window.ui", self)
        self.gridLayout2 = QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout2.setSpacing(0)
        self.gridLayout2.setObjectName(u"gridLayout_2")
        self.gridLayout2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout2.setHorizontalSpacing(10)
        self.gridLayout2.setVerticalSpacing(10)

        self.scrollArea = self.findChild(QScrollArea, "scrollArea_2")
        self.menu = self.findChild(QGridLayout, "gridLayout")
        self.settingsButton = self.findChild(QPushButton, "settings_button")
        self.leftMenuFrame = self.findChild(QFrame, "left_menu_frame")
        self.sideBarButton = self.findChild(QPushButton, "side_bar_button")
        self.allCards = self.findChild(QPushButton, "all_cards")
        self.favoriteCards = self.findChild(QPushButton, "favorite_cards")
        self.textCards = self.findChild(QPushButton, "text_cards")
        self.imageCards = self.findChild(QPushButton, "image_cards")
        self.linkCards = self.findChild(QPushButton, "link_cards")
        self.searchButton = self.findChild(QPushButton, "search_button")
        self.searchBar = self.findChild(QLineEdit, "lineEdit")


class TestMainWindow(unittest.TestCase):
    """
        This is a class to test the main window class of the project.

        The test class will create one instance of the main window to test.

    """

    @classmethod
    def setUpClass(cls):
        """
            The function to set up the class variables for the class test.

        """
        cls.app = QApplication(sys.argv)
        cls.testMainWindow = MainWindow()
        qr = cls.testMainWindow.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        cls.testMainWindow.move(qr.topLeft())
        cls.testMainWindow.show()

    @classmethod
    def tearDownClass(cls):
        """
            The function to close the window after the test.

        """

        cls.testMainWindow.close()

    def test_buttons(self):
        """
            The function to test if all buttons are clickable on the interface.

        """

        self.assertEqual(self.testMainWindow.settingsButton.objectName(), "settings_button")
        QTest.mouseClick(self.testMainWindow.settingsButton, Qt.LeftButton)

        self.assertEqual(self.testMainWindow.searchButton.objectName(), "search_button")
        QTest.mouseClick(self.testMainWindow.searchButton, Qt.LeftButton)

        self.assertEqual(self.testMainWindow.linkCards.objectName(), "link_cards")
        QTest.mouseClick(self.testMainWindow.linkCards, Qt.LeftButton)

        self.assertEqual(self.testMainWindow.imageCards.objectName(), "image_cards")
        QTest.mouseClick(self.testMainWindow.imageCards, Qt.LeftButton)

        self.assertEqual(self.testMainWindow.textCards.objectName(), "text_cards")
        QTest.mouseClick(self.testMainWindow.textCards, Qt.LeftButton)

        self.assertEqual(self.testMainWindow.favoriteCards.objectName(), "favorite_cards")
        QTest.mouseClick(self.testMainWindow.favoriteCards, Qt.LeftButton)

        self.assertEqual(self.testMainWindow.allCards.objectName(), "all_cards")
        QTest.mouseClick(self.testMainWindow.allCards, Qt.LeftButton)

    def test_position(self):

        """
            The function to test if the window is on the window appears at the center of the screen.

        """

        center = QDesktopWidget().availableGeometry().center().x()
        self.assertEqual(center, self.testMainWindow.frameGeometry().center().x())

    def test_slide_menu(self):

        """
            The function to test if the button to hide the menu functions correctly.

        """

        if self.testMainWindow.sideBarButton.isHidden():
            QTest.mouseClick(self.testMainWindow.sideBarButton, Qt.LeftButton)
            self.assertEqual(self.testMainWindow.sideBarButton.isVisible(), False)
        else:
            QTest.mouseClick(self.testMainWindow.sideBarButton, Qt.LeftButton)
            self.assertEqual(self.testMainWindow.sideBarButton.isVisible(), True)

    def test_app_visibility(self):

        """
           The function to test if the main window is visible.

       """

        self.assertEqual(self.testMainWindow.isVisible(), True)

    def test_defaults(self):

        """
           The function to test if the placeholder text in the search bar is corerct.

       """

        self.assertEqual(self.testMainWindow.searchBar.placeholderText(), 'Search')


if __name__ == "__main__":
    unittest.main()
