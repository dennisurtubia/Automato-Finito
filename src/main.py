#!/usr/bin/python3
import sys
from maquina import Maquina

def readlines (arquivo_descricao):
    
    """ Description
        Função responsável por fazer a coleta da configuração do autômato direto do arquivo passado por parâmetro

    :type arquivo_descricao: str
    :param arquivo_descricao: nome/diretório do arquivo de configuração do autômato finito

    :rtype: dict
    :return:
        dict {
            'alfabeto_entrada': list -> contem os caracteres que fazem parte do conjunto de simbolos de entrada
            'simbolo_epsilon': str -> caractere que representa o epsilon
            'estados': list -> conjunto com os nomes dos estados
            'estado': str -> nome do estado inicial
            'estados_finais': list -> conjunto dos nomes dos estados de aceitação

        }
    """
    arq = open(arquivo_descricao)
    lines = arq.readlines()
    arq.close()

    dados = {}

    dados['alfabeto_entrada'] = [x.strip() for x in lines[0].split(' ')]
    dados['simbolo_epsilon'] = lines[1].strip()
    dados['estados'] = [x.strip() for x in lines[2].split(' ')]
    dados['estado'] = lines[3].strip()
    dados['estados_finais'] = [x.strip() for x in lines[4].split(' ')]
    dados['transicoes'] = []

    for line in lines[5:]:
        transition = {}
        tmp = line.split(' ')
        transition['estadoAtual'] = tmp[0].strip()
        transition['simboloCorrente'] = tmp[1].strip()
        transition['estadoDestino'] = tmp[2].strip()
        dados['transicoes'].append(transition)


    return dados

if __name__ == "__main__":
    dados = readlines(sys.argv[1])
    machine = Maquina(dados, sys.argv[2]) ## cria uma Maquina passando os dados e a entrada fornecida
    machine.run() ## começa executar
