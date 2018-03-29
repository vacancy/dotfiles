#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File   : repom
# Author : Jiayuan Mao
# Email  : maojiayuan@gmail.com
# Date   : 29/03/2018
#
# This file is part of dotfiles.

import six
import sys
import os
import os.path as osp
import time
import argparse
import subprocess
import functools

_print = print
print = functools.partial(_print, file=sys.stderr)
print_out = functools.partial(_print, file=sys.stdout)

parser = argparse.ArgumentParser('Repo Manager')
parser.add_argument('--prefix', default=None)
parser.set_defaults(action='help')
subparsers = parser.add_subparsers()

parser_get = subparsers.add_parser('get', help='Get a repo from github.')
parser_get.set_defaults(action='get')
parser_get.add_argument('repo')

parser_list = subparsers.add_parser('list', help='List repos.')
parser_list.set_defaults(action='list')
parser_list.add_argument('--short', action='store_true')

parser_status = subparsers.add_parser('status', help='Show states of repos.')
parser_status.set_defaults(action='status')
parser_status.add_argument('--all', action='store_true')

parser_find = subparsers.add_parser('find', help='Find to a repo')
parser_find.set_defaults(action='find')
parser_find.add_argument('repo')

parser_go = subparsers.add_parser('go', help='Go to a repo')
parser_go.set_defaults(action='go')
parser_go.add_argument('repo')

args = parser.parse_args()
known_places = ['~/Projects', '~/projects']


class Repo(object):
    def __init__(self, path):
        self.name = osp.basename(path)
        self.path = path

    @property
    def remote(self):
        return cli_eval('git remote -v get-url origin', cwd=self.path)

    @property
    def last_update(self):
        return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(osp.getmtime(
            osp.join(self.path, '.git', 'HEAD')
        )))

    @property
    def porcelain(self):
        return cli_eval('git status --porcelain', cwd=self.path)

    @property
    def is_clean(self):
        return len(self.porcelain) == 0

    def print(self, short=False):
        if short:
            print('{name}'.format(name=self.name))
        else:
            print('{name}\n  - Remote: {remote}\n  - LastUpdate: {last_update}'.format(
                    name=self.name,
                    remote=self.remote,
                    last_update=self.last_update
            ))

    def exec(self, cmd):
        return cli_exec(cmd, cwd=self.path)

    def go(self):
        print_out('cd {}'.format(self.path))


class RepoList(list):
    def print(self, short=False):
        for l in self:
            l.print(short=short)

    def find(self, name):
        name, name_input = name.lower(), name
        founds = []
        for l in self:
            if name in l.name.lower():
                founds.append(l)
        if len(founds) == 0:
            print('Unable to find repo: {}'.format(name_input))
            return None
        elif len(founds) == 1:
            print('Found repo: {}'.format(founds[0].name))
            return founds[0]
        else:
            print('Found multiple matched repos: '.format(name_input), end='')
            print(*[l.name for l in founds], sep='\t')
            return None


def locate_projects():
    if args.prefix is not None:
        return osp.realpath(args.prefix)
    for place in known_places:
        place = osp.expanduser(place)
        if osp.exists(place):
            return place


def find_projects(root):
    repos = RepoList()
    for directory in os.listdir(root):
        if osp.exists(osp.join(root, directory, '.git')):
            repos.append(Repo(osp.join(root, directory)))
    return repos


def main():
    root = locate_projects()
    repos = find_projects(root)
    if args.action == 'get':
        dest = osp.join(root, args.repo)
        if not osp.exists(dest):
            cli_exec('git clone https://vacancy@github.com/vacancy/{}'.format(args.repo), cwd=root)
            print('Repo {} has been cloned to {}'.format(args.repo, dest))
        else:
            print('Repo {} already exists at {}'.format(args.repo, dest))
    elif args.action == 'list':
        repos.print(short=args.short)
    elif args.action == 'status':
        for repo in repos:
            if args.all or not repo.is_clean:
                print('-' * 50)
                repo.print()
                print('-' * 50)
                repo.exec('git status')
    elif args.action == 'find':
        repo = repos.find(args.repo)
    elif args.action == 'go':
        repo = repos.find(args.repo)
        if repo is not None:
            repo.go()
    elif args.action == 'help':
        parser.print_help(file=sys.stderr)
    else:
        raise ValueError('Unknown action: {}'.format(args.action))


def cli_eval(command, *args, **kwargs):
    if isinstance(command, six.string_types):
        command = command.split()
    return subprocess.check_output(command, *args, **kwargs).decode('utf-8').strip()


def cli_exec(command, *args, **kwargs):
    if isinstance(command, six.string_types):
        command = command.split()
    kwargs.setdefault('stdout', sys.stderr)
    return subprocess.check_call(command, *args, **kwargs)


if __name__ == '__main__':
    main()

