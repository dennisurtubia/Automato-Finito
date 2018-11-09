class Estado:
    def __init__(self, nome):
      self.nome = nome
      self.inicial = False
      self.final = False
    
    def getNome(self):
      return self.nome
    def setNome(self, nome):
      self.nome = nome

    def isInicial(self):
      return self.inicial
    def setInicial(self):
      self.inicial = True
    
    def isFinal(self):
      return self.final
    def setFinal(self)
      self.final = True