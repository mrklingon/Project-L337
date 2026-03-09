from microbit import *
import speech
import random

consts = [ "Camelopardalis", "Ursa Minor", "Lyra",
           "Piscis Austrinus", "Sagittarius", "Auriga",
           "Leo Minor", "Capricornus", "Bootes",
           "Coma Berenices", "Aquila", "Cassiopeia",
           "Cepheus", "Delphinus", "Cancer", "Cygnus",
           "Crater", "Corvus"]

#constellation Camelopardalis
star1 = Image(
    "10000:"
    "00000:"
    "01010:"
    "01001:"
    "01000:"
)
#constellation Ursa Minor
star2 = Image(
    "00800:"
    "03000:"
    "00300:"
    "03008:"
    "00050:"
)
#constellation Lyra
star3 = Image(
    "00010:"
    "00080:"
    "20100:"
    "00000:"
    "30300:"
)
#constellation Piscis Austrinus
star4 = Image(
    "00000:"
    "03000:"
    "80000:"
    "01112:"
    "00000:"
)
#constellation Sagittarius
star5 = Image(
    "00300:"
    "04022:"
    "30000:"
    "00030:"
    "00000:"
)
#constellation Auriga
star6 = Image(
    "03080:"
    "00002:"
    "20000:"
    "00003:"
    "05000:"
)
#constellation Leo Minor
star7 = Image(
    "00000:"
    "03001:"
    "30020:"
    "02000:"
    "00000:"
)
#constellation Capricornus
star8 = Image(
    "00007:"
    "87010:"
    "00000:"
    "05003:"
    "00030:"
)
#constellation Bootes
star9 = Image(
    "03000:"
    "30040:"
    "00030:"
    "00500:"
    "00094:"
)
#constellation Coma Berenices
star10 = Image(
    "00000:"
    "03003:"
    "00000:"
    "03000:"
    "00000:"
)

#constellation Aquila
star11 = Image(
    "00303:"
    "07000:"
    "00030:"
    "02000:"
    "30001:"
)

#constellation Cassiopeia
star12 = Image(
    "20005:"
    "03300:"
    "00020:"
    "00003:"
    "00000:"
)

#constellation Cepheus
star13 = Image(
    "500000:"
    "00000:"
    "50050:"
    "00055:"
    "55000:"
)

#constellation Delphinus
star14 = Image(
    "33000:"
    "01200:"
    "00000:"
    "00030:"
    "00000:"
)
#constellation Cancer
star15 = Image(
    "003000:"
    "00000:"
    "001000:"
    "00200:"
    "10005:"
)

#constellation Cygnus
star16 = Image(
    "06001:"
    "00430:"
    "04040:"
    "30000:"
    "00004:"
)

#constellation Crater
star17 = Image(
    "10000:"
    "00100:"
    "00030:"
    "10201:"
    "00010:"
)

#constellation Corvus
star18 = Image(
    "00000:"
    "04000:"
    "00004:"
    "00000:"
    "20003:"
)



ALLCONSTS = [star1, star2, star3, star4, star5, star6,
            star7, star8, star9, star10, star11, star12,
            star13, star14, star15, star16, star17, star18]


hyper01 = Image(
    "00000:"
    "00000:"
    "00900:"
    "00000:"
    "00000:"
)
hyper02 = Image(
    "00000:"
    "09090:"
    "00300:"
    "09090:"
    "00000:"
)

hyper03 = Image(
    "90009:"
    "03030:"
    "00000:"
    "03030:"
    "90009:"
)
hyper04 = Image(
    "30003:"
    "00000:"
    "00900:"
    "00000:"
    "30003:"
)

ALLHYP = [hyper01, hyper02, hyper03, hyper04]

l337 = [
    "They don't even serve our kind here.",
    "Oh, you'll have me wiped? ",
    "You couldn't get from here to Black Spire without me. ",
    "And now you're going to make the Kessel run?",
    "Oh why? Because you're my organic Overlord?",
    "You don't want to press that button with me.",
    "I'm so glad we took this job!",
    "Do I need anything? Equal rights?",
    "Get your presumptuous ass out of my seat."  ]

display.show(star1)
display.show(ALLCONSTS)
cnst = len(ALLCONSTS)-1

while True:

    if button_a.is_pressed():
        speech.say(random.choice(l337),pitch=45)
        cnst = random.randrange(len(ALLCONSTS))
        for a in [1, 2, 3, 4]:
            display.show(ALLHYP,delay=100)
        display.show(ALLCONSTS[cnst])
        speech.say(consts[cnst],pitch=45)
        display.show(ALLCONSTS[cnst])

    if button_b.is_pressed():
        speech.say(consts[cnst],pitch=45)

    if pin1.is_touched():
        for a in [1, 2, 3, 4]:
            display.show(Image.DIAMOND)
            sleep(200)
            display.show(Image.DIAMOND_SMALL)
            sleep(200)
        display.clear()

    if  (pin2.is_touched()):
        display.scroll(consts[cnst])
        display.show(ALLCONSTS[cnst])

    if (accelerometer.was_gesture('shake')):
        display.scroll(consts[cnst])
        display.show(ALLCONSTS[cnst])