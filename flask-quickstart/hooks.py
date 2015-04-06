# coding=utf8

"""

文件和处理钩子的映射表

* author: Yufei Li
* github: http://github.com/yufeiminds
* datetime: 2015-04-06 12:08:00.379592

"""

from utils import render
from config import META as meta

def hook(f):
    def hook_wrapper(template):
        return f(template)
    return hook_wrapper


def init_hook(template):
    return render(template, meta=meta)


def models_hook(template):
    return render(template, meta=meta)


def views_hook(template):
    return render(template, meta=meta)


def forms_hook(template):
    return render(template, meta=meta)


def errors_hook(template):
    """
        钩子函数
    """
    return render(template, meta=meta)


def extra_hook(template):
    return render(template, meta=meta)


maps = [
    (r'__init__.py', init_hook),
    (r'models.py', models_hook),
    (r'views.py', views_hook),
    (r'forms.py', forms_hook),
    (r'errors.py', errors_hook),
    (r'.*', extra_hook),
]
