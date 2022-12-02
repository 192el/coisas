# esse monte de comentário é porque eu vou postar no github, e se alguém for se inspirar com o meu código espero que
# entendam a minha lógica se algum colega vir isso no github por favor tente entender como eu fiz e tente fazer a sua
# propria lógica se tiver alguma dúvida sobre a minha lógica manda mensagem no discord, ou me marca no servidor do
# discord também pode mandar pelo WhatsApp, mas eu não olho tanto quanto o discord

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
                print('todos os assentos estão ocupados')
            else:
                print(f'os assentos são {self.dicionario_das_reservas}')
                # se tiver um assento livre será mostrado os assentos
                assento = int(input("digite o numero do assento que deseja reservar:\n"))
                # pedindo a 'chave' (numero) do assento para reservar
                if self.dicionario_das_reservas[assento] == 'assento livre':  # se o assento estiver livre;
                    self.dicionario_das_reservas[
                        assento] = 'assento reservado'  # o valor dele será mudado para 'assento reservado'
                    print(self.dicionario_das_reservas[assento])  # retorna 'assento reservado'
                elif self.dicionario_das_reservas[assento] == 'assento reservado':
                    print('esse assento já está reservado')
        except:  # esse execept devolve uma mensagem de erro caso o programa tente(try) uma chave que não existe
            raise KeyError('esse não é um assento valido')

    def mostrar(self):  # função que retorna os assentos e o valor dele ('assento livre' ou 'assento reservado')
        return self.dicionario_das_reservas


# daqui para frente é só coisa que nós já fizemos outras vezes, acredito que não seja necessario muitos comentarios
listaAvioes = []


def criaraviao():
    quant_avioes = int(input('digite quantos aviões quer registrar:\n '))
    return quant_avioes


def cond():
    condicao = int(input(
        "digite [1] para registrar um avião, [2] para criar uma reserva em um avião especifico, [3] para ver as "
        "reservas de um avião especifico [0] para sair:\n"))
    return condicao


condicao = cond()
while condicao != 0:
    if condicao == 1:
        quant_avioes = criaraviao()
        for i in range(len(listaAvioes), quant_avioes + len(listaAvioes)):
            quant_assentos = int(input(f"digite quantos assentos o avião {i + len(listaAvioes)} tem:\n"))
            listaAvioes.append(
                sweetFlight(quant_assentos))  # isso cria uma instancia da classe sweetflight e coloca ela numa lista
        condicao = cond()  # se der print nessa lista ele mostra onde na memória essa instancia está alocada
    elif condicao == 2:
        qual_aviao = int(input(f"digite o numero do avião (começando com 0):\n"))
        listaAvioes[qual_aviao].reservar()  # utilizando a função reservar na instância especificada
        condicao = cond()
    elif condicao == 3:
        try:
            qual_aviao = int(input(f"digite o numero do avião (começando com 0):\n"))
            print(listaAvioes[qual_aviao].mostrar())
            condicao = cond()
        except:
            raise ValueError("esse avião não foi registrado")
