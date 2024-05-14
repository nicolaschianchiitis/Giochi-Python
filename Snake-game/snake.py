from turtle import Turtle

# Definizione costanti
INITIAL_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
FWD_STEP = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.corpo = []
        self.crea_corpo()
        self.testa = self.corpo[0]

    def crea_corpo(self):
        for pos in INITIAL_POSITIONS:
            self.add_segment(pos)

    def move_fwd(self):
        for num_parte in range(len(self.corpo) - 1, 0, -1):
            # Compatta i quadrati (parti del corpo) e spostali dall'ultimo
            # al primo, partendo dalla coda. Poi "spingiamo" avanti la testa
            new_x = self.corpo[num_parte - 1].xcor()
            new_y = self.corpo[num_parte - 1].ycor()
            self.corpo[num_parte].goto(x=new_x, y=new_y)
        self.testa.forward(FWD_STEP)

    # Ora basta solo cambiare la direzione (heading) della testa per far muovere il serpente
    # Ricordare che self.corpo[0] è la testa del serpente!

    def up(self):
        if self.testa.heading() != DOWN:
            self.testa.setheading(UP)

    def down(self):
        if self.testa.heading() != UP:
            self.testa.setheading(DOWN)

    def left(self):
        if self.testa.heading() != RIGHT:
            self.testa.setheading(LEFT)

    def right(self):
        if self.testa.heading() != LEFT:
            self.testa.setheading(RIGHT)

    def add_segment(self, pos):
        parte_corpo = Turtle("square")
        parte_corpo.color("white")
        # Dimensioni default: 20x20
        parte_corpo.penup()
        parte_corpo.goto(pos)
        self.corpo.append(parte_corpo)

    def extend(self):
        self.add_segment(self.corpo[-1].position())
