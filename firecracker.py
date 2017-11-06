import threading, time
from random import randint

class Firecracker(object):
  def __init__(self, num):
    self.id = num
  
  def light_fuse(self):
    print("Firecracker", self.id, " is lit...")
    x = randint(100,300)
    x = 2 + x / 300
    time.sleep(x)
    print("Firecracker", self.id, " has exploded !!!after", str(x) , "s" )

if (__name__ == '__main__'):
  ex1 = Firecracker(1) #This was 1-5
  ex2 = Firecracker(2)
  ex3 = Firecracker(3)
  ex4 = Firecracker(4)
  ex5 = Firecracker(5)

  ex.light_fuse()
  interrupt_thread = threading.Thread(target=ex1.light_fuse)
  interrupt_thread.start()
  interrupt_thread = threading.Thread(target=ex2.light_fuse)
  interrupt_thread.start()
  interrupt_thread = threading.Thread(target=ex3.light_fuse)
  interrupt_thread.start()
  interrupt_thread = threading.Thread(target=ex4.light_fuse)
  interrupt_thread.start()
  interrupt_thread = threading.Thread(target=ex5.light_fuse)
  interrupt_thread.start()
  
  #def now_loop(self):
   # for i in range (0, 5):
      #ex = Firecracker(i)
      #v_thread = Thread.threading(
      #v_thread.(start)



 # def 
    