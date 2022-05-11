from flask_script import Manager, Server
from flask_migrate import Migrate,MigrateCommand
from app import create_app,db
app = create_app('dev')
from app.models import User
manager = Manager(app)
manager.add_command('server', Server)

@manager.shell
def make_shell_context():
    return dict(app = app,db = db,User = User )
migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)


if __name__ ==  '__main__':

    manager.run()