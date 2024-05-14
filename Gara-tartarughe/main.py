from turtle import Turtle, Screen
from random import randint

pgm_screen = Screen()
pgm_screen.setup(width=500, height=500)
# pgm_screen.bgcolor("black")
pgm_screen.bgpic("./assets/img/pista.png")
prompt = "Which turtle will win the race? Enter a color: "
user_bet = pgm_screen.textinput(title="Make your bet", prompt=prompt)

turtles_colors = ["blue", "green", "yellow", "orange", "red", "purple", "brown"]
y_coords = [220, 140, 65, 0, -70, -140, -210]
all_turtles = []

for turtle_index in range(len(turtles_colors)):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(turtles_colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_coords[turtle_index])
    all_turtles.append(new_turtle)

is_race_on = False
# Se l'utente ha fatto la scommessa
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            # Colore tartaruga
            winning_color = turtle.pencolor()
            if user_bet == winning_color:
                print("You've won! =)")
                break
            else:
                print("You've lost... =(")
                break
        turtle.forward(randint(0, 10))

pgm_screen.exitonclick()
