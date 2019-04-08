# Created by Olaf, TPE 2018/2019
# Hwoyee, Kaymont, Pawan balloons only

import math
import time

print "Algorithme de lancement de ballons"
print "Marque du ballon?"
m = raw_input()
print "Masse du ballon? (g)"
mb = input()
# mb = balloon mass
print "Masse de la charge? (g)"
mp = input()
# mp = payload mass
if mp > 20000:
    print "Masse de la charge trop elevee!"
print "Altitude d'eclatement desiree? (m)"
tba = input()
# tba = target burst altitude
print "Masse=", mb, "g"
print "Masse de la charge=", mp, "g"
print "Altitude d'eclatement desiree=", tba, "m"

# balloon burst diameters given by manufacturer from http://www.hwoyee.com/index.php?m=content&c=index&a=lists&catid=30

if m in ["Hwoyee","hwoyee", "HWOYEE"]:
    if mb == 100:
        # y = burst diameter
        y = 2.0
        print "Burst diameter = 2.0 m"
    elif mb == 140:
        y = 2.0
        print "Burst diameter = 2.0 m"
    elif mb == 200:
        y = 2.97
        print "Burst diameter = 2.97 m"
    elif mb == 300:
        y = 3.8
        print "Burst diameter = 4.3 m"
    elif mb == 350:
        y = 4.8
        print "Burst diameter = 4.8 m"
    elif mb == 500:
        y = 5.8
        print "Burst diameter = 5.8 m"
    elif mb == 600:
        y = 6.5
        print "Burst diameter = 6.5 m"
    elif mb == 750:
        y = 6.9
        print "Burst diameter = 6.9 m"
    elif mb == 800:
        y = 7.0
        print "Burst diameter = 7.0 m"
    elif mb == 1000:
        y = 8.0
        print "Burst diameter = 8.0 m"
    elif mb == 1200:
        y = 9.1
        print "Burst diameter = 9.1 m"
    elif mb == 1600:
        y = 10.0
        print "Burst diameter = 10.0 m"
    elif mb == 2000:
        y = 10.0
        print "Burst diameter = 10.0 m"
    elif mb == 3000:
        y = 12.0
        print "Burst diameter = 12.0 m"

if m in ["Kaymont", "kaymont", "KAYMONT"]:
    if mb == 200:
        y = 3.0
        print "Burst diameter = 3.0 m"
    elif mb == 300:
        y = 3.78
        print "Burst diameter = 3.78 m"
    elif mb == 350:
        y = 4.12
        print "Burst diameter = 4.12 m"
    elif mb == 450:
        y = 4.72
        print "Burst diameter = 4.72 m"
    elif mb == 500:
        y = 4.99
        print "Burst diameter = 4.99 m"
    elif mb == 600:
        y = 6.02
        print "Burst diameter = 6.02 m"
    elif mb == 700:
        y = 6.53
        print "Burst diameter = 6.53 m"
    elif mb == 800:
        y = 7.00
        print "Burst diameter = 7.00 m"
    elif mb == 1000:
        y = 7.86
        print "Burst diameter = 7.86 m"
    elif mb == 1200:
        y = 8.63
        print "Burst diameter = 8.63 m"
    elif mb == 1500:
        y = 9.44
        print "Burst diameter = 9.44 m"
    elif mb == 2000:
        y = 10.54
        print "Burst diameter = 10.54 m"
    elif mb == 3000:
        y = 13.0
        print "Burst diameter = 13.0 m"

if m in ["Pawan", "pawan", "PAWAN"]:
    # Pawan data from http://randomaerospace.com/Random_Aerospace/Balloons.html
    if mb == 100:
        y = 1.6
    elif mb == 350:
        y = 4.0
        print "Burst diameter = 4.0 m"
    elif mb == 600:
        y = 5.8
        print "Burst diameter = 5.8 m"
    elif mb == 800:
        y = 6.6
        print "Burst diameter = 6.6 m"
    elif mb == 900:
        y = 7.0
        print "Burst diameter = 7.0 m"
    elif mb == 1200:
        y = 8.0
        print "Burst diameter = 8.0"
    elif mb == 1600:
        y = 9.5
        print "Burst diameter = 9.5"
    elif mb == 2000:
        y = 10.2
        print "Burst diameter = 10.2"


if 600 < mb < 1200:
    cd = 0.3
else:
    cd = 0.25

# constant
adm = 7238.3
# adm = air density model (scale height) (constant)
rhoa = 1.251
# rhoa = air density (kg/m3)
rhog = 0.1786
# rhog = gas density (kg/m3)
ga = 9.80665
# ga = gravitational acceleration constant (m/s^2)

# now find the burst altitude/ascent rate

bv = (4./3)*math.pi*(y/2)**3.0
# bv = burst volume
print "Burst volume=", bv, "m3"

lv = bv*math.exp((-tba)/adm)
# lv = launch volume
print "Launch volume=", lv, "m3"

lr = ((3*lv)/(4*math.pi))**(1./3)
# lr = launch radius
print "Launch radius=", lr, "m"

# now find ascent rate from target burst altitude

la = math.pi*(lr)**2
# la = launch area

dd = rhoa-rhog
# dd = density difference

gl = lv*dd
# gl = gross lift
print "Gross lift=", gl

tm = (mp+mb)/1000
# tm = total mass

fl = (gl-tm)*ga
# fl = free lift

vr = lv/bv
# vr = volume ratio
print "volume ratio=", vr

ba = -(adm)*math.log(vr)
# ba = burst altitde
print "Burst altitude=", ba, "m"
time.sleep(0.5)

ar = (fl/(0.5*cd*la*rhoa))**(1./2)
# ar = ascent rate (m/s)
print "Ascent rate=", ar, "m/s"
time.sleep(0.5)

ttb = (ba/ar)/60
# ttb = time to burst
print "Time to burst=", ttb, "min"
time.sleep(0.5)

print "Launch volume=", lv, "m3"
