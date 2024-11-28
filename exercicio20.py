'''
20. Escreva um programa que usa um laço for para somar todos os números pares entre 1 e 100 e exibe o resultado. 
'''

# Inicializar a soma
soma = 0

# Laço de repetição para somar os números pares entre 1 e 100
for i in range(1, 101):
    if i % 2 == 0:
        soma += i

# Exibir o resultado
print(f"A soma dos números pares entre 1 e 100 é {soma}.")
