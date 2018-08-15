import os

DEBUG = True

SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL", 'sqlite:///test.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False

THREADS_PER_PAGE = 2

APP_NAME = 'BestApp'

SECRET_KEY = "cBWegL8d367vPzTp9Y2pJudLLtaKi5Jtw8//WsRjZrc="
