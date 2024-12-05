import os

# Read the password from the secret file
with open('/run/secrets/db-password', 'r') as f:
    db_password = f.read().strip()

SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://root:{db_password}@db:3306/example'
SQLALCHEMY_TRACK_MODIFICATIONS = False
