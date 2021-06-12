
def jogar():
	import random

	print("###############################")
	print("Bem vindo ao jogo de Adivinhacao")
	print("###############################")

	numero_secreto = int(round(random.randrange(1 , 101)))
	total_de_tentativas = 0
	pontos = 1000

	print("Escolha o nivel de dificuldade")
	print("(1)-Facil (2)-Medio (3)-Dificil")

	dificuldade = int(input("Insira o nivel de dificuldade:  "))
	if(dificuldade == 1):
		total_de_tentativas = 20
	elif(dificuldade == 2):
		total_de_tentativas = 10
	else:
		total_de_tentativas = 5

	print(" Voce possui {} tentativas".format(total_de_tentativas))
	for rodada in range(1, total_de_tentativas + 1):
		print("Tentativa {} de {}" .format(rodada ,total_de_tentativas ))
		chute_str = input("digite o seu numero: ")
		print("voce digitou ", chute_str)
		chute = int(chute_str)

		if(chute < 1 or chute > 100):
			print("###############################")
			print("O valor so deve ser entre 1 e 100")
			print("###############################")
			continue

		maior = numero_secreto < chute
		menor = numero_secreto > chute

		if (numero_secreto == chute):
			print("Voce acertou e ficou com {} pontos".format(pontos))
			break
		else:
			if(menor):
				print("O seu chute foi menor")
			elif(maior):
				print("O seu chute foi maior")
		rodada = rodada + 1

		pontos_perdidos = abs(numero_secreto - chute)
		pontos = pontos - pontos_perdidos


	print("Fim de jogo e ficou com {} pontos".format(pontos))

if(__name__ == "__main__"):
	jogar()
