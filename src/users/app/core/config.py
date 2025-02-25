import os

class Config:
    DB_USER = os.getenv("DB_USER", "admin")
    DB_PASSWORD = os.getenv("DB_PASSWORD", "secret")
    DB_HOST = os.getenv("DB_HOST", "user_db")
    DB_NAME = os.getenv("DB_NAME", "users_db")
    SQLALCHEMY_DATABASE_URI = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"