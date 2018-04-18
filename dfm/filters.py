# -*- coding: utf-8 -*-
# File   : filters.py
# Author : Jiayuan Mao
# Email  : maojiayuan@gmail.com
# Date   : 09/03/2018
#
# This file is part of dotfiles.

import os.path as osp
import platform

from .logging import get_logger

logger = get_logger(__file__)

__all__ = ['Filter', 'PlatformFilter', 'OSXFilter', 'LinuxFilter', 'NotExists', 'ConditionalCallable']


class Filter(object):
    def __call__(self):
        return self.eval()

    def eval(self):
        raise NotImplementedError()


class PlatformFilter(Filter):
    def __init__(self, allows):
        if isinstance(allows, str):
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


class NotExists(Filter):
    def __init__(self, file):
        self.file = file
        if self.file.startswith('~'):
            self.file = osp.expanduser(self.file)

    def eval(self):
        return osp.exists(self.file)


class ConditionalCallable(object):
    def __init__(self, desc=None, filters=None):
        self.desc = desc
        self.filters = filters if filters is not None else []

    def __call__(self, *args, **kwargs):
        if self.eval_filter():
            if self.desc is not None:
                logger.critical('[Exec] {}'.format(self.desc))
            self.eval()
        else:
            if self.desc is not None:
                logger.critical('[Skip] {}'.format(self.desc))

    def eval(self):
        raise NotImplementedError()

    def eval_filter(self):
        ret = True
        for f in self.filters:
            if not f():
                ret = False
        return ret
