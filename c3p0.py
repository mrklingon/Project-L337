from microbit import *
import speech
import random
import music

c3po = [   "We're doomed!",
   "This is all your fault.",
   "This is madness!",
   "And I am C-3PO, human-cyborg relations.",
   "Sir, the possibility of successare approximately 3,720 to 1.",
   "I can assure you they will never get me onto one of those dreadful starships.",
   "In the event I don't make it back, I want you to know you've been a real friend, R2.",
   "I beg your pardon, but what do you mean, `naked?' My parts are showing?",
   "I am not sure this floor is entirely stable.",
   "Oh my goodness! Shut me down. Machines building machines. How   perverse.",
   "I'm programmed for etiquette, not destruction!",
   "Listen to them! They're dying, R2! Curse my metal body!"
   "Help! I think I'm melting! This is all your fault!",
   "You must repair him!",
   "Sir, if any of my circuits or gears will help,I'll donate them.",
   "No, I don't think he likes you at all. No, I don't like you either.",
   "We seem to be made to suffer. It's our lot in life.",
   "He made a fair move. Screaming about it can't help you.",
   "That malfunctioning little twerp, this is all his fault.",
   "You watch your language!",
   "My joints are freezing up.",
   "I thought that hairy beast would be the end of me.",
   "Just open the door, you stupid lug!",
   "Stop, please! I am not ready to die!",
   "It's against my programming to impersonate a deity.",
   "This isn't the afterlife, is it? Are droids allowed here?",
   "You didn't say my name, sir, but I'm all right.",
   "Will this agony ever end?",
   "For a mechanic, you seem to do an incessant amount of thinking.",
   "Don't call me a mindless philosopher, you overweight glob of grease.",
   "Don't worry about Master Luke. I'm sure he'll be all right. ",
   "Sir, I don't know where your ship learned to communicate",
   " your ship has   the most peculiar dialect.",
   "I do believe they think I am some sort of god.",
   "`Exciting' is hardly the word I would choose." ]

def cwsay():
    display.show(Image.HEART)
    word = random.randrange(len(c3po))
    speech.say(c3po[word])
    display.scroll(c3po[word],75,wait=False,loop=True)


def csay():
    display.show(Image.HEART_SMALL)
    word = random.randrange(len(c3po))
    speech.say(c3po[word])
    display.show(Image.HEART,clear=True)



First = True

while True:
    if (accelerometer.was_gesture('shake')):
        music.play(music.POWER_UP)

    if (accelerometer.was_gesture('left')):
        pin1.write_digital(1)

    if (accelerometer.was_gesture('right')):
        pin1.write_digital(0)

    if (First):
        music.play(music.POWER_UP)
        First = False

    if button_a.is_pressed():
        csay()

    if button_b.is_pressed():
        cwsay()
