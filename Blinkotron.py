############################################
# filename: Blinkotron.py
# author: rodgerthat
# description: main logic to control RGB LEDs
############################################

import sys
import termios
import tty

# from pynput.keyboard import Key, Listener
from RGB import RGB


class BlinkoTron:
    redIsOn = False
    greenIsOn = False
    blueIsOn = False

    frustrationCounter = 0
    button_delay = 0.2

    def __init__(self):
        pass

    def go(self):

        # instantiate new RGB LED class, one for each LED
        # pass in RGB pins as arguments to the constructor
        # in this order: Red Pin, Green Pin, Blue Pin
        led1 = RGB(11, 13, 15)  # GPIOs 17, 27, 22
        led2 = RGB(33, 35, 37)  # GPIOs 13, 19, 26
        led3 = RGB(36, 38, 40)  # GPIOs 16, 20, 21
        led4 = RGB(12, 16, 18)  # GPIOs 18, 23, 24

        # key controls
        # led1 : RGB => qwe
        # led2 : RGB => rty
        # led3 : RGB => uio
        # led4 : RGB => p[]

        while True:

            c = self.get_char()

            # LED 1

            if c == "q":
                led1.toggle_red()

            elif c == "w":
                led1.toggle_green()

            elif c == "e":
                led1.toggle_blue()

            # LED 2

            elif c == "r":
                led2.toggle_red()

            elif c == "t":
                led2.toggle_green()

            elif c == "y":
                led2.toggle_blue()

            # LED 3

            elif c == "u":
                led3.toggle_red()

            elif c == "i":
                led3.toggle_green()

            elif c == "o":
                led3.toggle_blue()

            # LED 4

            elif c == "p":
                led4.toggle_red()

            elif c == "[":
                led4.toggle_green()

            elif c == "]":
                led4.toggle_blue()

            # QUIT

            elif c == "~":
                sys.exit(0)

            else:

                if self.frustrationCounter == 5:
                    print("Press '~' to Quit")

                else:
                    print("Command Unknown")
                    self.frustrationCounter += 1

        return

    @staticmethod
    def get_char():

        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


# main program logic
def main():
    blinkotron = BlinkoTron()
    blinkotron.go()  # go


main()
