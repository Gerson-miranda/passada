numeros = []

for x in range(10):
    numero = int(input(f'digite os numeros {x + 1}:'))
    
    numeros.append(numero)

media = sum(numeros)

print(f'a media dos numeros é {media}:')