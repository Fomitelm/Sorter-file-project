# If is used as a conditional
import random
x = random.randint (1, 100)
if x < 33:
    print (x)
elif 33 < x < 66:
    print ("x is more than 33, but less than 66")
else:
    print(x)