# coding=utf8

from flask import Flask
from flask.ext.script import Manager, Shell
from config import META
from datetime import datetime
import generator

app = Flask(__name__)
manager = Manager(app)

def make_shell_context():
    return dict(app=app)

@manager.command
def new():
    " Generate a single python file. "
    meta = META.copy()
    meta['datetime'] = str(datetime.now())
    meta['description'] = u'生成一个简单的Python文件'
    print generator.render('app/__init__.py', meta=meta).encode('utf8')
    return 0


@manager.option('-p', '--path', help='Your docs path name')
def docs(path):
    return generator.docs(path)


@manager.command
def project():
    " Generate a single project directory tree. "
    generator.core('templates/project', 'build')
    generator.core('templates/app', 'build/app')
    return 0


if __name__ == '__main__':
    manager.add_command("shell", Shell(make_context=make_shell_context))
    manager.run()
