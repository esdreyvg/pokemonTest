from sqlalchemy import Integer, Column, String, DateTime
from sqlalchemy import MetaData
from .base import *

meta = MetaData()

class Pokemon(Base):

    __tablename__ = 'sn_pokemons_pokemon'

    id = Column('sn_pokemon_id', Integer, primary_key=True)
    name = Column('sn_pokemon_name', String(50))
    fktypepokemon = Column('sn_pokemon_type', Integer)
    fkskills = Column('sn_pokemon_skills', Integer)
    enabled = Column('sn_pokemon_enabled', Integer, default=1)
