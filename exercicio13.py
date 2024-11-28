'''
Escreva um algoritmo que receba dois números e informe a diferença do maior pelo menor.
'''
# Solicitar dois números do usuário
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

# Calcular a diferença do maior pelo menor
if numero1 > numero2:
    diferenca = numero1 - numero2
else:
    diferenca = numero2 - numero1

# Exibir a diferença
print(f"A diferença do maior pelo menor é {diferenca}.")
