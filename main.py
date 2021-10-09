from gpiozero import LEDBoard
from time import sleep
from signal import pause

# Define variables
lights = LEDBoard(20, 21)  # R, G
red = lights[0]
green = lights[1]


def main():
    show_welcome()


def show_welcome():
    print("Welcome to Trivia Pi!")

    for x in range(5):
        red.on()
        sleep(.5)
        red.off()
        green.on()
        sleep(.5)
        green.off()

# TODO: fetch() questions Function
# TODO: ask() get user answer
# TODO: answer() with validation
# TODO: is_right_answer() to return if
# TODO: show_right_alert() and show_wrong_alert()
#       take true or false, then show the alert in the terminal and LEDs


if __name__ == '__main__':
    main()

pause()
