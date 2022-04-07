from typing import List
from app.interfaces.application.pokemon import IPokemonContext
from app.domain.pokemon import Pokemon as DomainPokemons
from app.persistence.entities.pokemonModel import Pokemon as PersistencePokemon
from app.persistence.entities.userModel import User as PersistenceUser
from app.persistence import session
from sqlalchemy import select

class PokemonContext(IPokemonContext):

    pokemonContext = session.execute(PersistencePokemon)

    def listPokemon(self) -> List:
        pokemon = [DomainPokemons]

        return pokemon
    
    def getPokemonByUser(self, idUser) -> List:
        pokemon = [DomainPokemons]

        userPokemon = select(PersistenceUser.fkteampokemon).where(PersistenceUser.id == idUser)
        pokemonList = select(PersistencePokemon).where(PersistencePokemon.id == userPokemon)

        for pokemonByUser in pokemonList:
            pokemon.append(pokemonByUser)

        return pokemon
