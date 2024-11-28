'''
5.	Escreva um algoritmo que receba um número e mostre o número, se ele estiver entre quinze (inclusive) e quarenta. 
'''

# Solicitar um número do usuário
numero = float(input("Digite um número: "))

# Verificar se o número está entre 15 e 40 (inclusive)
if 15 <= numero <= 40:
    print(f"O número é {numero}.")
else:
    print("O número não está entre 15 e 40.")
