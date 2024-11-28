'''
8.	Construa um algoritmo que receba um número e mostre se o número recebido é ímpar.
'''
# Solicitar um número do usuário
numero = int(input("Digite um número: "))

# Verificar se o número é ímpar
if numero % 2 != 0:
    print(f"O número {numero} é ímpar.")
else:
    print(f"O número {numero} não é ímpar.")
