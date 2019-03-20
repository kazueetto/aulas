op = input ("par ou impar?")
numj = int (input("insira o numero:"))
import random
numc = random.randint (0, 10)
print (numc)
paridade = (numj + numc) % 2
if (op == "par" and paridade == 0) or (op == "impar" and paridade == 1):
    print ("tu vanceu, ma va te volta")
else:
    print ( "tu perdestes. vai se ruim meu fi")