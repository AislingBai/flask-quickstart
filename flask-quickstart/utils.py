# coding=utf8

import os
import jinja2


def render(path, **kwargs):
    """
        Jinja2 快速模版渲染
    """
    env = jinja2.Environment(loader=jinja2.FileSystemLoader('templates'))
    t = env.get_template(path)
    return t.render(**kwargs)


def abs_render(path, **kwargs):
    """
        Jinja2 绝对路径渲染
    """
    t = jinja2.Template(path)
    return t.render(**kwargs)

