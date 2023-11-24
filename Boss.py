import pygame
from GameObject import GameObject
import pygame, sys, datetime
import random
from pygame import mixer

#Full Class
class Boss(GameObject):
  def __init__(self,x,y,width,height,image,vx,vy,speed,boss):
    super().__init__(x,y,width,height,image)
    #Main Properties
    self.vx = vx
    self.vy = vy
    self.speed = speed
    self.boss = boss
    self.health = 200

    #Animations
    self.frames = []
    self.state = "IDLE"
    self.current_frame_index = 0
    self.frame_time = datetime.timedelta(milliseconds=200)
    self.next_frame_timestamp = datetime.datetime.now() + self.frame_time
    self.invulnerableTime = datetime.timedelta(milliseconds=1000)
    self.stopInvulnerability = datetime.datetime.now() + self.invulnerableTime

    #Flip
    self.facingRight = True
    self.img_flip = pygame.transform.flip(self.img, True, False)

  #Running animation
  def addFrames(self,image):
    img = pygame.image.load(image)
    img = pygame.transform.scale(img,(self.width,self.height))
    self.frames.append(img)

  #Running animation
  def update(self):
    self.img = self.frames[self.current_frame_index]
    self.img = pygame.transform.scale(self.img,(self.width,self.height))
    if self.next_frame_timestamp < datetime.datetime.now():
      self.current_frame_index += 1
      if self.current_frame_index == len(self.frames):
        self.current_frame_index = 0
      self.next_frame_timestamp = datetime.datetime.now() + self.frame_time
    self.img_flip = pygame.transform.flip(self.img, True, False)
    self.hitbox = pygame.Rect(self.x,self.y,self.width,self.height)

    if self.boss == "PETEY PIRANHA" or self.boss == "RIDLEY":
      self.y -= 1
      self.hitbox = pygame.Rect(self.x,self.y,self.width,self.height)
      if self.InAir == False:
        self.vy = -4
    if self.boss == "GIGA BOWSER":
      self.y -= 1
      self.hitbox = pygame.Rect(self.x,self.y,self.width,self.height)
      if self.InAir == False:
        self.vy = -1
    

  #Attack renders
  def attack1(self):
    if self.boss == "PETEY PIRANHA":
      self.changeImage("Assets/Bosses/PeteyPiranha/peteyPiranhaBite.png")
      self.img_flip = pygame.transform.flip(self.img, True, False)
    if self.boss == "RIDLEY":
      self.changeImage("Assets/Bosses/Ridley/ridleyClaw.png")
      self.img_flip = pygame.transform.flip(self.img, True, False)
    if self.boss == "GIGA BOWSER":
      self.changeImage("Assets/Bosses/GigaBowser/gigaBowserPunch.png")
      self.img_flip = pygame.transform.flip(self.img, True, False)
    if self.boss == "MASTER HAND":
      self.changeImage("Assets/Bosses/MasterHand/masterHandPunch.png")
      self.img_flip = pygame.transform.flip(self.img, True, False)

  #Sets up the boss
  def bossSetup(self):
    self.y += self.vy
    self.x += self.vx
    if self.boss == "PETEY PIRANHA":
      if self.state == "IDLE":
        self.changeImage("Assets/Bosses/PeteyPiranha/peteyPiranha.png")
        self.img_flip = pygame.transform.flip(self.img, True, False)
    if self.boss == "RIDLEY":
      if self.state == "IDLE":
        self.changeImage("Assets/Bosses/Ridley/ridley.png")
        self.img_flip = pygame.transform.flip(self.img, True, False)
    if self.boss == "GIGA BOWSER":
      if self.state == "IDLE":
        self.changeImage("Assets/Bosses/GigaBowser/gigaBowser.png")
        self.img_flip = pygame.transform.flip(self.img, True, False)
    if self.boss == "MASTER HAND":
      if self.state == "IDLE":
        self.changeImage("Assets/Bosses/MasterHand/masterHand.png")
        self.img_flip = pygame.transform.flip(self.img, True, False)
    if self.state == "ATTACK1":
      self.attack1()
    if self.state == "RUNNING" and self.state != "JUMP":
      self.update()
    
  #Gravity
  def gravity(self,ground):
      self.check_collision(ground.hitbox)
      if self.collision[7]:
          self.vy = 0
          self.InAir = False
          self.y = ground.y - self.height
      elif self.collision[6]:
          self.y += 2
  
      if self.collision[4]:
          self.x += self.speed
      if self.collision[5]:
          self.x -= self.speed
      if self.collision[6]:
          self.vy = 0

  #Gravity part 2
  def gravity2(self,ground,gravity,screenDisplay):
     collide_platform = False
     self.gravity(ground)
     collide_platform = True in self.collision
  
     if collide_platform == False:
           self.InAir = True
  
     if self.InAir == True:
           self.vy = self.vy + gravity
     self.y += self.vy


  #Knockback and attack logic
  def knockback(self,speed):
    self.y -= 1
    self.hitbox = pygame.Rect(self.x,self.y,self.width,self.height)
    self.vy = -6
    self.vx = speed

  def attackLogic(self,player2,grounds):
    player2.check_collision(self.hitbox)
    for i in range(len(self.collision)):
      if player2.collision[i] and (self.state == "ATTACK1"):
        hitSound = mixer.Sound("Sounds/hitSound.mp3")
        hitSound.play()
        if datetime.datetime.now() > player2.stopInvulnerability:
          player2.health -= 10
          player2.state = "KNOCKBACK"
          
          player2.img_flip = pygame.transform.flip(player2.img, True, False)
          if(self.facingRight == True):
              player2.knockback(5)
          if(self.facingRight == False):
          
              player2.knockback(-5)

          player2.stopInvulnerability = datetime.datetime.now() + player2.invulnerableTime
          
    for ground in grounds:
      player2.check_collision(ground.hitbox)
      for i in range(len(player2.collision)):
        if player2.collision[i] and player2.state == "KNOCKBACK":
          player2.state = "IDLE"
          player2.vx = 0

  #Boss logic
  def bossLogic(self,player,ground):
    if self.state != "KNOCKBACK":
      if self.x > player.x:
        self.x -= self.speed
        self.facingRight = False
        self.img_flip = pygame.transform.flip(self.img, True, False)
        self.state = "RUNNING"
      elif self.x < player.x:
        self.x += self.speed
        self.facingRight = True
        self.img_flip = pygame.transform.flip(self.img, True, False)
        self.state = "RUNNING"
      else:
        self.state = "IDLE"
  
      attack = 1
      self.check_collision(player.hitbox)
      for i in range(len(self.collision)):
        if not(True in self.collision):
          attack = random.randint(1,3)
          
        if self.collision[i]:
          if attack == 1:
              self.state = "ATTACK1"
          if attack >= 2:
              self.state = "ATTACK2"

  #Sets up the bosses for each level during the game
  def bossFunction(self,player,ground,grounds,gravity,screen,screenDisplay):
    if self.facingRight == True:     
      self.drawFlip(screen)
    else:
      self.draw(screen)
    self.changeHitbox()
    self.bossSetup()
    self.bossLogic(player,ground)
    self.gravity2(ground,gravity,screenDisplay)
    self.attackLogic(player,grounds)
    player.damageBoss(self,ground)
    if self.y >= 500:
      self.y = -300
      self.x = 500
 
