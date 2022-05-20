from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, \
    QLineEdit, QFrame, QGridLayout, \
    QStackedWidget, QDesktopWidget
import grab_clipboard as grabClip
from PyQt5 import uic, QtCore
import sys
import dao
import card_generator
import settings
import loginPage
import icons

QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

class MainWindow(QMainWindow):
    """
        This is a class to display the main user interface of the clipboard manager.

        Attributes:
            STATUS (dictionary): A dictionary with card categories as keys and booleans as values.
            gridLayout2 (QGridlayout class instance): A grid like structure to display cards.
            dao (DataAccessor class instance): An object that holds methods to query the database.
            cardMaker (CardRenderer class instance): An object that holds methods to create and add cards
            to the user interface.
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

    STATUS = {'ALL_STATE': True, 'FAVORITE_STATE': False, 'TEXT_STATE': False, 'IMAGE_STATE': False, 'URL_STATE': False}

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
        self.dao = dao.DataAccessor()
        self.cardMaker = card_generator.CardRenderer(self.gridLayout2)
        self.menu = self.findChild(QGridLayout, "gridLayout")
        self.settingsButton = self.findChild(QPushButton, "settings_button")
        self.settingsButton.clicked.connect(self.openSettingsWindow)
        self.leftMenuFrame = self.findChild(QFrame, "left_menu_frame")
        self.sideBarButton = self.findChild(QPushButton, "side_bar_button")
        self.sideBarButton.clicked.connect(self.slideMenu)
        self.allCards = self.findChild(QPushButton, "all_cards")
        self.allCards.clicked.connect(self.showAllCards)
        self.favoriteCards = self.findChild(QPushButton, "favorite_cards")
        self.favoriteCards.clicked.connect(self.showFavoriteCards)
        self.textCards = self.findChild(QPushButton, "text_cards")
        self.textCards.clicked.connect(self.showTextCards)
        self.imageCards = self.findChild(QPushButton, "image_cards")
        self.imageCards.clicked.connect(self.showImageCards)
        self.linkCards = self.findChild(QPushButton, "link_cards")
        self.linkCards.clicked.connect(self.showUrlCards)
        self.searchButton = self.findChild(QPushButton, "search_button")
        self.searchButton.clicked.connect(self.search)
        self.searchBar = self.findChild(QLineEdit, "lineEdit")
        self.searchBar.returnPressed.connect(self.search)
        self.highlightButton(self.allCards)

    def updateCategory(self, newState):
        """
            The function to change the program's record of the currently selected card category on the user interface.

            Parameters:
                newState (string): The card category to turn to True

        """

        for state in self.STATUS:
            self.STATUS[state] = False
        self.STATUS[newState] = True

    def setCategory(self):
        """
            The function to visually highlight the currently selected card category on the user interface.

        """

        for i in range(self.menu.count()):
            widget = self.menu.itemAt(i).widget()
            if widget.objectName() == "all_cards" and self.STATUS['ALL_STATE']:
                self.highlightButton(widget)

            elif widget.objectName() == "favorite_cards" and self.STATUS['FAVORITE_STATE']:
                self.highlightButton(widget)

            elif widget.objectName() == "text_cards" and self.STATUS['TEXT_STATE']:
                self.highlightButton(widget)

            elif widget.objectName() == "image_cards" and self.STATUS['IMAGE_STATE']:
                self.highlightButton(widget)

            elif widget.objectName() == "link_cards" and self.STATUS['URL_STATE']:
                self.highlightButton(widget)

            elif widget.objectName() != "label_4":
                widget.setStyleSheet(u"QPushButton:hover{\n"
                             "background-color: rgba(255, 227, 251, 59);\n"
                             "}"
                              u"QPushButton{\n"
                                     "border: node;\n"
                                     "}")

    def highlightButton(self, button):
        """
            The function to change the appearance of the menu button that is clicked.

            The function makes use of CSS to make the visual changes.

            Parameters:
            button (QPushButton class instance): The menu button that represents a card category.

        """

        button.setStyleSheet(u"QPushButton{\n"
                             "  background-color: rgba(255, 227, 251, 59);\n"
                             "}"
                             u"QPushButton{\n"
                             "border: solid;\n"
                             "}"
                             )

    def emptyGrid(self):
        """
            The function to remove all the cards in the grid.

            The function resets the next available position in the grid stored in the CardRenderer instance attribute.

        """

        self.cardMaker.resetGridPosition()
        layout = self.gridLayout2
        for i in reversed(range(layout.count())):
            widgetToRemove = layout.itemAt(i).widget()
            layout.removeWidget(widgetToRemove)
            widgetToRemove.deleteLater()

    def showAllCards(self):
        """
            The function to set the current card category to ALL_CARDS.

            The currently selected card category is updated in the program and visually on the user interface. All the
            cards on the grid are removed and a new call to the database is made to retrieve all the cards and add them
            to the grid.

        """

        self.updateCategory('ALL_STATE')
        self.setCategory()
        self.emptyGrid()
        self.cardMaker.contentRequestCategory = 1
        self.cardMaker.initializeCardDisplay(self.dao.getAllCards(), self.dao, self.showAllCards)

    def showTextCards(self):
        """
            The function to set the current card category to TEXT_CARDS.

            The currently selected card category is updated in the program and visually on the user interface. All the
            cards on the grid are removed and a new call to the database is made to retrieve all the cards of the text
            category and add them to the grid.

        """

        self.updateCategory('TEXT_STATE')
        self.setCategory()
        self.emptyGrid()
        # print(self._cardMaker._position, 'in reset function after reset')
        self.cardMaker.contentRequestCategory = 2
        self.cardMaker.initializeCardDisplay(self.dao.getTextCards(), self.dao, self.showAllCards)

    def showImageCards(self):
        """
            The function to set the current card category to IMAGE_CARDS.

            The currently selected card category is updated in the program and visually on the user interface. All the
            cards on the grid are removed and a new call to the database is made to retrieve all the cards of the image
            category and add them to the grid.

        """

        self.updateCategory('IMAGE_STATE')
        self.setCategory()
        self.emptyGrid()
        # print(self._cardMaker._position, 'in reset function after reset')
        self.cardMaker.contentRequestCategory = 3
        self.cardMaker.initializeCardDisplay(self.dao.getImageCards(), self.dao, self.showAllCards)

    def showUrlCards(self):
        """
            The function to set the current card category to URL_CARDS.

            The currently selected card category is updated in the program and visually on the user interface. All the cards
            on the grid are removed and a new call to the database is made to retrieve all the cards of the url
            category and add them to the grid.

        """

        self.updateCategory('URL_STATE')
        self.setCategory()
        self.emptyGrid()
        self.cardMaker.contentRequestCategory = 4
        self.cardMaker.initializeCardDisplay(self.dao.getUrlCards(), self.dao, self.showAllCards)

    def search(self):
        """
        The function to search and display cards with a specific key word.

        The currently selected card category is updated in the program and visually on the user interface. All the cards
        on the grid are removed and a new call to the database is made to retrieve all the cards that contain the search
        term and add them to the grid.

        """

        searchTerm = self.lineEdit.text()

        if searchTerm:
            self.updateCategory("ALL_STATE")
            self.setCategory()
            self.emptyGrid()
            self.cardMaker.contentRequestCategory = 5
            self.cardMaker.initializeCardDisplay(self.dao.getSearchCards(searchTerm), self.dao, self.showAllCards)
        else:
            if not self.STATUS["ALL_STATE"]:
                self.showAllCards()


    def showFavoriteCards(self):
        """
            The function to set the current card category to FAVORITE_CARDS.

            The currently selected card category is updated in the program and visually on the user interface. All the cards
            on the grid are removed and a new call to the database is made to retrieve all the cards with the favorite
            property and add them to the grid.

        """

        self.updateCategory('FAVORITE_STATE')
        self.setCategory()
        self.emptyGrid()
        self.cardMaker.contentRequestCategory = 6
        self.cardMaker.initializeCardDisplay(self.dao.getFavoriteCards(), self.dao, self.showAllCards)

    def slideMenu(self):
        """
            The function to hide and show the left menu.

        """

        if self.leftMenuFrame.isVisible():
            self.leftMenuFrame.hide()
        else:
            self.leftMenuFrame.show()

    def openSettingsWindow(self):
        """
            The function to open the settings window.

        """
        self.window = QStackedWidget()
        window1 = settings.MainSetting(self, self.dao, self.window)
        window2 = settings.SetFirstPassword(self.dao, self.window)
        window3 = settings.ChangePasswordPage(self.dao, self.window)
        window4 = settings.ResetApplication(self.dao, self.window, self)
        window5 = settings.DisablePasswordPage(self.dao, self.window)
        self.window.addWidget(window1)
        self.window.addWidget(window2)
        self.window.addWidget(window3)
        self.window.addWidget(window4)
        self.window.addWidget(window5)
        self.window.setFixedHeight(493)
        self.window.setFixedWidth(370)
        self.window.show()
        self.hide()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = MainWindow()
    ui.cardMaker.initializeCardDisplay(ui.dao.getAllCards(), ui.dao, ui.showAllCards)
    gc = grabClip.ClipboardManager(ui.cardMaker, ui.dao, ui.STATUS)
    gc.manageClip()

    widget = QStackedWidget()
    window1 = loginPage.WelcomeScreen(ui.dao, widget, ui)
    window2 = loginPage.NewUser(ui.dao, widget, ui)
    window3 = loginPage.WelcomeScreenPasswordPage(ui.dao, widget, ui)
    widget.addWidget(window1)
    widget.addWidget(window2)
    widget.addWidget(window3)

    widget.setFixedHeight(493)
    widget.setFixedWidth(370)
    qr = widget.frameGeometry()
    cp = QDesktopWidget().availableGeometry().center()
    qr.moveCenter(cp)
    widget.move(qr.topLeft())
    qr1 = ui.frameGeometry()
    qr1.moveCenter(cp)
    ui.move(qr1.topLeft())
    widget.show()
    sys.exit(app.exec_())
