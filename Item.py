import pygame, sys, datetime

from GameObject import GameObject

#Main class
class Item(GameObject):
  def __init__(self,x,y,width,height,image,itemType):
    #Properties
    super().__init__(x,y,width,height,image)
    self.hideTime = datetime.timedelta(seconds=15)
    self.showTime = datetime.datetime.now() + self.hideTime
    self.show = False
    self.itemType = itemType

  #Shows and Hides items
  def itemLogic(self,screen):
    if datetime.datetime.now() > self.showTime:
      self.show = True
    if self.show == True:
      self.draw(screen)