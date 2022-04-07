from distutils.debug import DEBUG
import os

DATABASE = {
    "engine": "sqlite",
    "database": 'PokemonDB',
    "user": 'Test',
    "pass": 'PokemonTest123',
    "host": "localhost",
    "port": "1433"
}

SERVER = {
    "host": "localhost",
    "port": "8080"
}

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

LOG_FILENAME = 'logs/errores.log'