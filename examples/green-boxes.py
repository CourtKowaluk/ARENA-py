import sys

sys.path.append("../")
import time
import random
import arena

arena.init("oz.andrew.cmu.edu", "realm", "demo")

arena.start()

color = (0, 255, 0)

# more complex case: Create many boxes

x = 1

while True:
    # Create a bunch of green boxes drawn directly to screen
    location = (random.randrange(10)-5, random.randrange(10), -random.randrange(10))
    arena.Object(
        location=location,
        color=color,
    )
    x = x + 1
    time.sleep(0.5)
    print("object " + str(x-1) + " at " + str(location))
    arena.flush_events()

arena.stop()
