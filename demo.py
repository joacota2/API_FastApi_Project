from fastapi import FastAPI
from routes.user import user
from routes.consultas import consulta

app= FastAPI(
    title = "Users CRUD API",
    description=" this allows you to create update delete and visualize data from SQL-Database",
    openapi_tags=[{
        "name" : "users",
        "description" : "users routes"
    }]

)


app.include_router(user)

app.include_router(consulta)

