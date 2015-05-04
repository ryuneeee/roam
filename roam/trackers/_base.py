import os

from abc import abstractmethod
from http import cookiejar
from urllib import request, parse
import urllib

__author__ = 'Ryun'

class Tracker():

    def __init__(self):
        super().__init__()
        self.name = os.path.splitext(os.path.basename(__file__))[0]
        self.cj = None

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

    def cookie(self):
        if self.cj is None:
            raise ValueError('Cookie is not yet.')
        return self.cj


    def request_post(self, url, data=None, cookie_jar=cookiejar.CookieJar()):

        encoded_data = self.prepare_urlencode(data)
        opener = request.build_opener(request.HTTPCookieProcessor(cookie_jar))

        resp = opener.open(url, encoded_data)
        return cookie_jar, resp

    def request_get(self, url, cookie_jar):
        cj, resp = self.request_post(url, cookie_jar=cookie_jar)
        return resp

    def request_login(self, url, data):
        cj, resp = self.request_post(url, data)
        return cj

    def prepare_urlencode(self, data):
        if data is None:
            return data
        elif type(data) is dict:
            data = parse.urlencode(data)
            return data.encode('utf-8')
        else:
            return parse.quote(data)