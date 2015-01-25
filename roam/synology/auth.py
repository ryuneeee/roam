import os
import re

def is_syno_user(user, password):
    result = os.popen('synouser --login %s %s' % (user, password)).read()
    return result == 'LOGIN OK.'


def is_group_member(user, group):
    result = os.popen('synogroup --get %s' % group).read().split('\n')[4:-1]
    list = tuple(result)
    for one in list:
        p = re.compile('\[.*\]')
        if user == p.search(one).group()[1:-1]:
            return True
    return False