# coding=UTF-8
# Small programm that is just interactiong with minimum of functions with help of
# https://www.youtube.com/watch?v=TburgnvAPLE
# todo das olle .idea aus Github entfernen

import random

name = "knuddeliger kleiner Plüschball"
bild = "..::oöo::.."
gewicht = 1
alter = 1
hunger = True
beenden = False
spreuche = ("SchnurrSchnurrSchnurr", "PrrrrrBrrrrPrrrr", "Ich will ein Tamagotchi sein")


# Funktion um den Status des py_pets zu sehen


def start_pet():
    print('Hallo, ich bin dein py_pet!')


def stats():
    print("Ich heiße " + name + " " + bild)
    print("Ich bin " + str(alter) + " Jahre alt und wiege " + str(gewicht))
    if hunger:
        print("UND ICH BIN HUNGRIG!")
    else:
        print("Und ich bin schön satt!")


start_pet()


while not beenden:
    print("###################################")
    user_input = input('>')
    if user_input == "Ende":
        beenden = True
    elif user_input == "Status":
        stats()
    elif user_input == "Füttern":
        gewicht = gewicht + 1
        hunger = False
        print("NomNomNom! Das war lecker!")
        print("Ich wiege jetzt " + str(gewicht))
    elif user_input == "Hallo":
        print(random.choice(spreuche))
    else:
        # Hier immer alle möglichen User Inputs ergänzen
        print("Wie bitte? Du kannst nur Status, Füttern, Hallo oder Ende nutzen!")


print("Bis zum nächsten Mal!")
