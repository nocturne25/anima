# -*- coding: utf-8 -*-
# Copyright (c) 2012-2014, Anima Istanbul
#
# This module is part of anima-tools and is released under the BSD 2
# License: http://www.opensource.org/licenses/BSD-2-Clause

import os
import re
import itertools
import logging
import calendar
import datetime


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# tr_chars = {
#     # lower letters
#     u'\xc3\xa7': 'c',
#     u'\xc4\x9f': 'g',
#     u'\xc4\xb1': 'i',
#     u'\xc3\xb6': 'o',
#     u'\xc5\x9f': 's',
#     u'\xc3\xbc': 'u',
#
#     # upper letters
#     u'\xc3\x87': 'C',
#     u'\xc4\x9e': 'G',
#     u'\xc4\xb0': 'I',
#     u'\xc3\x96': 'O',
#     u'\xc5\x9e': 'S',
#     u'\xc3\x9c': 'U',
# }

validFileNameChars = r' abcdefghijklmnoprqstuvwxyzABCDEFGHIJKLMNOPRQSTUVWXYZ' \
                     r'0123456789._-'
validTextChars = validFileNameChars + r'!^+%&(){}[]:;?,|@`\'"/=*~$#'

validFileNameCharsPattern = re.compile(r'[\w\.\- ]+')
validTextCharsPattern = re.compile(
    r'[\w\.\- !\^+%&\(\)\{\}\[\]:;?,|\\@`\'"/=*~$#]+')


def all_equal(elements):
    """return True if all the elements are equal, otherwise False.
    """
    first_element = elements[0]

    for other_element in elements[1:]:
        if other_element != first_element:
            return False

    return True


def common_prefix(*sequences):
    """return a list of common elements at the start of all sequences, then a
    list of lists that are the unique tails of each sequence.
    """
    # if there are no sequences at all, we're done
    if not sequences:
        return [], []
    # loop in parallel on the sequences
    common = []
    for elements in itertools.izip(*sequences):
        # unless all elements are equal, bail out of the loop
        if not all_equal(elements):
            break

        # got one more common element, append it and keep looping
        common.append(elements[0])

    # return the common prefix and unique tails
    return common, [sequence[len(common):] for sequence in sequences]


def relpath(p1, p2, sep=os.path.sep, pardir=os.path.pardir):
    """return a relative path from p1 equivalent to path p2.

    In particular:

        the empty string, if p1 == p2;
        p2, if p1 and p2 have no common prefix.

    """
    # replace any trailing slashes at the end
    p1 = re.sub(r"[/]+$", "", p1)
    p1 = re.sub(r"[\\]+$", "", p1)

    common, (u1, u2) = common_prefix(p1.split(sep), p2.split(sep))
    if not common:
        return p2  # leave path absolute if nothing at all in common

    return sep.join([pardir] * len(u1) + u2)


def open_browser_in_location(path):
    """Opens the os native browser at the given path

    :param path: The path that the browser should be opened at.
    """
    import os
    import subprocess
    import platform

    command = []

    platform_info = platform.platform()

    path = os.path.normpath(os.path.expandvars(path))

    if not os.path.exists(path):
        path = os.path.dirname(path)

    if platform_info.startswith('Linux'):
        command = 'nautilus ' + path
    elif platform_info.startswith('Windows'):
        if os.path.isdir(path):
            command = 'explorer ' + path.replace('/', '\\')
        elif os.path.isfile(path):
            command = 'explorer /select,' + path.replace('/', '\\')
    elif platform_info.startswith('Darwin'):
        # TODO: finder can not open files for now, fix it later
        if not os.path.isdir(path):
            path = os.path.dirname(path)
        command = 'open -a /System/Library/CoreServices/Finder.app ' + path

    if os.path.exists(path):
        subprocess.call(command, shell=True)
    else:
        raise IOError("%s doesn't exists!" % path)


def md5_checksum(path):
    """generates md5 of a file with the given path

    :param path: absolute path to  the file
    """
    import hashlib

    m = hashlib.md5()
    with open(path) as f:
        chunk = f.read(8192)
        while chunk:
            m.update(chunk)
            chunk = f.read(8192)
    return m.digest()


class StalkerThumbnailCache(object):
    """A simple file cache system
    """

    @classmethod
    def get(cls, thumbnail_full_path, login=None, password=None):
        """returns the file either from cache or from stalker server
        """
        import anima

        # look up in the cache first
        filename = os.path.basename(thumbnail_full_path)
        logger.debug('filename : %s' % filename)

        cache_path = os.path.expanduser(anima.local_cache_folder)
        cached_file_full_path = os.path.join(cache_path, filename)

        url = '%s/%s' % (
            anima.stalker_server_internal_address,
            thumbnail_full_path
        )
        login_url = '%s/login' % anima.stalker_server_internal_address

        logger.debug('cache_path            : %s' % cache_path)
        logger.debug('cached_file_full_path : %s' % cached_file_full_path)
        logger.debug('url                   : %s' % url)

        if not os.path.exists(cached_file_full_path) and login and password:
            # download the file and put it on to the cache
            import urllib
            import urllib2
            import cookielib

            cj = cookielib.CookieJar()
            opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
            login_data = urllib.urlencode({
                'login': login,
                'password': password,
                'submit': True
            })
            opener.open(login_url, login_data)

            resp = opener.open(url)
            data = resp.read()

            # put it in to a file
            # TODO: from header decide ascii or binary mode
            if not os.path.exists(cache_path):
                os.makedirs(cache_path)

            with open(cached_file_full_path, 'wb') as f:
                f.write(data)

        return cached_file_full_path


def multiple_replace(text, adict):
    rx = re.compile('|'.join(map(re.escape, adict)))

    def one_xlat(match):
        return adict[match.group(0)]

    return rx.sub(one_xlat, text)


def unique(s):
    """ Return a list of elements in s in arbitrary order, but without
    duplicates.
    """

    # Try using a set first, because it's the fastest and will usually work
    try:
        return list(set(s))
    except TypeError:
        pass  # Move on to the next method

    # Since you can't hash all elements, try sorting, to bring equal items
    # together and then weed them out in a single pass
    t = list(s)
    try:
        t.sort()
    except TypeError:
        del t  # Move on to the next method
    else:
        # the sort worked, so we are fine
        # do weeding
        return [x for i, x in enumerate(t) if not i or x != t[i - 1]]
    # Brute force is all that's left
    u = []
    for x in s:
        if x not in u:
            u.append(x)

    return u


def embedded_numbers(s):
    re_digits = re.compile(r'(\d+)')
    pieces = re_digits.split(str(s))
    pieces[1::2] = map(int, pieces[1::2])
    return pieces


def sort_strings_with_embedded_numbers(data):
    """Sorts a string with embedded numbers

    :param list data: A list of strings
    """
    return sorted(data, key=embedded_numbers)


def do_db_setup():
    """the common routing for setting up the database
    """
    from sqlalchemy.exc import UnboundExecutionError

    from stalker import db
    from stalker.db import DBSession

    DBSession.remove()
    DBSession.close()

    try:
        DBSession.connection()
        print('already connected, not creating any new connections')
    except UnboundExecutionError:
        # no connection do setup
        print('doing a new connection')
        db.setup()


def utc_to_local(utc_dt):
    """converts utc time to local time

    based on the answer of J.F. Sebastian on
    http://stackoverflow.com/questions/4563272/how-to-convert-a-python-utc-datetime-to-a-local-datetime-using-only-python-stand/13287083#13287083
    """
    # get integer timestamp to avoid precision lost
    timestamp = calendar.timegm(utc_dt.timetuple())
    local_dt = datetime.datetime.fromtimestamp(timestamp)
    assert utc_dt.resolution >= datetime.timedelta(microseconds=1)
    return local_dt.replace(microsecond=utc_dt.microsecond)


def local_to_utc(local_dt):
    """converts local datetime to utc datetime

    based on the answer of J.F. Sebastian on
    http://stackoverflow.com/questions/4563272/how-to-convert-a-python-utc-datetime-to-a-local-datetime-using-only-python-stand/13287083#13287083
    """
    # get the utc_dt as if the local_dt is utc and calculate the timezone
    # difference and add it to the local dt object
    logger.debug('utc_to_local(local_dt) : %s' % utc_to_local(local_dt))
    logger.debug('utc - local            : %s' % (utc_to_local(local_dt) - local_dt))
    logger.debug('local - (utc - local)  : %s' % (local_dt - (utc_to_local(local_dt) - local_dt)))
    return local_dt - (utc_to_local(local_dt) - local_dt)
