from fastapi import FastAPI
# from app.database import engine, Base
from app.routes.participant import router

# Crear las tablas en la base de datos (si las usas)
# Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router)