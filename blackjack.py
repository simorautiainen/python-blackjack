from cards import *
from sys import exit
import random

class game(object):
    def __init__(self):
        self.keys = list(deck_cards.keys())
        self.vihunkortit = []
        self.pelaajankortit = []
        self.summa = 0
        self.vihunsumma = 0
    def vihun_kortit(self):
        self.vihunkortit.clear()
        self.vihunsumma = 0
        for i in (0, 1):
            try:

                valinta = random.choice(self.keys)
                self.vihunkortit.append(valinta)
                self.keys.remove(valinta)
            except IndexError:
                self.keys = list(deck_cards.keys())
                vihu.vihun_kortit()
        print("\nVihulla on", self.vihunkortit[0], "ja käännetty kortti\n")

    def pelaajan_kortit(self):
        self.pelaajankortit.clear()
        self.summa = 0

        for i in (0, 1):
            try:

                valinta = random.choice(self.keys)
                self.pelaajankortit.append(valinta)
                self.keys.remove(valinta)
            except IndexError:
                self.keys = list(deck_cards.keys())
                pelaaja.pelaajan_kortit()
    def more_cards_pelaaja(self):
        try:

            valinta = random.choice(self.keys)
            self.pelaajankortit.append(valinta)
            self.keys.remove(valinta)
            print("\nOtit kortin lisää.")
            pelaaja.cards()
        except IndexError:
            self.keys = list(deck_cards.keys())
            pelaaja.more_cards_pelaaja()
    def more_cards_vihu(self):
        try:
            valinta = random.choice(self.keys)
            self.vihunkortit.append(valinta)
            self.keys.remove(valinta)
            print("\nVihu otti lisää kortteja\n")
            vihu.cards()
        except IndexError:
            self.keys = list(deck_cards.keys())
            vihu.more_cards_vihu()

    def end(self):

        print("Do you which to play again?")
        valinnainen = input("> ")
        valinta3 = valinnainen.lower()

        if valinta3 == "yes":

            start()
        elif valinta3 == "no":
            exit()
        elif valinta3 == "hack":
            print(self.keys)
            game.end()
        else:
            print("thats not valid")
            game.end()

class pelaaja(game):

    def cards(self):

        for card in self.pelaajankortit:

            print("You just got cards", card.title(),
            "which is valued as", deck_cards[card])
            pelaajan_arvot.append(deck_cards[card])


        for number in pelaajan_arvot:
            self.summa += number

        print("And if you add them together you get", self.summa, "\n\n")

        if self.summa == 21:
            print("Voitit koska sait tasan", self.summa)
            pelaaja.end()

        elif self.summa > 21 and "hertta ässä" in self.pelaajankortit:
            deck_cards["hertta ässä"] = 1;
            self.summa = 0
            pelaajan_arvot.clear()
            print("You went over 21 but one of them was ässä so it converts",
            "to 1")
            pelaaja.cards()

        elif self.summa > 21 and "pata ässä" in self.pelaajankortit:
            deck_cards["pata ässä"] = 1;
            self.summa = 0
            pelaajan_arvot.clear()
            print("You went over 21 but one of them was ässä so it converts",
            "to 1")
            pelaaja.cards()
        elif self.summa > 21 and "risti ässä" in self.pelaajankortit:
            deck_cards["risti ässä"] = 1;
            self.summa = 0
            pelaajan_arvot.clear()
            print("You went over 21 but one of them was ässä so it converts",
            "to 1")
            pelaaja.cards()
        elif self.summa > 21 and "ruutu ässä" in self.pelaajankortit:
            deck_cards["ruutu ässä"] = 1;
            self.summa = 0
            pelaajan_arvot.clear()
            print("You went over 21 but one of them was ässä so it converts",
            "to 1")
            pelaaja.cards()
        elif self.summa > 21:
            print("You lost by getting over 21 with", self.summa)
            pelaaja.end()
        else:
            pass
        print("Do you wish to get more cards? yes or no")
        valinnainen = input("> ")
        pien = valinnainen.lower()

        if pien == "yes":
            pelaajan_arvot.clear()
            self.summa = 0
            pelaaja.more_cards_pelaaja()

        elif pien == "no":
            print("\nNow its your opponents turn!")

            pelaajan_arvo.append(self.summa)
            vihu.cards()
        else:

            pelaajan_arvot.clear()
            self.summa = 0
            pelaaja.cards()

class vihu(game):

    def cards(self):

        for card in self.vihunkortit:

            print("Your enemy has", card.title(), "which is valued as",
                deck_cards[card])
            vihun_arvot.append(deck_cards[card])
        for number in vihun_arvot:
            self.vihunsumma += number

        tobias = pelaajan_arvo[-1]

        print("And theyare added together", self.vihunsumma)

        if self.vihunsumma >= tobias and self.vihunsumma >= 17\
        and self.vihunsumma <= 21:
            print("Vihu voitti koska sinulla oli", tobias, "ja vihulla oli",
                self.vihunsumma)
            vihu.end()

        elif self.vihunsumma < 17:
            vihun_arvot.clear()
            self.vihunsumma = 0
            vihu.more_cards_vihu()

        elif self.vihunsumma > 21 and "hertta ässä" in self.vihunkortit:
            deck_cards["hertta ässä"] = 1;
            self.vihunsumma = 0
            vihun_arvot.clear()
            print("You went over 21 but one of them was ässä so it converts",
            "to 1")
            vihu.cards()

        elif self.vihunsumma > 21 and "pata ässä" in self.vihunkortit:
            deck_cards["pata ässä"] = 1;
            self.vihunsumma = 0
            vihun_arvot.clear()
            print("You went over 21 but one of them was ässä so it converts",
            "to 1")
            vihu.cards()
        elif self.vihunsumma > 21 and "risti ässä" in self.vihunkortit:
            deck_cards["risti ässä"] = 1;
            self.vihunsumma = 0
            vihun_arvot.clear()
            print("You went over 21 but one of them was ässä so it converts",
            "to 1")
            vihu.cards()
        elif self.vihunsumma > 21 and "ruutu ässä" in self.vihunkortit:
            deck_cards["ruutu ässä"] = 1;
            self.vihunsumma = 0
            vihun_arvot.clear()
            print("You went over 21 but one of them was ässä so it converts",
            "to 1")
            vihu.cards()

        elif self.vihunsumma > 21:
            print("\n\nYou won with", tobias, "and enemy went over 21 coz, ",
            self.vihunsumma)

            vihu.end()
        else:
            print("Voitit koska sinulla oli", tobias, "vihulla oli",
                self.vihunsumma)

            vihu.end()

def bettaus():
    print("Welcome, tell me how much you want to bet, you start from 2k")
    try:

        valinta = int(input("> "))
    except ValueError:
        print("ERROR! Thats not a number!")
        bettaus()

    minus = money[-1] - valinta
    money.append(minus)
    valinta.append(bet)

bet = []
money = [2000]
pelaajan_arvot = []
vihun_arvot = []
pelaajan_arvo= []
game = game()
pelaaja = pelaaja()
vihu = vihu()

def start():
    print("","-" * 40, "\n\tWelcome to play blackjack!\n","-" * 40)
    vihun_arvot.clear()
    pelaajan_arvo.clear()
    pelaajan_arvot.clear()
    vihu.vihun_kortit()
    pelaaja.pelaajan_kortit()
    pelaaja.cards()

start()
