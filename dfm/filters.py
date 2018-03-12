# -*- coding: utf-8 -*-
# File   : filters.py
# Author : Jiayuan Mao
# Email  : maojiayuan@gmail.com
# Date   : 09/03/2018
#
# This file is part of dotfiles.

import six
import platform


class Filter(object):
    def __call__(self):
        return self.eval()

    def eval(self):
        raise NotImplementedError()


class PlatformFilter(Filter):
    def __init__(self, allows):
        if isinstance(allows, six.string_types):
            allows = [allows]
        self.allows = [s.lower() for s in allows]

    def eval(self):
        sys = platform.system().lower()
        return sys in self.allows


class OSXFilter(PlatformFilter):
    def __init__(self):
        super(OSXFilter, self).__init__('Darwin')


class LinuxFilter(PlatformFilter):
    def __init__(self):
        super(LinuxFilter, self).__init__('Linux')


class ConditionalCallable(object):
    def __init__(self, filters=None):
        self.filters = filters if filters is not None else []

    def __call__(self, *args, **kwargs):
        if self.eval_filter():
            self.eval()

    def eval(self):
        raise NotImplementedError()

    def eval_filter(self):
        ret = True
        for f in self.filters:
            if not f():
                ret = False
        return ret
