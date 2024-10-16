import random


nomes = []


for i in range(10):
    nome = input(f"Digite o {i+1}º nome: ")
    nomes.append(nome)


nome_sorteado = random.choice(nomes)


print("O nome sorteado é:", nome_sorteado)