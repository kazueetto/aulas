import random
p = input ("impar ou par?")
n = input ("escolha um numero de 0 a 10: ")
ns = random.randint (0,10)
print (ns)
im = (n + ns) %2
if (p == "impar" and im == 1)
    print ("Parabens, vc ganhou!")
elif (p == "par" and im == 0)
    print ("Parabens, vc ganhou!")
else:
    print ("Boa tentaiva mas, vc perdeu")
