numeros = []


for i in range(10):
            numero = int(input(f"Digite o {i+1}º número: "))
            
            numeros.append(numero)

            
print("Lista de números:", numeros)
    
maior_numero = max(numeros)
        
print("O maior número é:", maior_numero)

soma_numeros = sum(numeros)

print("A soma de todos os números é:", soma_numeros)