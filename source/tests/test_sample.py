import sys
import os

def larie(caminho: str):

  escape = '\\'

  caminho = caminho.split(escape)
  caminho.pop()
  caminho = escape.join(caminho)

  return caminho

# seila = os.path.abspath(__file__).split('\\')
seila = larie(os.path.abspath(__file__))
seila = larie(seila)
sys.path.append(seila)
print(seila)

from models.PessoaModel import Pessoa, getPersonByIndex
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

# def test_answer():
#   print('alooo', getPessoasSize())
#   assert func(3) == 5



