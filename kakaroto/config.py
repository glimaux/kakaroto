import os

APP_NAME = 'KakarotoWebApi'

GITHUB = {
    'WEBHOOK_SIGNATURE_KEY': os.environ.get('{}_GITHUB_WEBHOOK_SIGNATURE_KEY'.format(APP_NAME)),
    'SECRET_KEY': os.environ.get('{}_GITHUB_SECRET_KEY'.format(APP_NAME))
}

DATABASE = {
    'DRIVER': 'mysql+pymysql',
    'USER': os.environ.get('{}_DATABASE_USER'.format(APP_NAME)),
    'PASS': os.environ.get('{}_DATABASE_PASSWORD'.format(APP_NAME)),
    'HOST': 'localhost',
    'PORT': '3306',
    'DB_NAME': 'kkrt'
}

CONNECTION_STRING = '{DRIVER}://{USER}:{PASS}@{HOST}:{PORT}/{DB_NAME}'.format(**DATABASE)
