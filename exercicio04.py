'''
4.	Crie um algoritmo que receba do usuário dois números e mostre a diferença somente quando o primeiro for maior que o segundo.
'''
# Solicitar dois números do usuário
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

# Verificar se o primeiro número é maior que o segundo
if numero1 > numero2:
    diferenca = numero1 - numero2
    print(f"A diferença entre {numero1} e {numero2} é {diferenca}.")
else:
    print("O primeiro número não é maior que o segundo.")
