"""
That module provides two function for extracting favicons:
    * find_favicon_from_url
    * find_favicon_from_dump

Technical details about favicon: http://en.wikipedia.org/wiki/Favicon
"""
import urllib2
import re
from urlparse import urljoin, urlsplit
import logging
import socket

__all__ = ['find_favicon_from_url', 'find_favicon_from_dump']

RE_LINK = re.compile(r'<link[^>]+>', re.I | re.S)
RE_ICON_REL = re.compile(r'rel*=\s*["\']?\s*(?:shortcut\s+)?icon[ "\'>]', re.I | re.S)
RE_HREF = re.compile(r'href\s*=\s*["\']?([^"\' >]+)', re.I | re.S)
SOCKET_TIMEOUT = 30

def setup_socket_timeout(func):
    def decorated(*args, **kwargs):
        oldtimeout = socket.getdefaulttimeout()
        socket.setdefaulttimeout(SOCKET_TIMEOUT)
        try:
            return func(*args, **kwargs)
        finally:
            socket.setdefaulttimeout(oldtimeout)
    return decorated


@setup_socket_timeout
def find_favicon_from_url(url):
    """
    Try to find the favicon of domain which hosts given url.

    If no link tag was found then try to check default URL for existing image.

    Returns:
        The favicon full URL or None if no favicon was found.
    """

    try:
        dump = urllib2.urlopen(url).read()
    except Exception, ex:
        logging.error(ex.message)
    else:
        icon_url = find_favicon_from_dump(dump, url)
        if icon_url:
            return icon_url

    host = urlsplit(url).hostname
    icon_url = 'http://%s/favicon.ico' % host
    try:
        req = urllib2.urlopen(icon_url)
    except Exception, ex:
        logging.error(ex.message)
    else:
        if req.code == 200:
            ctype = req.headers.get('content-type', '')
            if ctype.startswith('image/'):
                return icon_url

    return None



def find_icon_element(dump):
    """
    Find <link> element with proper rel attribute and existing href attribute.

    Returns:
        HTML code of <link> element or None if it was not found
    """

    for link in RE_LINK.findall(dump):
        match = RE_ICON_REL.search(link)
        if match:
            match = RE_HREF.search(link)
            if match:
                return match.group(1)
    return None


def find_favicon_from_dump(dump, page_url=None):
    """
    Try to find favicon url in given HTML dump.

    If url was found try to make it absolute if url was given.

    Returns:
        Favicon URL or None if it was not found.
    """

    icon_url = find_icon_element(dump)
    if icon_url and page_url:
        icon_url = urljoin(page_url, icon_url)
    return icon_url


if __name__ == '__main__':
    assert find_icon_element('<link rel="icon" href="foo">')
    assert find_icon_element('<link rel=\'icon\' href="foo">')
    assert find_icon_element('<link rel=icon href="foo">')
    assert find_icon_element('<link rel="shortcut icon" href="foo">')
    assert find_icon_element('<link rel="shortcut icon " href="foo">')
    
    assert find_favicon_from_dump('<link rel="icon" href="foo">') == 'foo'
    assert find_favicon_from_dump('<link rel="icon" href="foo">', 'http://ya.ru') == 'http://ya.ru/foo'
    assert find_favicon_from_dump('<link rel="icon" href="/foo">', 'http://ya.ru/bar') == 'http://ya.ru/foo'
    #print find_favicon_from_url('http://ya.ru')
    #print find_favicon_from_url('http://bitbucket.org')
