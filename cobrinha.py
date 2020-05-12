import turtle
import random
import time


# Funcoes que tenham a ver com desenho
def desenhaborda():
    caneta.goto(-300, -300)
    caneta.setheading(0)
    caneta.pensize(3)
    caneta.pendown()
    caneta.forward(600)
    caneta.left(90)
    caneta.forward(600)
    caneta.left(90)
    caneta.forward(600)
    caneta.left(90)
    caneta.forward(600)
    caneta.left(90)
    caneta.penup()
    caneta.goto(-290, 320)
    caneta.write("Pontos: ", font=("Arial", 30, "normal"))
    caneta.goto(100, 320)
    caneta.write("Recorde: ", font=("Arial", 30, "normal"))


def desenha_pontos():
    caneta_pontos.undo()
    caneta_pontos.write(len(rabo) - 1, font=("Arial", 30, "normal"))


def desenha_recorde(rec):
    caneta_recorde.undo()
    caneta_recorde.write(rec, font=("Arial", 30, "normal"))


# Funcao pra comida
def checa_comida():
    global variavel_da_comida
    if cobrinha.distance(comida) < 15:
        comida.goto(random.randint(-290, 290), random.randint(-290, 290))
        rabo_cresce()
        desenha_pontos()
        variavel_da_comida = len(rabo)+1
        inchar.goto(cobrinha.pos())
        inchar.showturtle()


def comida_passando():
    global variavel_da_comida
    if variavel_da_comida > 0:
        variavel_da_comida = variavel_da_comida - 1
    if variavel_da_comida == 0:
        inchar.hideturtle()


# Funcoes que tenham a ver com a cobrinha
def cobrinha_esquerda():
    global velocidade
    velocidade = 18
    if cobrinha.heading() == 90:
        cobrinha.setheading(180)
    elif cobrinha.heading() == 270:
        cobrinha.setheading(180)


def cobrinha_direita():
    global velocidade
    velocidade = 18
    if cobrinha.heading() == 90:
        cobrinha.setheading(0)
    elif cobrinha.heading() == 270:
        cobrinha.setheading(0)


def cobrinha_cima():
    global velocidade
    velocidade = 18
    if cobrinha.heading() == 0:
        cobrinha.setheading(90)
    elif cobrinha.heading() == 180:
        cobrinha.setheading(90)


def cobrinha_baixo():
    global velocidade
    velocidade = 18
    if cobrinha.heading() == 0:
        cobrinha.setheading(270)
    elif cobrinha.heading() == 180:
        cobrinha.setheading(270)


def rabo_cresce():
    rabo.append([rabo[-1][0].clone(), rabo[-1][0].pos()])


def apaga_rabo():
    comida.goto(random.randint(-290, 290), random.randint(-290, 290))
    while len(rabo) > 0:
        rabo[-1][0].hideturtle()
        rabo.pop()


def rabo_anda():
    for i in range(1, len(rabo)):
        rabo[-i][1] = rabo[-i-1][0].pos()
    for i in range(0, len(rabo)):
        rabo[i][0].goto(rabo[i][1])


def checa_se_bateu():
    global rabo, velocidade
    if cobrinha.xcor() > 290 or cobrinha.xcor() < -290 or cobrinha.ycor() > 290 or cobrinha.ycor() < -290:
        apaga_rabo()
        cobrinha.goto(0, 0)
        corpo.showturtle()
        rabo = [[corpo.clone(), cobrinha.pos()]]
        corpo.hideturtle()
        velocidade = 0
        caneta_pontos.undo()
        caneta_pontos.write(len(rabo) - 1, font=("Arial", 30, "normal"))
    for item in rabo:
        if cobrinha.distance(item[0].pos()) < 15:
            apaga_rabo()
            cobrinha.goto(0, 0)
            corpo.showturtle()
            rabo = [[corpo.clone(), cobrinha.pos()]]
            corpo.hideturtle()
            velocidade = 0
            caneta_pontos.undo()
            caneta_pontos.write(len(rabo) - 1, font=("Arial", 30, "normal"))


def mainloop():
    desenhaborda()
    recorde = 0
    global rabo, velocidade
    while True:
        tela.update()
        tela.listen()
        rabo[0][1] = cobrinha.pos()
        cobrinha.forward(velocidade)
        time.sleep(0.1)
        if velocidade != 0:
            checa_se_bateu()
        rabo_anda()
        checa_comida()
        comida_passando()
        if len(rabo)-1 > recorde:
            recorde = len(rabo)-1
            desenha_recorde(recorde)
    # fim
    # turtle.done()


# Tamanho e fundo da tela
tela = turtle.Screen()
tela.setup(width=800, height=800)
tela.tracer(0)
tela.bgcolor("#8FBC8F")
tela.title("SNAKE")
# Aqui ja tem mais a ver com a animacao e as entradas de teclas
tela.onkeypress(cobrinha_esquerda, key="Left")
tela.onkeypress(cobrinha_direita, key="Right")
tela.onkeypress(cobrinha_cima, key="Up")
tela.onkeypress(cobrinha_baixo, key="Down")
tela.onkeypress(rabo_cresce, key="space")
tela.onkeypress(cobrinha_esquerda, key="a")
tela.onkeypress(cobrinha_direita, key="d")
tela.onkeypress(cobrinha_cima, key="w")
tela.onkeypress(cobrinha_baixo, key="s")

# Desenhos da tela
caneta = turtle.Turtle()
caneta.hideturtle()
caneta.penup()
caneta.speed(0)
caneta.color("white")

# Cobrinha
cobrinha = turtle.Turtle()
cobrinha.penup()
cobrinha.shape("square")
cobrinha.color("grey")
cobrinha.shapesize(0.7, 0.7)
cobrinha.speed(0)
velocidade = 0  # 18

# rabo
corpo = turtle.Turtle()
corpo.penup()
corpo.shape("square")
corpo.color("white")
corpo.shapesize(0.7, 0.7)
corpo.speed(0)
rabo = [[corpo.clone(), cobrinha.pos()]]
corpo.hideturtle()

# inchaco da cobra
inchar = corpo.clone()
inchar.hideturtle()
inchar.shapesize(1, 1)
inchar.shape("circle")

# pontuacao e recorde
caneta_pontos = caneta.clone()
caneta_pontos.goto(-170, 320)
caneta_pontos.write(len(rabo) - 1, font=("Arial", 30, "normal"))

caneta_recorde = caneta.clone()
caneta_recorde.goto(250, 320)
caneta_recorde.write("0", font=("Arial", 30, "normal"))

# comida
comida = turtle.Turtle()
comida.penup()
comida.shape("circle")
comida.color("red")
comida.shapesize(0.7, 0.7)
comida.goto(random.randint(-290, 290), random.randint(-290, 290))

variavel_da_comida = 0

# O jogo em si
mainloop()
