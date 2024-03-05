import random

class Carta:
    def __init__(self, fnaipe, numero):
        self.fnaipe = fnaipe
        self.numero = numero
        if fnaipe == 0:
            self.naipe = '♣'
        elif fnaipe == 1:
            self.naipe = '♦'
        elif fnaipe == 2:
            self.naipe = '♥'
        elif fnaipe == 3:
            self.naipe = '♠'

    def __str__(self):
        letra = f'{self.numero}'
        if self.numero == 11:
            letra = 'J'
        elif self.numero == 12:
            letra = 'Q'
        elif self.numero == 13:
            letra = 'K'
        elif self.numero == 14 or self.numero == 1:
            letra = 'A'
        return f"{letra}{self.naipe}"

class Baralho:
    def __init__(self):
        self.cartas = []
        self.build()

    def build(self):
        for fnaipe in range (0, 3):
            for numero in range(2, 14):
                self.cartas.append(Carta(fnaipe, numero))

    def embaralhar(self):
        random.shuffle(self.cartas)

    def dar_carta(self):
        if len(self.cartas) > 0:
            return self.cartas.pop()
        else:
            return print("Não há mais cartas")

class Mao:
    def __init__(self, cartas):
        self.cartas = sorted(cartas, key=lambda carta: carta.numero)

    def trocar_mao(self):
        while True:
            resposta = input("Deseja trocar a mão? (s/n): ").lower()
              
            if resposta == 's':
                for i in range(0,2):
                    while True:
                        try:
                            print('Sua mão atualmente:' + str(self))
                            escolha = input(f"digite o numero da {i+1}ª carta ou 'n' para não trocar:\n")
                            if escolha == 'n':
                                break
                            elif int(escolha) > 0 and int(escolha) < 6-i:
                                self.cartas.pop(int(escolha)-1)
                                break
                            else:
                                print("Invalido.")
                        except:
                            print("Invalido.")
                break

            elif resposta == 'n':
                break 
            else:
                print("Resposta inválida. Por favor, digite 's' para trocar ou 'n' para manter a mão.")

    def comprar_carta(self, Baralho):
        if len(Baralho.cartas) > 1:
            for _ in range(5-self.cartas.__len__()):
                self.cartas.append(Baralho.dar_carta())
            self.cartas = sorted(self.cartas, key=lambda carta: carta.numero)
        else:
            return print("Não há mais cartas suficientes")
        

    def tratar_as(self):
        self.cartas.append(Carta(self.cartas[4].fnaipe,1))
    
    def clona(self):
        return Mao(self.cartas)

    def __str__(self):
        return ', '.join([str(Carta) for Carta in self.cartas])
    
class ComparaMao:
    def __init__(self, jogador1, jogador2):
        self.mao1 = jogador1.clona()
        self.mao1.alta = jogador1.cartas[4].numero
        if(14 == jogador1.cartas[4].numero):
            self.mao1.tratar_as()
            self.mao1.cartas = sorted(self.mao1.cartas, key=lambda carta: carta.numero)
        self.mao1.temstraight = 0 #retorna a carta mais alta do straight    
        self.mao1.temflush = 4 #retorna o naipe do flush
        self.mao1.ptq = [0,0,0] #1 pra saber se é par, trinca... 2nd pra saber dois pares
        self.mao1.forca = 0
        self.mao1.forcan = -1

        self.mao2 = jogador2.clona()
        self.mao2.alta = jogador2.cartas[4].numero
        if(14 == jogador2.cartas[4].numero):
            self.mao2.tratar_as()
            self.mao2.cartas = sorted(self.mao2.cartas, key=lambda carta: carta.numero)
        self.mao2.temstraight = 0 #retorna a carta mais alta do straight    
        self.mao2.temflush = 4 #retorna o naipe do flush
        self.mao2.ptq = [0,0,0] #1 pra saber o numero da mais alto #2 pra saber se é par, trinca... 3nd pra saber dois pares
        self.mao2.forca = 0
        self.mao2.forcan = -1

        self.Straight(self.mao1)
        self.Straight(self.mao2)
        self.Flush(self.mao1)
        self.Flush(self.mao2)
        self.Pares(self.mao1)
        self.Pares(self.mao2)
        
        print(jogador1)
        print("JOGADOR 1: ",self.Resultado(self.mao1))
        print(jogador2)
        print("JOGADOR 2: ",self.Resultado(self.mao2))
        if(self.mao1.forca > self.mao2.forca):
            print("Jogador 1 Venceu!")
        elif(self.mao1.forca < self.mao2.forca):
            print("Jogador 2 Venceu!")
        else:
            if(self.mao1.ptq[0] > self.mao2.ptq[0]):
                print("Jogador 1 Venceu!")
            elif(self.mao1.ptq[0] < self.mao2.ptq[0]):
                print("Jogador 2 Venceu!")
            else:
                if(self.mao1.forcan > self.mao2.forcan):
                    print("Jogador 1 Venceu!")
                elif(self.mao1.forcan < self.mao2.forcan):
                    print("Jogador 2 Venceu!")
                else:
                    print("Empate!")


    def Straight(self,mao):            
        contador_sequencia = 1

        for i in range(len(mao.cartas) - 1):
            if mao.cartas[i].numero + 1 == mao.cartas[i+1].numero:
                contador_sequencia += 1
                if contador_sequencia == 5:
                    mao.temstraight = mao.cartas[i+1].numero
                    mao.forca += 5
                    mao.forcan = mao.cartas[i+1].fnaipe
                    break
            else:
                contador_sequencia = 1
                mao.temstraight = 0
    
    def Flush(self,mao):
        flush = set([cartas.fnaipe for cartas in mao.cartas])
        print()
        if len(flush) == 1:
            mao.temflush = flush.pop()
            mao.forca +=6
            mao.forcan = mao.cartas[0].fnaipe
    
    def Pares(self,mao):
        numeros = [cartas.numero for cartas in mao.cartas]
        contagem = {numero: numeros.count(numero) for numero in set(numeros)}

        if 4 in contagem.values():
            mao.forca +=8
            mao.ptq = [[numero for numero, count in contagem.items() if count == 4][0], 4, 1]
            naipes = [cartas.fnaipe for cartas in mao.cartas if cartas.numero == mao.ptq[0]]
            mao.forcan = max(naipes)
            return
        if 3 in contagem.values() and 2 in contagem.values():
            mao.forca +=7
            mao.ptq = [[numero for numero, count in contagem.items() if count == 3][0], 3, 2]
            naipes = [cartas.fnaipe for cartas in mao.cartas if cartas.numero == mao.ptq[0]]
            mao.forcan = max(naipes)
            return
        if 3 in contagem.values():
            mao.forca +=4
            mao.ptq = [[numero for numero, count in contagem.items() if count == 3][0], 3, 1]
            naipes = [cartas.fnaipe for cartas in mao.cartas if cartas.numero == mao.ptq[0]]
            mao.forcan = max(naipes)
            return    
        if list(contagem.values()).count(2) == 2:
            mao.forca +=3
            pares = [numero for numero, count in contagem.items() if count == 2]
            mao.ptq = [max(pares),2,2]
            naipes = [cartas.fnaipe for cartas in mao.cartas if cartas.numero == max(pares)]
            mao.forcan = max(naipes)
            return
        if 2 in contagem.values():
            mao.forca +=2
            mao.ptq = [[numero for numero, count in contagem.items() if count == 2][0],2,1]
            naipes = [cartas.fnaipe for cartas in mao.cartas if cartas.numero == mao.ptq[0]]
            mao.forcan = max(naipes)
            return    
        else:
            mao.forcan = mao.cartas[-1].fnaipe 


    def Resultado(self, mao):
        if(mao.temstraight > 0 and mao.temflush < 4 and mao.temstraight == 14):
            return('ROYAL FLUSH!!!')
        elif(mao.temstraight > 0 and mao.temflush < 4):
            return('Straight Flush!!!')
        elif(mao.ptq[1] == 4):
            return('Quadra!!')
        elif(mao.ptq[1] == 3 and mao.ptq[2] == 2):
            return("Fullhouse!")
        elif(mao.temflush < 4):
            return ("Flush")
        elif(mao.temstraight > 0):
            return ("Straight")
        elif(mao.ptq[1] == 3):
            return ("Trinca")
        elif(mao.ptq[2] == 2):
            return ("Dois Pares")
        elif(mao.ptq[1] == 2):
            return ("Par")
        else:
            return ("Carta Alta")

    def build(self):
        for fnaipe in range (0, 3):
            for numero in range(2, 14):
                self.cartas.append(Carta(fnaipe, numero))

    def embaralhar(self):
        random.shuffle(self.cartas)


baralho = Baralho()
baralho.embaralhar()

jogador1 = Mao([baralho.dar_carta() for _ in range(5)])
jogador2 = Mao([baralho.dar_carta() for _ in range(5)])
print("Mão 1:", jogador1)
print("Mão 2:", jogador2)
print("Jogador 1:")
jogador1.trocar_mao()
print("Jogador 2:")
jogador2.trocar_mao()
jogador1.comprar_carta(baralho)
jogador2.comprar_carta(baralho)

rfe = Mao(Carta(3, x) for x in range(10,15))
rfc = Mao(Carta(2, x) for x in range(10,15))
alta1 = Mao([Carta(1, 2), Carta(1, 5), Carta(2, 6), Carta(3, 7), Carta(2, 14)])
alta2 = Mao([Carta(1, 3), Carta(1, 7), Carta(2, 8), Carta(3, 4), Carta(3, 14)])
par1 = Mao([Carta(1, 2), Carta(1, 3), Carta(2, 4), Carta(3, 5), Carta(2, 5)])
par2 = Mao([Carta(2, 2), Carta(3, 3), Carta(3, 4), Carta(0, 5), Carta(1, 5)])
dpar1 = Mao([Carta(1, 2), Carta(1, 4), Carta(0, 4), Carta(1, 5), Carta(2, 5)])
dpar2 = Mao([Carta(2, 2), Carta(3, 4), Carta(2, 4), Carta(0, 5), Carta(3, 5)])
flc = Mao([Carta(2, 2), Carta(2, 5), Carta(2, 8), Carta(2, 10), Carta(2, 14)])
fle = Mao([Carta(3, 2), Carta(3, 5), Carta(3, 8), Carta(3, 10), Carta(3, 14)])
st1 = Mao([Carta(1, 4), Carta(2, 5), Carta(0, 6), Carta(0, 7), Carta(1, 8)])
st2 = Mao([Carta(2, 2), Carta(3, 3), Carta(1, 4), Carta(1, 5), Carta(3, 6)])
st3 = Mao([Carta(1, 4), Carta(2, 5), Carta(0, 6), Carta(0, 7), Carta(1, 8)])
st4 = Mao([Carta(2, 4), Carta(3, 5), Carta(1, 6), Carta(2, 7), Carta(3, 8)])

ComparaMao(dpar1, dpar2)

# ComparaMao(jogador1, jogador2)

