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
        numero_tentativas = 6
        print(letras_acertadas)

        while (not acertou and not enforcou): # while só funciona se a condicao for true, (and) tornara a expressão verdadeira
            chute = input("digite uma letra: ")
            chute = chute.lower().strip()  # corrigindo possiveis falhas do usuário

            if (chute in palavra_secreta):
                index = 0
                for letra in palavra_secreta:
                    if (chute == letra):
                        letras_acertadas[index] = letra
                    index += 1
            else:

                erros += 1
                numero_tentativas -= 1
                print("Voce ainda possui um total de: {} tentativas".format(numero_tentativas))

            enforcou = erros == 6  # comparar ate dar true e parar o laço
            acertou = caracter_especial not in letras_acertadas
            print(letras_acertadas)

            if (acertou):
                print("Você ganhou")
                break

        print("Fim de jogo")


if (__name__ == "__main__"):
        jogar()


