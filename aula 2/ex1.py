quantidade = int(input("digite quantos numeros voce quer"))
salvar = quantidade
soma = 0
while quantidade>0:
    numero = int(input("digite um numero"))
    quantidade = quantidade -1
    soma = soma + numero
print (soma/salvar)
