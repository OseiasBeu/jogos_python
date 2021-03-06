import random
import csv

def jogar():

    mensagem_boas_vindas()
    palavra_secreta = carrega_palavra_secreta()

    letras_acertadas = inicializa_letras_acertadas(palavra_secreta[0])

    enforcou = False
    acertou  = False
    erros = 0

    while (not acertou and not enforcou):

        chute = pede_chute()

        if (chute.upper() == 'DICA'):
            print("A dica é: {}".format(palavra_secreta[1]))
        elif (chute.upper() == 'SAIR'):
            print("Saindo....")
            erros = 7
        elif (chute in palavra_secreta[0]):
            marca_chute_correto(chute, letras_acertadas, palavra_secreta[0])
        else:
            erros += 1

        desenha_forca(erros)

        enforcou = erros == 7
        acertou = "_" not in letras_acertadas
        print(exibir_palavra(letras_acertadas))

    if (acertou):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta[0])

def mensagem_boas_vindas():
    print("************************************")
    print("*   Bem vindo ao jogo da Forca!    *")
    print("************************************")
    print("* Opções:                          *")
    print("*  1. Informe uma letra para chute *")
    print("*  2. Digite DICA para obter ajuda *")
    print("*  3. Digite SAIR para finalizar   *")
    print("************************************")

def carrega_palavra_secreta(primeira_linha_valida = 0, nome_arquivo="palavras.txt"):
    palavras = []
    dicas = []
    with open(nome_arquivo, 'r') as arquivo:
        reader = csv.reader(arquivo, delimiter='\t')
        for palavra, dica in reader:
            palavras.append(palavra.strip())
            dicas.append(dica.strip())

    posicao = random.randrange(primeira_linha_valida, len(palavras))

    return [palavras[posicao].upper(), dicas[posicao]]

def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]

def pede_chute():
    chute = input("Qual letra? ")
    chute = chute.strip().upper()
    return chute

def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = letra
        index += 1

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

def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
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

def exibir_palavra(palavra):
    conteudo = ""
    for letra in palavra:
        conteudo = conteudo + ' ' + letra
    return conteudo

if(__name__ == "__main__"):
    jogar()
