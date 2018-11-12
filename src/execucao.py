from copy import deepcopy
class Execucao:
  def __init__ (self, estado, entrada, epsilon):

    """ Description
        Método construtor do objeto de execução que é responsável de executar determinada transição

    :type estado: Estado
    :param estado: Estado que a execução deve se iniciar

    :type entrada: list
    :param entrada: Estrada restante que deve ser processada pela execução

    :type epsilon: str
    :param epsilon: Simbolo que respresenta o epsilon para a execução
    """
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
    """ Description
        Método que retorna a situação da execução no momento, se está terminado ou não
    :rtype: int
    """
    if  len(self.entrada) == 0:
      if self.estadoAtual.isFinal():
        return 1

  def descricao(self): ## mostra descricao instantanea da execucao
    """ Description
        Mostra a descrição da execução no momento
    """
    print("<", end=' ')
    print(self.estadoAtual.getNome(), end=', ')
    for i in self.entrada:
        print(i, end='')
    print(" >")

  def execute(self, transicao): ## metodo responsavel por executar uma transicao

    """ Description
        Função que faz a execução de uma transição passada por parâmentro

    :type transicao: Transição
    :param transicao: transição que será executada nesta instancia

    :rtype: int
    """
    simbolo = transicao.getSimbolo() ## simbolo entrada (transicao)
    if simbolo != self.epsilon:
      self.shift() ## consome entrada

    self.estadoAtual = transicao.getnovoEstado() ## novo estado

    return 1