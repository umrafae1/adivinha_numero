import random
import os

secreto = random.randint(1,100)

tentativa=0

print('Bem vindo o jogo da adivinhação!')

while True:
    palpite = int(input('Digite um número entre 1 é 100: '))
    os.system('cls') #limpa o terminal

    if palpite == secreto:
        print(f'Parabéns, você acertou o número secreto em {tentativa} vezes !!')
        break
    elif palpite<secreto:
        print('Tente um número maior!!')
        tentativa+=1
    else:
        print('Tente um número menor!!')
        tentativa+=1
