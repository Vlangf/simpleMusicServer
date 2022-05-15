import os

file_dir = os.path.join(os.getcwd(), 'Music')
if not os.path.exists(file_dir):
    os.mkdir(os.path.normpath(file_dir).split(os.sep)[-1])
db_connect_string = os.getenv('DB_URL')
