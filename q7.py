
numeros = []
numeros_negativos = []
soma_positivos = 0
contagem_positivos = 0
contagem_negativos = 0


for i in range(10):
    while True:
        try:
            numero = float(input(f"Digite o {i+1}º número: "))
            numeros.append(numero)
            break
        except ValueError:
            print("Por favor, digite um número válido.")


for numero in numeros:
    if numero > 0:
        soma_positivos += numero
        contagem_positivos += 1
    elif numero < 0:
        numeros_negativos.append(numero)
        contagem_negativos += 1


print(f"Quantidade de números positivos: {contagem_positivos}")
print(f"Quantidade de números negativos: {contagem_negativos}")
print("Lista de números negativos:", numeros_negativos)
print(f"Soma dos números positivos: {soma_positivos}")