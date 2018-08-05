from utils.functions import create_app
from flask_script import Manager

app = create_app()

manage = Manager(app=app)

if __name__ == '__main__':
    manage.run()
