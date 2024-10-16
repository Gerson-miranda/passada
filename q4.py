nomes = []

for x in range(5):
    nome = input(f'digite os nomes {x + 1}:')
    nomes.append(nome)

nomes.sort()

print('Nomes em ordem alfabética:')

for nome in nomes:
    print(nome)