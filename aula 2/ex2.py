numeros = [] 
while num != (-1): 
    num=int(input("Digite um número ")) 
    numeros.append(num) 
numeros.pop(-1) 
print("Maior valor:",max(numeros)) 
print("Menor valor:",min(numeros)) 