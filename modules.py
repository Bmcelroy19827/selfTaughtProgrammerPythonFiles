import math
import random
import statistics
import keyword #check keywords
import modulesChallenge as mc

print(math.pow(2,3))
print(random.randint(0,100))

# for statistics module
nums = [1,5,33,12,46,33,2]

print(statistics.mean(nums))
print(statistics.median(nums))
print(statistics.mode(nums))

print(keyword.iskeyword("for"))
print(keyword.iskeyword("football"))

#Challenges

#1
print(statistics.stdev(nums))

#2
print(mc.cube_the_number(3))

