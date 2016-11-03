#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys, random, time
lines = open('workfile.txt').read().splitlines()
start_time = 0
capital = ""

def welcome():
    print("""
         __      __  ___   _       ___    ___    __  __   ___
         \ \    / / | __| | |     / __|  / _ \  |  \/  | | __|
          \ \/\/ /  | _|  | |__  | (__  | (_) | | |\/| | | _|
           \_/\_/   |___| |____|  \___|  \___/  |_|  |_| |___|
    """)
    print("""
                    ________________________
                    |  __________))_________|
                    | | / /      ||
                    | |/ /       ||
                    | | /        ||.''''.
                    | |/         |/  _   )
                    | |          ||  `/,)
                    | |          (  `_.'
                    | |         .-`--'.
                    | |         Y . . Y
                    | |         ||   ||
                    | |         || . ||
                    | |         ||   ||
                    | |          || ||
                    | |          || ||
                    | |          || ||
                    | |          || ||
                    | |        (| | | |)
                    ---------|           |---------
                    ---------|           |---------
    """)
    print("""
      _    _              _   _    _____   __  __              _   _
     | |  | |     /\     | \ | |  / ____| |  \/  |     /\     | \ | |
     | |__| |    /  \    |  \| | | |  __  | \  / |    /  \    |  \| |
     |  __  |   / /\ \   | . ` | | | |_ | | |\/| |   / /\ \   | . ` |
     | |  | |  / ____ \  | |\  | | |__| | | |  | |  / ____ \  | |\  |
     |_|  |_| /_/    \_\ |_| \_|  \_____| |_|  |_| /_/    \_\ |_| \_|

    """)

def start():
    name = input("Jak się nazywasz? ")
    print("Cześć", (name), ", czas na grę w wisielca! \n")
    print ("Rozpoczynamy zgadywanie stolicy:")

def guessing():
    list_of_input = []
    global capital
    capital = random.choice(lines)
    capital = capital.upper()
    guesses = ''
    step = 0
    turns = 5
    start_time = time.time()
    while turns > 0:
        failed = 0
        for char in capital:
            if char in guesses:
                print(char.upper() + " ", end='')
            else:
                print("_ ", end='')
                failed += 1
        print("\n")
        if failed == 0:
            time_guess=(time.time() - start_time)
            time_guess=round(time_guess)
            print("\n\nWYGRAŁEŚ!!! \nZgadłeś po", step, "literach. Zajęło Ci to", time_guess, "sekund\n")
            win()
        print("Litery, których nie było w słowie: {}".format(list_of_input))
        guess = input("Zgadnij literkę: ")
        guess = guess.upper()
        while guess in list_of_input:
            guess = input("Literka już była , podaj inną: ")

        step += 1
        if len(guess) > 1:
            turns += 1
        else:
            guesses += guess
        if guess not in capital:
            if len(guess) > 1:
                pass
            else:
                list_of_input.append(guess)
            turns -= 1
            print("Ni mo jej!!")
            print("Zostało Ci", (turns), "prób")
        if turns == 0:
            time_guess=(time.time() - start_time)
            time_guess=round(time_guess)
            print("\nTwój czas : {} sekund ale żeś PRZEGRAŁ!!!".format(time_guess))
            lose()
            capital = random.choice(lines)

def win():
    time.sleep(1)
    z = input(str("Czy chcesz zagrać ponownie(y/n)? "))
    if z == 'y' or z == 'Y':
        guessing()
    elif z == 'n' or z == 'N':
        sys.exit()

def lose():
    print("\nTa stolica to: {}\n".format(capital))
    time.sleep(1)
    z = input(str("Czy chcesz zagrać ponownie(y/n)? "))
    if z == 'y' or z == 'Y':
        guessing()
    elif z == 'n' or z == 'N':
        sys.exit()

def timee():
    start_time = time.time()

def main():
    welcome()
    start()
    guessing()

if __name__ == '__main__':
    main()
