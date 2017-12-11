# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from random import random
from numpy import arange


class RandomEvent(object):

    def imitate(self):
        raise NotImplementedError


class SimpleRandomEvent(RandomEvent):

    def __init__(self, p):
        self._p = p

    def imitate(self):
        x = random()
        return x <= self._p


class ComplexRandomEvent(RandomEvent):

    def __init__(self, pa):
        self._pa = pa

    def imitate(self):
        x1 = random()
        x2 = random()
        return (x1 <= self._pa and x2 <= self._pa)


class ComplexDependentRandomEvent(RandomEvent):

    def __init__(self, pa, pb, pba):
        self._pa = pa
        self._pb = pb
        self._pba = pba
        self._pbna = (pb - pba * pa) / (1 - pa)

    def imitate(self):
        x1 = random()
        x2 = random()
        a = (x1 <= self._pa)
        b = (a and (x2 <= self._pba)) or (not a and (x2 <= self._pbna))
        return a, b


class CompleteGroupRandomEvent(RandomEvent):

    def __init__(self, p):
        # assert sum(p) == 1
        self._p = p

    def imitate(self):
        x = random()
        k = 0
        while x > sum(self._p[:k]):
            k += 1
        return k - 1