__author__ = 'Ruslan'
import winsound
import time

morse = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    ".": ".-.-.-",
    ",": "--..--"
}
dit = 150
dah = 3*dit
frequency = 700
def short():
    winsound.Beep(frequency, dit)
def long():
    winsound.Beep(frequency, dah)
def inter_element_gap():
    time.sleep(dit/1000)
def short_gap():
    time.sleep(3*dit/1000)
def medium_gap():
    time.sleep(7*dit/1000)


def morse_sound(text):
    text = text.upper()
    for letter in text:
        if letter == ' ':
            medium_gap()
        else:
            symbols = morse[letter]
            for i in range(0, len(symbols)):
                if symbols[i] == '.':
                    short()
                else:
                    long()
                if i != len(symbols)-1:
                    inter_element_gap()
            short_gap()


morse_sound('Hallo Welt')