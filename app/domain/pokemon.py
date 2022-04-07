from app.domain.base import Base


class Pokemons(Base):

    def __init__(self):
        Base.__init__(self)
        self.name = ""
        self.fktypepokemon = 0
        self.fkskills = 0
        self.enabled = 0

    def to_json(self):
        return {'name': self.name, 'id': self.id, 'fktypepokemon': self.fktypepokemon, 'fkskills': self.fkskills}


