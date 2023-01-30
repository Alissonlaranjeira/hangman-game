import random

#funcoes:
#obs: o lugar da funcao nao importa,eu poderia chamar uma funcao q foi feita depois e ia funcionar
#obs: funcao n pode ter o mesmo nome de variavel

def apresentacao():
    print('*********************************************')
    print('Olá!Bem vindo ao jogo de forca!')
    print('*********************************************') #
def escolher_palavra():
    # arquivo:
    arquivo = open('palavras.txt', 'r')  # abrir e ler
    palavras = []
    for linha in arquivo:  # ler todas as linhas
        palavras.append(linha.strip())  # tira caracteres especiais como \n
    arquivo.close()  # fechar

    # escolher uma palavra aleatóriamente:
    numero = random.randrange(0, len(palavras))  # escolhe uma posicao aleatoria de 0 até a ultima posicao do vetor
    palavra_secreta = palavras[numero].upper()  # deixa em maiusculo!
    return  palavra_secreta
def mostrar_letras_acertadas(palavra):
    ##lista dinâmica
    letras_acertadas = ['_' for letra in palavra]  # percorra toda a palavra secreta e coloca '-' em letras_acertadas
    print(letras_acertadas)
    return ['_' for letra in palavra]
def pede_chute():
    chute = input('Diga uma letra:')
    chute = chute.strip().upper()  # strip()=remove espaços no inicio e no fim! upper()=maiusculo!
    return chute
def marca_chute_correto(chute,palavra_secreta,letras_acertadas):
    index = 0  # posicao!

    for letra in palavra_secreta:  # é um for onde ele passa a palavra_secreta inteira e em cada instante letra=letra da palavra
        if (chute.upper() == letra.upper()):  # passa as letras para maiusculo e compara
            letras_acertadas[index] = letra  # substirui um "_" pela chute
        index += 1  # index = index + 1
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

def jogar():

    apresentacao()
    palavra_secreta  = escolher_palavra()
    letras_acertadas = mostrar_letras_acertadas(palavra_secreta)

    enforcou = False
    acertou  = False
    erros    = 0 #tentativas

    while(not enforcou and not acertou): #enquanto nao inforcou e nao acertou-->TRUE AND TRUE = TRUE

        chute = pede_chute()

        if (chute in palavra_secreta): #se o chute estiver na palavra
            marca_chute_correto(chute,palavra_secreta,letras_acertadas)
        else:
                erros += 1
                print('Ops,você errou,falta {} tentativas'.format(len(palavra_secreta)-erros))
                desenha_forca(erros)
        enforcou = erros == 7 #se erros iguais a 7,se for vdd enforcou passa a ser true
        acertou = "_" not in letras_acertadas #testando se  NÃO HÁ "_"
        print(letras_acertadas)
        letras_faltando = str(letras_acertadas.count('_'))
        print('Faltam {} letras'.format(letras_faltando))


    if(acertou):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)
    print('FIM DO JOGO!')



if(__name__=="__main__"): #se o "forca" for o programa principal,chame a funcao jogar()
    jogar()
