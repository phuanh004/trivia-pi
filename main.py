import base64
from enum import Enum
from gpiozero import LEDBoard
from time import sleep
import random
from signal import pause
import requests


# Define classes
class Color(Enum):
    RED = 1
    GREEN = 2


class Answer(Enum):
    A = 'a'
    B = 'b'
    C = 'c'
    D = 'd'


# Define variables
lights = LEDBoard(20, 21)  # R, G
red = lights[0]
green = lights[1]
api_url = "https://opentdb.com/api.php?amount=10&category=18&difficulty=easy&type=multiple&encode=base64"


# Main function
def main():
    show_welcome()
    res = fetch(api_url)
    display_questions(res)


def show_welcome():
    print("Welcome to Trivia Pi!")

    for _ in range(3):
        blink(red, .1, 1)
        blink(green, .1, 1)


def blink(led, secs, times):
    """ Blink effect """
    for _ in range(times):
        led.on()
        sleep(secs)
        led.off()
        sleep(secs)


# TODO: fetch() questions Function
def fetch(url):
    return requests.get(url)


def display_questions(data):
    questions = data.json()['results']

    a = random.choice(list(Answer))
    print(a)

    # for q in questions:
    #     print(base64_to_string(q['question']))
    #     print("+ " + base64_to_string(q['correct_answer']))
    #
    #     for i_a in q['incorrect_answers']:
    #         print("+ " + base64_to_string(i_a))


# Helpers
def base64_to_string(b):
    return base64.b64decode(b).decode('utf-8')


# TODO: ask() get user answer
# TODO: answer() with validation
# TODO: is_right_answer() to return if
# TODO: show_right_alert() and show_wrong_alert()
#       take true or false, then show the alert in the terminal and LEDs


if __name__ == '__main__':
    main()

pause()
