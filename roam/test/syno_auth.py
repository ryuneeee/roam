import unittest

from auth.synology import *
from test.fake_syno_shell import FakeSyno


class synoAuth(unittest.TestCase):


    def setUp(self):
        self.syno = FakeSyno(user='ryun', password='secret')

    def test_login(self):
        assert True == is_syno_user('ryun', 'secret')
        assert False == is_syno_user('ryun', 'hello')
        assert False == is_syno_user('not user', 'not user')

    def test_group(self):
        self.syno.add_user_to_group('ryun', 'ryunbox')
        self.syno.add_user('ryuneeee', 'secret2', 'ryunbox')
        assert True == is_group_member(user='ryun', group='ryunbox')
        assert True == is_group_member(user='ryuneeee', group='ryunbox')
        assert False == is_group_member('ryunbox', 'empty')
        assert False == is_group_member('empty', 'ryun')

    def tearDown(self):
        self.syno.rollback_popen()

