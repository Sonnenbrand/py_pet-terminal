# coding=UTF-8
# Small programm that is just interactiong with minimum of functions with help of
# https://www.youtube.com/watch?v=TburgnvAPLE

import random

py_pluesch = {
    "name": "knuddeliger kleiner Plüschball",
    "bild": "..::oOo::..",
    "gewicht": 1,
    "alter": 1,
    "hunger": True,
    "sprueche": ["SchnurrSchnurrSchnurr", "PrrrrrBrrrrPrrrr", "Ich will ein Tamagotchi sein"],
}

beenden = False

# Funktion um den Status des py_pets zu sehen


def start_pet():
    print('Hallo, ich bin dein py_pet!')


def stats():
    print("Ich heiße " + py_pluesch["name"] + " und so sehe ich aus   " + py_pluesch["bild"])
    print("Ich bin " + str(py_pluesch["alter"]) + " Jahre alt und wiege " + str(py_pluesch["gewicht"]))
    if py_pluesch["hunger"]:
        print("UND ICH BIN HUNGRIG!")
    else:
        print("Und ich bin schön satt!")


start_pet()

# todo: Wenn Gewicht größer 10 Pet stirbt aber "Trainieren" macht Gewicht Weniger

while not beenden:
    print("###################################")
    user_input = input('>')
    if user_input == "Ende":
        beenden = True
    elif user_input == "Status":
        stats()
    elif user_input == "Füttern":
        py_pluesch["gewicht"] = py_pluesch["gewicht"] + 1
        py_pluesch["hunger"] = False
        print("NomNomNom! Das war lecker!")
        print("Ich wiege jetzt " + str(py_pluesch["gewicht"]))
    elif user_input == "Hallo":
        print(random.choice(py_pluesch["sprueche"]))
    elif user_input == "Schau":
        print(str(py_pluesch["bild"]))
    else:
        # Hier immer alle möglichen User Inputs ergänzen
        print("Wie bitte? Du kannst nur Status, Füttern, Hallo, Schau oder Ende nutzen!")


print("Bis zum nächsten Mal!")
