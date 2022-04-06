from flask import Flask, render_template, request
import logging
from app.controllers.usersControllers import route_user
from app.controllers.pokemonsControllers import route_pokemon
from config import LOG_FILENAME

app = Flask(__name__)

app.config.from_object('config')


@app.errorhandler(404)
def error_404(error):
    app.logger.error('Page not found: %s', str(request.path))
    return render_template('404.html'), 404


@app.errorhandler(500)
def error_500(error):
    app.logger.error('Server Error: %s', str(error))
    return render_template('500.html'), 500


@app.errorhandler(Exception)
def unhandled_exception(error):
    app.logger.error('Unhandled Exception: %s', str(error))
    return render_template('500.html'), 500


app.register_blueprint(route_user)
app.register_blueprint(route_pokemon)

logging.basicConfig(filename=LOG_FILENAME, level=logging.DEBUG)
