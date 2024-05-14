from random import choice

punteggioLettere = {
    "a": 1,
    "b": 5,
    "c": 2,
    "d": 5,
    "e": 1,
    "f": 5,
    "g": 8,
    "h": 8,
    "i": 1,
    "j": 10,
    "k": 10,
    "l": 3,
    "m": 3,
    "n": 3,
    "o": 1,
    "p": 5,
    "q": 10,
    "r": 2,
    "s": 2,
    "t": 2,
    "u": 3,
    "v": 5,
    "w": 10,
    "x": 10,
    "y": 10,
    "z": 8
}

sacchettoLettere = []

def preparaSacchetto():
    for _ in range(14):
        sacchettoLettere.append("a")
    for _ in range(3):
        sacchettoLettere.append("b")
    for _ in range(6):
        sacchettoLettere.append("c")
    for _ in range(3):
        sacchettoLettere.append("d")
    for _ in range(11):
        sacchettoLettere.append("e")
    for _ in range(3):
        sacchettoLettere.append("f")
    for _ in range(2):
        sacchettoLettere.append("g")
    for _ in range(2):
        sacchettoLettere.append("h")
    for _ in range(12):
        sacchettoLettere.append("i")
    sacchettoLettere.append("j")
    sacchettoLettere.append("k")
    for _ in range(5):
        sacchettoLettere.append("l")
    for _ in range(5):
        sacchettoLettere.append("m")
    for _ in range(5):
        sacchettoLettere.append("n")
    for _ in range(15):
        sacchettoLettere.append("o")
    for _ in range(3):
        sacchettoLettere.append("p")
    sacchettoLettere.append("q")
    for _ in range(6):
        sacchettoLettere.append("r")
    for _ in range(6):
        sacchettoLettere.append("s")
    for _ in range(6):
        sacchettoLettere.append("t")
    for _ in range(5):
        sacchettoLettere.append("u")
    for _ in range(3):
        sacchettoLettere.append("v")
    sacchettoLettere.append("w")
    sacchettoLettere.append("x")
    sacchettoLettere.append("y")
    for _ in range(2):
        sacchettoLettere.append("z")

def punteggioScrabble(parola):
    parola = parola.lower()
    punteggio = 0
    # Togli i numeri se ci sono
    for ch in parola:
        if ch not in punteggioLettere:
            parola = parola.replace(ch, "")
    # Calcola il punteggio
    for ch in parola:
        punteggio += punteggioLettere[ch]
    return punteggio

def estraiLettere():
    lettereEstratte = []
    while len(lettereEstratte) < 8:
        lettera = choice(sacchettoLettere)
        lettereEstratte.append(lettera)
        sacchettoLettere.remove(lettera)
    return lettereEstratte

def controllaParola(parola, lettereEstratte):
    # Apertura in modalita' rt (read-text)
    fileDizionario = open("280000_parole_italiane.txt")
    # Lettura del file
    dizionarioItaliano = fileDizionario.read()
    fileDizionario.close()

    parolaComponibile = True
    for let in parola:
        if let not in lettereEstratte:
            parolaComponibile = False
            break
        lettereEstratte.remove(let)

    parolaNelDizionario = False
    if parola in dizionarioItaliano:
        parolaNelDizionario = True

    return parolaComponibile and parolaNelDizionario

def main():
    preparaSacchetto()
    lettereUscite = estraiLettere()
    print(f"Sono uscite le lettere {lettereUscite}")
    parola = input("> Forma una parola con le lettere date (non per forza tutte): ")
    if controllaParola(parola, lettereUscite):
        print(f"La parola {parola} e' valida.")
        print(f'La parola "{parola}" vale {punteggioScrabble(parola)} punti.')
    else:
        print(f"La parola {parola} NON e' valida")

main()