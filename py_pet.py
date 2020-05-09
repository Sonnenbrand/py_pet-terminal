# Small programm that is just interactiong with minimum of functions

name = "knuddeliger kleiner Plüschball"
bild = "..::oöo::.."
gewicht = 1
alter = 1
hunger = True

# Funktion um den Status des py_pets zu sehen
# todo Wie ruft der User die Stats auf?


def start_pet():
    print('Hallo, ich bin dein py_pet!')


def stats():
    print("Ich heiße " + name + " " + bild)
    print("Ich bin " + str(alter) + " Jahre alt und wiege " + str(gewicht))
    if hunger:
        print("UND ICH BIN HUNGRIG!")
    else:
        print("Und ich bin schön satt!")


def fuettern():
    print("nix")


start_pet()
stats()

beenden = False

while not beenden:
    print("###################################")
    user_input = input('>')
    if user_input == "Ende":
        beenden = True


print("Bis zum nächsten Mal!")
