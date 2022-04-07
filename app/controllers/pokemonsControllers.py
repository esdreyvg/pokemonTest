import json
from app.persistence.contexts.pokemon import *
from flask import Blueprint, request, Response

pokemon_context = PokemonContext()

route_pokemon = Blueprint('pokemon', __name__, url_prefix="/pokemon")


@route_pokemon.route('/', methods=['POST'])
def get_pokemonByUser():
    status = 500
    try:
        if request.method == 'POST':
            idUser = int(request.values.get("idUser"))
            pokemons = pokemon_context.getPokemonByUser(idUser)
            response = json.dumps(pokemons.to_json()),
            status = 200
            return Response(response=response, status=status, mimetype='application/json')
    except Exception as ex:
        raise ex
    return Response(status=status)

