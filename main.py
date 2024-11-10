from colorama import Fore
import shutil
import random
import time

width = shutil.get_terminal_size().columns # znajduje szerokosc okna
print(Fore.RED + "💲💲💲 Witamy w Kasynie 💲💲💲".center(width*2))

# funkcja która pobiera imię i sprawdza czy jest poprawnee
def get_user_name():
    while True:
        user_name1 = input(Fore.RESET + "Podaj swoję imię: ")
        if user_name1.isalpha() and user_name1[0].isupper(): #sprawdza czy zmienna ma litery i czy zaczyna sie z dużej
            return user_name1
        print("Błąd, imię nie może zawierać cyfr lub znaków specjalnych. Pierwsza litera powinna być drukowana :D")

# funkcja losująca początkowa ilość pieniędzy
def get_money_amount():
    return random.randint(100,1000)

# funkcja "witająca" użytkownika, podaje jego imię oraz ilość pieniędzy korzystając z dwóch funkcji: get_user_name i get_money_amount
def welcome():
    print(f"Cześć {get_user_name()}, twoja początkowa ilośc pieniędzy to: {get_money_amount()}$."
          f" Baw się dobrze!")

def chose_game_place():
    while True:
        try:
            game_place = int(input(f"\n Wybierz stanowisko do gry: \n 1. Blackjack \n "
                           f"2. Jednoręki bandyta \n 3. Ruletka \n"))
            if game_place in [1,2,3]:
                break
            else:
                print("blad")
        except ValueError:
            print("mega blad")


    match game_place:
        case 1:
            print("wybrałes blacjack")
        case 2:
            print("wybrałes bandyte")
        case 3:
            print("wybrałes ruletke")




welcome()
time.sleep(1)
chose_game_place()

