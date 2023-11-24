import pygame

from GameObject import GameObject

#Main class
class StageSelect(GameObject):
  def __init__(self,x,y,width,height,image,stage,music):
    #Properties
    super().__init__(x,y,width,height,image)
    self.stage = stage
    self.music = music

  #Hover
  def selHover(self,img1,img2):
    mouse = pygame.mouse.get_pos()
    if mouse[0] >= self.x and mouse[0] <= self.x + self.width and mouse[1] > self.y and mouse[1] < self.y + self.height:
      self.img = pygame.image.load(img2)
      self.img = pygame.transform.scale(self.img,(self.width,self.height))
    else:
      self.img = pygame.image.load(img1)
      self.img = pygame.transform.scale(self.img,(self.width,self.height))

  def getStage(self):
    return self.stage

  #Click
  def selClick(self):
    mouse = pygame.mouse.get_pos()
    if mouse[0] >= self.x and mouse[0] <= self.x + self.width and mouse[1] > self.y and mouse[1] < self.y + self.height:
      return True