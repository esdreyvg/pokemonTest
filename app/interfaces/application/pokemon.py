from abc import ABC, abstractmethod
from typing import List
from app.domain.pokemon import Pokemons as DomainPokemons


class IPokemonsContext(ABC):

    @abstractmethod
    def save_Pokemons(self, Pokemons: DomainPokemons):
        pass

    @abstractmethod
    def update_Pokemons(self, Pokemons: DomainPokemons):
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
