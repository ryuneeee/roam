import pytest
from auth.synology import *
from test.fake_syno_shell import FakeSyno



def test_login():

    syno = FakeSyno(user='ryun', password='secret')
    assert True == is_syno_user('ryun', 'secret')
    assert False == is_syno_user('ryun', 'hello')
    assert False == is_syno_user('not user', 'not user')
    syno.rollback_popen()

def test_group():

    syno = FakeSyno(user='ryun', password='secret', group='ryunbox')
    syno.add_user('ryuneeee', 'secret2', 'ryunbox')
    assert True == is_group_member(user='ryun', group='ryunbox')
    assert True == is_group_member(user='ryuneeee', group='ryunbox')
    assert False == is_group_member('ryunbox', 'empty')
    assert False == is_group_member('empty', 'ryun')
    syno.rollback_popen()

