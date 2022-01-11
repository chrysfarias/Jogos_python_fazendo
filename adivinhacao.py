import random


def jogar():
    print("Bem vindo ao jogo de adivinhação, por favor digite um número entre 1 e 50")
    print("Qual o nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")
    nivel = int(input("Defina o nível: "))
    nivel_facil       = nivel ==1
    nivel_medio       = nivel ==2
    nivel_dificil     = nivel ==3
    nivel_invalido    = nivel <1 or nivel >3
    numero_secreto    =  random.randrange(1,51)
    tentativas        = 0
    pontuacao_inicial = 100
    soma_pontuacao    = 0

    if(nivel_facil):
        tentativas = 12

    elif(nivel_medio):
        tentativas = 9

    elif(nivel_dificil):
        tentativas = 6

    for rodada_atual in range(1, tentativas + 1):

        print("Tentativa {} de {}" .format(rodada_atual,tentativas))
        chute_str = input("Digite um número: ")

        print("Você digitou", chute_str)

        chute = int(chute_str)  # converteu para inteiro o dado que antes era str
        soma_pontuacao =  soma_pontuacao +  abs(chute - numero_secreto)   # sempre devolver valor positivo
        print("Sua Pontuação Atual: {} " .format(pontuacao_inicial - soma_pontuacao))

        acertou         = chute == numero_secreto
        chute_maior     = chute > numero_secreto and chute > 0
        chute_menor     = chute < numero_secreto and chute > 0
        numero_invalido = chute <=0 or chute > 50

        if(acertou):
            print("voce acertou e fez: {} pontos ".format(pontuacao_inicial - soma_pontuacao))
            break

        elif(chute_menor ):
            print("voce chutou um valor menor que o numero secreto")

        elif(chute_maior):
            print("voce chutou um valor maior que o numero secreto")

        elif(numero_invalido):
           print("Por favor, digite um número entre 1 e 50")
           continue

    print("O numero secreto era: {}" . format(numero_secreto))
    print("Fim de jogo!")

if(__name__ == "__main__"):
    jogar()


