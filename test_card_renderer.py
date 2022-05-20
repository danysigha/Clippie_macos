import card_generator
import unittest


class TestMainWindow(unittest.TestCase):
    """
            This is a class to test the cardRender class of the project.

            The test class will create one instance of the cardRenderer to test.

    """

    @classmethod
    def setUpClass(cls):
        """
            The function to set up the class variables for the class test.

        """
        cls.testCardRenderer = card_generator.CardRenderer(None)

    def test_resetGridPosition(self):
        """
            The function to test the function resetGridPosition for the cardRender class.

            The function sets the grid position back to the default value.

        """

        self.testCardRenderer.resetGridPosition()
        self.assertEqual(self.testCardRenderer._position, [0,0,1,1])

    def test_update_position(self):
        """
            The function to test the function resetGridPosition for the cardRenderr class.

            The function simulates the addition of cards to the interface and checks if the
            next available grid position was updated correctly.

        """
        self.testCardRenderer._position = [32, 2, 1, 1]
        self.testCardRenderer.updateGridPostion()
        self.assertEqual(self.testCardRenderer._position, [33, 0, 1, 1])

        self.testCardRenderer._position = [21, 1, 1, 1]
        self.testCardRenderer.updateGridPostion()
        self.assertEqual(self.testCardRenderer._position, [21, 2, 1, 1])


if __name__ == "__main__":
    unittest.main()
