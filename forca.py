import random

def jogar():
    print("###############################")
    print("Bem vindo ao jogo de Forca")
    print("###############################")


    arquivo = open("palavras.txt" , "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))

    palavra_secreta =  palavras[numero].upper()
    letra_acertada = ["_" for letra in palavra_secreta]
    print("A palavra contem {} caracters".format(len(palavra_secreta)))
    print(letra_acertada)

    enforcou = False
    acertou =  False
    erros = 0

    while (not acertou and not enforcou):

        chute = input("Digite a letra: ")
        chute = chute.strip().upper()

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    letra_acertada[index] = chute
                    print("Acertou a letra {} na posicao {}".format(letra.upper(), index))
                index += 1

        else:
            erros += 1
            print("voce errou {} vezes e tem {} chances de errar ".format(erros, 6-erros))

        enforcou = erros == 6
        acertou = "_" not in letra_acertada
        print(letra_acertada)

    if(acertou):
        print("Voce ganhou!")
    else:
        print("Voce perdeu!")
        print("A palavra era {}".format(palavra_secreta))
    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()

























6
