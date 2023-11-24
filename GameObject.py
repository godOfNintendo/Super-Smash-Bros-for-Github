import pygame

#Main Class
class GameObject:
  def __init__(self,x,y,width,height,image):
    self.x = x
    self.y = y
    self.width = width
    self.height = height
    self.img = pygame.image.load(image)
    self.img = pygame.transform.scale(self.img,(width,height))

    #Hitbox
    self.InAir = True
    self.collision = [False] * 9
    self.hitbox = pygame.Rect(self.x,self.y,self.width,self.height)
    self.img_flip = pygame.transform.flip(self.img, True, False)

  #Draw
  def draw(self,screen):
    screen.blit(self.img,(self.x,self.y))

  #Flip image
  def drawFlip(self,screen):
    screen.blit(self.img_flip,(self.x,self.y))

  #Changes an image
  def changeImage(self,image):
    self.img = pygame.image.load(image)
    self.img = pygame.transform.scale(self.img,(self.width,self.height))

  #Collision detection
  def check_collision(self, rect):
    self.collision[0] = rect.collidepoint(self.hitbox.topleft)
    self.collision[1] = rect.collidepoint(self.hitbox.topright)
    self.collision[2] = rect.collidepoint(self.hitbox.bottomleft)
    self.collision[3] = rect.collidepoint(self.hitbox.bottomright)
    self.collision[4] = rect.collidepoint(self.hitbox.midleft)
    self.collision[5] = rect.collidepoint(self.hitbox.midright)
    self.collision[6] = rect.collidepoint(self.hitbox.midtop)
    self.collision[7] = rect.collidepoint(self.hitbox.midbottom)
    self.collision[8] = rect.collidepoint(self.hitbox.center)

  def changeHitbox(self):
    self.hitbox = pygame.Rect(self.x,self.y,self.width,self.height)

  #Button clicking
  def click(self):
    mouse = pygame.mouse.get_pos()
    if mouse[0] >= self.x and mouse[0] <= self.x + self.width and mouse[1] > self.y and mouse[1] < self.y + self.height:
      return True

  def selHover(self,img1,img2):
    mouse = pygame.mouse.get_pos()
    if mouse[0] >= self.x and mouse[0] <= self.x + self.width and mouse[1] > self.y and mouse[1] < self.y + self.height:
      self.img = pygame.image.load(img2)
      self.img = pygame.transform.scale(self.img,(self.width,self.height))
    else:
      self.img = pygame.image.load(img1)
      self.img = pygame.transform.scale(self.img,(self.width,self.height))
