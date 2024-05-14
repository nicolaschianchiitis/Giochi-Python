from turtle import Screen
from time import sleep
from snake import Snake
from food import Food
from scoreboard import Scoreboard

REFRESH_TIME_SECS = 0.1

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")

# Spegniamo il tracer (non viene mostrata l'animazione in corso)
# Il refresh automatico dell'immagine va disattivato.
# Bisogna ricreare il frame rate del gioco, ovvero dire quando
# bisogna ricalcolare l'immagine
screen.tracer(0)

serpente = Snake()
cibo = Food()
tabellone_punti = Scoreboard()

# Ridisegna l'immagine. Attenzione però! Il tracer va disattivato, altrimenti non va!
screen.update()

# Inizia ad ascoltare gli eventi riguardanti la tastiera
screen.listen()
screen.onkey(key="Up", fun=serpente.up)
screen.onkey(key="Down", fun=serpente.down)
screen.onkey(key="Left", fun=serpente.left)
screen.onkey(key="Right", fun=serpente.right)
screen.onkey(key="w", fun=serpente.up)
screen.onkey(key="s", fun=serpente.down)
screen.onkey(key="a", fun=serpente.left)
screen.onkey(key="d", fun=serpente.right)
screen.onkey(key="p", fun=tabellone_punti.reset_record)

game_is_on = True
while game_is_on:
    # Gestiamo l'animazione:
    # Refresh immagine
    screen.update()
    # Velocità di refresh (e velocità del serpente)
    sleep(REFRESH_TIME_SECS)
    # Muoviamo il serpente in avanti
    serpente.move_fwd()

    # Rileva la collisione col cibo...
    # La distanza può essere calcolata tra due oggetti
    # Turtle direttamente, altrimenti si devono passare
    # le coordinate (x;y). Vediamo se la testa del
    # serpente tocca il cibo...
    if serpente.testa.distance(cibo) < 15:
        # Posiziona il cibo in una posizione casuale
        cibo.refresh()
        # Incrementa il punteggio
        tabellone_punti.incrementa_punti()
        # Allunga il serpente di un blocchetto
        serpente.extend()

    # Controlliamo se il serpente ha toccato la parete
    if (serpente.testa.xcor() > 280 or serpente.testa.xcor() < -280
            or serpente.testa.ycor() > 280 or serpente.testa.ycor() < -280):
        tabellone_punti.game_over()
        game_is_on = False

    # Controlliamo se la testa collide col corpo
    # Facciamo lo slicing della lista, così prendiamo
    # tutto meno la testa
    # NOTA: con lo slicing posso prendere una parte, da
    # indice incluso a indice escluso (es. [2:6]);
    # dall'inizio a un certo indice escluso (es. [:6]);
    # da un indice incluso alla fine (es. [2:]); rovesciando
    # l'iterabile ([::-1]); se faccio, per esempio, [2:6:4],
    # prende da indice 2 a 6 escluso,
    for segmento in serpente.corpo[1:]:
        if serpente.testa.distance(segmento) < 10:
            game_is_on = False
            tabellone_punti.game_over()

screen.exitonclick()
