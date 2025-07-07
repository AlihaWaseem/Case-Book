# config.py

import os

class Config:
    # PostgreSQL connection string
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://postgres:!ALIHA24%40@127.0.0.1:5432/casebookDB"

    # SQLAlchemy performance
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Flask app security
    SECRET_KEY = os.environ.get("SECRET_KEY", "supersecretkey")
    JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY", "your_jwt_secret")

