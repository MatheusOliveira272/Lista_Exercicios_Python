'''
12. Construa um algoritmo que receba dois números e mostre quando o primeiro for maior e quando for menor 
que o segundo. 
'''

# Solicitar dois números do usuário
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

# Verificar se o primeiro número é maior ou menor que o segundo
if numero1 > numero2:
    print(f"O primeiro número ({numero1}) é maior que o segundo ({numero2}).")
elif numero1 < numero2:
    print(f"O primeiro número ({numero1}) é menor que o segundo ({numero2}).")
else:
    print("Os números são iguais.")
