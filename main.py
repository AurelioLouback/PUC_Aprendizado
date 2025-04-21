from fastapi import FastAPI
#Comentario - Gerar teste
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/teste1")
async def funcaoteste():
    return {"teste":"Deu certo"}