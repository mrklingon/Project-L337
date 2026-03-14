import time
import random
import board
from adafruit_circuitplayground import cp
from bach import *

def setperiod():
   return [24, 62, 100, 188]

def rndperiod():
   return [random.randrange(20)+10,
        random.randrange(50)+30,
        random.randrange(80)+30,
        random.randrange(150)+90]

def setcolor():
    return [(16,16,16), (64,60,7), (0, 62, 0), (36, 0, 0)]

def rndcolor():
    return [(random.randrange(100),random.randrange(20),random.randrange(20)),
            (random.randrange(20),random.randrange(20),random.randrange(100)),
            (random.randrange(20),random.randrange(100),random.randrange(20)),
            (random.randrange(50),random.randrange(40),random.randrange(30))]

words = ["doomed","hello","point","talking","god","madness","rude","technical"]
period = setperiod()
planets = ["Mercury", "Venus", "Earth", "Mars"]
pix = setcolor()

loc = [0, 0 ,0,0]
counter = [0,0,0,0]
def clearplanets(lcx):
    for i in range(10):
        cp.pixels[i] = (0,0,0)
def showplanets(lcx):

    for p in range(4):
        cp.pixels[loc[p]] = pix[p]

def mvplanet(planet):
    cp.pixels[loc[p]]=(0,0,0)
    loc[planet] = (loc[planet]+1)%10
    cp.pixels[loc[p]]=pix[p]

if cp.switch:
    quiet = True
else:
    quiet = False
locate = 2 # start at Earth
Wandering = 1
SpaceTravel = 2
State = Wandering
if not quiet: compthink(1)
swtune(1)
C3P0 = 0
R2D2 = 5
while True:
    if cp.switch:
        quiet = True
    else:
        quiet = False

    if State == Wandering:
        cp.pixels.fill((0,0,0))
        cp.pixels[C3P0] = (64,60,7)
        cp.pixels[R2D2] = (0,0,40)

        C3P0 = C3P0 + (1- random.randrange(3))
        if C3P0 > 9:
            C3P0 = 0
        if C3P0 < 0:
            C3P0 = 9

        R2D2 = R2D2 + (1- random.randrange(3))
        if R2D2 > 9:
            R2D2 = 0
        if R2D2 < 0:
            R2D2 = 9

        if R2D2 == C3P0:
            if not quiet:  cp.play_file("c3p0/rude.wav")
            if not quiet: compthink(1)
            C3P0 = C3P0+1
            if C3P0 > 9:
                C3P0 = 0
        cp.pixels.fill((0,0,0))
        cp.pixels[C3P0] = (64,60,7)
        cp.pixels[R2D2] = (0,0,40)
        time.sleep(.2)
        if random.randrange(10) > 8:
            if not quiet:  cp.play_file("c3p0/"+random.choice(words)+".wav")



    if State == SpaceTravel:
        for p in range(4):
            counter[p] = counter[p]+1
            print (str(planets[p])+":"+str(counter[p])+":"+str(loc[p]))
            if counter[p]>period[p]:
                mvplanet(p)
                counter[p]=0
            showplanets(loc)


    if cp.button_a:
        C3P0 = 0
        R2D2 = 5
        State = Wandering
        for x in range(random.randrange(20)+10):
            cp.pixels[x%10]=(random.randrange(100),random.randrange(20),random.randrange(20))
            time.sleep(.05)
        cp.pixels.fill((0,0,0))
        if not quiet:  cp.play_file("c3p0/"+random.choice(words)+".wav")

    if cp.button_b:
        State = SpaceTravel
        cp.pixels.fill((20,20,20))
        time.sleep(.2)
        cp.pixels.fill((0,0,0))
        for i in range(random.randrange(20)+10):
            time.sleep(.1)
            cp.pixels[random.randrange(10)]=(random.randrange(50),random.randrange(40),random.randrange(30))
        cp.pixels.fill((0,0,0))
        period = rndperiod()
        pix = rndcolor()
        if not quiet:  cp.play_file("c3p0/regret.wav")

    if cp.touch_A1:
        compthink(1)

