import base64
from enum import Enum
from gpiozero import LEDBoard
from time import sleep
import random
import requests


# Define classes
class Color(Enum):
    RED = 1
    GREEN = 2


class Answer(Enum):
    a = 0
    b = 1
    c = 2
    d = 3


# Define variables
lights = LEDBoard(20, 21)  # R, G
red = lights[0]
green = lights[1]
api_url = "https://opentdb.com/api.php?amount=10&category=18&difficulty=easy&type=multiple&encode=base64"

questions = []
answers = []
correct_answers = []  # Enum Answer


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
    res = data.json()['results']

    for i, data in enumerate(res):
        question = data['question']
        # print(random.choice(list(Answer)))
        incorrect_answers = data['incorrect_answers']
        current_incorrect_answer = 0
        correct_choice = random.choice(list(Answer))

        questions.append(question)
        correct_answers.append(correct_choice)

        answers[i][correct_choice.value] = data['correct_answer']

        for j, a in enumerate(answers[i]):
            if a == -1:
                answers[i][j] = incorrect_answers[current_incorrect_answer]
                current_incorrect_answer += 1


def fill_answer():
    for _ in range(0, 10):
        answers.append([-1, -1, -1, -1])  # a, b, c, d


# Helpers
def base64_to_string(b):
    return base64.b64decode(b).decode('utf-8')


def print_base64(b):
    print(base64_to_string(b))


def show_right_alert():
    green.blink(.1, .1, 5, True)
    print(">> You are right!")


def show_wrong_alert():
    red.blink(.5, .1, 2, True)
    print(">> Oops!")


# TODO: ask() get user answer
# TODO: answer() with validation
# TODO: is_right_answer() to return if
# TODO: show_right_alert() and show_wrong_alert()
#       take true or false, then show the alert in the terminal and LEDs


if __name__ == '__main__':
    usr_answer = ''

    fill_answer()
    main()

    for i, question in enumerate(questions):
        print("{}{}".format((i + 1), ". "), end='')
        print_base64(question)

        for j, answer in enumerate(answers[i]):
            print(Answer(j).name + ". ", end='')
            print_base64(answer)

        usr_answer = input("Enter your answer: ")

        if usr_answer.lower() == correct_answers[i].name.lower():
            show_right_alert()
        else:
            show_wrong_alert()
