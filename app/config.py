import os


class Config:
    """
    Configuration settings for the application.
    """
    SQLALCHEMY_DATABASE_URI = os.getenv('DB_URL', 'postgresql://postgres:postgres@localhost:5432/postgres')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
