import pygame
from pygame import mixer
from GameObject import GameObject

#Class
class CharacterSelect(GameObject):
  def __init__(self,x,y,width,height,image,character,show):
    super().__init__(x,y,width,height,image)
    self.character = character
    self.show = show

  #Hover
  def selHover(self,img1,img2):
    mouse = pygame.mouse.get_pos()
    if mouse[0] >= self.x and mouse[0] <= self.x + self.width and mouse[1] > self.y and mouse[1] < self.y + self.height:
      self.img = pygame.image.load(img2)
      self.img = pygame.transform.scale(self.img,(self.width,self.height))
    else:
      self.img = pygame.image.load(img1)
      self.img = pygame.transform.scale(self.img,(self.width,self.height))

  #Click
  def selClick(self):
    mouse = pygame.mouse.get_pos()
    if mouse[0] >= self.x and mouse[0] <= self.x + self.width and mouse[1] > self.y and mouse[1] < self.y + self.height:
      return True

  #Sets up the character
  def chooseCharacter(self,player):
    player.character = self.character
    player.speed = 6
    player.frames.clear()
    if player.character == "MARIO":
          player.addFrames("Assets/Characters/Mario/mario.png")
          player.addFrames("Assets/Characters/Mario/marioRun.png")
          player.addFrames("Assets/Characters/Mario/mario.png")
          player.addFrames("Assets/Characters/Mario/marioRun2.png")
          player.width = 70
          player.height = 90
          player.speed = 5
    if player.character == "DONKEY KONG":
          player.addFrames("Assets/Characters/DK/donkeyKong.png")
          player.addFrames("Assets/Characters/DK/donkeyKongRunning.png")
          player.addFrames("Assets/Characters/DK/donkeyKong.png")
          player.addFrames("Assets/Characters/DK/donkeyKongRunning.png")
          player.width = 125
          player.height = 118
          player.speed = 4
    if player.character == "LINK":
          player.addFrames("Assets/Characters/Link/link.png")
          player.addFrames("Assets/Characters/Link/linkWalk.png")
          player.addFrames("Assets/Characters/Link/link.png")
          player.addFrames("Assets/Characters/Link/linkWalk2.png")
          player.width = 70
          player.height = 98
          player.speed = 3
    if player.character == "BOTW LINK":
        player.addFrames("Assets/Characters/BOTWLink/link.png")
        player.addFrames("Assets/Characters/BOTWLink/linkWalk.png")
        player.addFrames("Assets/Characters/BOTWLink/link.png")
        player.addFrames("Assets/Characters/BOTWLink/linkWalk2.png")
        player.width = 70
        player.height = 98
        player.speed = 3
    if player.character == "SAMUS":
          player.addFrames("Assets/Characters/Samus/samus.png")
          player.addFrames("Assets/Characters/Samus/samusRun.png")
          player.addFrames("Assets/Characters/Samus/samus.png")
          player.addFrames("Assets/Characters/Samus/samusRun2.png")
          player.width = 70
          player.height = 105
          player.speed = 4
    if player.character == "YOSHI":
          player.addFrames("Assets/Characters/Yoshi/yoshi.png")
          player.addFrames("Assets/Characters/Yoshi/yoshiWalk.png")
          player.addFrames("Assets/Characters/Yoshi/yoshi.png")
          player.addFrames("Assets/Characters/Yoshi/yoshiWalk2.png")
          player.width = 110
          player.height = 100
          player.speed = 6
    if player.character == "KIRBY":
          player.addFrames("Assets/Characters/Kirby/kirby.png")
          player.addFrames("Assets/Characters/Kirby/kirbyWalk.png")
          player.addFrames("Assets/Characters/Kirby/kirby.png")
          player.addFrames("Assets/Characters/Kirby/kirbyWalk2.png")
          player.width = 60
          player.height = 60
          player.speed = 5
    if player.character == "FOX":
          player.addFrames("Assets/Characters/Fox/fox.png")
          player.addFrames("Assets/Characters/Fox/foxWalk.png")
          player.addFrames("Assets/Characters/Fox/fox.png")
          player.addFrames("Assets/Characters/Fox/foxWalk2.png")
          player.width = 50
          player.height = 90
          player.speed = 8
    if player.character == "PIKACHU":
          player.addFrames("Assets/Characters/Pikachu/pikachu.png")
          player.addFrames("Assets/Characters/Pikachu/pikachuRun.png")
          player.addFrames("Assets/Characters/Pikachu/pikachu.png")
          player.addFrames("Assets/Characters/Pikachu/pikachuRun.png")
          player.width = 67
          player.height = 60
          player.speed = 6
    if player.character == "LUIGI":
          player.addFrames("Assets/Characters/Luigi/luigi.png")
          player.addFrames("Assets/Characters/Luigi/luigiRun.png")
          player.addFrames("Assets/Characters/Luigi/luigi.png")
          player.addFrames("Assets/Characters/Luigi/luigiRun2.png")
          player.width = 70
          player.height = 98
          player.speed = 5
    if player.character == "CAPTAIN FALCON":
          player.addFrames("Assets/Characters/CaptainFalcon/captainFalcon.png")
          player.addFrames("Assets/Characters/CaptainFalcon/captainFalconRun.png")
          player.addFrames("Assets/Characters/CaptainFalcon/captainFalcon.png")
          player.addFrames("Assets/Characters/CaptainFalcon/captainFalconRun2.png")
          player.width = 57
          player.height = 112
          player.speed = 8
    if player.character == "PEACH":
          player.addFrames("Assets/Characters/Peach/peach.png")
          player.addFrames("Assets/Characters/Peach/peachWalk.png")
          player.addFrames("Assets/Characters/Peach/peach.png")
          player.addFrames("Assets/Characters/Peach/peachWalk2.png")
          player.width = 72
          player.height = 104
          player.speed = 3
    if player.character == "BOWSER":
          player.addFrames("Assets/Characters/Bowser/bowser.png")
          player.addFrames("Assets/Characters/Bowser/bowserRun.png")
          player.addFrames("Assets/Characters/Bowser/bowser.png")
          player.addFrames("Assets/Characters/Bowser/bowserRun2.png")
          player.width = 177
          player.height = 150
          player.speed = 6
    if player.character == "SONIC":
      player.addFrames("Assets/Characters/Sonic/sonicRun.png")
      player.addFrames("Assets/Characters/Sonic/sonicRun.png")
      player.addFrames("Assets/Characters/Sonic/sonicRun.png")
      player.addFrames("Assets/Characters/Sonic/sonicRun.png")
      player.width = 50
      player.height = 88
      player.speed = 10
    if player.character == "GANON":
      player.addFrames("Assets/Characters/Ganon/ganonWalk.png")
      player.addFrames("Assets/Characters/Ganon/ganon.png")
      player.addFrames("Assets/Characters/Ganon/ganonWalk2.png")
      player.addFrames("Assets/Characters/Ganon/ganon.png")
      player.width = 81
      player.height = 125
      player.speed = 3
    if player.character == "MEWTWO":
      player.addFrames("Assets/Characters/Mewtwo/mewtwoFly.png")
      player.addFrames("Assets/Characters/Mewtwo/mewtwoFly.png")
      player.addFrames("Assets/Characters/Mewtwo/mewtwoFly.png")
      player.addFrames("Assets/Characters/Mewtwo/mewtwoFly.png")
      player.width = 90
      player.height = 120
      player.speed = 8
    if player.character == "WARIO":
      player.addFrames("Assets/Characters/Wario/warioWalk.png")
      player.addFrames("Assets/Characters/Wario/wario.png")
      player.addFrames("Assets/Characters/Wario/warioWalk2.png")
      player.addFrames("Assets/Characters/Wario/wario.png")
      player.width = 65
      player.height = 92
      player.speed = 4
    if player.character == "CHARIZARD":
      player.addFrames("Assets/Characters/Charizard/charizardFly.png")
      player.addFrames("Assets/Characters/Charizard/charizard.png")
      player.addFrames("Assets/Characters/Charizard/charizardFly.png")
      player.addFrames("Assets/Characters/Charizard/charizard.png")
      player.width = 112
      player.height = 100
      player.speed = 4
    if player.character == "DEDEDE":
      player.addFrames("Assets/Characters/Dedede/dededeWalk.png")
      player.addFrames("Assets/Characters/Dedede/dedede.png")
      player.addFrames("Assets/Characters/Dedede/dededeWalk2.png")
      player.addFrames("Assets/Characters/Dedede/dedede.png")
      player.width = 110
      player.height = 110
      player.speed = 3
    if player.character == "KING K ROOL":
      player.addFrames("Assets/Characters/KRool/kRoolWalk.png")
      player.addFrames("Assets/Characters/KRool/kRool.png")
      player.addFrames("Assets/Characters/KRool/kRoolWalk2.png")
      player.addFrames("Assets/Characters/KRool/kRool.png")
      player.width = 135
      player.height = 150
      player.speed = 4
    if player.character == "STEVE":
      player.addFrames("Assets/Characters/Steve/steveWalk.png")
      player.addFrames("Assets/Characters/Steve/steve.png")
      player.addFrames("Assets/Characters/Steve/steveWalk2.png")
      player.addFrames("Assets/Characters/Steve/steve.png")
      player.width = 60
      player.height = 90
      player.speed = 3
    if player.character == "DOOM SLAYER":
      player.addFrames("Assets/Characters/Doomslayer/doomslayerWalk.png")
      player.addFrames("Assets/Characters/Doomslayer/doomslayer.png")
      player.addFrames("Assets/Characters/Doomslayer/doomslayerWalk2.png")
      player.addFrames("Assets/Characters/Doomslayer/doomslayer.png")
      player.width = 70
      player.height = 115
      player.speed = 6
    if player.character == "KRATOS":
      player.addFrames("Assets/Characters/Kratos/kratosRun.png")
      player.addFrames("Assets/Characters/Kratos/kratos.png")
      player.addFrames("Assets/Characters/Kratos/kratosRun2.png")
      player.addFrames("Assets/Characters/Kratos/kratos.png")
      player.width = 57
      player.height = 114
      player.speed = 7

  #How each characterSelect Operates
  def characterSelLogic(self,player):
          self.chooseCharacter(player)
          selectSound = mixer.Sound("Sounds/select.mp3")
          selectSound.play()

    