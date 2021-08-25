import os

# Database
DATABASE_HOST = os.getenv('DATABASE_HOST', '127.0.0.1')
DATABASE_PORT = str(os.getenv('DATABASE_PORT', '3306'))
DATABASE_USER = os.getenv('DATABASE_USER', 'docker')
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD', 'docker')
DATABASE_NAME = os.getenv('DATABASE_NAME', 'sample_database')
PASSPHRASE = os.getenv('PASSPHRASE', 'passphrase')
