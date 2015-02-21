import re
from ..settings import REGEX


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

    s = re.search(regex, sub, re.IGNORECASE)

    if s:
        ends = []
        for group in s.groups():
            if group is not None: ends.append(int(group))

        res.extend(tuple_by_ends(ends))

    return tuple(res)


def extract_seasons(sub):
    return extract_groups(REGEX['seasons'], sub)


def extract_episode(sub):
    return extract_groups(REGEX['episodes'], sub)

def extract_date(sub):
    return extract_etc(sub, REGEX['date'])

def extract_etc(sub, regex):
    return tuple(re.findall(regex, sub, re.IGNORECASE))

def extract_resolution(sub):
    return extract_etc(sub, REGEX['resolution'])

def extract_video_codec(sub):
    return extract_etc(sub, REGEX['video_codec'])

def extract_audio_codec(sub):
    return extract_etc(sub, REGEX['audio_codec'])

def extract_source(sub):
    return extract_etc(sub, REGEX['source'])