class Transicao:
  def __init__(self, estado, novoEstado, simbolo):
    self.estado = estado
    self.simbolo = simbolo
    self.novoEstado = novoEstado

  def getEstado(self):
    return self.estado

  def setEstado(self, estado):
    self.estado = estado

  def getSimbolo(self):
    return self.simbolo

  def setSimbolo(self, simbolo):
    self.simbolo = simbolo

  def getnovoEstado(self):
    return self.novoEstado
    
  def setnovoEstado(self, novoEstado):
    self.novoEstado = novoEstado

  def mostra(self):
    print(self.estado.getNome(), self.simbolo, self.novoEstado.getNome())
