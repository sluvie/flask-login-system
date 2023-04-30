import logging

TIMEZONE = 'Asia/Jakarta'

APP_NAME = "invest.me"

# DEBUG can only be set to True in a development environment for security reasons
DEBUG = True

# secret key for generating tokens
SECRET_KEY = "ducelle-system-2023"

# Admin credentials
ADMIN_CREDENTIALS = ('admin', 'Pa$$word')

# Configuration of a Email account for sending and receiving mails
MAIL_ACCOUNT = [
    {
        "default": {
            "ACCOUNT": "rocket.saas@gmail.com",
            "SERVER": "smtp.googlemail.com",
            "IMAP_PORT": 993,
            "SMTP_PORT": 465,
            "USE_TLS": False,
            "USE_SSL": True,
            "USERNAME": "",
            "PASSWORD": ""
        }
    }
]

# Configuration of a Database account
DATABASE_ACCOUNT = {
        "memedb": {
            "server": "51.79.206.3",
            "port": 5499,
            "user": "meme",
            "password": "meme",
            "database": "memedb",
        },
    }

# Number of times a password is hashed
BCRYPT_LOG_ROUNDS = 12

LOG_LEVEL = logging.DEBUG
LOG_FILENAME = 'activity.log'
LOG_MAXBYTES = 1024
LOG_BACKUPS = 2

# Application
APP_TITLE = "Ducelle System"
APP_VERSION = "1.0.0"