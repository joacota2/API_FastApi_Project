from venv import create
from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://root:administrador@localhost:3306/pi_individual")
#engine = create_engine("mysql+pymysql://u653914786_henrypi123:Administrador1@45.132.157.154:3306/u653914786_henrypi")

meta = MetaData()

conn = engine.connect()
