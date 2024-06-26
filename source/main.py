from fastapi import FastAPI
from typing import Union
from typing import List
from lib.helpers import find

app = FastAPI()

class Pessoa:

  def __init__(self, cpf, name, birthdate):
    self.cpf = cpf
    self.name = name
    self.birthdate = birthdate
  
  def _get(self):
    return { "cpf": self.cpf, "name": self.name, "birthdate": self.birthdate }

Pessoas: List[Pessoa] = list([
  Pessoa("123", "benedito", "45"),
  Pessoa("321", "Jerlinda", "41"),
  Pessoa("111", "Tchanco", "48"),
])

def getPersonByIndex(array: List[Pessoa], index: int) -> Union[Pessoa, None]:
  try:
    return array[index]
  except: return None


@app.get("/")
async def root():
  return { "message": "System is working" }

@app.post("/pessoa")
async def createPessoa(cpf: str, name: str, birthdate: str):
      
  currentPessoa = Pessoa(cpf, name, birthdate)

  Pessoas.append(currentPessoa)

  return {"message": "Pessoa adicionada com sucesso"}

@app.get('/pessoa/list')
def list():
  return Pessoas

@app.get("/pessoa/search")
def search(search: Union[str, None] = None, value: Union[str, None] = None): 

  if not isinstance(search, str):
    return {"message": "Parâmetro de busca inválido!", "invalid": { "search": search }}  

  if not isinstance(value, str) and not isinstance(value, int):
    return {"message": "Parâmetro de busca inválido!", "invalid": { "value": value }}

  def finder(el, comp=value):
    currentElement = el._get()

    currentValue = currentElement.get(search)

    print(currentValue)

    return currentValue == comp

  pessoa = find(Pessoas, finder)

  if pessoa != None:
    return { "message": "Pessoa encontrada com sucesso", "data": pessoa }
  
  return { "message": "Pessoa não cadastrada"}

@app.get("/pessoa/{id}")
def withParams(id: int):

  pessoa = getPersonByIndex(Pessoas, id)

  if pessoa == None:
    return { "message": "Pessoa não cadastrada" }
  return { "message": "Pessoa encontrada com sucesso", "data": pessoa }

@app.patch("/pessoa/{id}")
async def withParams(id: int, cpf: Union[str, None] = None, name: Union[str, None] = None, birthdate: Union[str, None] = None):
  pessoa = getPersonByIndex(Pessoas, id)

  if pessoa == None:
    return { "message": "Pessoa não cadastrada" }

  if cpf != None:
    Pessoas[id].cpf = cpf

  if name != None:
    Pessoas[id].name = name

  if birthdate != None:
    Pessoas[id].birthdate = birthdate

  return { "message": "Pessoa modificada com sucesso"}

@app.put("/pessoa/{id}")
async def createPessoa(id: int, cpf: str, name: str, birthdate: str):

  pessoa = getPersonByIndex(Pessoas, id)

  if pessoa == None:
    return { "message": "Pessoa não cadastrada" }

  Pessoas[id] = Pessoa(cpf, name, birthdate)

  return {"message": "Pessoa adicionada com sucesso"}

@app.delete("/pessoa/{id}")
def removePessoa(id: int):
  pessoa = getPersonByIndex(Pessoas, id)

  if pessoa == None:
    return { "message": "Pessoa não cadastrada"}

  Pessoas.pop(id)
  
  return { "message": "Pessoa removida com sucesso" }

