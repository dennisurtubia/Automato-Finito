from copy import deepcopy
class Execucao:
  def __init__ (self, estado, entrada, epsilon):

    self.estadoAtual = estado
    self.entrada = entrada
    self.epsilon = epsilon
    
  def getCopia(self): ## funcao que faz a copia de uma execucao, com base nos dados atuais dela
    return deepcopy(self)

  def getEntrada(self): ## retorn elemento na entrada
    if len(self.entrada) >= 1:
      return self.entrada[0]

  def shift(self): ## "consome" simbolo da entrada
    self.entrada = self.entrada[1:]

  def getEstado(self):
    return self.estadoAtual

  def isFinished(self): ## verificacao de aceitacao da entrada pela execucao
    if  len(self.entrada) == 0:
      if self.estadoAtual.isFinal():
        return 1

  def descricao(self): ## mostra descricao instantanea da execucao
    print("<", end=' ')
    print(self.estadoAtual.getNome(), end=', ')
    for i in self.entrada:
        print(i, end='')
    print(" >")

  def execute(self, transicao): ## metodo responsavel por executar uma transicao

    simbolo = transicao.getSimbolo() ## simbolo entrada (transicao)
    if simbolo != self.epsilon:
      self.shift() ## consome entrada

    self.estadoAtual = transicao.getnovoEstado() ## novo estado

    return 1

  pass