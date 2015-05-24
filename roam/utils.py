from http import cookiejar
from urllib import request, parse

__author__ = 'Ryun'


def request_post(url, data=None, cookie_jar=cookiejar.CookieJar()):
    encoded_data = prepare_urlencode(data)
    opener = request.build_opener(request.HTTPCookieProcessor(cookie_jar))

    resp = opener.open(url, encoded_data)
    return cookie_jar, resp

def request_get(url, cookie_jar):
    cj, resp = request_post(url, cookie_jar=cookie_jar)
    return resp

def request_login(url, data):
    cj, resp = request_post(url, data)
    return cj

def prepare_urlencode(data):
    if data is None:
        return data
    elif type(data) is dict:
        data = parse.urlencode(data)
        return data.encode('utf-8')
    else:
        return parse.quote(data)
