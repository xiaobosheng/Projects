# Find PI to the Nth Digit
# -*- coding: utf-8 -*-

from math import atan
from types import IntType
def pidecimal(n):
    assert type(n) is IntType, "number is not an interger %r" %n
    print ('{:.%df}' % n).format(4 * (4 * atan(1.0/5.0) - atan(1.0/239.0)))

pidecimal(10)
