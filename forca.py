import random

def jogar():
    mensagem_abertura()
    palavra_secreta = carrega_palavra_secreta()
    verifica_chute_usuario(palavra_secreta)


def mensagem_abertura():
    print("Bem vindo ao jogo da Forca")


def carrega_palavra_secreta():

        arquivo = open("palavras.txt", "r")  # abrir arquivo no modo leitura
        palavras = []

        for linha in arquivo:
            linha = linha.strip()  # tirar o \n
            palavras.append(linha)

        arquivo.close()

        numero = random.randrange(0, len(palavras))
        palavra_secreta = palavras[numero]
        return palavra_secreta


def verifica_chute_usuario(palavra_secreta):
    letras_acertadas = ["_" for letra in palavra_secreta]
    acertou = False
    enforcou = False
    erros = 0
    caracter_especial = "_"
    numero_tentativas = 7
    print(letras_acertadas)

    while (
            not acertou and not enforcou):  # while só funciona se a condicao for true, (and) tornara a expressão verdadeira
        chute = input("digite uma letra: ")
        chute = chute.lower().strip()  # corrigindo possiveis falhas do usuário

        if (chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if (chute == letra):
                    letras_acertadas[index] = letra
                index += 1

        if (chute in letras_acertadas):
            print("Voce ainda possui um total de: {} tentativas".format(numero_tentativas))
            numero_tentativas -= 1
            erros += 1

        else:
            erros += 1
            desenha_forca(erros)
            numero_tentativas -= 1
            print("Voce ainda possui um total de: {} tentativas".format(numero_tentativas))

        enforcou = erros == 7  # comparar ate dar true e parar o laço
        acertou = caracter_especial not in letras_acertadas
        print(letras_acertadas)

        if (enforcou):
            imprime_mensagem_perdedor(palavra_secreta)

        if (acertou):
            imprime_mensagem_vencedor()
            break

    print("Fim de jogo")



def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era: {}".format(palavra_secreta))
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




if (__name__ == "__main__"):
        jogar()


