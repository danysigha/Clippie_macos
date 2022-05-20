from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import QLabel, QMenu
from PyQt5.QtGui import QPixmap
import card


class CardRenderer:
    """
        This is a class for generating and displaying cards.

        Attributes:
            parent (QGridlayout class instance): A grid like structure to display cards.
            row (int): The integer representing the initial row position in the empty gridlayout.
            column (int): The integer representing the initial column position in the empty gridlayout.
            rowSpan  (int): The integer representing the initial rowSpan in the gridlayout.
            columnSpan (int): The integer representing the initial columnSpan in the gridlayout.
            position (list of int): The list which contains the reference to the latest position available in the grid.
            contentRequestCategory (int): The integer which indicates the card category currently selected on
            the interface.

    """

    def __init__(self, parent):
        """
            The constructor for the CardRenderer class.

        """

        self.parent = parent
        self._row = 0
        self._column = 0
        self._rowSpan = 1
        self._columnSpan = 1
        self._position = [self._row, self._column, self._rowSpan, self._columnSpan]
        self.contentRequestCategory = 1

    def initializeCardDisplay(self, dbContent, dao, showAllCards):
        """
            The function to create and display card objects for all entries in the database.

            The function is also used to create and display a subset of the database entries based of category,
            and search terms.

            Parameters:
            content (list of tuples): A list of tuples with all or a subset of the entries in the database.
            position (list of integers): The list which contains the reference to the latest position available in the
            grid.

        """

        for record in dbContent:
            newCard = CardObject(self.parent, dao, self, showAllCards)
            cardData = card.Card(record[0], record[1], record[2], record[3], record[4])
            newCard.addToInterface(cardData)

    def resetGridPosition(self):
        """
            The function to set the latest available position in the grid to 0.

        """

        self._position = [self._row, self._column, self._rowSpan, self._columnSpan]

    def getAvailableGridPostion(self):
        """
            The function to return the latest available position in the grid.

            Returns:
            list of int: The coordinates of the next available position in the grid.

        """

        return self._position

    def updateGridPostion(self):
        """
            The function to calculate the next available position in the grid.

            The function updates the coordinates of the next available position in the grid
            to fill up the grid in a 3 by 3 layout.

        """

        if (self._position[1] + 1) % 3 == 0:
            self._position[0] += 1
            self._position[1] = 0
        else:
            self._position[1] += 1

class CardObject:
    """
            This is a class for generating cards.

            Attributes:
                parent (QGridlayout class instance): A grid like structure to display cards.
                cardData (Card class instance): A card object that contains the properties of each card.
                dao (DataAccessor class instance): An object that holds methods to query the database.
                cardMaker (CardRenderer class instance): An object that holds methods to create and add cards
                to the interface.
                showAllCards (function): The function to set the current card category to ALL_CARDS.
                label (QLabel class instance): An object that represents a label on the interface.

        """

    def __init__(self, parent, dao, cardMaker, showAllCards=None):
        """
            The constructor for the CardObject class.

        """

        self.cardData = None
        self.label = QLabel()
        self._dao = dao
        self._cardMaker = cardMaker
        self.parent = parent
        self.showAllCards = showAllCards

    def addToInterface(self, cardData):
        """
            The function to add the card to the interface.

            The function updates the coordinated of the next available position that will be used to add
            the next card to the interface.

            Parameters:
            cardData (Card class instance): A card object that contains the properties of each card.

        """

        self.cardData = cardData
        self.label.setMinimumSize(QSize(200, 150))
        self.label.setMaximumSize(QSize(200, 150))
        self.setCardContent()
        if self.cardData.getViewStatus():
            self.hideCardContent()

        self.label.setContextMenuPolicy(Qt.CustomContextMenu)
        self.label.customContextMenuRequested.connect(lambda pos, child=self.label: self.customMenuEvent(pos))
        position = self._cardMaker.getAvailableGridPostion()
        self.parent.addWidget(self.label, position[0], position[1], position[2], position[3], Qt.AlignTop)
        self._cardMaker.updateGridPostion()

    def setCardLayout(self):
        """
            The function to set the visual properties of all cards.

            The function uses CSS to modify the appearance of the QLabel widget.

        """

        self.label.setStyleSheet(u"*{\n"
                                 "border:4px solid black;\n"
                                 "  border-radius: 15px;\n"
                                 "  padding: 15px;\n"
                                 "  background-color: white;\n"
                                 "color: black;\n"
                                 "}")
        self.label.setWordWrap(True)
        self.label.setTextFormat(Qt.RichText)
        self.label.setOpenExternalLinks(True)

    def setCardContent(self):
        """
            The function to set the content of the card.

            The function uses html to make links browser accessible.

        """

        content = self.cardData.getContent()
        self.setCardLayout()
        if self.cardData.getCategory() == "URL":
            content = "<a href={}>{}</a>".format(content, content)
            self.label.setText(content)
            self.label.setTextFormat(Qt.RichText)
            self.label.setOpenExternalLinks(True)
            self.label.setTextInteractionFlags(Qt.TextBrowserInteraction)

        elif self.cardData.getCategory() == 'Text':
            self.label.setText(content)
            self.label.setTextInteractionFlags(Qt.TextBrowserInteraction)

        elif self.cardData.getCategory() == 'Image':
            pixmap4 = QPixmap(content)
            pixmap4.setDevicePixelRatio(2.0)
            pixmap4 = pixmap4.scaled(400, 300, Qt.KeepAspectRatio)
            self.label.setPixmap(pixmap4)
            self.label.setAlignment(Qt.AlignCenter)

    def hideCardContent(self):
        """
            The function to hide the content of a card.

            The function makes the card content color the same as the background.

        """

        self.label.setTextFormat(Qt.PlainText)
        self.label.setOpenExternalLinks(False)
        self.label.setTextInteractionFlags(Qt.NoTextInteraction)
        self.label.setStyleSheet(u"*{\n"
                                 "border:4px solid black;\n"
                                 "  border-radius: 15px;\n"
                                 "  padding: 15px;\n"
                                 "  background-color: white;\n"
                                 "color: white;\n"
                                 "}")

        if self.cardData.getCategory() == "Image":
            pixmap = QPixmap()
            pixmap.fill(Qt.white)
            self.label.setPixmap(pixmap)

    def resetCardDisplay(self):
        """
            The function to empty the grid and display a specified set of cards.

            Extended description of function.

        """

        self._cardMaker.resetGridPosition()
        layout = self.parent
        for i in reversed(range(layout.count())):
            widgetToRemove = layout.itemAt(i).widget()
            layout.removeWidget(widgetToRemove)
            widgetToRemove.setParent(None)
            widgetToRemove.deleteLater()

        if self._cardMaker.contentRequestCategory == 1:
            self._cardMaker.initializeCardDisplay(self._dao.getAllCards(), self._dao, self.showAllCards)
        elif self._cardMaker.contentRequestCategory == 2:
            self._cardMaker.initializeCardDisplay(self._dao.getTextCards(), self._dao, self.showAllCards)
        elif self._cardMaker.contentRequestCategory == 3:
            self._cardMaker.initializeCardDisplay(self._dao.getImageCards(), self._dao, self.showAllCards)
        elif self._cardMaker.contentRequestCategory == 4:
            self._cardMaker.initializeCardDisplay(self._dao.getURLCards(), self._dao, self.showAllCards)
        elif self._cardMaker.contentRequestCategory == 6:
            self._cardMaker.initializeCardDisplay(self._dao.getFavoriteCards(), self._dao, self.showAllCards)

    def customMenuEvent(self, eventPosition):
        """
            The function to create a menu for each card.

            The function creates a menu that will appear at a specific coordinate within the widget
            where it was requested.

            Parameters:
            eventPosition (QPoint class instance): A x coordinate and a y coordinate.

        """

        contextMenu = QMenu()
        favoriteCard = contextMenu.addAction("Favorite")
        removeFavoriteCard = contextMenu.addAction("Remove Favorite")
        hideCard = contextMenu.addAction("Toggle visibility")
        delCard = contextMenu.addAction("Delete")
        action = contextMenu.exec_(self.label.mapToGlobal(eventPosition))

        if action == favoriteCard:
            self._dao.favoriteCard(self.cardData.getId(), 1)

        if action == removeFavoriteCard:
            self._dao.favoriteCard(self.cardData.getId(), 0)
            self.resetCardDisplay()

        if action == delCard:
            self._dao.deleteCard(self.cardData.getId(), self.cardData.getCategory(), self.cardData.getContent())
            if self.showAllCards:
                self.showAllCards()
            self.resetCardDisplay()

        if action == hideCard:
            if not self.cardData.getViewStatus():
                self._dao.hideCard(1, self.cardData.getId())
                self.hideCardContent()
                self.cardData.setHidden(True)
            else:
                self._dao.hideCard(0, self.cardData.getId())
                self.setCardContent()
                self.cardData.setHidden(False)
