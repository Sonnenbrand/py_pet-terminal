# coding=UTF-8
# Small program that is just interacting with minimum of functions with help of
# https://www.youtube.com/watch?v=TburgnvAPLE
# todo andere py_pets zur Auswahl machen
import random
from settings_api import wetterapikey
import json
import requests
import datetime



py_pluesch = {
    "name": "knuddeliger kleiner Plüschball",
    "bild": "..::oOo::..",
    "gewicht": 1,
    "alter": 1,
    "hunger": True,
    "sprueche": ["SchnurrSchnurrSchnurr", "PrrrrrBrrrrPrrrr", "Ich will ein Tamagotchi sein"],
}
stadt = "München"
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

def tod():
    print("Ahhhhhhhhhhhhhhhhhhhhhhhhh")
    print("Dein py_pet ist tot")
    beenden = True


def wetter():
    response = requests.get("http://api.openweathermap.org/data/2.5/weather?q=" + str(stadt) + "&units=metric&APPID=" + wetterapikey)
    wetterdaten = response.json()
    # debugging - wirft JSON daten aus: print(json.dumps(wetterdaten, indent=4, sort_keys=True))
    print("Ich sage dir das Wetter für die Stadt " + str(stadt) + ".")
    print("Die Temperatur ist: {}° C".format(str(wetterdaten["main"]["temp"])))


start_pet()


# todo: Wenn Gewicht größer 10 Pet stirbt aber "Trainieren" macht Gewicht Weniger
# todo: zu viel training füht zum Tod


while not beenden:
    print("###################################")
    user_input = input('>')
    if user_input == "Ende":
        beenden = True
    elif user_input == "Status":
        stats()
    elif user_input == "Füttern":
        py_pluesch["gewicht"] = py_pluesch["gewicht"] + 1
        if py_pluesch["gewicht"] > 5:
            tod()
        else:
            py_pluesch["hunger"] = False
            print("NomNomNom! Das war lecker!")
            print("Ich wiege jetzt " + str(py_pluesch["gewicht"]))
    elif user_input == "Hallo":
        print(random.choice(py_pluesch["sprueche"]))
    elif user_input == "Schau":
        print(str(py_pluesch["bild"]))
    elif user_input == "Wetter":
        wetter()
    elif user_input == "Training":
            if py_pluesch["gewicht"] < 1:
                py_pluesch["gewicht"] = py_pluesch["gewicht"] - 1
                print("Ufff, das war anstrengend!")
                py_pluesch["hunger"] = True
            else:
                tod()
    else:
        # Hier immer alle möglichen User Inputs ergänzen
        print("Wie bitte? Du kannst nur Status, Füttern, Hallo, Training, Schau, Wetter oder Ende nutzen!")


print("Bis zum nächsten Mal!")
