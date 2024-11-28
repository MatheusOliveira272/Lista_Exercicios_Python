'''
Construa um algoritmo que receba a idade de uma pessoa e retorne a faixa etária de acordo com os dados a 
seguir:
'''

# Solicitar a idade da pessoa
idade = int(input("Digite a idade da pessoa: "))

# Verificar a faixa etária e exibir a mensagem correspondente
if 0 <= idade <= 12:
    print("Criança")
elif 13 <= idade <= 17:
    print("Adolescente")
elif 18 <= idade <= 64:
    print("Adulto")
elif idade >= 65:
    print("Idoso")
else:
    print("Idade inválida")
