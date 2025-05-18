import os

class Config:
    """Base configuration."""
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-key-change-in-production')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'mysql+pymysql://root:Astrico_AI%40123@localhost/astrico_db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True