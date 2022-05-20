

class Card:

    def __init__(self, id, cardContent, cardCategory, hideCard=False, favoriteCard =False):
        self._cardId = id
        self._cardContent = cardContent
        self._cardCategory = cardCategory
        if hideCard == 0:
            self._hideCard = False
        elif hideCard == 1:
            self._hideCard = True
        else:
            self._hideCard = hideCard

        if favoriteCard == 0:
            self._favoriteCard = False
        elif favoriteCard == 1:
            self._favoriteCard = True
        else:
            self._favoriteCard = favoriteCard

    def getId(self):
        """returns card Id"""
        return self._cardId

    def getCategory(self):
        """returns the type of card content"""
        return self._cardCategory

    def getContent(self):
        return self._cardContent

    def getViewStatus(self):
        """returns the hidden status of the card"""
        return self._hideCard

    def getFavoriteStatus(self):
        """returns the favorite status of the card"""
        return self._favoriteCard

    def setCategory(self, e):
        """
        sets card content to passed argument
        
        parameters:
            e (str): the value to set the card category to
        """

        if not isinstance(e, str):
            raise Exception("Card label must be str type")

        self._cardCategory = e

    def setContent(self, e):
        """
        sets card content to passed argument
        
        parameters:
            e (str): the value to set the card content to
        """
        if not isinstance(e, str):
            raise Exception("Card content must be str type")
        self._cardContent = e

    def setHidden(self, H):
        """
        sets card object hidden status
        
        parameters:
            H (bool): the value to set the hideCard to
        """
        self._hideCard = H

    def setId(self, id):
        """sets the id of the card"""
        self._cardId = id

    def setFavorite(self, newStatus):
        """sets the favorite status of the card"""
        self._favoriteCard = newStatus

    def __str__(self):
        """returns string representation for card object"""
        string = "{\n" + "card ID: " + str(self._cardId) + ", " + "\ncard content: " + "\"" + str(
            self._cardContent) + "\"" + ", " + "\ncard type: " + str(
            self._cardCategory) + " , " + "\nHidden: " + str(self._hideCard) + "\nFavorite: " + str(self._favoriteCard)\
                 + "\n}"
        return string
