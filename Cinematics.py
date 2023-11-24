import pygame, sys, datetime

from GameObject import GameObject

#Class
class Cinematics(GameObject):
  def __init__(self,x,y,width,height,image):
    #Properties
    super().__init__(x,y,width,height,image)

  #Text movement
  def theatrics(self,number):
    if self.y < number:
        self.y += 3
    else:
      return True
