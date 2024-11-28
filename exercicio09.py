'''
9.	Crie uma calculadora que receba dois números e a operação desejada (+, -, *, /) e exiba o resultado.
- Exemplo de saída para (4, 2, "+")
- Resultado: 6
'''

# Solicitar dois números do usuário
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

# Solicitar a operação desejada
operacao = input("Digite a operação desejada (+, -, *, /): ")

# Realizar a operação com base na entrada
if operacao == "+":
    resultado = numero1 + numero2
elif operacao == "-":
    resultado = numero1 - numero2
elif operacao == "*":
    resultado = numero1 * numero2
elif operacao == "/":
    if numero2 != 0:
        resultado = numero1 / numero2
    else:
        resultado = "Erro: divisão por zero"
else:
    resultado = "Operação inválida"

# Exibir o resultado
print(f"Resultado: {resultado}")
