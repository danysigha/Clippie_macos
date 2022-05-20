import unittest
import card
import uuid
import card_generator
from PyQt5.QtWidgets import QMainWindow, QApplication, QGridLayout

from PyQt5 import uic

import sys


class MainWindow(QMainWindow):

    """
            This is a class to display the main user interface of the clipboard manager.

            Attributes:
                gridLayout2 (QGridlayout class instance): A grid like structure to display cards.

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


class TestMainWindow(unittest.TestCase):
    """
        This is a class to test the display the card object class of the clipboard manager.

        The test class will open and close the display immediately.

    """

    @classmethod
    def setUpClass(cls):
        """
            The function to set up the class variables for the class test.

            The function creates a window to display and the instance of the car object class we will test.

        """

        cls.app = QApplication(sys.argv)
        cls.testMainWindow = MainWindow()
        cls.testCardRenderer = card_generator.CardRenderer(cls.testMainWindow.gridLayout2)
        cls.testCardObject = card_generator.CardObject(cls.testMainWindow.gridLayout2, None,
                                                       cls.testCardRenderer)

    def test_add_to_interface(self):
        """
            The function to test the function addToInterface of the card object class.

            The function adds cards to the interface and checks if the gridlayout was updated accordingly.

        """
        card1 = card.Card(uuid.uuid4().hex, "Test 1", 1, 1)
        card2 = card.Card(uuid.uuid4().hex, "Test 2", 0, 0)
        card3 = card.Card(uuid.uuid4().hex, "Test 3", 1, 0)
        card4 = card.Card(uuid.uuid4().hex, "Test 4", 0, 1)

        self.assertEqual(self.testMainWindow.gridLayout2.columnCount(), 1)
        self.assertEqual(self.testMainWindow.gridLayout2.rowCount(), 1)

        self.testCardObject.addToInterface(card1)
        self.testCardObject.addToInterface(card2)
        self.testCardObject.addToInterface(card3)
        self.testCardObject.addToInterface(card4)

        self.assertEqual(self.testCardRenderer._position, [1, 1, 1, 1])
        self.assertEqual(self.testMainWindow.gridLayout2.columnCount(), 3)
        self.assertEqual(self.testMainWindow.gridLayout2.rowCount(), 2)


if __name__ == "__main__":
    unittest.main()
