import os

soma = 0


while True:
   
    numero = int(input("Digite um número inteiro (0 para sair): "))
    
    os.system('cls')
   
    if (numero == 0):
        break
    
    
    soma += numero


print(f"A soma dos números digitados é: {soma}")