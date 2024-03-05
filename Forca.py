import random
vencedor = '''
  +---+
      |
      |
 \o/  |
  |   |
 / \  |
=========
'''
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

palavras = ["rogerio escudero"]

def escolher_palavra():
    return random.choice(palavras)

def mostrar_interface(palavra_secreta, letras_corretas, letras_incorretas, tentativas_restantes):
    if tentativas_restantes > 10:
      print(stages[6])
    elif tentativas_restantes > 8:
      print(stages[5])
    elif tentativas_restantes > 6:
      print(stages[4])
    elif tentativas_restantes > 4:
      print(stages[3])
    elif tentativas_restantes > 2:
      print(stages[2])
    elif tentativas_restantes > 0:
      print(stages[1])
      
    print("\nPalavra: " + " ".join(letra if letra in letras_corretas else "_" for letra in palavra_secreta))
    print("Letras erradas: " + ", ".join(letras_incorretas))
    print("Tentativas restantes:", tentativas_restantes)

def jogar_forca():
    print(logo)
    print("Bem-vindo ao Jogo da Forca!")
    print("Regras:")
    print("- Você tem um número limitado de tentativas para adivinhar a palavra.")
    print("- Se acertar uma letra, o número de tentativas restantes diminui.")
    print("- Você pode chutar a palavra inteira a qualquer momento, mas só tem 1 chance.")
    print("- Boa sorte!")

    palavra_secreta = escolher_palavra()
    letras_corretas = set()
    letras_incorretas = set()
    tentativas_restantes = len(palavra_secreta) - 2


    while tentativas_restantes > 0:
        mostrar_interface(palavra_secreta, letras_corretas, letras_incorretas, tentativas_restantes)
        try:
           palpite = input("Digite uma letra ou chute a palavra inteira: ").lower()
        except EOFError as e:
           print("EOF Não funciona")
           continue
        except KeyboardInterrupt:
           print("\nVai jogar até o fim!")
           continue

        if len(palpite) == 1:
            if tentativas_restantes == 1:
               print("A ultima tentativa precisa ser uma palavra inteira!")
               continue
            if palpite in letras_corretas or palpite in letras_incorretas:
                print("Você já tentou essa letra e perdeu uma tentativa pra deixar de ser besta. Tente novamente.")
                tentativas_restantes -= 1
            elif palpite in palavra_secreta:
                letras_corretas.add(palpite)
                tentativas_restantes -= 1
            else:
                letras_incorretas.add(palpite)
                tentativas_restantes -= 1
        elif len(palpite) == len(palavra_secreta):
            if palpite == palavra_secreta:
                print(vencedor)
                print("Parabéns! Você acertou a palavra!")
                return
            else:
                print(stages[0])
                print("Você perdeu! A palavra correta era:", palavra_secreta)
                return
        else:
            print("Por favor, insira apenas uma letra ou chute a palavra inteira.")
            
        if all(letra in letras_corretas for letra in palavra_secreta):
            print(vencedor)
            print("Parabéns! Você ganhou!")
            return
    print(stages[0])
    print("Você perdeu! A palavra correta era:", palavra_secreta)

jogar_forca()
