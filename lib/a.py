from __future__ import absolute_import
import importlib
b = importlib.import_module('..b', __name__)

def test_a():
    print(b.test_b)
