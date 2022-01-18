import random


def jogar():
    print("Bem vindo ao jogo da Forca")

    arquivo = open("palavras.txt","r")   #abrir arquivo no modo leitura
    palavras =[]


    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))

    palavra_secreta = palavras[numero]
    letras_acertadas = ["_" for letra in palavra_secreta]
    acertou  = False
    enforcou = False
    erros = 0
    caracter_especial = "_"
    numero_tentativas = 6

    while (not acertou and not enforcou):  # while só funciona se a condicao for true, (and) tornara a expressão verdadeira

        chute = input("qual a letra?: ")
        chute = chute.lower().strip()       # corrigindo possiveis falhas do usuário

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:   # varrer a lista letras_acertadas
                if(chute == letra):
                    letras_acertadas[index] = letra
                index += 1
        else:

            erros += 1
            numero_tentativas -=1
            print("Voce ainda possui um total de: {} tentativas".format(numero_tentativas))


        enforcou = erros == 6  # comparar ate dar true e parar o laço
        acertou = caracter_especial not in letras_acertadas
        print(letras_acertadas)

        if(acertou):
            print("Você ganhou")
            break



    print("Fim de jogo")


if (__name__ == "__main__"):
        jogar()