'''
14. Faça um algoritmo que receba a matrícula e duas notas do aluno. Calcular a média e mostrar a matrícula do 
aluno com as seguintes mensagens de acordo com os dados a seguir: 
'''
# Solicitar a matrícula e as notas do aluno
matricula = input("Digite a matrícula do aluno: ")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

# Calcular a média
media = (nota1 + nota2) / 2

# Exibir a matrícula e a média
print(f"Matrícula: {matricula}")
print(f"Média: {media:.1f}")

# Mensagens de acordo com a média
if media > 7.0:
    print("Aluno Aprovado")
elif media == 7.0:
    print("Aluno em Recuperação")
else:
    print("Aluno Reprovado")
