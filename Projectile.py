import pygame, sys, datetime

from GameObject import GameObject

#Main Class
class Projectile(GameObject):
  def __init__(self,x,y,width,height,image):
    super().__init__(x,y,width,height,image)
    #properties
    self.projectileOn = False
    self.facingRight = True
    self.vx = 0

    self.frame_time = datetime.timedelta(milliseconds=10)
    self.next_frame_timestamp = datetime.datetime.now() + self.frame_time

  #Damaging players
  def projectileLogic(self,player,originalPlayer):
    self.check_collision(player.hitbox)
    for i in range(len(self.collision)):
      if self.collision[i]:
        self.projectileOn = False
        self.x = originalPlayer.x
        player.health -= 5
        break

  #Sets up the projectiles
  def setUpProjectile(self,player,player2,screen):
    if self.projectileOn == True:
      self.draw(screen)
      self.projectileLogic(player2,player)
      self.x += self.vx
      if self.facingRight == True:
        self.vx = 10
      if self.facingRight == False:
        self.vx = -10
      if self.x < 0 or self.x > 1000:
        self.x = player.x
        self.projectileOn = False
        
    if self.projectileOn == False:
      self.y = player.y + (1/2 * player.height)
      self.x = player.x
      if player.facingRight == True:
        self.facingRight = True
      if player.facingRight == False:
        self.facingRight = False

    self.changeHitbox()

    if player.state == "ATTACK2":
      if player.character == "LINK" or player.character == "BOTW LINK":
          self.projectileOn = True
          self.changeImage("Assets/Projectiles/ancientArrow.png")
          self.width = 30
          self.height = 8
      if player.character == "SAMUS":
        self.projectileOn = True
        self.changeImage("Assets/Projectiles/plasma.png")
        self.width = 70
        self.height = 70
      if player.character == "FOX":
        self.projectileOn = True
        self.changeImage("Assets/Projectiles/foxProjectile.png")
        self.width = 10
        self.height = 6
      if player.character == "MEWTWO":
        self.projectileOn = True
        self.changeImage("Assets/Projectiles/mewtwoProjectile.png")
        self.width = 50
        self.height = 50
      if player.character == "KING K ROOL":
        self.projectileOn = True
        self.changeImage("Assets/Projectiles/crown.png")
        self.width = 20
        self.height = 15
      if player.character == "DOOM SLAYER":
        self.projectileOn = True
        self.changeImage("Assets/Projectiles/doomslayerProjectile.png")
        self.width = 30
        self.height = 15
      