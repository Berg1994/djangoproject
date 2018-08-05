from flask_script import Manager

from utils.app import create_app

# 这里只需要展示启动内容
app = create_app()

manager = Manager(app)

if __name__ == '__main__':
    manager.run()
