'''
10.	Peça ao usuário para inserir uma frase e conte quantas palavras essa frase contém.
'''
# Solicitar uma frase do usuário
frase = input("Digite uma frase: ")

# Contar o número de palavras na frase
quantidade_palavras = len(frase.split())

# Exibir o número de palavras
print(f"A frase contém {quantidade_palavras} palavras.")
