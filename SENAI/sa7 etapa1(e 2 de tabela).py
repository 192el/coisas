# esse monte de comentário é porque eu vou postar no github, e se alguém for se inspirar com o meu código espero que
# entendam a minha lógica se algum colega vir isso no github por favor tente entender como eu fiz e tente fazer a sua
# propria lógica se tiver alguma dúvida sobre a minha lógica manda mensagem no discord, ou me marca no servidor do
# discord também pode mandar pelo WhatsApp, mas eu não olho tanto quanto o discord
assento_reservado_pessoa = {}


class sweetFlight:
    def __init__(self, n_de_assentos):  # cada instância dessa classe é um avião e os assentos começam do zero
        self.dicionario_das_reservas = {}
        for i in range(n_de_assentos):
            self.dicionario_das_reservas[i] = 'assento livre'
        # criando um dicionário com a chave de 0 a N = 'assento livre'

    def reservar(self):
        # self é necessario para guardar uma variavel numa instância desse objeto, "self" é só convenção
        # pode ser outro nome
        try:  # esse try é para o programa tentar fazer o que ta dentro dele, observe o except para mais informações
            quant_assentoslivres = 0
            for i in range(len(self.dicionario_das_reservas)):  # contando assentos livres
                if self.dicionario_das_reservas[i] == 'assento livre':
                    quant_assentoslivres += 1
            if quant_assentoslivres == 0:  # checando se tem algum assento livre
                print('não há assentos disponiveis para este avião')
            else:
                print(f'os assentos são {self.dicionario_das_reservas}')
                # se tiver pelo menos um assento livre será mostrado os assentos
                nome = input("digite o nome do passageiro:\n")
                assento = int(input("digite o numero do assento para reservar:\n"))
                # pedindo a 'chave' (numero) do assento para reservar
                if self.dicionario_das_reservas[assento] == 'assento livre':  # se o assento estiver livre;
                    self.dicionario_das_reservas[assento] = f'assento reservado por {nome}'
                    assento_reservado_pessoa[f'Av n°{qual_aviao} Assento n° {assento}'] = nome
                    # o valor dele será mudado para 'assento reservado por (nome da pessoa)'
                    # e no outro dicionário o nome e qual assento esta reservado
                    print(self.dicionario_das_reservas[assento])  # retorna 'assento reservado'
                else:
                    print('esse assento já está reservado')
        except:  # esse execept devolve uma mensagem de erro caso o programa tente(try) uma chave que não existe
            raise KeyError('esse não é um assento valido')

    def mostrar(self):  # função que retorna os assentos e o valor dele ('assento livre' ou 'assento reservado')
        return self.dicionario_das_reservas


# daqui para frente é só coisa que nós já fizemos outras vezes, acredito que não seja necessario muitos comentarios
listaAvioes = {}


def criaraviao():
    quant_avioes = int(input('digite quantos aviões serão registrados:\n '))
    return quant_avioes


def cond():
    condicao = int(input("digite [1] para registrar o numero de cada avião, [2] para registrar a quantidade de "
                         "assentos em cada avião, [3] para reservar passagem, [4] para consultar por avião, "
                         "[5] para consulta por passageiro, [6] para encerrar:\n"))
    return condicao


condicao = cond()
while condicao != 6:
    if condicao == 1:
        quant_avioes = criaraviao()
        for i in range(quant_avioes):
            try:
                chave_aviao = int(input("digite o numero do avião:\n"))
                listaAvioes[chave_aviao] = 'aguardando registro da quantidade de assentos'
            except:
                raise TypeError("só podemos registrar uma quantidade inteira de aviões")
        condicao = cond()
    elif condicao == 2:
        lista_numero_avioes = list(listaAvioes)
        while lista_numero_avioes != []:
            try:
                quant_assentos = int(input(f"digite o numero de assentos do avião n°{lista_numero_avioes[0]}:\n"))
                listaAvioes[lista_numero_avioes[0]] = sweetFlight(quant_assentos)
                lista_numero_avioes.pop(0)
            except:
                raise TypeError('apenas numeros inteiros serão aceitos')
        condicao = cond()
    elif condicao == 3:
        avioesdisponiveis = []
        keys = list(listaAvioes)
        for i in range(len(listaAvioes)):
            if listaAvioes[keys[i]] != 'aguardando registro da quantidade de assentos':
                avioesdisponiveis.append(keys[i])
        print(f'os aviões disponiveis são {avioesdisponiveis}')
        qual_aviao = int(input("digite o numero do avião:\n"))
        try:
            listaAvioes[qual_aviao].reservar()
            condicao = cond()
        except:
            KeyError("Este avião não existe")
    elif condicao == 4:
        try:
            qual_aviao = int(input("digite o numero do avião:\n"))
            print(listaAvioes[qual_aviao].mostrar())
            condicao = cond()
        except:
            raise ValueError("esse avião não foi registrado")
    elif condicao == 5:
        nome = input("digite o nome do passageiro:\n")
        reservas_do_individuo = [key for key in assento_reservado_pessoa if assento_reservado_pessoa[key] == nome]
        print("os assentos reservados por esse passageiro são:")
        print(reservas_do_individuo)
        condicao = cond()
