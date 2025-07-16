import requests
import keyboard
import colorama
import time
from colorama import Fore, Style

print(Fore.LIGHTRED_EX + " ▄▄▄      ▒█████   ██████   ██  ██ ▄▄▄▄      ")
print(                   "▒████▄   ▒██▒  ██▒██    ▒█▒ ██  ██ █████▄    ")
print(                   "▒██  ▀█▄ ▒██░  ██░██     ██ ████   █▌  ▀█▄  ")
print(                   "░██▄▄▄▄██▒██   ██░██     █░ ██ ██ ░██▄▄▄▄██ ")
print(                   " ▓█    ██░ ████▓▒▒███████▒░▒██  ██ ██    ██▒")
print(                   " ▒▒   ▓▒ ░ ▒░▒░▒░▒ ▒▓▒ ▒ ░ ▒▒▓  ▒  ▒▒   ▓▒ ░")
print(                   "  ▒   ▒▒ ░ ░ ▒ ▒░░ ░▒  ░ ░ ░ ▒  ▒   ▒   ▒▒ ░")
print(                   "  ░   ▒  ░ ░ ░ ▒ ░  ░  ░   ░ ░  ░   ░   ▒   ")
print(                   "      ░  ░   ░ ░       ░     ░          ░  ░")
Fore.RESET
print(f"{Fore.RED}Este programa te permite buscar los movimientos de un pokemon asi como su tipo.")
Fore.RESET

while  True:

    URL = "https://pokeapi.co/api/v2/pokemon/"

    print(Style.RESET_ALL)
    pokemon = input("Ingrese el nombre del Pokémon: ")

    respuesta = requests.get(URL + pokemon)

    datos = respuesta.json()
    print(f"---movimientos de {pokemon}---")

    for type in datos['types']:
        print("tipo: " + Fore.RED + "",type['type']['name'])
        print(Style.RESET_ALL)

    for move in datos['moves']:
        print("movimientos: " + Fore.GREEN + "",move['move']['name'])
        print(Style.RESET_ALL)
        

    
    




