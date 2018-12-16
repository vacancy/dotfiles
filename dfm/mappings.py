# -*- coding: utf-8 -*-
# File   : mappings.py
# Author : Jiayuan Mao
# Email  : maojiayuan@gmail.com
# Date   : 09/03/2018
#
# This file is part of dotfiles.

import os
import os.path as osp
import shutil
import contextlib

from .filters import ConditionalCallable
from .logging import get_logger

logger = get_logger(__file__)

__all__ = ['Copy', 'Link', 'FSMappings']


class FSMappingBase(ConditionalCallable):
    BASEPATH_SRC = '/'
    BASEPATH_DST = '/'

    def _get_path_src(self, path):
        return osp.realpath(osp.join(FSMappingBase.BASEPATH_SRC, path))

    def _get_path_dst(self, path):
        return osp.join(FSMappingBase.BASEPATH_DST, path)

    def _make_dir_of_file(self, file):
        if not osp.isdir(osp.dirname(file)):
            os.makedirs(osp.dirname(file), exist_ok=True)
        if osp.exists(file):
            if osp.isdir(file):
                shutil.rmtree(file, ignore_errors=True)
            if osp.isfile(file):
                os.remove(file)


class Copy(FSMappingBase):
    def __init__(self, file, dest, overwrite=True, follow_symlinks=False, *, desc=None, filters=None):
        super(Copy, self).__init__(desc=desc, filters=filters)

        self.file = file
        self.dest = dest
        self.overwrite = overwrite
        self.follow_symlinks = follow_symlinks

    def eval(self):
        file = self._get_path_src(self.file)
        dest = self._get_path_dst(self.dest)

        if osp.exists(dest):
            if not self.overwrite:
                logger.warning('  Skip existing file: "{}".'.format(dest))
                return
            else:
                logger.warning('  Overwriting existing file: "{}".'.format(dest))

        self._make_dir_of_file(dest)

        logger.info('  Copy: src="{}", dst="{}".'.format(file, dest))

        if osp.isdir(file):
            if osp.isdir(dest):
                dest = osp.join(dest, osp.basename(file))
            shutil.copytree(file, dest, symlinks=not self.follow_symlinks)
        else:
            shutil.copy2(file, dest, follow_symlinks=self.follow_symlinks)


class Link(FSMappingBase):
    def __init__(self, file, dest, relative=False, *, desc=None, filters=None):
        super(Link, self).__init__(desc=desc, filters=filters)

        self.file = file
        self.dest = dest
        self.relative = relative

    def eval(self):
        file = self._get_path_src(self.file)
        dest = self._get_path_dst(self.dest)

        self._make_dir_of_file(dest)

        logger.info('  Link: src="{}", dst="{}".'.format(file, dest))

        if os.path.exists(dest):
            os.remove(dest)
        if self.relative:
            src_path = osp.relpath(file, start=osp.dirname(dest))
        else:
            src_path = file
        os.symlink(src_path, dest)


class FSMappings(FSMappingBase):
    def __init__(self, directory, *args, desc=None, filters=None, directory_dest=''):
        super(FSMappings, self).__init__(desc=desc, filters=filters)
        self.directory = directory.strip()
        self.directory_dest = directory_dest.strip()
        self.modules = args

    def eval(self):
        if self.directory != '/':
            with append_dir(self.directory, self.directory_dest):
                for m in self.modules:
                    m()
        else:
            for m in self.modules:
                m()


@contextlib.contextmanager
def change_dir(src_dir, dst_dir):
    backup = FSMappingBase.BASEPATH_SRC, FSMappingBase.BASEPATH_DST
    FSMappingBase.BASEPATH_SRC, FSMappingBase.BASEPATH_DST = src_dir, dst_dir
    logger.info('Change current directory: src="{}", dst="{}".'.format(src_dir, dst_dir))
    yield
    FSMappingBase.BASEPATH_SRC, FSMappingBase.BASEPATH_DST = backup


@contextlib.contextmanager
def append_dir(src_dir, dst_dir):
    backup = FSMappingBase.BASEPATH_SRC, FSMappingBase.BASEPATH_DST
    FSMappingBase.BASEPATH_SRC, FSMappingBase.BASEPATH_DST = osp.join(backup[0], src_dir), osp.join(backup[1], dst_dir)
    logger.info('Append current directory: src="{}", dst="{}".'.format(src_dir, dst_dir))
    yield
    FSMappingBase.BASEPATH_SRC, FSMappingBase.BASEPATH_DST = backup
