class Maquina:
  def __init__(self, dados, entrada):
		self.entrada = [entry for entry in entrada]
		self.alfabetoEntrada = dados['alfabeto_entrada']
		self.alfabetoTrabalho = dados['alfabeto_entrada']
		self.estadosTmp = dados['estados']
		self.estadoInicial = dados['estado']
		self.estadosFinais = dados['estados_finais']
		self.transicoesTmp = dados['transicoes']

		self.estados = []
		for state in self.estadosTmp: ##Cria objetos de Estado
			estado = Estado(state)
			if state == self.estadoInicial ##Define estado inicial
				self.estadoAtual = estado
				state.setInicial()
			if state in self.estadosFinais ##Define conjunto de estados finais
				estado.setFinal
			
			self.estados.append(estado)

		self.transicoes = []
		for transition in self.transicoesTmp:
			for i in self.estados:
				if i.getNome() == transition['estadoAtual']
					curState = i
				if i.getNome() == transition['estadoDestino']:
					newState = i

			simbolEnt = transition['simboloCorrente']

			self.transicoes.append(Transicao(curState, newState, simbolEnt))

		self.execucoes = [Algoz(self.entrada, self.estadoAtual)]
		
		def get_transicoes(self):
			pass 



	