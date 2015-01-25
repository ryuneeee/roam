import unittest
from synology.auth import is_syno_user, is_group_member

from test.fake_syno_shell import FakeSyno


class synoAuth(unittest.TestCase):
    def setUp(self):
        super().setUp()
        self.syno = FakeSyno(user='ryun', password='secret')

    def test_login(self):
        self.assertTrue(is_syno_user('ryun', 'secret'))
        self.assertFalse(is_syno_user('ryun', 'hello'))
        self.assertFalse(is_syno_user('not user', 'not user'))

    def test_group(self):
        self.syno.add_user_to_group('ryun', 'ryunbox')
        self.syno.add_user('ryuneeee', 'secret2', 'ryunbox')
        self.assertTrue(is_group_member(user='ryun', group='ryunbox'))
        self.assertTrue(is_group_member(user='ryuneeee', group='ryunbox'))
        self.assertFalse(is_group_member('ryunbox', 'empty'))
        self.assertFalse(is_group_member('empty', 'ryun'))

    def tearDown(self):
        super().tearDown()
        self.syno.rollback_popen()

