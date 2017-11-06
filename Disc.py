#Complete
import time
import threading

class Disc(object):
  def __init__(self, seq, diameter, duration, x, y):
    self.__seq = seq
    self.__diameter = diameter
    self.__duration = duration
    self.__origin_x = x
    self.__origin_y = y
    
    self.__timer = threading.Timer(duration, self.__boom)
    self.__timer.start()
    self.__start = time.clock()
    self.__end = self.__start + duration
    
    
  def __str__(self):
    return '[' + \
           'seq ' + str(self.__seq) + \
           ' diam ' + str(self.__diameter) + \
           ' dur ' + str(self.__duration) + \
           ' x ' + str(self.__origin_x) + \
           ' y ' + str(self.__origin_y) + \
           ']'
           
  def destroy(self):
    self.__end = time.clock()


  def __boom(self):
    final = self.__end - self.__start
    print ('BOOM! Disc number ' +str(self.__seq)+ ' exploded in ' +str(final)+ ' seconds!')
    