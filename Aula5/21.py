import random
baralho = list (range(1, 10))
baralho = baralho + [10, 10, 10]
baralho = baralho * 4
random.shuffle(baralho)
jogador = []
while (sum (jogador) < 21):
        carta = baralho.pop(0)
        jogador.append(carta)
        print ("Suas cartas: ")
        print (jogador)
        acao = input ("Digite 1 para parar, e qualquer outra tecla para continuar a jogar.")
        if (acao == 1):
            break
print ("Suas cartas: ", jogador)
print ("Voce fez ", sum (jogador), "pontos!")

