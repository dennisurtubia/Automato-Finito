from execucao import Execucao
from transicao import Transicao
from estado import Estado
class Maquina:
	def __init__(self, dados, entrada):
		
		""" Description
			Método construtor de Maquina

		:type dados: dict
		:param dados: dicionário com as configurações do autômato finito
	
		:type entrada: str
		:param entrada: entrada que será testada no automato

		"""

		## adiciona atributos a Maquina
		self.entrada = [entry for entry in entrada]
		self.epsilon = dados['simbolo_epsilon']
		self.alfabetoEntrada = dados['alfabeto_entrada']
		self.estadosTmp = dados['estados']
		self.estadoInicial = dados['estado']
		self.estadosFinais = dados['estados_finais']
		self.transicoesTmp = dados['transicoes']

		self.estados = []
		for state in self.estadosTmp:	##Cria objetos de Estado
			estado = Estado(state)
			if state == self.estadoInicial: ##Define estado inicial
				self.estadoAtual = estado
				estado.setInicial()
			if state in self.estadosFinais: ##Define conjunto de estados finais
				estado.setFinal()
			
			self.estados.append(estado)

		self.transicoes = []
		for transition in self.transicoesTmp: ## cria os objetos de transicoes
			for i in self.estados:
				if i.getNome() == transition['estadoAtual']: ## define o estado atual da transição
					curState = i
				if i.getNome() == transition['estadoDestino']: ## define o estado de destino da transição
					newState = i

			simbolEnt = transition['simboloCorrente'] ## define o simbolo da transição

			self.transicoes.append(Transicao(curState, newState, simbolEnt))

		self.execucoes = [Execucao(self.estadoAtual, self.entrada, self.epsilon)] ## cria a primeira Execução com o estado inicial
		
	def getTransicoes(self, execucao):

		""" Description
				Método responsável por fazer a coleta das transições correspondentes ao a execução
				a coleta esta "dividida" em duas partes: 
					coleta das transicoes disponiveis para o estado atual da execucao
					coleta das transicoes com o mesmo simbolo de entrada

		:type execucao: Execucao
		:param execucao: Objeto de execucao que será coletados as transições
	
		:rtype: list
		:retorno transiçoes disponiveis para serem executados pela execucao
		"""
		
		trasPostEstados = []
		for i in self.transicoes: ## coleta das transicoes com base no estado que a execucao esta
			if i.getEstado().getNome() == execucao.getEstado().getNome():
				trasPostEstados.append(i)
		
		# a partir das transicoes disponiveis para o estado atual da execucao
		# a(s) transicao(coes) com o mesmo simbolo de entrada eh(sao) coletada(s)
		trasPostSimbolos = []
		for i in trasPostEstados: 
			if i.getSimbolo() == self.epsilon: ## transicoes com "epsilon" sao coletas
				trasPostSimbolos.append(i)
			elif i.getSimbolo() == execucao.getEntrada():
				trasPostSimbolos.append(i)
		
		return trasPostSimbolos

	def run (self):
		"""	 Description
				Método responsável por fazer e gerenciar todas as execuçoes
		:rtype: int
		: retorno: -> 0 caso a palavra seja aceita, 1 caso a palavra seja recusada
		"""
		while True:
			auxExecs = []
			auxTrans = []

			for x in self.execucoes: ## verificacao de aceitacao das execucoes
				if x.isFinished() == 1:
					print("Entrada aceita", end=' - ')
					x.descricao()
					return 0

			rejeitadas = []
			for i in self.execucoes:

				#### IMPORTANT ####
				## transicoes nao sao copiadas, sao apenas passadas como referencia
				## existe apenas um vetor (que nao eh alterado) com as "verdadeiras" transicoes _> self.transicoes

				trans = self.getTransicoes(i) ## coleta as transicoes a partir de uma execucao

				if len(trans) >= 1: ## caso haja transicoes
					## mantem a execucao, guardando-a no auxiliar de execucoes
					auxExecs.append(i)
					## assim como, definindo qual transicao ira executar
					auxTrans.append(trans[0])

					for t in trans[1:]: ## caso haja mais que uma transicao para aquela execucao
						auxExecs.append(i.getCopia()) ## faz a copia desta
						auxTrans.append(t) ## determina transicao que sera executada por esta copia
				else:
					rejeitadas.append(i) ## caso nao haja transicoes disponiveis a execucao sera rejeitada


			for r in rejeitadas: ## para cada execucao regeitada, e mostrado sua descricao instantanea
				if len(auxTrans) != 0:
					print("Execução Recusada", end=' - ')
					r.descricao()

			if len(auxTrans) == 0: ## caso não haja nenhuma transicao disponivel, nao havera mais execucoes. a entrada foi recusada
				print("Entrada Recusada", end=' - ')
				rejeitadas[0].descricao()
				return 1

			for i in range( len(auxExecs) ): ## loop de execucao
				auxExecs[i].execute(auxTrans[i])

			self.execucoes = auxExecs ## vetor principal de execucoes tem as execucoes que ainda estao "ativas"

		return 0
