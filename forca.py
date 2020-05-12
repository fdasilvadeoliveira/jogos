import turtle
import random

# caneta que vai desenhar
caneta = turtle.Turtle()
caneta.hideturtle()
caneta.penup()
caneta.speed(0)

# tela
tela = turtle.Screen()
tela.setup(width=1000, height=700)


# listao vai conter todas as palavras do arquivo para serem depois selecionados random
def preenche_lista(fil):
    listao = []
    for line in fil:
        listao.append(line)
    return listao


# O arquivo contem muitas palavras que serao colocadas em uma lista python
def abre_arquivo():
    try:
        arquivo = open("listasalva.txt", "r")
        return arquivo
    except:
        arquivo = "Falha ao abrir arquivo"
        return arquivo


def pegainput():
    while True:
        letra = tela.textinput(" ", "Digite uma letra válida:")
        if letra and len(letra) == 1:
            return letra.upper()
            break


# escreve a palavra a na tela na posicao p
def escreve(a, p):
    caneta.goto(p)
    caneta.write(a, font=("Arial", 40, "normal"))


# aqui é o jogo em si.
def testa_letra(letter, word, pos, erro, acerto):
    contador = 0
    for letra in word:
        if letra == letter:
            escreve(letra, pos[contador])
            acerto = acerto + 1
        contador += 1
    if letter not in word:
        desenha_entrada(letter, erro)
        erro = erro + 1
        desenha_boneco(erro)
    t = (erro, acerto)
    return t


def pintar_posicoes(string):
    caneta.setheading(0)
    posicoes = [(-320, -180)]  # [(-300, -180), (-350, -180)]
    contador = 0
    for i in string:
        caneta.goto(posicoes[contador])
        caneta.pendown()
        caneta.forward(40)
        caneta.penup()
        posicoes.append((posicoes[contador][0] + 60, posicoes[contador][1]))
        contador += 1
    caneta.penup()
    return posicoes


def pintar_palavra(string):
    caneta.setheading(0)
    posic = (-320, -180)
    for i in string:
        caneta.goto(posic)
        escreve(i.upper(), posic)
        posic = (posic[0]+60, posic[1])


def desenhaborda():
    caneta.goto(-480, -330)
    caneta.setheading(0)
    caneta.color("black")
    caneta.pensize(3)
    caneta.pendown()
    caneta.forward(960)
    caneta.left(90)
    caneta.forward(660)
    caneta.left(90)
    caneta.forward(960)
    caneta.left(90)
    caneta.forward(660)
    caneta.left(90)
    caneta.penup()


def desenhaforca():
    caneta.goto(-400, -180)
    caneta.setheading(90)
    caneta.pendown()
    caneta.forward(350)
    caneta.right(90)
    caneta.forward(100)
    caneta.back(70)
    caneta.right(135)
    caneta.forward(42)
    caneta.back(42)
    caneta.left(135)
    caneta.forward(70)
    caneta.right(90)
    caneta.forward(50)
    caneta.penup()


def desenha_entrada(ent, num):
    caneta.goto(-220 + 120 * num, 250)
    if num != 0:
        caneta.write("-   " + ent, font=("Arial", 40, "normal"))
    else:
        caneta.write("    " + ent, font=("Arial", 40, "normal"))


def desenha_boneco(err):
    if err == 1:
        desenha_cabeca()
    if err == 2:
        desenha_corpo()
    if err == 3:
        desenha_braco_direito()
    if err == 4:
        desenha_braco_esquerdo()
    if err == 5:
        desenha_perna_direita()
    if err == 6:
        desenha_perna_esquerda()
        desenha_perdeu()


def desenha_cabeca():
    caneta.goto(-300, 80)
    caneta.pendown()
    caneta.circle(20)
    caneta.penup()


def desenha_corpo():
    caneta.goto(-300, 80)
    caneta.setheading(90)
    caneta.pendown()
    caneta.back(100)
    caneta.penup()


def desenha_braco_direito():
    caneta.goto(-300, 80)
    caneta.setheading(315)
    caneta.pendown()
    caneta.fd(50)
    caneta.penup()


def desenha_braco_esquerdo():
    caneta.goto(-300, 80)
    caneta.setheading(225)
    caneta.pendown()
    caneta.fd(50)
    caneta.penup()


def desenha_perna_direita():
    caneta.goto(-300, -20)
    caneta.setheading(315)
    caneta.pendown()
    caneta.fd(50)
    caneta.penup()


def desenha_perna_esquerda():
    caneta.goto(-300, -20)
    caneta.setheading(225)
    caneta.pendown()
    caneta.fd(50)
    caneta.penup()


def desenha_perdeu():
    caneta.goto(-100, 40)
    caneta.write("VOCÊ PERDEU!", font=("Arial", 60, "normal"))


def desenha_venceu():
    caneta.goto(-100, 40)
    caneta.write("PARABÉNS!", font=("Arial", 60, "normal"))


f = abre_arquivo()
lista = preenche_lista(f)


def mainloop():
    if f != "Falha ao abrir arquivo":
        palavra = lista[random.randrange(len(lista))].strip()
    else:
        palavra = "palavra"
    # print(palavra)
    letradigitada = []
    erros = 0
    acertos = 0
    position = pintar_posicoes(palavra)  # retorna uma lista com as posicoes
    while erros < 6 and acertos < len(palavra):
        entrada = pegainput()
        if entrada not in letradigitada:
            letradigitada.append(entrada)
            tupla = testa_letra(entrada.upper(), palavra.upper(), position, erros, acertos)
            erros = tupla[0]
            acertos = tupla[1]
            # print("erros: " + str(erros))
            # print("acertos: " + str(acertos))
    if acertos >= len(palavra):
        desenha_venceu()
    pintar_palavra(palavra)
    # print(palavra)
    # turtle.done()


while True:
    tela.clear()
    tela.bgcolor("lightgreen")
    desenhaborda()
    desenhaforca()
    mainloop()
    numero = turtle.numinput(" ", "Deseja jogar de novo?", default=1, minval=0, maxval=1)
    if numero == 1 or numero == 0:
        pass
    else:
        tela.bye()
        break
    # sair = tela.textinput(" ", "Digite uma letra válida:")

