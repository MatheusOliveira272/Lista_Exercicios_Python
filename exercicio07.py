'''
7.	Faça um algoritmo que receba nome, idade e altura, exiba somente o nome da pessoa com 1,70m e idade acima de 17 anos.
'''
# Solicitar o nome, idade e altura do usuário
nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))
altura = float(input("Digite a altura (em metros): "))

# Verificar se a altura é 1,70m e a idade é acima de 17 anos
if altura == 1.70 and idade > 17:
    print(f"O nome da pessoa é {nome}.")
else:
    print("A pessoa não atende aos critérios.")
