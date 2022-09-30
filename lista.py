from node import Node

class Lista:
  inicio = None

  def __init__(self):
    self.inicio = None


   #adicionar item à lista 
  def adicionar(self, valor, inicio = False):
    if(inicio):
      self.adicionar_no_inicio(valor)
    else:
      self.adicionar_no_fim(valor)

      
  #adicionar item no inicio da lista
  def adicionar_no_inicio(self, valor):
    adicionarComeco = Node(valor)
    adicionarComeco.proximo = self.inicio
    self.inicio = adicionarComeco
    
  #adicionar item no final da lsita
  def adicionar_no_fim(self, valor):
    if (self.inicio == None):
      self.inicio = Node(valor, None)
    else:
      aux = self.inicio

      while (aux.proximo != None):
        aux = aux.proximo

      aux.proximo = Node(valor, None)

  def show(self):
    aux = self.inicio
    print("[", end = '')
    
    while (aux.proximo != None):
      print(f"{aux.valor},", end = '')
      aux = aux.proximo
  
    print(f"{aux.valor}]", end = '')

  def remover(self, valor):
    if self.inicio.valor == valor:
        self.inicio = self.inicio.proximo
    else:
        anterior = None
        sequenciaLista = self.inicio
        while sequenciaLista and sequenciaLista.valor != valor:
            anterior = sequenciaLista
            sequenciaLista = sequenciaLista.proximo
        if sequenciaLista:
            anterior.proximo = sequenciaLista.proximo
        else:
            anterior.proximo = None

    if (aux == valor):
      aux = aux.proximo
      
    else:
      while (aux.proximo != valor):
        ant = aux
        aux = aux.proximo

      if aux:
        ant.proximo = aux.proximo
      else:
        ant.proximo = None
