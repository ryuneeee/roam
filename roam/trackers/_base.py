import os

from abc import abstractmethod
from http import cookiejar
from urllib import request, parse

__author__ = 'Ryun'

class Tracker():

    def __init__(self):
        super().__init__()
        self.name = os.path.splitext(os.path.basename(__file__))[0]

    @abstractmethod
    def login(self):
        """
        Login to tracker.
        :return: dumps cookie Jar
        """
        raise NotImplementedError('Not implemented yet.')

    @abstractmethod
    def fetch(self):
        """
        Fetch to main page at tracker using cookie store
        :return: torrent tuple
        """
        raise NotImplementedError('Not implemented yet.')

    @abstractmethod
    def search(self, keyword):
        """
        Search torrent
        :return: torrent tuple
        """
        raise NotImplementedError('Not implemented yet.')

    @abstractmethod
    def download(self):
        """
        Downlaod torrent from tracker
        :return: torrent binary
        """
        raise NotImplementedError('Not implemented yet.')

    def post(self, url, data):
        encoded_data = self.prepare_urlencode(data)
        cj = cookiejar.CookieJar()
        opener = request.build_opener(request.HTTPCookieProcessor(cj))
        resp = opener.open(url, encoded_data)
        return cj

    def prepare_urlencode(self, data):
        if type(data) is dict:
            data = parse.urlencode(data)
            return data.encode('utf-8')
        else:
            return data