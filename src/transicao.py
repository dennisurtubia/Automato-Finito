class Transicao:
  def __init__(self, estado, novoEstado, simbolo):
    
    """ Description
        Método construtor da classe transicao, cria um objeto com os atributo que uma trasicao tem
  
    :type estado: Estado
    :param estado: estado de origem da transicao
  
    :type novoEstado: Estado
    :param novoEstado: estado destino da transicao 
  
    :type simbolo: str
    :param simbolo: simbolo que será responsavel por executar esta transicao
    """
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
