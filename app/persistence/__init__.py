from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from config import DATABASE

config = DATABASE
conection = ""+config["engine"]+"://"+config["user"]+":"+config["pass"]+"@"+config["host"]+":"+config["port"]+"/"+config["database"]+""

engine = create_engine(conection)

session = Session(engine)
