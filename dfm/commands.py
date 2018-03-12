# -*- coding: utf-8 -*-
# File   : commands.py
# Author : Jiayuan Mao
# Email  : maojiayuan@gmail.com
# Date   : 12/03/2018
#
# This file is part of dotfiles.

import six
import os
import os.path as osp
import subprocess
import contextlib

from .filters import ConditionalCallable
from .logging import get_logger

logger = get_logger(__file__)

__all__ = ['Command', 'Commands']


class CommandBase(ConditionalCallable):
    BASEPATH_CWD = '/'

    def __init__(self, cwd='/', desc=None, filters=None):
        super(CommandBase, self).__init__(desc=desc, filters=filters)
        self.cwd = cwd

    def _get_working_dir(self ,cwd):
        return osp.join(CommandBase.BASEPATH_CWD, cwd)


class Command(CommandBase):
    def __init__(self, cmd, cwd='/', desc=None, filters=None):
        super(Command, self).__init__(cwd=cwd, desc=desc, filters=filters)
        self.cmd = cmd

    def eval(self):
        cmd = self.cmd
        cwd = self._get_working_dir(self.cwd)
        logger.info('  Execute (cwd: "{}"): {}'.format(cwd, self.cmd))
        if isinstance(cmd, six.string_types):
            backup = os.getcwd()
            os.chdir(cwd)
            os.system(cmd)
            os.chdir(backup)
        else:
            subprocess.check_call(cmd, cwd=cwd)


class Commands(CommandBase):
    def __init__(self, cwd, *args, desc=None, filters=None):
        super(Commands, self).__init__(cwd=cwd, desc=desc, filters=filters)
        self.modules = list(args)

    def extends(self, modules):
        self.modules.extend(modules)

    def eval(self):
        if self.cwd != '/':
            with append_dir(self.cwd):
                for m in self.modules:
                    m()
        else:
            for m in self.modules:
                m()


@contextlib.contextmanager
def change_dir(working_dir):
    backup = CommandBase.BASEPATH_CWD
    CommandBase.BASEPATH_CWD = working_dir
    logger.info('Change current working directory: "{}".'.format(working_dir))
    yield
    CommandBase.BASEPATH_CWD = backup


@contextlib.contextmanager
def append_dir(working_dir):
    backup = CommandBase.BASEPATH_CWD
    CommandBase.BASEPATH_CWD = osp.join(backup, working_dir)
    logger.info('Append current working directory: "{}".'.format(working_dir))
    yield
    CommandBase.BASEPATH_CWD = backup
