def print_isosceles(h):

    x = 1
    while (h>0):
        print(' '*h+'*'*x)
        h = h-1
        x = x+2
    return

h = int(input('how big is triangle'))
print_isosceles(h)

#____________________________________________________________________________________

def median_of_three(a, b, c):

    if b < a < c or c < a < b:  
        return(a)
    elif a < b < c or c < b < a:
        return(b)
    elif a < c < b or b < c < a:
        return(c)

a = int(input("insert an x value")) 
b = int(input("insert a y value")) 
c = int(input("insert a z value"))

print(median_of_three(a, b, c))

#__________________________________________________________________________________

from random import randint

x = randint(1,100)

def pokestop():
    
    if (1<=x<=40):
        return("Poke Ball")
    elif(41<=x<=62):
        return("Great Ball")
    elif(63<=x<=74):
        return("Razz Berry")
    elif(75<=x<=86):
        return("Potion")
    elif(87<=x<=93):
        return("Super Potion")
    elif(94<=x<=97):
        return("Hyper Potion")
    elif(98<=x<=99):
        return("Revive")
    else:
        return("Egg")

print(pokestop())

#__________________________________________________________________________________

def point_is_in_circle(origin_x, origin_y, diameter, x, y):
  radius = diameter/2
  centerx = radius+origin_x
  centery = radius+origin_y

  if ((x-centerx)**2 + (y-centery)**2) <= radius**2:
    return True
  else:
    return False

origin_x = int(input('Where is the upper left x-coordinate?'))
origin_y = int(input('Where is the upper left y-coordinate?'))
diameter = int(input('What is the diameter of your circle?'))
x = int(input('Type a random x value'))
y = int(input('Type a random y value'))


print(point_is_in_circle(origin_x, origin_y, diameter, x, y))


