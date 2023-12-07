from elements import *

water = Water()
fire = Fire()
air = Air()
ground = Ground()

storm = water + air
print(storm.title)

lava = fire + ground
print(lava.title)

none = ground + lava
print(none)