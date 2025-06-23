from tkinter import *
import tkintermapview
import requests
from urllib.parse import quote

# współrzędne wybranych księgarni
ksiegarnia_coords = {
    "TaniaKsiazka_Białystok": (53.1325, 23.1688),
    "Psychebook_Częstochowa": (50.8145, 19.1226),
    "BookBook_Gdańsk": (54.3520, 18.6466),
    "Bonito_Katowice": (50.2610, 19.0235),
    "BIKSA_Katowice": (50.2600, 19.0200),
    "Księgarnia_Akademicka_Katowice": (50.2649, 19.0238),
    "Massolit_Kraków": (50.0628, 19.9395),
    "Lokator_Kraków": (50.0495, 19.9494),
    "DeRevolutionibus_Kraków": (50.0620, 19.9370),
    "Bonobo_Kraków": (50.0621, 19.9363),
    "Matras_Kraków": (50.0647, 19.9450),
    "Świat_Książki_Lublin": (51.2465, 22.5684),
    "Aros_Łódź": (51.7730, 19.4560),
    "Bookszpan_Łódź": (51.7675, 19.4666),
    "AntykwariatTroszkiewiczów_Łódź": (51.7728, 19.4540),
    "Księgarnia_PWN_Łódź": (51.7592, 19.4560),
    "Dedalus_Poznań": (52.4064, 16.9252),
    "Bookarest_Poznań": (52.4065, 16.9330),
    "KsiegarniaŚwWojciecha_Poznań": (52.4096, 16.9312),
    "Matras_Poznań": (52.4089, 16.9347),
    "Empik_Poznań": (52.4091, 16.9350),
    "Księgarnia_Naukowa_Rzeszów": (50.0413, 21.9990),
    "Kulturka_Szczecin": (53.4235, 14.5485),
    "Aros_Wrocław": (51.1079, 17.0385),
    "TajneKomplety_Wrocław": (51.1090, 17.0320),
    "AmericanBookshop_Warszawa": (52.2223, 21.0129),
    "Bookoff_Warszawa": (52.2350, 21.0034),
    "CoLiber_Warszawa": (52.2410, 21.0115),
    "Empik_Warszawa": (52.2297, 21.0122),
    "Thebooks_Warszawa": (52.1218, 21.0336),
}


ksiegarnie = []
ksiegarnia_pracownicy = {}
ksiegarnia_klienci = {}

# lokalizacja punktu na mapie
class Ksiegarnia:
    def __init__(self, nazwa):
        self.nazwa = nazwa
        self.latitude, self.longitude = ksiegarnia_coords.get(self.nazwa, (52.23, 21.0))
        self.marker = map_widget.set_marker(
            self.latitude,
            self.longitude,
            text=self.nazwa.replace("_", " ")
        )