from typing import Union
from typing import List

class Pessoa:

  def __init__(self, cpf, name, birthdate):
    self.cpf = cpf
    self.name = name
    self.birthdate = birthdate
  
  def _get(self):
    return { "cpf": self.cpf, "name": self.name, "birthdate": self.birthdate }
  
  messages = {
    "notRegistred": "Pessoa não cadastrada"
  }
  
def getPersonByIndex(array: List[Pessoa], index: int) -> Union[Pessoa, None]:
  try:
    return array[index]
  except: return None