#creo un ambiente (correrlo en la terminal)
#conda create --ambiente_prueba python=3.13
#conda activate ambiente_prueba
#instalo fastapi y uvicorn (correrlo en la terminal)
#pip install fastapi uvicorn
#crear un ejemplo 
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"mensaje": "Hola, FastAPI está funcionando!"}
# uvicorn main:app --reload (terminal para correr el servidor)


