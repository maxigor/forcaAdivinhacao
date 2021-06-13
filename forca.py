import random


def jogar():

    mensagem_de_abertura()
    palavra_secreta = carrega_palavras()
    letra_acertada = inicializa_letras_acertadas(palavra_secreta)

    enforcou = False
    acertou =  False
    erros = 0

    print(letra_acertada)

    while (not acertou and not enforcou):
        chute = captura_chute()

        if(chute in palavra_secreta):
            comparando_chute(chute, letra_acertada, palavra_secreta)
        else:
            erros += 1
            desenha_forca(erros)

        enforcou = erros == 6
        acertou = "_" not in letra_acertada
        print(letra_acertada)

    if(acertou):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)


def captura_chute():
    chute = input("Digite a letra: ")
    chute = chute.strip().upper()
    return chute


def comparando_chute(chute, letra_acertada, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if(chute == letra):
            letra_acertada[index] = chute
            print("Acertou a letra {} na posicao {}".format(letra.upper(), index))
        index += 1


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

def imprime_mensagem_perdedor(palavra):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

        print(" |            ")
        print("_|___         ")
        print()

if(__name__ == "__main__"):
    jogar()
