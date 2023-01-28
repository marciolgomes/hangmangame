import requests
from lxml import html


def carregar_palavra_secreta():
    """
    Gera uma palavra aleatória a partir do site palavrasaleatorias.com usando webscraping
    :return: Palavra na língua portuguesa em letras maiúsculas
    """
    resposta = requests.get("https://www.palabrasaleatorias.com/palavras-aleatorias.php?fs=1&fs2=0&Submit=Nova+palavra")
    elemento = html.fromstring(resposta.content)
    palavra_secreta = elemento.xpath('//div[@style="font-size:3em; color:#6200C5;"]/text()')
    palavra_secreta = palavra_secreta[0].strip()
    return palavra_secreta.upper()


def feedback(palavra_jogo, acertos):
    """
    Retorna um feedback da palavra que o jogador conseguiu formar até a rodada
    que ele está, letras que ainda não acertaram ficam com _
    :param palavra: Uma palavra na língua portuguesa com letras maiúsculas
    :return: Palavra formada no até o momento da jogada. Ex: _O_L_
    """
    palavra_feedback = list(palavra_jogo).copy()
    for i, k in enumerate(palavra_jogo):
        if k in acertos:
            palavra_feedback[i] = k
        else:
            palavra_feedback[i] = '_'
    print(palavra_feedback)


def play_hangman():
    palavra = 'DINOSSAURO'
    acertos = list()
    tentativas_anteriores = []
    chances = 5

    while chances != 0:
        tentativa = str(input("Tente uma letra: ")).upper().strip()
        while tentativa in tentativas_anteriores:
            tentativa = input('Você já tentou essa letra, tente outra: ').upper().strip()
        if tentativa in palavra:
            acertos.append(tentativa)
            tentativas_anteriores.append(tentativa)
            print('Parece que essa letra faz parte da palavra...')
            feedback(palavra, acertos)
        else:
            tentativas_anteriores.append(tentativa)
            print('Essa letra não te ajuda...')
            chances -= 1
            print(f'Você tem {chances} chances')
        if len(set(palavra)) == len(set(acertos)):
            print(f"Você acertou a palavra {palavra}, parabéns!")
            break
        elif chances == 0:
            print(f'Parece que você não conseguiu :C A palavra era {palavra}!')


play_hangman()
