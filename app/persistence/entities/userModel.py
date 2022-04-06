from sqlalchemy import Integer, Column, String, DateTime
from sqlalchemy import MetaData
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.orm import relationship
from pokemonModel import Pokemon
from .base import *

meta = MetaData()

class TeamPokemon(Base):
    way = {'pokemon': {}}

    __tablename__ = 'sn_users_teampokemon'

    id = Column('sn_teampokemon_id', Integer, primary_key=True)
    name = Column('sn_teampokemon_name', String(50))
    description = Column('sn_teampokemon_description', String(50))
    fkpokemon = Column('sn_teampokemon_fkpokemon', Integer, ForeignKey(Pokemon.id), nullable=True)
    enabled = Column('sn_teampokemon_enabled', Integer, default=1)

    pokemon = relationship('Pokemon')

class User(Base):

    __tablename__ = 'sn_users_user'

    id = Column('sn_user_id', Integer, primary_key=True)
    name = Column('sn_user_name', String(50))
    lastname = Column('sn_user_lastname', String(50))
    ci = Column('sn_user_ci', Integer)
    phone = Column('sn_user_phone', Integer)
    mail = Column('sn_user_mail', String(50))
    username = Column('sn_user_username', String(50), nullable=False)
    password = Column('sn_user_password', String(200))
    fkteampokemon = Column('sn_user_fkteampokemon', Integer, ForeignKey(TeamPokemon.id), nullable=True)
    enabled = Column('sn_user_enabled', Integer, default=1)
