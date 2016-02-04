from __future__ import absolute_import
import importlib
c = importlib.import_module('..c', __name__)

def test_b():
    print(c.test_c)
