import random


def jogar():

    mensagem_de_abertura()
    palavra_secreta = carrega_palavras()
    letra_acertada = inicializa_letras_acertadas(palavra_secreta)


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



def mensagem_de_abertura():
    print("###############################")
    print("Bem vindo ao jogo de Forca")
    print("###############################")


def carrega_palavras():
    arquivo = open("palavras.txt" , "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta =  palavras[numero].upper()
    print("A palavra contem {} caracters".format(len(palavra_secreta)))
    return palavra_secreta


def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]



if(__name__ == "__main__"):
    jogar()
