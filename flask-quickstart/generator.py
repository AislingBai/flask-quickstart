# coding=utf8

"""
    一系列项目生成器的集合
"""

import re
import os
import sys
import jinja2
import subprocess
from utils import render
from hooks import maps
from config import META as meta


_filter = [
    lambda x: not x.startswith('.'), 
    lambda x: not x.endswith('.pyc'), 
]


def filter_all(filter_set, data):
    _data = data[:]
    for _filter in filter_set:
        _data = [_d for _d in _data if _filter(_d)]

    return _data


def core(template, dest, **kwargs):
    """
        目录扫描核心
    """
    BASEDIR = os.path.abspath(os.path.dirname(__file__))
    CMDDIR = os.path.abspath('.')
    TEMPLATE = os.path.join(BASEDIR, 'templates', '')
    dest = os.path.abspath(dest)
    template = os.path.abspath(template)

    if not os.path.exists(dest):
        os.mkdir(dest)
    if not os.path.isdir(template):
        raise Exception('Not a dir.')
    _d = filter_all(_filter, os.listdir(template))

    for f in _d:
        fpath = os.path.join(template, f)
        opath = os.path.join(dest, f)
        templatepath = fpath.replace(TEMPLATE, '')
        print(fpath, opath, templatepath)
        if os.path.isdir(fpath):
            if not os.path.exists(opath):
                os.mkdir(opath) 
            core(fpath, opath, **kwargs)
        else:
            with open(opath, 'w') as fobj:
                writed = runhook(templatepath)
                fobj.write(writed)


def runhook(key):
    for regular, proc in maps:
        if re.match(regular+'$', key):
            return proc(key)
    return ""


def docs(path):
    """
        生成Sphinx风格的文档
    """
    p = subprocess.Popen(['sphinx-quickstart', path])
    while sys.stdin != 'quit':
        p.communicate(sys.stdin)


def project(name):
    """
        生成项目目录
    """
    pass


if __name__ == '__main__':
    core('templates/project', 'build')
