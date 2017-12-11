# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from argparse import ArgumentParser
from time import time
from random import Random as PyRandom
from matplotlib import pyplot as plot


class Random(object):

    _n = 100000

    def __init__(self, seed=None):
        self._current = seed or int(time() * 10000)

    def next(self):
        raise NotImplementedError

    def stats(self):
        values = [self.next() for _ in xrange(self._n)]
        weights = [1.0 / self._n for _ in xrange(self._n)]
        plot.hist(values, 50, weights=weights)
        plot.show()


class MiddleSquareRandom(Random):

    __shift = 10 ** 2
    __module = 10 ** 4

    def next(self):
        square = self._current * self._current
        self._current = square // self.__shift % self.__module
        return float(self._current) / self.__module


class MultiplicativeCongruentialRandom(Random):

    __k = 10 ** 9 + 7
    __m = 2 ** 32 - 1

    def next(self):
        self._current = self.__k * self._current % self.__m
        return float(self._current) / self.__m

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-ms', '--middle-square', action='store_true')
    parser.add_argument('-mc', '--multiplicative-congruential', action='store_true')
    args = parser.parse_args()

    if args.middle_square:
        MiddleSquareRandom().stats()
    elif args.multiplicative_congruential:
        MultiplicativeCongruentialRandom().stats()

