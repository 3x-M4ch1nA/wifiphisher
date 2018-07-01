from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from future import standard_library
standard_library.install_aliases()
from builtins import *
from . import constants
import importlib
from functools import wraps


def uimethod(func):
    def _decorator(data, *args, **kwargs):
        response = func(data, *args, **kwargs)
        return response

    func.is_uimethod = True
    return wraps(func)(_decorator)
