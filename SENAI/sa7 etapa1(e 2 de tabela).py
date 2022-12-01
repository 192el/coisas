
#esse monte de comentário é porque eu vou postar no github, e se alguém for se inspirar com meu código espero que entendam a minha lógica
#se algum colega estiver vendo isso no github por favor tente entender como eu fiz e tente fazer sua propria lógica
#se tiver alguma duvida sobre a *minha* logica manda mensagem no discord, ou me marca no discord
#também pode mandar pelo whatsapp mas eu não olho tanto quanto o discord

class sweetflight():
    def __init__(self, n_de_assentos):          #cada instância dessa classe é um avião e os assentos começam do zero
        self.dicionario_das_reservas = {}
        for i in range(n_de_assentos):
            self.dicionario_das_reservas[i] = 'assento livre'                   #criando um dicionario com a chave de 0 a N = 'assento livre'
    def reservar(self):                                         #self é necessario para guardar uma variavel dentro de uma instancia desse objeto, "self" é só convenção pode ser outro nome
        try:                                                        #esse try é pro programa tentar fazer o que ta dentro dele, veja o except para mais informações
            quant_assentoslivres = 0
            for i in range(len(self.dicionario_das_reservas)):                                  #contando assentos livres
                if self.dicionario_das_reservas[i] == 'assento livre':
                    quant_assentoslivres += 1
            if quant_assentoslivres == 0:                                               #checando se tem algum assento livre
                print('todos os assentos estão ocupados')
            else:
                print(f'os assentos são {self.dicionario_das_reservas}')                                #se tiver um assento livre será mostrado os assentos
                assento = int(input("digite o numero do assento que deseja reservar:\n"))               #pedindo a 'chave' (numero) do assento para reservar
                if self.dicionario_das_reservas[assento] == 'assento livre':                            #se o assento estiver livre;
                    self.dicionario_das_reservas[assento] = 'assento reservado'                         #o valor dele será mudado para 'assento reservado'
                    print(self.dicionario_das_reservas[assento])                                       #retorna 'assento reservado'
                elif self.dicionario_das_reservas[assento] == 'assento reservado':
                    print('esse assento já está reservado')
        except:                                                                             #esse execept devolve uma mensagem de erro caso o programa tente(try) uma chave que não existe
            raise KeyError('esse não é um assento valido', self.dicionario_das_reservas)
    def mostrar(self):                                                                      #função que retorna os assentos e o valor dele ('assento livre' ou 'assento reservado')
        return self.dicionario_das_reservas


#daqui pra frente é só coisa que a gente já fez outras vezes, acredito que não seja necessario muitos comentarios
listaAvioes = []
def criaraviao():
    quant_avioes = int(input('digite quantos aviões quer registrar:\n '))
    return quant_avioes

def cond():
    condicao = int(input("digite [1] para registrar um avião, [2] para criar uma reserva em um avião especifico, [3] para ver as reservas de um avião especifico [0] para sair:\n"))
    return condicao


condicao = cond()
while condicao != 0:
    if condicao == 1:
        quant_avioes = criaraviao()
        for i in range(len(listaAvioes), quant_avioes + len(listaAvioes)):
            quant_assentos = int(input(f"digite quantos assentos o avião {i + len(listaAvioes)} tem:\n"))
            listaAvioes.append(sweetflight(quant_assentos))                        #aqui está criando uma instancia da classe sweetflight e colocando numa lista
        condicao = cond()                                                          #se vc der print nessa lista ele mostra onde na memoria essa instancia está alocada
    elif condicao == 2:
        qual_aviao = int(input(f"digite o numero do avião (começando com 0):\n"))
        listaAvioes[qual_aviao].reservar()                                        #utilizando a função reservar na instancia especificada
        condicao = cond()
    elif condicao == 3:
        try:
            qual_aviao = int(input(f"digite o numero do avião (começando com 0):\n"))
            print(listaAvioes[qual_aviao].mostrar())
            condicao = cond()
        except:
            raise indexError("esse avião não foi registrado")
            condicao = cond()
