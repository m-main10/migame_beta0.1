import pygame
class Mimodle:
  _NOT_IMPLEMENTED_ =True
  def __init__(self,name):
      self.type="export"
      self.name=name
      self.useng=False
  def __getattr__(self,var):
      if not self.useng:
          self.useng=True
          self.wark()
      return 0

  def wark(self):
      masend=f"Error creating module {self.name}   not exist import error"
      print(masend)
  def __bool__(self):
      return  False
try:
    from  . import  images

except:
    images=Mimodle("screen")
try:
    from  . import  screen
except:

    screen=Mimodle("images")

try:
    from  . import  color
except:

    color=Mimodle("color")
