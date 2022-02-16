# import os
# import urllib.parse
# basedir = os.path.abspath(os.path.dirname(__file__))
#
# ### BASIC APP CONFIG
# SALT = '$2b$12$yLUMTIfl21FKJQpTkRQXCu'
# SECRET_KEY = 'e951e5a1f4b94151b360f47edf596dd2'
# BIND_ADDRESS = '0.0.0.0'
# PORT = 9191
# HSTS_ENABLED = False
# OFFLINE_MODE = False
# FILESYSTEM_SESSIONS_ENABLED = False
#
# ### DATABASE CONFIG
# SQLA_DB_USER = 'pda'
# SQLA_DB_PASSWORD = 'changeme'
# SQLA_DB_HOST = '127.0.0.1'
# SQLA_DB_NAME = 'pda'
# SQLALCHEMY_TRACK_MODIFICATIONS = True
#
# ### DATABASE - MySQL
# SQLALCHEMY_DATABASE_URI = 'mysql://{}:{}@{}/{}'.format(
#     urllib.parse.quote_plus(SQLA_DB_USER),
#     urllib.parse.quote_plus(SQLA_DB_PASSWORD),
#     SQLA_DB_HOST,
#     SQLA_DB_NAME
# )
#
# ### DATABASE - SQLite
# # SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'pdns.db')
#
# # SAML Authnetication
# SAML_ENABLED = False
# SAML_ASSERTION_ENCRYPTED = True

import os
import urllib.parse
basedir = os.path.abspath(os.path.dirname(__file__))

### BASIC APP CONFIG
SALT = 'b2'
SECRET_KEY = 'e951e5a1f4b94151b360f47edf596dd2'
BIND_ADDRESS = '0.0.0.0'
PORT = 9191
HSTS_ENABLED = False
OFFLINE_MODE = False
FILESYSTEM_SESSIONS_ENABLED = False

# SAML Authnetication
SAML_ENABLED = False
SAML_ASSERTION_ENCRYPTED = True

### DATABASE CONFIG
SQLA_DB_USER = 'pdns_owner'
SQLA_DB_PASSWORD = 'w5FQtgmkNRgj4JqR'
SQLA_DB_HOST = '192.168.1.56'
SQLA_DB_NAME = 'pdns'
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_DB_PORT= '5432'

### DATABASE - PGSQL
SQLALCHEMY_DATABASE_URI = 'postgres+psycopg2://'+SQLA_DB_USER+':'+SQLA_DB_PASSWORD+'@'+SQLA_DB_HOST+':'+SQLALCHEMY_DB_PORT+'/'+SQLA_DB_NAME