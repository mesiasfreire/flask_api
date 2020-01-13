DEBUG =True

USERNAME = 'root'
PASSWORD = 'root'
SERVER = 'localhost'
DB = 'sidia'

SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{USERNAME}:{PASSWORD}@{SERVER}/{DB}'
#SQLALCHEMY_DATABASE_URI = 'sqlite:///database.sqlite3'

