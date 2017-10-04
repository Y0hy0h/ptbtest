from typing import List, Dict

from telegram.utils.request import Request


class MockRequest(Request):
    def __init__(self):
        super().__init__()
        self.sent_messages: List[Dict] = []

    def _request_wrapper(self, *args, **kwargs):
        pass

    def post(self, url, data, timeout=None):
        self.sent_messages.append(data)

    @staticmethod
    def _parse(json_data):
        pass
