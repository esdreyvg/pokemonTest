from abc import ABC, abstractmethod
from typing import List
from app.domain.pokemon import Pokemons as DomainPokemons


class IPokemonsContext(ABC):

    @abstractmethod
    def save_Pokemons(self, name: str, fk_type_pokemon: int, fk_skills: int):
        pass

    @abstractmethod
    def update_Pokemons(self, id:int, name: str, fk_type_pokemon: int, fk_skills: int):
        pass

    @abstractmethod
    def list_Pokemons(self) -> List:
        pass

    @abstractmethod
    def delete_Pokemons(self, id: int):
        pass

    @abstractmethod
    def get_Pokemons(self, id: int) -> DomainPokemons:
        pass
