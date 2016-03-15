#!/usr/bin/env python

#-----------------------------------------------------------------------------------------------------------------------
# INFO:
#-----------------------------------------------------------------------------------------------------------------------

"""
Author: Evan Hubinger
License: Apache 2.0
Description: Basic Coconut constants and compatibility handling.
"""

#-----------------------------------------------------------------------------------------------------------------------
# IMPORTS:
#-----------------------------------------------------------------------------------------------------------------------

from __future__ import print_function, absolute_import, unicode_literals, division

try:
    import readline
except ImportError:
    readline = None

import sys

#-----------------------------------------------------------------------------------------------------------------------
# CONSTANTS:
#-----------------------------------------------------------------------------------------------------------------------

VERSION = "0.3.6"
VERSION_NAME = "Odisha"
DEVELOP = True

if DEVELOP:
    VERSION += "-post_dev"
__version__ = VERSION
VERSION_STR = VERSION + " [" + VERSION_NAME + "]"
VERSION_TAG = "v" + VERSION_STR
PY2 = sys.version_info < (3,)
PY2_HEADER_BASE = r'''py2_chr, py2_filter, py2_hex, py2_input, py2_int, py2_map, py2_oct, py2_open, py2_print, py2_range, py2_raw_input, py2_str, py2_xrange, py2_zip = chr, filter, hex, input, int, map, oct, open, print, range, raw_input, str, xrange, zip
_coconut_int, _coconut_long, _coconut_print, _coconut_raw_input, _coconut_str, _coconut_unicode, _coconut_xrange = int, long, print, raw_input, str, unicode, xrange
from future_builtins import *
chr, str = unichr, unicode
from io import open
class range(object):
    __slots__ = ("_xrange",)
    __doc__ = _coconut_xrange.__doc__
    __coconut_is_lazy__ = True
    def __init__(self, *args):
        self._xrange = _coconut_xrange(*args)
    def __iter__(self):
        return __coconut__.iter(self._xrange)
    def __reversed__(self):
        return __coconut__.reversed(self._xrange)
    def __len__(self):
        return __coconut__.len(self._xrange)
    def __getitem__(self, index):
        if __coconut__.isinstance(index, __coconut__.slice):
            start, stop, step = index.start, index.stop, index.step
            if start is None:
                start = 0
            elif start < 0:
                start += __coconut__.len(self._xrange)
            if stop is None:
                stop = __coconut__.len(self._xrange)
            elif stop is not None and stop < 0:
                stop += __coconut__.len(self._xrange)
            if step is None:
                step = 1
            return __coconut__.map(self._xrange.__getitem__, self.__class__(start, stop, step))
        else:
            return self._xrange[index]
    def __repr__(self):
        return __coconut__.repr(self._xrange)[1:]
    def __reduce_ex__(self, protocol):
        return (self.__class__,) + self._xrange.__reduce_ex__(protocol)[1:]
class int(_coconut_int):
    __slots__ = ()
    __doc__ = _coconut_int.__doc__
    class __metaclass__(type):
        def __instancecheck__(cls, inst):
            return __coconut__.isinstance(inst, (_coconut_int, _coconut_long))
class bytes(_coconut_str):
    __slots__ = ()
    __doc__ = _coconut_str.__doc__
    class __metaclass__(type):
        def __instancecheck__(cls, inst):
            return __coconut__.isinstance(inst, _coconut_str)
    def __new__(cls, *args, **kwargs):
        return _coconut_str.__new__(cls, __coconut__.bytearray(*args, **kwargs))
def print(*args, **kwargs):
    if __coconut__.hasattr(_coconut_sys.stdout, "encoding") and _coconut_sys.stdout.encoding is not None:
        return _coconut_print(*(_coconut_unicode(x).encode(_coconut_sys.stdout.encoding) for x in args), **kwargs)
    else:
        return _coconut_print(*(_coconut_unicode(x).encode() for x in args), **kwargs)
def input(*args, **kwargs):
    if __coconut__.hasattr(_coconut_sys.stdout, "encoding") and _coconut_sys.stdout.encoding is not None:
        return _coconut_raw_input(*args, **kwargs).decode(_coconut_sys.stdout.encoding)
    else:
        return _coconut_raw_input(*args, **kwargs).decode()
print.__doc__, input.__doc__ = _coconut_print.__doc__, _coconut_raw_input.__doc__
def raw_input(*args):
    """Raises NameError."""
    raise __coconut__.NameError('Coconut uses Python 3 "input" instead of Python 2 "raw_input"')
def xrange(*args):
    """Raises NameError."""
    raise __coconut__.NameError('Coconut uses Python 3 "range" instead of Python 2 "xrange"')
if _coconut_sys.version_info < (2, 7):
    import functools as _coconut_functools, copy_reg as _coconut_copy_reg
    def _coconut_new_partial(func, args, keywords):
        return _coconut_functools.partial(func, *args, **keywords)
    _coconut_copy_reg.constructor(_coconut_new_partial)
    def _coconut_reduce_partial(self):
        return (_coconut_new_partial, (self.func, self.args, self.keywords))
    _coconut_copy_reg.pickle(_coconut_functools.partial, _coconut_reduce_partial)'''
PY2_HEADER = "import sys as _coconut_sys, os as _coconut_os\n" + PY2_HEADER_BASE + "\n"
PY2_HEADER_CHECK = r'''import sys as _coconut_sys
if _coconut_sys.version_info < (3,):
    import os as _coconut_os
'''
for _line in PY2_HEADER_BASE.splitlines():
    PY2_HEADER_CHECK += "    " + _line + "\n"
PY2_HEADER_CHECK += r'''else:
    py3_map, py3_zip = map, zip
'''
PY3_HEADER = r'''import sys as _coconut_sys
py3_map, py3_zip = map, zip
'''

#-----------------------------------------------------------------------------------------------------------------------
# SETUP:
#-----------------------------------------------------------------------------------------------------------------------

if PY2:
    import __builtin__ as __coconut__
    exec(PY2_HEADER)
