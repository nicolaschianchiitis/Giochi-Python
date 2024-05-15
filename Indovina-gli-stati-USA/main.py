import turtle, pandas

screen = turtle.Screen()
screen.setup(width=800, height=600)
# Titolo finestra
screen.title("Indovina gli stati USA")
# Immagine: cartina muta degli Stati Uniti
image = "blank_states_img.gif"

# Ottieni le coordinate x, y del click del mouse
# def get_mouse_click_coords(x, y):
#     print(x, y)

# Lettura csv con gli stati
# e memorizzazione in un
# dizionario
data = pandas.read_csv("50_states.csv")
data_dict = data.to_dict()
print(data_dict)

# Lista degli stati indovinati
# accessibile tramite indice,
# rispettando la struttura del
# dizionario
guessed_states = []
for _ in range(len(data_dict["state"])):
    guessed_states.append(False)

# Costanti
FONT = ("HelveticaNeue", 12, "normal")
ALIGN = "center"
text_pen = turtle.Turtle()
text_pen.color("black")
text_pen.penup()
text_pen.hideturtle()


def write_name_on_screen(state_item):
    name = state_item[1]
    pos = (data_dict["x"][state_item[0]], data_dict["y"][state_item[0]])
    text_pen.goto(pos)
    text_pen.write(arg=name, move=False, align=ALIGN, font=FONT)


# Aggiungi un'immagine allo schermo
screen.addshape(image)
# Impostiamo l'immagine con turtle
turtle.shape(image)

game_is_on = True

while game_is_on:
    user_guess = turtle.textinput("Indovina uno stato", "Digita il nome di uno stato USA...").strip().lower()
    for item in data_dict["state"].items():
        if item[1].lower() == user_guess and not guessed_states[item[0]]:
            guessed_states[item[0]] = True
            write_name_on_screen(item)
            break

    if False not in guessed_states:
        game_is_on = False

# Manteniamo il main aperto, è un loop infinito
# che mantiene aperta la finestra, finchè non si
# verifica un evento che scatena la chiusura.
turtle.mainloop()
