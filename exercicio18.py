'''
18. Escreva um programa que pede ao usuário um número inteiro e imprime a tabuada desse número de 1 a 10, 
usando um laço de repetição. 
'''
# Solicitar um número inteiro do usuário
numero = int(input("Digite um número inteiro: "))

# Laço de repetição para imprimir a tabuada de 1 a 10
print(f"Tabuada do {numero}:")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
