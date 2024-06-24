from fastapi import FastAPI
from typing import Union
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Pessoa(BaseModel):
   cpf: str
   name: str
   birthdate: str

Pessoas: List[Pessoa] = list()

def getPersonByIndex(array: List[Pessoa], index: int) -> Union[Pessoa, None]:
  try:
    return array[index]
  except: return None

@app.get("/")
async def root():
    return {"message": "Hello World!"}

@app.post("/pessoa")
async def createPessoa(cpf: str, name: str, birthdate: str):
   

   
   currentPessoa = Pessoa("ds")

   return {"message": cpf}
   

@app.get("/pessoa/{id}")
def withParams(id: int, yep: Union[str, None] = None):

  pessoa = getPersonByIndex(Pessoas, id)

  if pessoa == None:
      return { "message": "Pessoa não cadastrada"}
  return { "message": "Pessoa encontrada com sucesso", "data": pessoa }


# @app.post("/pessoa")
# def createPessoa()

@app.put("/pessoa/{id}")
def updatePessoa(id: int, pessoa: Pessoa):
   return { "message": f"Pessoa de id: {id} editada com sucesso!"}