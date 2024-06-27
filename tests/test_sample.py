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

from source.models.PessoaModel import Pessoa
from source.lib.helpers import find
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

def test_pessoa_size_init():
  assert getPessoasSize() == 3

def test_add_pessoa():
  Pessoas.append(Pessoa("654", "Flirovaldo", "1910-05-01"))
  assert getPessoasSize() == 4

def test_find_pessoa_by_cpf():

  def finder(el, cpf="321"):
    currentElement = el._get()

    currentValue = currentElement.get("cpf")

    return currentValue == cpf
  
  pessoa = find(Pessoas, finder)

  assert pessoa.name == "Jerlinda"

