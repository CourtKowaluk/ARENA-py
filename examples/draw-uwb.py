import sys
sys.path.append('../')
import time
import random
import numpy 
import arena



arena.init("oz.andrew.cmu.edu","/topic/render")

arena.start()

# Draw origin cube
rotation=(0.0,0.0,0.0,0.0)
scale=(0.1,0.1,0.1)
color=(255,0,0)
location=(0,0,0)
originCube = arena.cube(location,rotation,scale,color)
color=(0,255,0)

# Draw UWB tag locations
location=(1.079,0.789,0.071)
arena.cube(location,rotation,scale,color)
location=(1.079,0.789,0.778)
arena.cube(location,rotation,scale,color)
location=(2.674,0.789,0.071)
arena.cube(location,rotation,scale,color)
location=(2.674,0.789,0.778)
arena.cube(location,rotation,scale,color)

while True: 
  time.sleep(10)




arena.stop()

