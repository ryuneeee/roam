import re
from settings import REGEX_SEASONS, REGEX_EPISODES, REGEX_DATE


def tuple_by_ends(ends):

    if len(ends) < 1:
        return tuple(ends)
    else:
        ends.sort()
        start = ends[0]
        end = ends[len(ends) - 1]
        return tuple(map(lambda x: x, range(start, end + 1)))


def extract_groups(regex, sub):
    res = []

    s = re.search(regex, sub)

    if s:
        ends = []
        for group in s.groups():
            if group is not None: ends.append(int(group))

        res.extend(tuple_by_ends(ends))

    return tuple(res)

def extract_seasons(sub):
    return extract_groups(REGEX_SEASONS, sub)

def extract_episode(sub):
    return extract_groups(REGEX_EPISODES, sub)

def extract_date(sub):
    return tuple(re.findall(REGEX_DATE, sub))