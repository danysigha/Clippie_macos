import card_generator
import PIL.Image as Image
import uuid
import card
import io
import validators
from PyQt5.QtCore import QTimer
from AppKit import NSPasteboard, NSStringPboardType, NSTIFFPboardType, NSPasteboardTypePNG, NSURL, NSURLPboardType


class ClipboardManager:
    """
        This is a class for monitoring changes in the clipboard.

        Attributes:
            pasteBoard (NSPasteboard object): The operating system's clipboard object.
            currentCount (int): The count of all the items in the clipboard object.
            timer (Qtimer class instance): A high-level programming interface for timers.
            cardRenderer (CardRenderer class instance): An object that holds methods to create and
            add cards to the interface.
            uiStatus (dictionary): A dictionary with card categories as keys and booleans as values.
            dao (DataAccessor class instance): An object that holds methods to query the database.

    """

    def __init__(self, cardRenderer, dao, uiStatus):
        """
            The constructor for the ClipboardManager class.

        """

        self._pasteBoard = NSPasteboard.generalPasteboard()
        self._currentCount = NSPasteboard.generalPasteboard().changeCount()
        self._timer = QTimer()
        self.cardRenderer = cardRenderer
        self.dao = dao
        self._uiStatus = uiStatus

    def queryClipboard(self):
        """
            The function to check if clipboard item count changed and update interface accordingly
            by creating new cards.

            The function determines the type of the new clipboard content, stores it to the database, and
            depending on the currently selected category on the interface may create and display the card immediately.
            The bytes of each image are retrieved from the clipboard and stored as a png file in a folder in the same
            directory as the executable. The database stores the filepath.

        """

        if self._currentCount != self._pasteBoard.changeCount():

            dataType = self._pasteBoard.types()
            cardId = uuid.uuid4().hex
            if NSStringPboardType in dataType:
                pbstring = self._pasteBoard.stringForType_(NSStringPboardType)
                if validators.url(pbstring):
                    category = "URL"
                else:
                    category = "Text"
                if not pbstring.isspace():
                    self.dao.storeCard(cardId, pbstring, category, 0, 0)
                    if (self._uiStatus['ALL_STATE'] or (self._uiStatus['TEXT_STATE'] and category == 'Text')
                            or (self._uiStatus['URL_STATE'] and category == 'URL')):
                        cardData = card.Card(cardId, pbstring, category, 0, 0)
                        card_generator.CardObject(self.cardRenderer.parent, self.dao, self.cardRenderer).addToInterface(
                            cardData)
            elif NSTIFFPboardType in dataType:
                pbimage = self._pasteBoard.dataForType_(NSTIFFPboardType)
                image = Image.open(io.BytesIO(pbimage))
                filepath = "img_copy/" + str(uuid.uuid4()) + ".png"
                image.save(filepath, quality=95)
                category = "Image"
                self.dao.storeCard(cardId, filepath, category, 0, 0)

                if self._uiStatus['ALL_STATE'] or self._uiStatus['IMAGE_STATE']:
                    cardData = card.Card(cardId, filepath, category, 0, 0)
                    card_generator.CardObject(self.cardRenderer.parent, self.dao, self.cardRenderer).addToInterface(
                        cardData)
            self._currentCount = self._pasteBoard.changeCount()

    def manageClip(self):
        """
            The function to retrieve the count of items in the clipboard every second.

            The function calls the updateUi function to update the interface every second.

        """

        self._currentCount = self._pasteBoard.changeCount()
        self._timer.timeout.connect(lambda: self.queryClipboard())
        self._timer.start(1000)


if __name__ == "__main__":
    gc = ClipboardManager()
    gc.manage_clip()
    print()
