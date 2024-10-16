numeros = []

for x in range(3):
    
    num = int(input(f'Digite o número {x + 1}: '))
    numeros.append(num)
      
maior = max(numeros) 

print(f'O maior número é:{maior}')