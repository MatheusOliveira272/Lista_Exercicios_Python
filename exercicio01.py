'''
1.	Escreva um algoritmo que receba do usuário um número e mostre a sua metade somente quando ela for maior que cinquenta.
'''

# Solicitar um número do usuário
numero = float(input("Digite um número: "))

# Calcular a metade do número
metade = numero / 2

# Verificar se a metade é maior que 50 e exibir o resultado
if metade > 50:
    print(f"A metade de {numero} é {metade}.")
else:
    print("A metade do número não é maior que 50.")
