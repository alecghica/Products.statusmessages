from zope.interface import implements

from Products.statusmessages.message import Message
from Products.statusmessages.interfaces import IStatusMessageUtility

global_messages = {}

class StatusMessageUtility(object):
    """Utility for handling status messages.
    
    Let's make sure that this implementation actually fulfills the
    'IStatusMessageUtility' API.

      >>> from Products.statusmessages.interfaces import IStatusMessageUtility
      >>> from Products.statusmessages.utility import StatusMessageUtility

      >>> from zope.interface.verify import verifyClass
      >>> verifyClass(IStatusMessageUtility, StatusMessageUtility)
      True

    """
    implements(IStatusMessageUtility)

    def addStatusMessage(self, context, text, type=''):
        """Add a status message.
        """
        message = Message(text, type)

        # XXX
        browserid = 'user'
        if global_messages.has_key(browserid):
            global_messages[browserid].append(message)
        else:
            global_messages[browserid] = [message]

    def getStatusMessages(self, context):
        """Returns all status messages.
        """
        # XXX
        browserid = 'user'
        if not global_messages.has_key(browserid):
            return []
        return global_messages.get(browserid)

    def clearStatusMessages(self, context):
        """Removes all status messages.
        """
        # XXX
        browserid = 'user'
        if global_messages.has_key(browserid):
            global_messages[browserid] = []

    def showStatusMessages(self, context):
        """Removes all status messages and returns them for display.
        """
        messages = self.getStatusMessages(context)
        if messages is not []:
            self.clearStatusMessages(context)
        return messages

utility = StatusMessageUtility()
