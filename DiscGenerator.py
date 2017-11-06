#Complete
from Disc import Disc
from Score import Score
from random import randint
import time

class DiscGenerator(object):
  def __init__(self, scoreobj):
    self.__scoreobj = scoreobj
    
  def go(self, count):
    discnumber = 0
    while (discnumber < count):
       window_width_start = 0
       window_width_end = 500
       window_length_start = 0
       window_length_end = 500
      
       x =  randint(0,500)
       y = randint(0,500)
  
       diameter =  100*(1-(self.__scoreobj.get_level()/20))
       noise = randint(0,300)
       noise = noise/10
       addorsub = randint(1,2)
       if addorsub == 1:
        diameter =  diameter + noise
        radius = diameter/2
       if addorsub == 2:
        diameter = diameter - noise
        radius = diameter/2
       
       while ((x + radius > window_width_end or x - radius < window_width_start) or (y + radius > window_length_end or y - radius < window_length_start)):
          x =  randint(0,500)
          y = randint(0,500)
       
          diameter =  100*(1-(self.__scoreobj.get_level()/20))
          noise = randint(0,301)
          noise = noise/10
          addorsub = randint(1,2)
          if addorsub == 1:
            diameter =  diameter + noise
            radius = diameter/2
          if addorsub == 2:
            diameter = diameter - noise
            radius = diameter/2
        
       duration = 2*(1-(self.__scoreobj.get_level()/20))
       
       disc = Disc(discnumber, diameter, duration, x, y)
       discnumber = discnumber + 1
       
       s = 2*(1 - (self.__scoreobj.get_level()/20))
       noisedelay = randint(1, 5)
       noisedelay = noisedelay/10
       plusorminus = randint(1,2)
       if plusorminus == 1:
        s = s + noisedelay
       if plusorminus == 2:
        s = s - noisedelay
            
       
       print (disc)
       time.sleep(s)
    
def prompt_main():
  time.sleep(5)
  option = -1
  while not 0 <= option <= 2:
    print('Main Menu')
    print('0 Exit Game Simulation.')
    print('1 Adjust or view the score.')
    print('2 Generate some discs.')
    try:
      option = int(input('What would you like to do? '))
    except:
      continue # don't care what was wrong...try again
  return option
    
def prompt_count():
  count = -1
  while not 0 <= count:
    try:
      count = int(input('Please enter a non-negative integer. '))
    except:
      continue # don't care what went wrong...try again
  return count

def prompt_score(score):
  option = 6
  while 1 <= option <= 6:
    print('Adjust Score Menu')
    print('0 Return to Main Menu')
    print('1 Add points')
    print('2 Subtract points')
    print('3 Increment multiplier')
    print('4 Gain life')
    print('5 Lose life')
    print('6 View score')
    try:
      option = int(input('What would you like to do? '))
    except:
      continue # don't care what went wrong...try again
  
    if option == 1: # add points
      print('How many points would you like to add?')
      score.add_points(prompt_count())
    elif option == 2: # subtract points
      print('How many points would you like to subtract?')
      score.subtract_points(prompt_count())
    elif option == 3: # increment multiplier
      score.increment_multiplier()
    elif option == 4: # gain life
      score.gain_life()
    elif option == 5:
      score.lose_life()
    elif option == 6:
      print(score)
  
if __name__ == '__main__':
  player1 = Score('Player One')
  game = DiscGenerator(player1)
  
  #Initialize choice to anything that will enter the loop
  choice = 1
  while choice != 0:
    choice = prompt_main()
    if choice == 1:
      prompt_score(player1)
    if choice == 2:
      print('How many discs would you like to generate?')
      count = prompt_count()
      game.go(count)