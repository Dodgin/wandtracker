"""
Controller to interface with the Netflix-app.
Use the media controller to play, pause etc.
"""
from . import BaseController

MESSAGE_TYPE = "type"
TYPE_STATUS = "mdxSessionStatus"
ATTR_SCREEN_ID = "screenId"
APP_ID = "CA5E8412"


class NetflixController(BaseController):
    """ Controller to interact with Netflix namespace. """

    def __init__(self):
        super(NetflixController, self).__init__(
            "urn:x-cast:mdx-netflix-com:service:target:2", "233637DE")

        self.screen_id = None

    def receive_message(self, message, data):
        """ Called when a media message is received. """
        if data[MESSAGE_TYPE] == TYPE_STATUS:
            self._process_status(data.get('data'))

            return True

        return False

    def _process_status(self, status):
        """ Process latest status update. """
        self.screen_id = status.get(ATTR_SCREEN_ID)
