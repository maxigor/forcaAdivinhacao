import forca
import adivinhacao

def escolha_jogo():

    palavra = "aluracursos"
    palavra.find("s")
    palavra.find("l")
    palavra.find("a")
    palavra.find("b")

    print("###############################")
    print("Escolha o seu jogo")
    print("###############################")

    print("(1) - Forca // (2) - Adivinhacao")
    jogo = int(input("Qual jogo?"))

    if(jogo == 1 ):
        print("Voce escolheu forca")
        forca.jogar()
    elif(jogo == 2):
        print("Voce escolheu Adivinhacao")
        adivinhacao.jogar()


if (__name__ == '__main__'):
    escolha_jogo()
