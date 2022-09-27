from stanfordkarel import *


class ktools:
  def m(self):
    """Shorthand for move"""
    move()

  def tl(self):
    """Shorthand for Turn Left"""
    turn_left()

  def tr(self):
    """Shorthand for Turn Right"""
    self.tl()
    self.tl()
    self.tl()
    
  def ta(self):
    """Turn Around"""
    self.tl()
    self.tl()

  def pick(self):
    """Pick Beeper"""
    pick_beeper()

  def put(self):
    """Put Beeper"""
    put_beeper()

  def put2(self):
    """Put 2 beepers in a line"""
    self.put()
    self.m()
    self.put()

  def put5(self):
    """Put 5 beepers in a line"""
    self.put2()
    self.m()
    self.put2()
    self.m()
    self.put()

  def h(self):
    """Print H using beepers"""
    self.tl()
    self.put5()
    self.tr()  
    self.m()
    self.m()
    self.m()
    self.tr()
    self.put5()
    self.ta()
    self. m()
    self.m()
    self.tl()
    self.m()
    self.put2()
    self.tl()
    self.m()
    self.m()
    self.tl()
    self.m()
    self.m()
    self.m()
    self.m()

  def m4(self):
    """Move 4 times"""
    self.m()
    self.m()
    self.m()
    self.m()

  def m3(self):
    """Move 3 times"""
    self.m()
    self.m()
    self.m()

  def e(self):
    """Print E using beepers"""
    self.tl()
    self.put5()
    self.tr()
    self.m()
    self.put2()
    self.tr()
    self.m()
    self.m()
    self.tr()
    self.put2()
    self.m()
    self.tl()
    self.m()
    self.m()
    self.tl()
    self.m()
    self.put2()
    self.m()
    self.m()

  def l(self):
    self.tl()
    self.put5()
    self.tl()
    self.tl()
    self.m()
    self.m()
    self.m()
    self.m()
    self.tl()
    self.m()
    self.put2()
    self.m()
    self.m()


  def fic(self) -> bool:
    """Front is clear"""
    return front_is_clear()

  def fib(self) -> bool:
    """Front is block"""
    return not self.fic()

  def ric(self) -> bool:
    """Right is clear"""
    self.tr()
    if self.fic():
      self.tl()
      return True 
    self.tl()
    return False

  def rib(self) -> bool:
    """Right is blocked"""
    return not self.ric()

  def mazemove(self):
    """Maze Move"""
    if self.fib():
      self.tl()
    else:
      self.m()
      if self.ric():
        self.tr()
        self.m()
        if self.ric():
          self.tr()
          self.m()
    pass 

  def mm(self, num):
    """Move Multiple"""
    for number in range(num):
      self.m()

  def pickm(self, num):
    """Pick Multiple"""
    for i in range(num-1):
      self.pick()
      self.m()
      self.pick()

  def putm(self, num):
    """Put Multiple"""
    for i in range(num-1):
      self.put()
      self.m()
      self.put()

  def sob(self) -> bool:
    """Standing on beeper"""
    return beepers_present()

  def jump(self):
    """Jump for 510"""
    while self.fic():
      self.m()
    self.tl()
    while self.rib():
      self.m()
    self.tr()
    self.m()
    self.tr()
    while self.fic():
      self.m()
    self.tl()

  def find(self):
    """Find for 515"""
    while not facing_north():
      self.tl()
    self.m()
    if not self.sob():
      self.tl()
      self.m()
      self.tl()
      self.m()
    for _ in range(2):
      if not self.sob():
        self.m()
        self.tl()
        self.m()
    pass
    

def main():
    """ Karel code goes here! """
    kt = ktools()
    while not kt.sob():
      kt.jump()
    
    
    pass


if __name__ == "__main__":
    run_karel_program()