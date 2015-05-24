import os

from abc import abstractmethod

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
