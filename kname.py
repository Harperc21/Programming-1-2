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

  def a(self):
    """Print A using beepers"""
    self.tl()
    self.put5()
    self.tr()
    self.m()
    self.put2()
    self.m()
    self.put()
    self.tr()
    self.m()
    self.put2()
    self.m()
    self.put2()
    self.tl()
    self.tl()
    self.m()
    self.m()
    self.tl()
    self.m()
    self.put2()
    self.tl()
    self.tl()
    self.m4()
    self.tr()
    self.m()
    self.m()
    self.tl()

  def r(self):
    """Print R using beepers"""
    self.tl()
    self.put5()
    self.tr()
    self.m()
    self.put2()
    self.tr()
    self.m()
    self.put2()
    self.tr()
    self.m()
    self.put()
    self.tl()
    self.m()
    self.put()
    self.m()
    self.tl()
    self.m()
    self.put()
    self.m()
    self.m()

  def c(self):
    """Print C with beepers"""
    self.tl()
    self.put5()
    self.tr()
    self.m()
    self.put2()
    self.m()
    self.put()
    self.tr()
    self.m4()
    self.tr()
    self.put2()
    self.m()
    self.put()
    self.tl()
    self.tl()
    self.m4()

  def lm(self):
    """Print M using beepers"""
    self.tl()
    self.put5()
    self.tr()
    self.m()
    self.put2()
    self.tr()
    self.m()
    self.put2()
    self.m()
    self.put2()
    self.tl()
    self.tl()
    self.m4()
    self.tr()
    self.m()
    self.put2()
    self.tr()
    self.m()
    self.put2()
    self.m()
    self.put2()
    self.tl()
    self.m()
    self.m()

  def o(self):
    """Print O using beepers"""
    self.tl()
    self.put5()
    self.tr()
    self.m()
    self.put2()
    self.m()
    self.put2()
    self.tr()
    self.m()
    self.put2()
    self.m()
    self.put2()
    self.tr()
    self.m()
    self.put2()
    self.m()
    self.put()
    self.ta()
    self.m4()
    self.m()

  def n(self):
    """Print N using beepers"""
    self.tl()
    self.put5()
    self.tr()
    self.m()
    self.put2()
    self.m()
    self.tr()
    self.put5()
    
    

def main():
    """ Karel code goes here! """
    kt = ktools()
    kt.c()
    kt.a()
    kt.lm()
    kt.e()
    kt.r()
    kt.o()
    kt.n()
    
    pass


if __name__ == "__main__":
    run_karel_program()