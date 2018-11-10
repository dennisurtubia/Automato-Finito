import sys
#import maquina

class Main:
    def __init__(self, arquivo_descricao, entrada):
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

        print(dados)
        #maquina.Maquina(dados, entrada)


if __name__ == "__main__":
    Main(sys.argv[1], sys.argv[2])
