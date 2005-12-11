from zope.interface import Interface, Attribute

class IMessage(Interface):
    """A single status message."""

    message = Attribute('The text of this message. Usally a Message object.')

    type = Attribute('The type of this message.')


class IStatusMessageUtility(Interface):
    """A utility for handling status messages."""

    def addStatusMessage(context, text, type=''):
        """Add a status message."""

    def getStatusMessages(context):
        """Returns all status messages.
        """

    def clearStatusMessages(context):
        """Removes all status messages."""

    def showStatusMessages(context):
        """Removes all status messages and returns them for display.
        """

