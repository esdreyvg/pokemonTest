from sqlalchemy import create_engine
from app.persistence.entities.base import Base
from config import DATABASE

# Creando la configuracion para la conexión a la base de datos 
# predefinida en el archivo config.py

config = DATABASE
conection =""+config["engine"]+"://:"+config["user"]+":"+config["pass"]+"@/"+config["database"]+""

try:
    engine= create_engine(conection)

    Base.metadata.drop_all(engine, checkfirst=True)

    Base.metadata.create_all(engine, checkfirst=True)


except Exception as ex:
    print(ex)