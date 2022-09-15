from itertools import count
from fastapi import APIRouter, Response, status
from config.db import conn
from models.user import users
from schemas.user import User
from cryptography.fernet import Fernet
from starlette.status import HTTP_204_NO_CONTENT

key = Fernet.generate_key()
user = APIRouter()
f = Fernet(key)





#SELECT * USERS
@user.get("/users", tags=["users"])
def get_users():
    return conn.execute(users.select()).fetchall()

# CREATE NEW USER


@user.post("/userscreate", tags=["users"])
def create_user(user: User):
    new_user = {"name": user.name, "email": user.email}
    new_user["password"] = f.encrypt(user.password.encode("utf-8"))
    result = conn.execute(users.insert().values(new_user))
    print(result)
    print(result.lastrowid)
    return "usuario creado con exito", conn.execute(users.select().where(users.c.id == result.lastrowid)).first()


# GET USER BY ID
@user.get("/users/{id}", response_model=User, tags=["users"])
def get_user(id: str):
    return conn.execute(users.select().where(users.c.id == id)).first()

# DELETE USER BY ID


@user.delete("/users/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=["users"])
def delete_user(id: str):
    result = conn.execute(users.delete().where(users.c.id == id))
    return Response(status_code=HTTP_204_NO_CONTENT)


# UPDATE USER
@user.put("/users/{id}",response_model=User, tags=["users"])
def update_user(id: str, user: User):
    conn.execute(users.update().values(name=user.name,
                 email=user.email, password=f.encrypt(user.password.encode("utf-8"))).where(users.c.id == id))

    return conn.execute(users.select().where(users.c.id == id)).first()
