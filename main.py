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

#Para subirlo a github:
#siempre empezaer a programar con un git pull por si la otra persona subió algo
# 1. ver que github  este iniciado en VS Code
# 2. git add nombre_del_archivo.py o git add . (para agregar todos los archivos)
# 3. git commit -m "descripción del la actualización" (puedo hcer varios commits antes de subirlo)
# 4. git push (sube los cambios al repositorio remotoen internet)


