import random
import string

import requests

WORD_SITE = "https://random-word-api.herokuapp.com/word?number=10&swear=0"

MAX_TRIES = 0

Option_length = 0

HANGMAN_PICS = ['hanged_man_art.txt','not_hanged_man.txt']

WIN = False

def choose_word():

    response = requests.get(WORD_SITE)
    WORDS = response.content.decode("utf-8").lstrip("[").rstrip("]").replace('"',"").split(",")

    word = random.choice(WORDS)

    return word

def start():

    global MAX_TRIES, Option_length

    GAME_MODE = int(input("Choose game mode: (1) Easy, (2) Medium, (3) Hard: "))

    MAX_TRIES = 0

    Option_length = 0

    if GAME_MODE == 1:
        MAX_TRIES = 10
        Option_length = 12

    if GAME_MODE == 2:
        MAX_TRIES = 5
        Option_length = 7

    if GAME_MODE == 3:
        MAX_TRIES = 3
        Option_length = 5



def win(hangword):
    print("You win!")
    print("The word was: " + hangword)
    
    with open(HANGMAN_PICS[1], "r") as f:
        print(f.read())

def ded(hangword,tries):
    print("You lose!")
    print("The word was: " + hangword)
    
    with open(HANGMAN_PICS[0], "r") as h:
        print(h.read())
    
    print(f"You had {tries} chances to save him , but idk why the person u hanged seems happy wierd")

def gib_options(length, answer):
    options_total = list(string.ascii_lowercase)

    options = set(random.sample(options_total, length))
    options.add(answer)
    return options


while True:

    start()
    # print(MAX_TRIES)
    hangword = choose_word()

    print("\n" * 10)
    print("Welcome to Hangman!")
    print("\n" * 2)
    print("Hangman is a game of guessing letters in a word. The word is hidden from you, but you have to guess the letters one by one.\n")
    print("You have " + str(MAX_TRIES) + " tries to guess the word.\n")

    print("The word is: " + "_ " * len(hangword))

    # print(hangword)

    # guessed_letters = []

    GUESSED_WORD = ""

    number = 0

    for i in hangword:
        
        WIN = False
        
        number += 1
        
        options = gib_options(Option_length, i)

        for j in range(MAX_TRIES):
            
            guessed_letter = input(f"Guess the letter no.{number}\noptions are : {options} : ")

            if guessed_letter == i:
                GUESSED_WORD.join(guessed_letter)
                print("aha! u guessed the letter lol")
                
                break
            else:
                tries_left = (MAX_TRIES - j) - 1
                if tries_left == 0:
                    ded(hangword, MAX_TRIES)
                    WIN = False
                    exit()
                print(f"nope , u have {tries_left} tries")
            
        WIN = True

    if WIN == True:
        win(hangword)            
        
        # exit()
    

    # guess = input(f"Guess letter number {no}: ")
    # if guess == "":
    #     print("You can't leave the field empty!")
    #     continue

    