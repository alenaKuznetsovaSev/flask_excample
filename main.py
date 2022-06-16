from app import app, db
from app.models import User, Post


# making pre-import for console
# in order to use it, write: (venv) $ flask shell
@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}


# if __name__ == '__main__':
#     print('Main')
