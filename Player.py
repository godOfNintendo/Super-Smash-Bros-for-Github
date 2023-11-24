import pygame
from GameObject import GameObject
import pygame, sys, datetime
import random
from pygame import mixer

#Full Class
class Player(GameObject):
  def __init__(self,x,y,width,height,image,vx,vy,speed,character):
    super().__init__(x,y,width,height,image)
    #Main Properties
    self.vx = vx
    self.vy = vy
    self.speed = speed
    self.character = character
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
    self.y -= 1
    self.hitbox = pygame.Rect(self.x,self.y,self.width,self.height)
    if self.InAir == False:
      self.vy = -1
    

  #Jump
  def jump(self):
    jumpSound = mixer.Sound("Sounds/jump.wav")
    jumpSound.play()
    self.y -= 1
    self.hitbox = pygame.Rect(self.x,self.y,self.width,self.height)
    if self.InAir == False:
      self.vy = -4

  #Attack renders
  def attack1(self):
    if self.character == "MARIO":
      self.changeImage("Assets/Characters/Mario/marioPunch.png")
      self.img_flip = pygame.transform.flip(self.img, True, False)
    if self.character == "DONKEY KONG":
      self.changeImage("Assets/Characters/DK/donkeyKongPunch.png")
      self.img_flip = pygame.transform.flip(self.img, True, False)
      self.y -= 1
    if self.character == "LINK":
      self.changeImage("Assets/Characters/Link/linkSword.png")
      self.img_flip = pygame.transform.flip(self.img, True, False)
      self.y -= 1
    if self.character == "BOTW LINK":
      self.changeImage("Assets/Characters/BOTWLink/linkSword.png")
      self.img_flip = pygame.transform.flip(self.img, True, False)
      self.y -= 1
    if self.character == "SAMUS":
      self.changeImage("Assets/Characters/Samus/samusPunch.png")
      self.img_flip = pygame.transform.flip(self.img, True, False)
      self.y -= 1
    if self.character == "YOSHI":
      self.changeImage("Assets/Characters/Yoshi/yoshiTongue.png")
      self.img_flip = pygame.transform.flip(self.img, True, False)
      self.y -= 1
    if self.character == "KIRBY":
      self.changeImage("Assets/Characters/Kirby/kirbyHammer.png")
      self.img_flip = pygame.transform.flip(self.img, True, False)
      self.y -= 1
    if self.character == "FOX":
      self.changeImage("Assets/Characters/Fox/foxKick.png")
      self.img_flip = pygame.transform.flip(self.img, True, False)
      self.y -= 1
    if self.character == "PIKACHU":
      self.changeImage("Assets/Characters/Pikachu/pikachuThunder.png")
      self.img_flip = pygame.transform.flip(self.img, True, False)
      self.y -= 1
    if self.character == "LUIGI":
      self.changeImage("Assets/Characters/Luigi/luigiPunch.png")
      self.img_flip = pygame.transform.flip(self.img, True, False)
      self.y -= 1
    if self.character == "CAPTAIN FALCON":
      self.changeImage("Assets/Characters/CaptainFalcon/captainFalconPunch.png")
      self.img_flip = pygame.transform.flip(self.img, True, False)
      self.y -= 1
    if self.character == "PEACH":
      self.changeImage("Assets/Characters/Peach/peachPunch.png")
      self.img_flip = pygame.transform.flip(self.img, True, False)
      self.y -= 1
    if self.character == "BOWSER":
      self.changeImage("Assets/Characters/Bowser/bowserClaw.png")
      self.img_flip = pygame.transform.flip(self.img, True, False)
      self.y -= 1
    if self.character == "SONIC":
      self.changeImage("Assets/Characters/Sonic/sonicPunch.png")
      self.img_flip = pygame.transform.flip(self.img, True, False)
      self.y -= 1
    if self.character == "GANON":
      self.changeImage("Assets/Characters/Ganon/ganonPunch.png")
      self.img_flip = pygame.transform.flip(self.img, True, False)
      self.y -= 1
    if self.character == "MEWTWO":
      self.changeImage("Assets/Characters/Mewtwo/mewtwoPunch.png")
      self.img_flip = pygame.transform.flip(self.img, True, False)
      self.y -= 1
    if self.character == "WARIO":
      self.changeImage("Assets/Characters/Wario/warioPunch.png")
      self.img_flip = pygame.transform.flip(self.img, True, False)
      self.y -= 1
    if self.character == "CHARIZARD":
      self.changeImage("Assets/Characters/Charizard/charizardClaw.png")
      self.img_flip = pygame.transform.flip(self.img, True, False)
      self.y -= 1
    if self.character == "DEDEDE":
      self.changeImage("Assets/Characters/Dedede/dededeHammer.png")
      self.img_flip = pygame.transform.flip(self.img, True, False)
      self.y -= 1
    if self.character == "KING K ROOL":
      self.changeImage("Assets/Characters/KRool/kRoolPunch.png")
      self.img_flip = pygame.transform.flip(self.img, True, False)
      self.y -= 1
    if self.character == "STEVE":
      self.changeImage("Assets/Characters/Steve/steveSword.png")
      self.img_flip = pygame.transform.flip(self.img, True, False)
      self.y -= 1
    if self.character == "DOOM SLAYER":
      self.changeImage("Assets/Characters/Doomslayer/doomslayerSpear.png")
      self.img_flip = pygame.transform.flip(self.img, True, False)
      self.y -= 1
    if self.character == "KRATOS":
      self.changeImage("Assets/Characters/Kratos/kratosPunch.png")
      self.img_flip = pygame.transform.flip(self.img, True, False)
      self.y -= 1
      
  def attack2(self):
    if self.character == "MARIO":
      self.changeImage("Assets/Characters/Mario/marioUpPunch.png")
      self.img_flip = pygame.transform.flip(self.img, True, False)
      self.y -= 1
      self.jump()
    if self.character == "DONKEY KONG":
      self.changeImage("Assets/Characters/DK/donkeyKongSmash.png")
      self.img_flip = pygame.transform.flip(self.img, True, False)
      self.y -= 1
    if self.character == "LINK":
      self.changeImage("Assets/Characters/Link/linkBow.png")
      self.img_flip = pygame.transform.flip(self.img, True, False)
      self.y -= 1
    if self.character == "BOTW LINK":
      self.changeImage("Assets/Characters/BOTWLink/linkBow.png")
      self.img_flip = pygame.transform.flip(self.img, True, False)
      self.y -= 1
    if self.character == "SAMUS":
      self.changeImage("Assets/Characters/Samus/samusProjectile.png")
      self.img_flip = pygame.transform.flip(self.img, True, False)
      self.y -= 1
    if self.character == "YOSHI":
      self.changeImage("Assets/Characters/Yoshi/yoshiPunch.png")
      self.img_flip = pygame.transform.flip(self.img, True, False)
      self.y -= 1
    if self.character == "KIRBY":
      self.changeImage("Assets/Characters/Kirby/kirbySwallow.png")
      self.img_flip = pygame.transform.flip(self.img, True, False)
      self.y -= 1
    if self.character == "FOX":
      self.changeImage("Assets/Characters/Fox/foxProjectile.png")
      self.img_flip = pygame.transform.flip(self.img, True, False)
      self.y -= 1
    if self.character == "PIKACHU":
      self.changeImage("Assets/Characters/Pikachu/pikachuLightning.png")
      self.img_flip = pygame.transform.flip(self.img, True, False)
      self.y -= 1
    if self.character == "LUIGI":
      self.changeImage("Assets/Characters/Luigi/luigiUpPunch.png")
      self.img_flip = pygame.transform.flip(self.img, True, False)
      self.y -= 1
      self.y -= 1
      self.jump()
    if self.character == "CAPTAIN FALCON":
      self.changeImage("Assets/Characters/CaptainFalcon/captainFalconKick.png")
      self.img_flip = pygame.transform.flip(self.img, True, False)
      self.y -= 1
    if self.character == "PEACH":
      self.changeImage("Assets/Characters/Peach/peachGolf.png")
      self.img_flip = pygame.transform.flip(self.img, True, False)
      self.y -= 1
    if self.character == "BOWSER":
      self.changeImage("Assets/Characters/Bowser/bowserFire.png")
      self.img_flip = pygame.transform.flip(self.img, True, False)
      self.y -= 1
    if self.character == "GANON":
      self.changeImage("Assets/Characters/Ganon/ganonSword.png")
      self.img_flip = pygame.transform.flip(self.img, True, False)
      self.y -= 1
    if self.character == "SONIC":
      self.changeImage("Assets/Characters/Sonic/sonicDash.png")
      self.img_flip = pygame.transform.flip(self.img, True, False)
      self.y -= 1
    if self.character == "MEWTWO":
      self.changeImage("Assets/Characters/Mewtwo/mewtwoProjectile.png")
      self.img_flip = pygame.transform.flip(self.img, True, False)
      self.y -= 1
    if self.character == "WARIO":
      self.changeImage("Assets/Characters/Wario/warioFart.png")
      self.img_flip = pygame.transform.flip(self.img, True, False)
      self.y -= 1
    if self.character == "CHARIZARD":
      self.changeImage("Assets/Characters/Charizard/charizardFire.png")
      self.img_flip = pygame.transform.flip(self.img, True, False)
      self.y -= 1
    if self.character == "DEDEDE":
      self.changeImage("Assets/Characters/Dedede/dededeEat.png")
      self.img_flip = pygame.transform.flip(self.img, True, False)
      self.y -= 1
    if self.character == "KING K ROOL":
      self.changeImage("Assets/Characters/KRool/kRoolThrow.png")
      self.img_flip = pygame.transform.flip(self.img, True, False)
      self.y -= 1
    if self.character == "STEVE":
      self.changeImage("Assets/Characters/Steve/stevePickaxe.png")
      self.img_flip = pygame.transform.flip(self.img, True, False)
      self.y -= 1
    if self.character == "DOOM SLAYER":
      self.changeImage("Assets/Characters/Doomslayer/doomslayerProjectile.png")
      self.img_flip = pygame.transform.flip(self.img, True, False)
      self.y -= 1
    if self.character == "KRATOS":
      self.changeImage("Assets/Characters/Kratos/kratosAxe.png")
      self.img_flip = pygame.transform.flip(self.img, True, False)
      self.y -= 1

  #Sets up the character
  def characterSetup(self):
    self.y += self.vy
    self.x += self.vx
    if self.character == "MARIO":
      if self.state == "IDLE":
        self.changeImage("Assets/Characters/Mario/mario.png")
        self.img_flip = pygame.transform.flip(self.img, True, False)
      if self.state == "JUMP":
        self.changeImage("Assets/Characters/Mario/marioUpPunch.png")
        self.img_flip = pygame.transform.flip(self.img, True, False)
      if self.state == "KNOCKBACK":
        self.changeImage("Assets/Characters/Mario/marioDamage.png")

    if self.character == "DONKEY KONG":
      if self.state == "IDLE":
        self.changeImage("Assets/Characters/DK/donkeyKong.png")
        self.img_flip = pygame.transform.flip(self.img, True, False)
      if self.state == "KNOCKBACK":
        self.changeImage("Assets/Characters/DK/donkeyKongDamage.png")

    if self.character == "LINK":
      if self.state == "IDLE":
        self.changeImage("Assets/Characters/Link/link.png")
        self.img_flip = pygame.transform.flip(self.img, True, False)
      if self.state == "KNOCKBACK":
        self.changeImage("Assets/Characters/Link/linkDamage.png")

    if self.character == "BOTW LINK":
      if self.state == "IDLE":
        self.changeImage("Assets/Characters/BOTWLink/link.png")
        self.img_flip = pygame.transform.flip(self.img, True, False)
      if self.state == "KNOCKBACK":
        self.changeImage("Assets/Characters/BOTWLink/linkDamage.png")
        
    if self.character == "SAMUS":
      if self.state == "IDLE":
        self.changeImage("Assets/Characters/Samus/samus.png")
        self.img_flip = pygame.transform.flip(self.img, True, False)
      if self.state == "KNOCKBACK":
        self.changeImage("Assets/Characters/Samus/samusDamage.png")

    if self.character == "YOSHI":
      if self.state == "IDLE":
        self.changeImage("Assets/Characters/Yoshi/yoshi.png")
        self.img_flip = pygame.transform.flip(self.img, True, False)
      if self.state == "KNOCKBACK":
        self.changeImage("Assets/Characters/Yoshi/yoshiDamage.png")

    if self.character == "KIRBY":
      if self.state == "IDLE":
        self.changeImage("Assets/Characters/Kirby/kirby.png")
        self.img_flip = pygame.transform.flip(self.img, True, False)
      if self.state == "KNOCKBACK":
        self.changeImage("Assets/Characters/Kirby/kirbyDamage.png")

    if self.character == "FOX":
      if self.state == "IDLE":
        self.changeImage("Assets/Characters/Fox/fox.png")
        self.img_flip = pygame.transform.flip(self.img, True, False)
      if self.state == "KNOCKBACK":
        self.changeImage("Assets/Characters/Fox/foxDamage.png")

    if self.character == "PIKACHU":
      if self.state == "IDLE":
        self.changeImage("Assets/Characters/Pikachu/pikachu.png")
        self.img_flip = pygame.transform.flip(self.img, True, False)
      if self.state == "KNOCKBACK":
        self.changeImage("Assets/Characters/Pikachu/pikachuDamage.png")

    if self.character == "LUIGI":
      if self.state == "IDLE":
        self.changeImage("Assets/Characters/Luigi/luigi.png")
        self.img_flip = pygame.transform.flip(self.img, True, False)
      if self.state == "KNOCKBACK":
        self.changeImage("Assets/Characters/Luigi/luigiDamage.png")

    if self.character == "CAPTAIN FALCON":
      if self.state == "IDLE":
        self.changeImage("Assets/Characters/CaptainFalcon/captainFalcon.png")
        self.img_flip = pygame.transform.flip(self.img, True, False)
      if self.state == "KNOCKBACK":
        self.changeImage("Assets/Characters/CaptainFalcon/captainFalconDamage.png")

    if self.character == "PEACH":
      if self.state == "IDLE":
        self.changeImage("Assets/Characters/Peach/peach.png")
        self.img_flip = pygame.transform.flip(self.img, True, False)
      if self.state == "KNOCKBACK":
        self.changeImage("Assets/Characters/Peach/peachDamage.png")

    if self.character == "BOWSER":
      if self.state == "IDLE":
        self.changeImage("Assets/Characters/Bowser/bowser.png")
        self.img_flip = pygame.transform.flip(self.img, True, False)
      if self.state == "KNOCKBACK":
        self.changeImage("Assets/Characters/Bowser/bowserDamage.png")

    if self.character == "GANON":
      if self.state == "IDLE":
        self.changeImage("Assets/Characters/Ganon/ganon.png")
        self.img_flip = pygame.transform.flip(self.img, True, False)
      if self.state == "KNOCKBACK":
        self.changeImage("Assets/Characters/Ganon/ganonDamage.png")

    if self.character == "SONIC":
      if self.state == "IDLE":
        self.changeImage("Assets/Characters/Sonic/sonic.png")
        self.img_flip = pygame.transform.flip(self.img, True, False)
      if self.state == "KNOCKBACK":
        self.changeImage("Assets/Characters/Sonic/sonicDamage.png")
    if self.character == "MEWTWO":
      if self.state == "IDLE":
        self.changeImage("Assets/Characters/Mewtwo/mewtwo.png")
        self.img_flip = pygame.transform.flip(self.img, True, False)
      if self.state == "KNOCKBACK":
        self.changeImage("Assets/Characters/Mewtwo/mewtwoDamage.png")
    if self.character == "WARIO":
      if self.state == "IDLE":
        self.changeImage("Assets/Characters/Wario/wario.png")
        self.img_flip = pygame.transform.flip(self.img, True, False)
      if self.state == "KNOCKBACK":
        self.changeImage("Assets/Characters/Wario/warioDamage.png")
    if self.character == "CHARIZARD":
      if self.state == "IDLE":
        self.changeImage("Assets/Characters/Charizard/charizard.png")
        self.img_flip = pygame.transform.flip(self.img, True, False)
      if self.state == "KNOCKBACK":
        self.changeImage("Assets/Characters/Charizard/charizardDamage.png")
    if self.character == "DEDEDE":
      if self.state == "IDLE":
        self.changeImage("Assets/Characters/Dedede/dedede.png")
        self.img_flip = pygame.transform.flip(self.img, True, False)
      if self.state == "KNOCKBACK":
        self.changeImage("Assets/Characters/Dedede/dededeDamage.png")
    if self.character == "KING K ROOL":
      if self.state == "IDLE":
        self.changeImage("Assets/Characters/KRool/kRool.png")
        self.img_flip = pygame.transform.flip(self.img, True, False)
      if self.state == "KNOCKBACK":
        self.changeImage("Assets/Characters/KRool/kRoolDamage.png")
    if self.character == "STEVE":
      if self.state == "IDLE":
        self.changeImage("Assets/Characters/Steve/steve.png")
        self.img_flip = pygame.transform.flip(self.img, True, False)
      if self.state == "KNOCKBACK":
        self.changeImage("Assets/Characters/Steve/steveDamage.png")
    if self.character == "DOOM SLAYER":
      if self.state == "IDLE":
        self.changeImage("Assets/Characters/Doomslayer/doomslayer.png")
        self.img_flip = pygame.transform.flip(self.img, True, False)
      if self.state == "KNOCKBACK":
        self.changeImage("Assets/Characters/Doomslayer/doomslayerDamage.png")
    if self.character == "KRATOS":
      if self.state == "IDLE":
        self.changeImage("Assets/Characters/Kratos/kratos.png")
        self.img_flip = pygame.transform.flip(self.img, True, False)
      if self.state == "KNOCKBACK":
        self.changeImage("Assets/Characters/Kratos/kratosDamage.png")
        
    if self.state == "ATTACK1":
      self.attack1()
    if self.state == "ATTACK2":
      self.attack2()
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

  def gravity2(self,ground,ground2,gravity,screenDisplay):
     collide_platform = False
     self.gravity(ground)
     collide_platform = True in self.collision

     if screenDisplay == 4:
       self.gravity(ground2)
       if not collide_platform:
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
    self.check_collision(player2.hitbox)
    for i in range(len(self.collision)):
      if self.collision[i] and (self.state == "ATTACK1" or self.state == "ATTACK2"):
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

  #Damaging bosses
  def damageBoss(self,boss,ground):
    self.check_collision(boss.hitbox)
    for i in range(len(self.collision)):   
      if self.collision[i] and (self.state == "ATTACK1" or self.state == "ATTACK2"):
        hitSound = mixer.Sound("Sounds/hitSound.mp3")
        hitSound.play()
        if datetime.datetime.now() > boss.stopInvulnerability:
          boss.health -= 40
          boss.state = "KNOCKBACK"
          boss.y -= 1
          boss.hitbox = pygame.Rect(boss.x,boss.y,boss.width,boss.height)
  
          boss.vy = -4
          boss.img_flip = pygame.transform.flip(boss.img, True, False)
          if(boss.facingRight == True):
  
            boss.knockback(-3)
          if(boss.facingRight == False):
  
            boss.knockback(3)
          boss.stopInvulnerability = datetime.datetime.now() + boss.invulnerableTime
      boss.check_collision(ground.hitbox)
      for i in range(len(boss.collision)):
          if boss.collision[i] and boss.state == "KNOCKBACK":
            boss.state = "IDLE"
            boss.vx = 0
  #Item
  def useItem(self, item):
    self.check_collision(item.hitbox)
    for i in range(len(self.collision)):
      if self.collision[i] and (self.state == "ATTACK1" or self.state == "ATTACK2") and item.show == True:
        powerup = mixer.Sound("Sounds/powerup.wav")
        powerup.play()
        item.show = False
        item.showTime = datetime.datetime.now() + item.hideTime
        if(item.itemType == "BURGER" and self.health <= 175):
          self.health += 25

  #CPU logic
  def cpu(self,player,ground2,ground):
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

    
      self.check_collision(ground2.hitbox)
      if self.collision[5] or self.collision[4]:
            self.jump()
  
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

    if self.x < ground.x or self.x > ground.x + ground.width:
      self.vx = -self.vx

  #Right and left movements
  def right(self):
        self.vx = self.speed
        self.facingRight = True
        self.state = "RUNNING"

  def left(self):
        self.vx = -self.speed
        self.facingRight = False
        self.state = "RUNNING"  
