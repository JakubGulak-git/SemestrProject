from colorama import Fore
import shutil
import random
import time

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

# funkcja "witająca" użytkownika, podaje jego imię oraz ilość pieniędzy korzystając z dwóch funkcji: get_user_name i get_money_amount
def welcome():
    print(f"Cześć {get_user_name()}, twoja początkowa ilośc pieniędzy to: {get_money_amount()}$."
          f" Baw się dobrze!")

def menu():
    while True:
        try:
            chose_from_menu = int(input(f"\n Menu: \n 1. Wybór gier \n "
                                   f"2. Top 100 wygranych \n 3. Opuść kasyno \n"))
            if chose_from_menu not in [1,2,3]:
                print("Błąd: wybierz opcję 1, 2 lub 3.")
            else:
                match chose_from_menu:
                    case 1:
                        print("wybrałes gry")
                        break
                    case 2:
                        print("Top 100 wygranych:")
                        f = open("top.txt", "r")
                        print(f.read())
                        back = input("Kliknij ENTER aby wrócić do menu kasyna...")
                    case 3:
                        print("Do zobaczenia!")
        except ValueError:
            print("mega blad")


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
menu()


