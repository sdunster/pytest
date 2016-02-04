from __future__ import absolute_import
import importlib
a = importlib.import_module('..a', __name__)

def test_c():
    print(a.test_a)
