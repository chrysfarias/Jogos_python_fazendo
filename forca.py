
def jogar():
    print("Bem vindo ao jogo da Forca")


    palavra_secreta = "banana"
    letras_acertadas = ["_","_","_","_","_","_"]
    acertou  = False
    enforcou = False
    erros = 0
    numero_tentativas = 6
    caracter_especial = "_"

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

        enforcou = erros == numero_tentativas  # comparar ate dar true e parar o laço
        acertou = caracter_especial not in letras_acertadas
        print(letras_acertadas)

        if(acertou):
            print("Você ganhou")

        else:
            print("Você perdeu")


    print("Fim de jogo")


if (__name__ == "__main__"):
        jogar()