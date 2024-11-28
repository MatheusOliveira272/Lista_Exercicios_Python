'''
17. Peça ao usuário para inserir um número inteiro positivo. Use um laço de repetição para somar todos os números 
de 1 até o número fornecido e exibir o resultado. 
'''
# Solicitar um número inteiro positivo do usuário
numero = int(input("Digite um número inteiro positivo: "))

# Inicializar a soma
soma = 0

# Verificar se o número é positivo
if numero > 0:
    # Laço de repetição para somar os números de 1 até o número fornecido
    for i in range(1, numero + 1):
        soma += i

    # Exibir o resultado
    print(f"A soma dos números de 1 até {numero} é {soma}.")
else:
    print("Por favor, insira um número inteiro positivo.")
