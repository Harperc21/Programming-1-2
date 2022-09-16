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

  def put4(self):
    """Put 4 beepers in a line"""
    self.put2()
    self.m()
    self.put2()

  def put3(self):
    """Put 3 beepers in a line"""
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

  def o(self):
    self.put4()
    self.tl()
    self.m()
    self.put4()
    self.tl()
    self.m()
    self.put3()
    self.tl()
    self.m()
    self.put3()
    self.m()
    
    

            
def main():
    """ Karel code goes here! """
    kt = ktools()
    kt.h()
    kt.e()
    kt.l()
    kt.l()
    kt.o()
    pass


if __name__ == "__main__":
    run_karel_program()