import os
import re

def signin(user, password):
    result = os.popen('synouser --login %s %s' % (user, password)).read()
    return 'OK' in result


def is_group_member(group, user):
    result = os.popen('synogroup --get %s' % group).read()
    list = tuple(result.split('\n'))[4:-1]
    for one in list:
        p = re.compile('\[.*\]')
        if user == p.search(one).group()[1:-1]:
            return True
    return False

