from fastapi import APIRouter
from config.db import conn
from models.consultas import consulta1, consulta2, consulta3, consulta4


consulta = APIRouter()

@consulta.get("/", tags=["consultas"])
def get_home():
        
        return "Para acceder a las consultas utilice las siguientes rutas--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------" , "/consulta/1 (Piloto con mayor cantidad de primeros puestos) --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------","/consulta/2 (Piloto con mayor cantidad de puntos en total, cuyo constructor sea de nacionalidad American o British)--------------------------------------------------------------------------------------------------------------------------------------------------- ","/consulta/3 (Año con mas carreras)-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------","/consulta/4 (Nombre del circuito mas corrido) "

@consulta.get("/consulta/1", tags=["consultas"])
def get_consulta1():
    return conn.execute(consulta1.select()).fetchall()



@consulta.get("/consulta/2", tags=["consultas"])
def get_consulta2():
    var1 = conn.execute(consulta2.select()).fetchall()
    
    return var1



@consulta.get("/consulta/3", tags=["consultas"])
def get_consulta3():
    return conn.execute(consulta3.select()).fetchall()




@consulta.get("/consulta/4", tags=["consultas"])
def get_consulta4():
    return conn.execute(consulta4.select()).fetchall()



