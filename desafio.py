'''
Crie um jogo de adivinhação em que o programa gera um número aleatório entre 1 e 50, e o jogador tem 5 tentativas 
para adivinhar o número. Após cada tentativa, o programa deve informar se o número é maior ou menor do que o valor 
digitado pelo jogador. Se o jogador adivinhar o número, o programa deve parabenizá-lo e terminar. Se o jogador não 
acertar após as 5 tentativas, o programa deve exibir o número correto.
'''

import random

# Gerar um número aleatório entre 1 e 50
numero_secreto = random.randint(1, 50)

print("Bem-vindo ao jogo de adivinhação! Tente adivinhar o número entre 1 e 50.")
print("Você tem 5 tentativas.")

# Laço para controlar o número de tentativas
for tentativa in range(1, 6):
    palpite = int(input(f"Tentativa {tentativa}: "))

    # Verificar se o palpite está correto
    if palpite == numero_secreto:
        print("Parabéns! Você acertou o número.")
        break
    elif palpite < numero_secreto:
        print("O número é maior que", palpite)
    else:
        print("O número é menor que", palpite)

# Exibir o número correto se o jogador não adivinhou
if palpite != numero_secreto:
    print(f"Você não acertou. O número correto era {numero_secreto}.")
