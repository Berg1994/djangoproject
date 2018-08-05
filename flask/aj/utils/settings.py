import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(BASE_DIR)
static_dir = os.path.join(BASE_DIR, 'static')
# print(static_dir)
template_dir = os.path.join(BASE_DIR, 'templates')
# print(template_dir)

# 上传图片地址
media_folder = os.path.join(static_dir, 'media')
print(media_folder)
upload_folder = os.path.join(media_folder, 'upload')
print(upload_folder)
MYSQL_DATABASE = {
    'USER': 'root',
    'PASSWORD': '123456',
    'HOST': '127.0.0.1',
    'DB': 'aj',  # NAME
    'ENGINE': 'mysql',
    'PORT': 3306,
    'DRIVER': 'pymysql'
}

REDIS_DATABASE = {
    'HOST': '127.0.0.1',
    'PORT': 6379,
}
