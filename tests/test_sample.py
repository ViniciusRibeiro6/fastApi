import sys
import os

def removeLastPath(caminho: str):

  escape = '\\'

  caminho = caminho.split(escape)
  caminho.pop()
  caminho = escape.join(caminho)

  return caminho

correctPath = removeLastPath(os.path.abspath(__file__))
correctPath = removeLastPath(correctPath)
sys.path.append(correctPath)

from source.models.PessoaModel import Pessoa, getPersonByIndex
from typing import List

Pessoas: List[Pessoa] = list([
  Pessoa("123", "benedito", "45"),
  Pessoa("321", "Jerlinda", "41"),
  Pessoa("111", "Tchanco", "48"),
])

def func(x):
  return x + 1

def getPessoasSize(): 
  return len(Pessoas)

def test_pessoaSize():
  result = getPessoasSize()
  assert result == 3
