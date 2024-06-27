from fastapi import FastAPI
from typing import Union, List
from lib.helpers import find
from models.HttpHandler import *
from models.PessoaModel import Pessoa, getPersonByIndex


app = FastAPI()

Pessoas: List[Pessoa] = list([
  Pessoa("123", "benedito", "45"),
  Pessoa("321", "Jerlinda", "41"),
  Pessoa("111", "Tchanco", "48"),
])

notfoundReturn = { "message": Pessoa.messages["notRegistred"]}

@app.get("/")
async def root():
  try:
    return HttpHandler.success(200, "Sistema funcionando!")
  except Exception as error:
    return HttpHandler.error(error)
  

@app.post("/pessoa")
async def createPessoa(cpf: str, name: str, birthdate: str):

  try:

    currentPessoa = Pessoa(cpf, name, birthdate)

    Pessoas.append(currentPessoa)

    return HttpHandler.success(200, "Pessoa adicionada com sucesso", { "createdPerson": currentPessoa })
  
  except Exception as error:
    return HttpHandler.error(error)
      
@app.get('/pessoa/list')
def list():
  try:
    return Pessoas
  except Exception as error:
    return HttpHandler.error(error)

@app.get("/pessoa/search")
def search(search: Union[str, None] = None, value: Union[str, None] = None): 

  try:
    if not isinstance(search, str):
      raise customError(403, "Parâmetro de busca inválido!", { "search": search })

    if not isinstance(value, str) and not isinstance(value, int):
      raise customError(403, "Parâmetro de busca inválido!", { "value": value })

    def finder(el, comp=value):
      currentElement = el._get()

      currentValue = currentElement.get(search)

      return currentValue == comp

    pessoa = find(Pessoas, finder)

    if pessoa is not None:
      return HttpHandler.success(200, "Pessoa encontrada com sucesso", pessoa)
    
    raise customError(404, "Pessoa não encontrada")
  except Exception as error:
    return HttpHandler.error(error)

@app.get("/pessoa/{id}")
def withParams(id: int):

  try:

    pessoa = getPersonByIndex(Pessoas, id)

    if pessoa is None:
      raise customError(404, "Pessoa não encontrada")
    return HttpHandler.success(200, "Pessoa encontrada com sucesso", pessoa)
  except Exception as error:
    return HttpHandler.error(error)

@app.patch("/pessoa/{id}")
async def withParams(id: int, cpf: Union[str, None] = None, name: Union[str, None] = None, birthdate: Union[str, None] = None):

  try:

    pessoa = getPersonByIndex(Pessoas, id)

    if pessoa is None:
      raise customError(404, "Pessoa não encontrada!")

    if cpf is not None:
      Pessoas[id].cpf = cpf

    if name is not None:
      Pessoas[id].name = name

    if birthdate is not None:
      Pessoas[id].birthdate = birthdate

    return HttpHandler.success(200, "Pessoa modificada com sucesso")

  except Exception as error:
    return HttpHandler.error(error)


@app.put("/pessoa/{id}")
async def createPessoa(id: int, cpf: str, name: str, birthdate: str):

  try:

    pessoa = getPersonByIndex(Pessoas, id)

    if pessoa is None:
      raise customError(404, "Pessoa não encontrada!")

    Pessoas[id] = Pessoa(cpf, name, birthdate)

    return HttpHandler.success(200, "Pessoa editada com sucesso")
  except Exception as error:
    return HttpHandler.error(error)


@app.delete("/pessoa/{id}")
def removePessoa(id: int):
  try:
    pessoa = getPersonByIndex(Pessoas, id)

    if pessoa is None:
      raise customError(404, "Pessoa não encontrada!")

    Pessoas.pop(id)
    return HttpHandler.success(200, "Pessoa removida com sucesso")
  except Exception as error:
    return HttpHandler.error(error)


