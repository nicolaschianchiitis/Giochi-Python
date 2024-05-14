from turtle import Turtle, Screen

tim = Turtle()
tim.shape("classic")


def move_forward():
    tim.forward(10)


def move_backwards():
    tim.back(10)


def turn_right():
    tim.right(5)


def turn_left():
    tim.left(5)


def clear():
    '''
    -- Alternativa --
        # Cancella il contenuto dello schermo
        s.clearscreen()
        # Solleva la penna
        tim.penup()
        # Ritorna al centro, da dov'è partita
        tim.home()
        # Appoggia la penna per ridisegnare
        tim.pendown()
    '''
    tim.penup()
    # Ritorna al centro, da dov'è partita
    tim.home()
    # Cancella il tracciato
    tim.clear()
    tim.pendown()


s = Screen()
s.listen()
s.onkey(key="w", fun=move_forward)
s.onkey(key="s", fun=move_backwards)
s.onkey(key="a", fun=turn_left)
s.onkey(key="d", fun=turn_right)
s.onkey(key="c", fun=clear)
s.exitonclick()
