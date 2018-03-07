#coding=utf-8
import os
from app import create_app

app = create_app(os.getenv('FLASK_CONFIG') or 'default')

manager = Manager(app)

def maker_shell_context():
    return dict(app=app)

manager.add_command('shell',Shell(make_context=maker_shell_context))

if __name__ == '__main__':
    manager.run()