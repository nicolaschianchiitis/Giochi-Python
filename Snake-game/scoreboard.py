from turtle import Turtle

ALIGN = "center"
FONT = ("HelveticaNeue", 18, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.punti = 0
        self.record = 0
        try:
            file_record = open("./record.txt", "rt")
            self.record = int(self.reformat_record(file_record.read()))
            file_record.close()
        except FileNotFoundError:
            self.record = 0
        # Mettere prima di scrivere! Altrimenti non vedo niente con lo sfondo nero!
        self.color("white")
        # Nascondi la freccia...
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=270)
        self.aggiorna_punteggio()

    def incrementa_punti(self):
        self.punti += 1
        self.aggiorna_punteggio()

    def aggiorna_punteggio(self):
        self.clear()  # Cancella il testo scritto prima
        if self.punti > self.record:
            try:
                file_record = open("./record.txt", "wt")
                file_record.write(f"{self.punti}")
                file_record.close()
                self.record = self.punti
            except FileNotFoundError:
                pass
        self.write(arg=f"Punti: {self.punti} -------- Record: {self.record}", align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(x=0, y=0)
        self.write(arg="GAME OVER", align=ALIGN, font=FONT)
        self.salva_record()

    def salva_record(self):
        try:
            record = open("./record.txt", "rt")
            if self.punti > int(self.reformat_record(record.read())):
                record.close()
                record = open("./record.txt", "wt")
                record.write(f"{self.punti}")
                record.close()
        except FileNotFoundError:
            file = open("./record.txt", "wt")
            file.write("0")
            file.close()
            self.salva_record()

    def reformat_record(self, record_in_file):
        for ch in record_in_file:
            if ch not in "0123456789":
                record_in_file = record_in_file.replace(ch, "")
        return record_in_file

    def reset_record(self):
        self.record = 0
        try:
            file_record = open("./record.txt", "wt")
            file_record.write("0")
            file_record.close()
        except FileNotFoundError:
            pass
        self.aggiorna_punteggio()
