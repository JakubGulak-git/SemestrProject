from typing import final

from colorama import Fore
import shutil
import random
import time

roulette_numbers = list(range(1,37))
red_numbers = {1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36}
black_numbers = [2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35]
green_number = {0}

width = shutil.get_terminal_size().columns # znajduje szerokosc okna
print(Fore.RED + "💲💲💲 Witamy w Kasynie 💲💲💲".center(width*2))

# funkcja która pobiera imię i sprawdza czy jest poprawne
def get_user_name():
    while True:
        user_name1 = input(Fore.RESET + "Podaj swoję imię: ")
        if user_name1.isalpha() and user_name1[0].isupper(): #sprawdza czy zmienna ma litery i czy zaczyna sie z dużej
            return user_name1
        print("Błąd, imię nie może zawierać cyfr lub znaków specjalnych. Pierwsza litera powinna być drukowana :D")

# funkcja losująca początkowa ilość pieniędzy
def get_money_amount():
    return random.randint(100,1000)

actuall_money = get_money_amount()
# funkcja "witająca" użytkownika, podaje jego imię oraz ilość pieniędzy korzystając z dwóch funkcji: get_user_name i get_money_amount
def welcome():
    print(f"Cześć {get_user_name()}, twoja początkowa ilośc pieniędzy to: {actuall_money}$."
          f" Baw się dobrze!")

def menu():
    while True:
        try:
            chose_from_menu = int(input(f"Menu: \n 1. Wybór gier \n "
                                   f"2. Top 100 wygranych \n 3. Opuść kasyno \n"))
            if chose_from_menu in [1,2,3]:
                match chose_from_menu:
                    case 1:
                        print("Wybrałeś wybór gier.")
                        chose_game_place()
                        break
                    case 2:
                        print("Top 100 wygranych:")
                        f = open("top.txt", "r")
                        print(f.read())
                        input("Kliknij ENTER aby wrócić do menu kasyna...")
                    case 3:
                        print("Do zobaczenia!")
                        exit()
            else:
                print("Błąd: wybierz opcję 1, 2 lub 3.")
        except ValueError:
            print("Błąd: wybierz opcję 1, 2 lub 3.")

def roulette(rn):
    x = input("CO chcesz obstawic? 1. czarne 2. czerwone 3. zielone")
    if x == "1":
        x = "czarny"
    if x == "2":
        x = "czerwony"
    if x == "3":
        x = "zielony"

    print("Rozpoczynam kręcenie ruletki...")
    time.sleep(2)
    for i in range(36):
        print(final_number := random.choice(rn))
        time.sleep(0.1)
    color = ""
    if final_number in red_numbers:
        color = "czerwony"
    if final_number in black_numbers:
        color = "czarny"
    if final_number in green_number:
        color = "zielony"
    print(f"Wylosowana liczba to: {final_number}, kolor: {color}")
    if color == x:
        print("Wygrałeś")
    else:
        print("Przegrałeś")


def chose_game_place():
    while True:
        try:
            game_place = int(input(f"Wybierz stanowisko do gry: \n 1. Blackjack \n "
                           f"2. Jednoręki bandyta \n 3. Ruletka \n 4. Powrót \n"))
            if game_place in [1,2,3,4]:
                break
            else:
                print("Błąd: wybierz opcję 1, 2, 3 lub 4.")
        except ValueError:
            print("Błąd: wybierz opcję 1, 2, 3 lub 4.")


    match game_place:
        case 1:
            print("Wybrałeś blackjack'a.")
        case 2:
            print("Wybrałeś jednorękiego bandytę.")
            # 💲 💎 💩
        case 3:
            print("Wybrałeś ruletkę.")
            print(f"Aktualna ilość pieniędzy: {actuall_money} $")
            roulette(roulette_numbers)
        case 4:
            menu()




welcome()
time.sleep(1)
menu()




