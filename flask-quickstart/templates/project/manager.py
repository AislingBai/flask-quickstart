{% extends "single.py" %}

{% block content %}
import os
from flask.ext.script import Manager, Shell
from flask.ext.migrate import Migrate, MigrateCommand

manager = Manager(app)
migrate = Migrate(app, db)


def make_shell_context():
    return dict(app=app, db=db)


manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)


@manager.command
def run():
    from gevent.pywsgi import WSGIServer
    http = WSGIServer(('', 8000), app)
    http.serve_forever()


if __name__ == '__main__': 
    manager.run()

{% endblock %}
