'''
6.	Construa um algoritmo que receba um número e mostre o número somente se ele estiver entre trinta e duzentos e oitenta e um (inclusive).
'''
# Solicitar um número do usuário
numero = float(input("Digite um número: "))

# Verificar se o número está entre 30 e 281 (inclusive)
if 30 <= numero <= 281:
    print(f"O número é {numero}.")
else:
    print("O número não está entre 30 e 281.")
