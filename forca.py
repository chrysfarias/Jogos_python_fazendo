
def jogar():
    print("Bem vindo ao jogo da Forca")
    print("Fim de jogo!")

    palavra_secreta = "banana"
    letras_acertadas = ["_","_","_","_","_","_"]

    acertou  = False
    enforcou = False

    while (not acertou and not enforcou ):  # while só funciona se a condicao for true, (and) tornara a expressão verdadeira
        chute = input("qual a letra ?")
        chute = chute.lower().strip()  # corrigindo possiveis falhas do usuário
        index = 0

        for letra in palavra_secreta:
            if(chute == letra):
                letras_acertadas[index] = letra
               # print("foi encontrada a letra {} na posicao {}".format(chute,index))
            index = index + 1
        print(letras_acertadas)


if (__name__ == "__main__"):
        jogar()