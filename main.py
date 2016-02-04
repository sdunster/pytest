from __future__ import absolute_import
import sys, os
sys.path.append(os.path.dirname(__file__))

import lib

print(dir(lib))
lib.test_a()
lib.test_b()
lib.test_c()
