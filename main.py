#Screendisplays
'''
-0 is main menu
-1 is p1 character select
-2 is p2 character select
-3 is stage select
-4 is main game
-5 is p1 win
-6 is p2 win
-7 is character select for boss rush
-8 - 11 are boss levels
-12 is game over
-13 is boss rush win
-20 is the stats
'''

#imports
import pygame, sys, datetime
from pygame import mixer
import pygame, sys, datetime
from pygame.locals import (KEYDOWN, KEYUP, K_SPACE, K_RIGHT, K_LEFT, K_UP, K_o,
                           K_p, K_w, K_a, K_d, K_z, K_x,K_b)

from GameObject import GameObject
from CharacterSelect import CharacterSelect
from StageSelect import StageSelect
from Player import Player
from Item import Item
from Projectile import Projectile
from Cinematics import Cinematics
from Boss import Boss
from SaveData import SaveData

#Setup
pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((1000, 500))
pygame.display.set_caption('SUPER SMASH BROS FOR REPLIT - GRAND EDITION')
clock = pygame.time.Clock()

#Basic Variables
screenDisplay = 0
background = "NONE"
gravity = 0.25
CPU = False
switchEcho = 1
CPUWaitTime = 0

#SaveData
saveLoadManager = SaveData()

if saveLoadManager.checkForFile("games") == False:
  games = 0
else:
  games = saveLoadManager.loadData("games")
if saveLoadManager.checkForFile("bossRush") == False:
  bossRushGames = 0
else:
  bossRushGames = saveLoadManager.loadData("bossRush")
if saveLoadManager.checkForFile("player1Wins") == False:
  p1Wins = 0
else:
  p1Wins = saveLoadManager.loadData("player1Wins")
if saveLoadManager.checkForFile("player2Wins") == False:
  p2Wins = 0
else:
  p2Wins = saveLoadManager.loadData("player2Wins")
  
#Fonts
player1HealthFont = pygame.font.SysFont('Comic Sans MS', 25)
player2HealthFont = pygame.font.SysFont('Comic Sans MS', 25)
statFont = pygame.font.SysFont('Comic Sans MS', 50)

#OBJECTS
#Main Objects
border = GameObject(0, 0, 1000, 500, "Assets/MainAssets/border.png")
bigBorder = GameObject(0, 0, 1000, 500, "Assets/MainAssets/bigBorder.png")

#Title Objects
logo = Cinematics(400, -100, 200, 200, "Assets/TitleScreen/logo.png")
spaceToStart = GameObject(250, 350, 500, 38, "Assets/Text/spaceToStart.png")
bossRushText = GameObject(262.5, 400, 475, 38, "Assets/Text/bossRush.png")

#Character Selects
chooseCharacterP1 = Cinematics(250, -100, 500, 50,
                               "Assets/Text/charactersP1.png")
chooseCharacterP2 = Cinematics(250, -100, 500, 50,
                               "Assets/Text/charactersP2.png")

marioSel = CharacterSelect(80, 125, 120, 120,
                           "Assets/CharacterSelect/MarioSel/marioSel.png",
                           "MARIO",1)
DKSel = CharacterSelect(200, 125, 120, 120,
                           "Assets/CharacterSelect/DKSel/DKSel.png",
                           "DONKEY KONG",0)
linkSel = CharacterSelect(320, 125, 120, 120,
                           "Assets/CharacterSelect/LinkSel/linkSel.png",
                           "LINK",1)
BOTWLinkSel = CharacterSelect(320, 125, 120, 120,
 "Assets/CharacterSelect/BOTWLinkSel/BOTWLinkSel.png",
 "BOTW LINK",2)
samusSel = CharacterSelect(440, 125, 120, 120,
                           "Assets/CharacterSelect/SamusSel/samusSel.png",
                           "SAMUS",0)
yoshiSel = CharacterSelect(560, 125, 120, 120,
                           "Assets/CharacterSelect/YoshiSel/yoshiSel.png",
                           "YOSHI",0)
kirbySel = CharacterSelect(680, 125, 120, 120,
                           "Assets/CharacterSelect/KirbySel/kirbySel.png",
                           "KIRBY",0)
foxSel = CharacterSelect(800, 125, 120, 120,
                           "Assets/CharacterSelect/FoxSel/foxSel.png",
                           "FOX",0)
pikachuSel = CharacterSelect(80, 245, 120, 120,
                           "Assets/CharacterSelect/PikachuSel/pikachuSel.png",
                           "PIKACHU",0)
luigiSel = CharacterSelect(80, 125, 120, 120,
                           "Assets/CharacterSelect/LuigiSel/luigiSel.png",
                           "LUIGI",2)
captainFalconSel = CharacterSelect(200, 245, 120, 120,
                           "Assets/CharacterSelect/CaptainFalconSel/captainFalconSel.png",
                           "CAPTAIN FALCON",0)
peachSel = CharacterSelect(320, 245, 120, 120,
                           "Assets/CharacterSelect/PeachSel/peachSel.png",
                           "PEACH",0)
bowserSel = CharacterSelect(440, 245, 120, 120,
                           "Assets/CharacterSelect/BowserSel/bowserSel.png",
                           "BOWSER",0)
ganonSel = CharacterSelect(560, 245, 120, 120,
 "Assets/CharacterSelect/GanonSel/ganonSel.png",
 "GANON",0)
mewtwoSel = CharacterSelect(680, 245, 120, 120,
 "Assets/CharacterSelect/MewtwoSel/mewtwoSel.png",
 "MEWTWO",0)
warioSel = CharacterSelect(800, 245, 120, 120,
 "Assets/CharacterSelect/WarioSel/warioSel.png",
 "WARIO",0)
sonicSel = CharacterSelect(200, 365, 120, 120,
 "Assets/CharacterSelect/SonicSel/sonicSel.png",
 "SONIC",0)
charizardSel = CharacterSelect(80, 365, 120, 120,
 "Assets/CharacterSelect/CharizardSel/charizardSel.png",
 "CHARIZARD",0)
dededeSel = CharacterSelect(320, 365, 120, 120,
 "Assets/CharacterSelect/DededeSel/dededeSel.png",
 "DEDEDE",0)
kRoolSel = CharacterSelect(440, 365, 120, 120,
 "Assets/CharacterSelect/KRoolSel/kRoolSel.png",
 "KING K ROOL",0)
steveSel = CharacterSelect(560, 365, 120, 120,
 "Assets/CharacterSelect/SteveSel/steveSel.png",
 "STEVE",0)
doomslayerSel = CharacterSelect(680, 365, 120, 120,
 "Assets/CharacterSelect/DoomslayerSel/doomslayerSel.png",
 "DOOM SLAYER",0)
kratosSel = CharacterSelect(800, 365, 120, 120,
 "Assets/CharacterSelect/KratosSel/kratosSel.png",
 "KRATOS",0)

CPUText = GameObject(20,20,76,20,"Assets/MainAssets/CPU/CPUOff.png")
swapEcho = GameObject(825,25,50,50,"Assets/MainAssets/EchoSwap/echoSwap.png")
echoText = GameObject(880,25,95,25,"Assets/Text/echoText.png")

characterSels = [marioSel,DKSel,linkSel,BOTWLinkSel,samusSel,yoshiSel,kirbySel,foxSel,pikachuSel,luigiSel,captainFalconSel,peachSel,bowserSel,ganonSel,mewtwoSel,warioSel,sonicSel,charizardSel,dededeSel,kRoolSel,steveSel,doomslayerSel,kratosSel]

#Stats
statsButton = GameObject(25,25,75,75,"Assets/MainAssets/Stats/stats.png")
back = GameObject(25,25,50,50,"Assets/MainAssets/EchoSwap/echoSwap.png")
statText = GameObject(105,25,136,40,"Assets/Text/statText.png")
statText2 = GameObject(432,25,136,40,"Assets/Text/statText.png")
reset = GameObject(900,25,75,50,"Assets/MainAssets/Reset/reset.png")

#Stage Selects
stageText = Cinematics(362.5, -100, 275, 50, "Assets/Text/stageText.png")

mushroomKingdomSel = StageSelect(
  125, 125, 250, 125,
  "Assets/StageSelects/MushroomKingdom/mushroomKingdomSel.png",
  "MUSHROOM KINGDOM","marioWorldTheme.mp3")
DKCountrySel = StageSelect(
  375, 125, 250, 125,
  "Assets/StageSelects/DKCountry/DKCountrySel.png",
  "DONKEY KONG JUNGLE","dkCountryTheme.mp3")
brinstarSel = StageSelect(
  625, 125, 250, 125,
  "Assets/StageSelects/DKCountry/DKCountrySel.png",
  "BRINSTAR","brinstar.mp3")
norfairSel = StageSelect(
  125, 250, 250, 125,
  "Assets/StageSelects/Norfair/norfairSel.png",
  "NORFAIR","norfair.mp3")
battlefieldSel = StageSelect(
  375, 250, 250, 125,
  "Assets/StageSelects/BattlefieldSel/battlefieldSel.png",
  "BATTLE FIELD","battlefield.mp3")
greenHillZoneSel = StageSelect(
  625, 250, 250, 125,
  "Assets/StageSelects/GreenHillZoneSel/greenHillZoneSel.png",
  "GREEN HILL ZONE","greenHillZone.mp3")
stageSels = [mushroomKingdomSel,DKSel,brinstarSel,norfairSel,battlefieldSel]

#Main Game Objects
backgroundImage = GameObject(50, 50, 900, 400,
                             "Assets/Backgrounds/mushroomKingdom.png")

ground = GameObject(200, 250, 600, 250, "Assets/Grounds/grassGround.png")
ground2 = GameObject(500,175,300,75,"Assets/Grounds/grassGround.png")
grounds = [ground,ground2]

player = Player(300, -50, 70, 90, "Assets/Characters/Mario/mario.png", 0, 0, 4,
                "MARIO")
player2 = Player(700, -50, 70, 90, "Assets/Characters/Mario/mario.png", 0, 0, 4,
                "MARIO")

projectile = Projectile(player.x,player.y,15,15,"Assets/Projectiles/ancientArrow.png")
projectile2 = Projectile(player2.x,player2.y,15,15,"Assets/Projectiles/ancientArrow.png")

damagePanel = GameObject(400, 335, 100, 75, "Assets/MainAssets/damagePanel.png")
damagePanel2 = GameObject(500, 335, 100, 75, "Assets/MainAssets/damagePanel.png")
damagePanel3 = GameObject(412.5, 335, 100, 75, "Assets/MainAssets/damagePanel.png")
damagePanel4 = GameObject(512.5, 335, 75, 75, "Assets/MainAssets/damagePanel.png")

player1Marker = GameObject(0,0,20,20,"Assets/Text/player1.png")
player2Marker = GameObject(0,0,20,20,"Assets/Text/player2.png")

#Items
burger = Item(450,ground.y - 50, 50,50,"Assets/Items/burger.png","BURGER")

#Win screen
winScreenP1 = GameObject(0, 0, 1000, 500, "Assets/MainAssets/player1WinScreen.png")
winScreenP2 = GameObject(0, 0, 1000, 500, "Assets/MainAssets/player2WinScreen.png")
gameOverScreen = GameObject(0, 0, 1000, 500, "Assets/MainAssets/gameOverScreen.png")
winScreen = GameObject(0, 0, 1000, 500, "Assets/MainAssets/winScreen.png")

winText = GameObject(100,0,322,35,"Assets/Text/player1wins.png")
winText2 = GameObject(100,0,322,35,"Assets/Text/player2wins.png")
gameOverText = GameObject(100,0,231,35,"Assets/Text/gameOver.png")
winTextBossRush = GameObject(100,0,231,35,"Assets/Text/youWin.png")

#Bosses
peteyPiranha = Boss(700,ground.y - 200,152,200,"Assets/Bosses/PeteyPiranha/peteyPiranha.png",0,0,1,"PETEY PIRANHA")
ridley = Boss(500,ground.y - 200,300,180,"Assets/Bosses/Ridley/ridley.png",0,0,1,"RIDLEY")
gigaBowser = Boss(500,ground.y - 200,330,225,"Assets/Bosses/GigaBowser/gigaBowser.png",0,0,1,"GIGA BOWSER")
masterHand = Boss(500,ground.y - 200,225,150,"Assets/Bosses/MasterHand/masterHand.png",0,0,1,"MASTER HAND")

#Sounds
def playMusic(sound):
  mixer.music.stop()
  mixer.music.load(sound)
  pygame.mixer.music.play(-1)
  
playMusic("Sounds/menuSound2.mp3")
#Basic Methods
def resetItems(burger):
  burger.showTime = datetime.datetime.now() + burger.hideTime


#Main Gameloop
running = True
while running == True:
  clock.tick(1000000)

  #DataSaving
  saveLoadManager.saveData(games,"games")
  saveLoadManager.saveData(bossRushGames,"bossRush")
  saveLoadManager.saveData(p1Wins,"player1Wins")
  saveLoadManager.saveData(p2Wins,"player2Wins")
  
  #Event Handler
  for event in pygame.event.get():

    if event.type == pygame.QUIT:
      running = False

    #Keypresses
    if (screenDisplay == 4 or (screenDisplay >= 8 and screenDisplay <= 11)) and event.type == KEYDOWN:
      if event.key == pygame.K_RIGHT and player.state != "ATTACK":
        player.right()
      if event.key == pygame.K_LEFT and player.state != "ATTACK":
        player.left()
      if event.key == pygame.K_UP:
        player.y -= 1
        player.jump()
        player.state == "JUMP"
      if event.key == pygame.K_o and player.state != "ATTACK2":
        player.state = "ATTACK1"
      if event.key == pygame.K_p and player.state != "ATTACK1":
        player.state = "ATTACK2"
        if player.character == "LINK":
          projectile.projectileOn = True
          projectile.changeImage("Assets/Projectiles/ancientArrow.png")

      if CPU == False:
        if event.key == pygame.K_d and player2.state != "ATTACK":
          player2.right()
        if event.key == pygame.K_a and player2.state != "ATTACK":
          player2.left()
        if event.key == pygame.K_w:
          player2.y -= 1
          player2.jump()
        if event.key == pygame.K_z and player2.state != "ATTACK2":
          player2.state = "ATTACK1"
        if event.key == pygame.K_x and player2.state != "ATTACK1":
          player2.state = "ATTACK2"
    #Keyreleases
    if event.type == KEYUP:
      if event.key == pygame.K_RIGHT:
        player.vx = 0
        player.state = "IDLE"
      if event.key == pygame.K_LEFT:
        player.vx = 0
        player.state = "IDLE"
      if event.key == pygame.K_o:
        player.state = "IDLE"
      if event.key == pygame.K_p:
        player.state = "IDLE"

      if event.key == pygame.K_d:
        player2.vx = 0
        player2.state = "IDLE"
      if event.key == pygame.K_a:
        player2.vx = 0
        player2.state = "IDLE"
      if event.key == pygame.K_z:
        player2.state = "IDLE"
      if event.key == pygame.K_x:
        player2.state = "IDLE"

    #Buttons
    if event.type == pygame.MOUSEBUTTONDOWN:
      if screenDisplay == 1:
        if chooseCharacterP1.y >= 50:
          for sel in characterSels:
            if sel.selClick() == True and (sel.show == 0 or switchEcho == sel.show):
              sel.characterSelLogic(player)
              screenDisplay = 2
      elif screenDisplay == 2:
        if CPUText.click() == True:
            if CPU == False:
              CPU = True
            elif CPU == True:
              CPU = False   
        if chooseCharacterP2.y >= 50:
              for sel in characterSels:
                if sel.selClick() == True and (sel.show == 0 or switchEcho == sel.show):
                  sel.characterSelLogic(player2)
                  screenDisplay = 3
      if screenDisplay == 7:
          for sel in characterSels:
            if sel.selClick() == True and (sel.show == 0 or switchEcho == sel.show):
              sel.characterSelLogic(player)
              screenDisplay = 8
              playMusic("Sounds/finalBattle.mp3")
      if screenDisplay == 1 or screenDisplay == 2 or screenDisplay == 7:
        if swapEcho.click() == True:
          if switchEcho == 1:
            switchEcho = 2
          elif switchEcho == 2:
            switchEcho = 1

      elif screenDisplay == 0:
        if statsButton.click() == True:
          screenDisplay = 20
      elif screenDisplay == 3 and stageText.y >= 50:
          if mushroomKingdomSel.selClick() == True:
            screenDisplay = 4
            background = mushroomKingdomSel.stage
            resetItems(burger)
            selectSound = mixer.Sound("Sounds/select.mp3")
            selectSound.play()
            playMusic("Sounds/" + mushroomKingdomSel.music)
            CPUWaitTime = datetime.datetime.now()
            player.y = 250 - player.height
            player2.y = 175 - player2.height
          if DKCountrySel.selClick() == True:
            screenDisplay = 4
            background = DKCountrySel.stage
            resetItems(burger)
            selectSound = mixer.Sound("Sounds/select.mp3")
            selectSound.play()
            playMusic("Sounds/" + DKCountrySel.music)
            CPUWaitTime = datetime.datetime.now()
            player.y = 325 - player.height
            player2.y = 250 - player2.height
          if norfairSel.selClick() == True:
            screenDisplay = 4
            background = norfairSel.stage
            resetItems(burger)
            selectSound = mixer.Sound("Sounds/select.mp3")
            selectSound.play()
            playMusic("Sounds/" + norfairSel.music)
            CPUWaitTime = datetime.datetime.now()
            player.y = 175 - player.height
            player2.y = 250
          if brinstarSel.selClick() == True:
            screenDisplay = 4
            background = brinstarSel.stage
            resetItems(burger)
            selectSound = mixer.Sound("Sounds/select.mp3")
            selectSound.play()
            playMusic("Sounds/" + brinstarSel.music)
            CPUWaitTime = datetime.datetime.now()
            player.y = 175 - player.height
            player2.y = 250
          if battlefieldSel.selClick() == True:
            screenDisplay = 4
            background = battlefieldSel.stage
            resetItems(burger)
            selectSound = mixer.Sound("Sounds/select.mp3")
            selectSound.play()
            playMusic("Sounds/" + battlefieldSel.music)
            CPUWaitTime = datetime.datetime.now()
            player.y = 250
            player2.y = 175 - player2.height
          if greenHillZoneSel.selClick() == True:
            screenDisplay = 4
            background = greenHillZoneSel.stage
            resetItems(burger)
            selectSound = mixer.Sound("Sounds/select.mp3")
            selectSound.play()
            playMusic("Sounds/" + greenHillZoneSel.music)
            CPUWaitTime = datetime.datetime.now()
            player.y = 300 - player.height
            player2.y = 225 - player2.height

      elif screenDisplay == 20:
        if back.click() == True:
          screenDisplay = 0
        if reset.click() == True:
          saveLoadManager.deleteFile("bossRush")
          saveLoadManager.deleteFile("games")
          saveLoadManager.deleteFile("player1Wins")
          saveLoadManager.deleteFile("player2Wins")
          bossRushGames = 0
          games = 0
          p1Wins = 0
          p2Wins = 0

    #Spacebar at the beginning
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_SPACE and screenDisplay == 0 and logo.y >= 100:
        screenDisplay = 1
        selectSound = mixer.Sound("Sounds/select.mp3")
        selectSound.play()
      if event.key == pygame.K_SPACE and (winText.y >= 100 and screenDisplay == 6):
        games+= 1
        screenDisplay = 0
        selectSound = mixer.Sound("Sounds/select.mp3")
        selectSound.play()
        p1Wins += 1
        playMusic("Sounds/menuSound2.mp3")
      if event.key == pygame.K_SPACE and winText2.y >= 100 and screenDisplay == 5:
        games+= 1
        screenDisplay = 0
        selectSound = mixer.Sound("Sounds/select.mp3")
        selectSound.play()
        p2Wins += 1
        playMusic("Sounds/menuSound2.mp3")

      if event.key == pygame.K_SPACE and gameOverText.y >= 100 and screenDisplay == 12:
        screenDisplay = 0
        selectSound = mixer.Sound("Sounds/select.mp3")
        selectSound.play()
        playMusic("Sounds/menuSound2.mp3")
      if event.key == pygame.K_SPACE and winTextBossRush.y >= 100 and screenDisplay == 13:
        bossRushGames+= 1
        screenDisplay = 0
        selectSound = mixer.Sound("Sounds/select.mp3")
        selectSound.play()
        playMusic("Sounds/menuSound2.mp3")
      if event.key == pygame.K_b and (screenDisplay == 0 and logo.y >= 100):
        screenDisplay = 7
        selectSound = mixer.Sound("Sounds/select.mp3")
        selectSound.play()

  #RENDERS
  #Title
  if screenDisplay == 0:
    screen.fill((0, 0, 0))
    logo.draw(screen)
    logo.theatrics(100)
    if logo.theatrics(100) == True:
      spaceToStart.x = 250
      spaceToStart.draw(screen)
      bossRushText.draw(screen)

    statsButton.draw(screen)
    statsButton.selHover("Assets/MainAssets/Stats/stats.png","Assets/MainAssets/Stats/stats2.png")
    statText.draw(screen)
  #Character Select screens
  if screenDisplay == 1:
    screen.fill((0, 0, 0))
    chooseCharacterP1.draw(screen)
    chooseCharacterP1.theatrics(50)

    player.state = "IDLE"
    player2.state = "IDLE"
    player.health = 200
    player2.health = 200
    player.x = 300
    player2.x = 700
    player.y = -100
    player2.y = -100
    player2.x = 700-player2.width
    winText.y = -100
    winText2.y = -100
    player2.facingRight = False
    player.facingRight = True
    projectile.projectileOn = False
    projectile2.projectileOn = False
    
  if screenDisplay == 2:
    screen.fill((0, 0, 0))
    chooseCharacterP2.draw(screen)
    chooseCharacterP2.theatrics(50)
    if CPU == False:
      CPUText.changeImage("Assets/MainAssets/CPU/CPUOff.png")
    elif CPU == True:
      CPUText.changeImage("Assets/MainAssets/CPU/CPUOn.png")
    CPUText.draw(screen)
    
  if screenDisplay == 7:
      player.y = -50
      player.x = 300
      player.health = 500
      screen.fill((0, 0, 0))
      chooseCharacterP1.draw(screen)
      chooseCharacterP1.theatrics(50)
    
      peteyPiranha.addFrames("Assets/Bosses/PeteyPiranha/peteyPiranhaFly.png")
      peteyPiranha.addFrames("Assets/Bosses/PeteyPiranha/peteyPiranha.png")
      peteyPiranha.addFrames("Assets/Bosses/PeteyPiranha/peteyPiranhaFly.png")
      peteyPiranha.addFrames("Assets/Bosses/PeteyPiranha/peteyPiranha.png")
      peteyPiranha.health = 200
      peteyPiranha.facingRight = False
      peteyPiranha.x = 700

      ridley.addFrames("Assets/Bosses/Ridley/ridley.png")
      ridley.addFrames("Assets/Bosses/Ridley/ridley.png")
      ridley.addFrames("Assets/Bosses/Ridley/ridley.png")
      ridley.addFrames("Assets/Bosses/Ridley/ridley.png")
      ridley.health = 250
      ridley.facingRight = False
      ridley.x = 500

      gigaBowser.addFrames("Assets/Bosses/GigaBowser/gigaBowserWalk2.png")
      gigaBowser.addFrames("Assets/Bosses/GigaBowser/gigaBowser.png")
      gigaBowser.addFrames("Assets/Bosses/GigaBowser/gigaBowserWalk.png")
      gigaBowser.addFrames("Assets/Bosses/GigaBowser/gigaBowser.png")
      gigaBowser.health = 500
      gigaBowser.facingRight = False
      gigaBowser.x = 500

      masterHand.addFrames("Assets/Bosses/MasterHand/masterHand.png")
      masterHand.addFrames("Assets/Bosses/MasterHand/masterHand.png")
      masterHand.addFrames("Assets/Bosses/MasterHand/masterHand.png")
      masterHand.addFrames("Assets/Bosses/MasterHand/masterHand.png")
      masterHand.health = 750
      masterHand.facingRight = False
      masterHand.x = 500
          
  if screenDisplay == 1 or screenDisplay == 2 or screenDisplay == 7:

    if switchEcho == 1:
      marioSel.draw(screen)
      marioSel.selHover("Assets/CharacterSelect/MarioSel/marioSel.png",
                        "Assets/CharacterSelect/MarioSel/marioSel2.png")
      linkSel.draw(screen)
      linkSel.selHover("Assets/CharacterSelect/LinkSel/linkSel.png",
                        "Assets/CharacterSelect/LinkSel/linkSel2.png")
    if switchEcho == 2:
      luigiSel.draw(screen)
      luigiSel.selHover("Assets/CharacterSelect/LuigiSel/luigiSel.png",
                        "Assets/CharacterSelect/LuigiSel/luigiSel2.png")
      BOTWLinkSel.draw(screen)
      BOTWLinkSel.selHover("Assets/CharacterSelect/BOTWLinkSel/BOTWLinkSel.png",
                        "Assets/CharacterSelect/BOTWLinkSel/BOTWLinkSel2.png")

    DKSel.draw(screen)
    DKSel.selHover("Assets/CharacterSelect/DKSel/DKSel.png",
                      "Assets/CharacterSelect/DKSel/DKSel2.png")

    samusSel.draw(screen)
    samusSel.selHover("Assets/CharacterSelect/SamusSel/samusSel.png",
                      "Assets/CharacterSelect/SamusSel/samusSel2.png")

    yoshiSel.draw(screen)
    yoshiSel.selHover("Assets/CharacterSelect/YoshiSel/yoshiSel.png",
                      "Assets/CharacterSelect/YoshiSel/yoshiSel2.png")

    kirbySel.draw(screen)
    kirbySel.selHover("Assets/CharacterSelect/KirbySel/kirbySel.png",
                      "Assets/CharacterSelect/KirbySel/kirbySel2.png")

    foxSel.draw(screen)
    foxSel.selHover("Assets/CharacterSelect/FoxSel/foxSel.png",
                      "Assets/CharacterSelect/FoxSel/foxSel2.png")

    pikachuSel.draw(screen)
    pikachuSel.selHover("Assets/CharacterSelect/PikachuSel/pikachuSel.png",
                      "Assets/CharacterSelect/PikachuSel/pikachuSel2.png")

    captainFalconSel.draw(screen)
    captainFalconSel.selHover("Assets/CharacterSelect/CaptainFalconSel/captainFalconSel.png",
                      "Assets/CharacterSelect/CaptainFalconSel/captainFalconSel2.png")

    peachSel.draw(screen)
    peachSel.selHover("Assets/CharacterSelect/PeachSel/peachSel.png",
                      "Assets/CharacterSelect/PeachSel/peachSel2.png")

    bowserSel.draw(screen)
    bowserSel.selHover("Assets/CharacterSelect/BowserSel/bowserSel.png",
                      "Assets/CharacterSelect/BowserSel/bowserSel2.png")

    sonicSel.draw(screen)
    sonicSel.selHover("Assets/CharacterSelect/SonicSel/sonicSel.png",
                      "Assets/CharacterSelect/SonicSel/sonicSel2.png")

    ganonSel.draw(screen)
    ganonSel.selHover("Assets/CharacterSelect/GanonSel/ganonSel.png",
                      "Assets/CharacterSelect/GanonSel/ganonSel2.png")

    mewtwoSel.draw(screen)
    mewtwoSel.selHover("Assets/CharacterSelect/MewtwoSel/mewtwoSel.png",
                      "Assets/CharacterSelect/MewtwoSel/mewtwoSel2.png")

    warioSel.draw(screen)
    warioSel.selHover("Assets/CharacterSelect/WarioSel/warioSel.png",
                      "Assets/CharacterSelect/WarioSel/warioSel2.png")

    charizardSel.draw(screen)
    charizardSel.selHover("Assets/CharacterSelect/CharizardSel/charizardSel.png",
                      "Assets/CharacterSelect/CharizardSel/charizardSel2.png")

    dededeSel.draw(screen)
    dededeSel.selHover("Assets/CharacterSelect/DededeSel/dededeSel2.png",
                      "Assets/CharacterSelect/DededeSel/dededeSel.png")

    kRoolSel.draw(screen)
    kRoolSel.selHover("Assets/CharacterSelect/KRoolSel/kRoolSel.png",
                      "Assets/CharacterSelect/KRoolSel/kRoolSel2.png")

    steveSel.draw(screen)
    steveSel.selHover("Assets/CharacterSelect/SteveSel/steveSel.png",
                      "Assets/CharacterSelect/SteveSel/steveSel2.png")

    doomslayerSel.draw(screen)
    doomslayerSel.selHover("Assets/CharacterSelect/DoomslayerSel/doomslayerSel.png",
                      "Assets/CharacterSelect/DoomslayerSel/doomslayerSel2.png")

    kratosSel.draw(screen)
    kratosSel.selHover("Assets/CharacterSelect/KratosSel/kratosSel.png",
                      "Assets/CharacterSelect/KratosSel/kratosSel2.png")
    
    swapEcho.draw(screen)
    swapEcho.selHover("Assets/MainAssets/EchoSwap/echoSwap.png","Assets/MainAssets/EchoSwap/echoSwap2.png")
    echoText.draw(screen)


  #Stage Selects
  if screenDisplay == 3:
    screen.fill((0, 0, 0))
    stageText.draw(screen)
    stageText.theatrics(50)

    mushroomKingdomSel.draw(screen)
    mushroomKingdomSel.selHover(
      "Assets/StageSelects/MushroomKingdom/mushroomKingdomSel.png",
      "Assets/StageSelects/MushroomKingdom/mushroomKingdomSel2.png")

    DKCountrySel.draw(screen)
    DKCountrySel.selHover(
      "Assets/StageSelects/DKCountry/DKCountrySel.png",
      "Assets/StageSelects/DKCountry/DKCountrySel2.png")

    brinstarSel.draw(screen)
    brinstarSel.selHover(
      "Assets/StageSelects/Brinstar/brinstarSel.png",
      "Assets/StageSelects/Brinstar/brinstarSel2.png")

    norfairSel.draw(screen)
    norfairSel.selHover(
      "Assets/StageSelects/Norfair/norfairSel.png",
      "Assets/StageSelects/Norfair/norfairSel2.png")

    battlefieldSel.draw(screen)
    battlefieldSel.selHover(
      "Assets/StageSelects/BattlefieldSel/battlefieldSel.png",
      "Assets/StageSelects/BattlefieldSel/battlefieldSel2.png")

    greenHillZoneSel.draw(screen)
    greenHillZoneSel.selHover(
      "Assets/StageSelects/GreenHillZoneSel/greenHillZoneSel.png",
      "Assets/StageSelects/GreenHillZoneSel/greenHillZoneSel2.png")

  #Main Game
  if screenDisplay == 4:
    screen.fill((0, 0, 0))
    
    #Background
    if background == mushroomKingdomSel.stage:
      backgroundImage.changeImage("Assets/Backgrounds/mushroomKingdom.png")
      ground.changeImage("Assets/Grounds/grassGround.png")
      ground2.changeImage("Assets/Grounds/grassGround.png")
      burger.x = 450
      burger.y = ground.y - 50
      ground.x = 200
      ground.y = 250
      ground2.x = 500
      ground2.y = 175
      ground2.width = 300
      ground2.height = 75

    if background == DKCountrySel.stage:
      backgroundImage.changeImage("Assets/Backgrounds/DKCountryBackground.png")
      ground.changeImage("Assets/Grounds/dkGround.png")
      ground2.changeImage("Assets/Grounds/dkGround.png")
      burger.x = 450
      burger.y = ground.y - 50
      ground.x = 200
      ground.y = 325
      ground2.x = 500
      ground2.y = 250
      ground2.width = 300
      ground2.height = 75

    if background == brinstarSel.stage:
      backgroundImage.changeImage("Assets/Backgrounds/brinstarBackground.png")
      ground.changeImage("Assets/Grounds/brinstarGround.png")
      ground2.changeImage("Assets/Grounds/brinstarGround2.png")
      burger.x = 525
      burger.y = ground.y - 50
      ground.x = 200
      ground.y = 250
      ground2.x = 200
      ground2.y = ground.y - ground2.height
      ground2.width = 300
      ground2.height = 75

    if background == norfairSel.stage:
      backgroundImage.changeImage("Assets/Backgrounds/norfairBackground.png")
      ground.changeImage("Assets/Grounds/norfairGround.png")
      ground2.changeImage("Assets/Grounds/norfairGround.png")
      burger.x = 525
      burger.y = ground.y - 50
      ground.x = 200
      ground.y = 250
      ground2.x = 200
      ground2.y = ground.y - ground2.height
      ground2.width = 300
      ground2.height = 75

    if background == battlefieldSel.stage:
      backgroundImage.changeImage("Assets/Backgrounds/battleFieldBackground.png")
      ground.changeImage("Assets/Grounds/battlefieldGround.png")
      ground2.changeImage("Assets/Grounds/battlefieldGround2.png")
      burger.x = 450
      burger.y = ground.y - 50
      ground.x = 200
      ground.y = 250
      ground2.x = 550
      ground2.y = 175
      ground2.width = 200
      ground2.height = 40

    if background == greenHillZoneSel.stage:
      backgroundImage.changeImage("Assets/Backgrounds/greenHillZoneBackground.png")
      ground.changeImage("Assets/Grounds/grassGround2.png")
      ground2.changeImage("Assets/Grounds/grassGround2.png")
      burger.x = 450
      burger.y = ground.y - 50
      ground.x = 200
      ground.y = 300
      ground2.x = 500
      ground2.y = 225
      ground2.width = 300
      ground2.height = 75
  
    backgroundImage.draw(screen)
    #Ground
    ground.draw(screen)
    ground2.draw(screen)
    ground.changeHitbox()
    ground.changeHitbox()
    ground2.changeHitbox()

    #Items
    burger.itemLogic(screen)
    player.useItem(burger)
    player2.useItem(burger)
    burger.changeHitbox()
    
    #Players
    player.changeHitbox()
    player2.changeHitbox()
    player.characterSetup()
    player2.characterSetup()
    player.gravity2(ground, ground2, gravity,screenDisplay)
    player2.gravity2(ground, ground2, gravity,screenDisplay)
    player.attackLogic(player2,grounds)
    player2.attackLogic(player,grounds)

    #Markers
    player1Marker.x = player.x + 1/2 * player.width
    player1Marker.y = player.y - 30
    player1Marker.draw(screen)

    player2Marker.x = player2.x + 1/2 * player2.width
    player2Marker.y = player2.y - 30
    player2Marker.draw(screen)

    #If player falls of the screen
    if player.y > 500:
      screenDisplay = 5
    if player2.y > 500:
      screenDisplay = 6

    #Draw players
    if player.facingRight == True:
      player.draw(screen)
    else:
      player.drawFlip(screen)
    if player2.facingRight == True:
      player2.draw(screen)
    else:
      player2.drawFlip(screen)

    #CPU
    currentTime = datetime.datetime.now()
    if CPU == True and (currentTime + datetime.timedelta(seconds=2) > CPUWaitTime):
      player2.cpu(player,ground2,ground)

    #Damage meters
    damagePanel.draw(screen)
    damagePanel2.draw(screen)

    player1Health = player1HealthFont.render(str(player.health), False, (150, 75, 0))
    screen.blit(player1Health,(damagePanel.x + 21,damagePanel.y + 20))
    if player.health <= 0:
      screenDisplay = 5
      
    player2Health = player1HealthFont.render(str(player2.health), False, (150, 75, 0))
    screen.blit(player2Health,(damagePanel2.x + 21,damagePanel2.y + 20))
    if player2.health <= 0:
      screenDisplay = 6

    #A border
    bigBorder.draw(screen)

  #Win Screens
  if screenDisplay == 5:
    winScreenP1.draw(screen)
    winText2.draw(screen)
    if winText2.y < 100:
      winText2.y += 2
    if winText2.y >= 100:
      spaceToStart.x = 100
      spaceToStart.draw(screen)
      
  if screenDisplay == 6:
    winScreenP2.draw(screen)
    winText.draw(screen)
    if winText.y < 100:
      winText.y += 2
    if winText.y >= 100:
      spaceToStart.x = 100
      spaceToStart.draw(screen)

  #Game Over
  if screenDisplay == 12:
    gameOverScreen.draw(screen)
    gameOverText.draw(screen)
    if gameOverText.y < 100:
      gameOverText.y += 2
    if gameOverText.y >= 100:
      spaceToStart.x = 100
      spaceToStart.draw(screen)

  #Win screen for boss rush
  if screenDisplay == 13:
    winScreen.draw(screen)
    winTextBossRush.draw(screen)
    if winTextBossRush.y < 100:
      winTextBossRush.y += 2
    if winTextBossRush.y >= 100:
      spaceToStart.x = 100
      spaceToStart.draw(screen)

  if screenDisplay == 5 or screenDisplay == 6 or screenDisplay == 12 or screenDisplay == 13:
    chooseCharacterP1.y = -100
    chooseCharacterP2.y = -100
    stageText.y = -100
    if player2.state == "KNOCKBACK":
        player2.state = "IDLE"
        player2.vx = 0
    if player.state == "KNOCKBACK":
        player.state = "IDLE"
        player.vx = 0 

  #BossRush
  if screenDisplay >= 8 and screenDisplay <= 11:
    screen.fill((0, 0, 0))
    player.changeHitbox()
    #Backgrounds
    if screenDisplay == 8:
      backgroundImage.changeImage("Assets/Backgrounds/mushroomKingdom.png")
      ground.changeImage("Assets/Grounds/grassGround.png")
      ground.x = 200
      ground.y = 250
    if screenDisplay == 9:
      backgroundImage.changeImage("Assets/Backgrounds/norfairBackground.png")
      ground.changeImage("Assets/Grounds/norfairGround.png")
      ground.x = 200
      ground.y = 250
    if screenDisplay == 10:
      backgroundImage.changeImage("Assets/Backgrounds/battleFieldBackground.png")
      ground.changeImage("Assets/Grounds/battlefieldGround.png")
      ground.x = 200
      ground.y = 250
    if screenDisplay == 11:
      backgroundImage.changeImage("Assets/Backgrounds/finalDestinationBackground.png")
      ground.changeImage("Assets/Grounds/finalDestinationGround.png")
      ground.x = 200
      ground.y = 250
    backgroundImage.draw(screen)
    
    #Bosses
    if screenDisplay == 8:
      BossHealth = player1HealthFont.render(str(peteyPiranha.health), False, (255, 0, 0))
      peteyPiranha.bossFunction(player,ground,grounds,gravity,screen,screenDisplay)   
      if peteyPiranha.health <= 0:
        player.x = 300
        player.y = -50
        player.state = "IDLE"
        screenDisplay = 9
    if screenDisplay == 9:
      BossHealth = player1HealthFont.render(str(peteyPiranha.health), False, (255, 0, 0))
      ridley.bossFunction(player,ground,grounds,gravity,screen,screenDisplay)    
      if ridley.health <= 0:
        player.x = 300
        player.y = -50
        player.state = "IDLE"
        screenDisplay = 10
    if screenDisplay == 10:
      BossHealth = player1HealthFont.render(str(peteyPiranha.health), False, (255, 0, 0))
      gigaBowser.bossFunction(player,ground,grounds,gravity,screen,screenDisplay)
      if gigaBowser.health <= 0:
        player.x = 300
        player.y = -50
        player.state = "IDLE"
        screenDisplay = 11
    if screenDisplay == 11:
      BossHealth = player1HealthFont.render(str(masterHand.health), False, (255, 0, 0))
      masterHand.bossFunction(player,ground,grounds,gravity,screen,screenDisplay)
      if masterHand.health <= 0:
        player.x = 300
        player.y = -50
        player.state = "IDLE"
        screenDisplay = 13

    #BossHealth
    if screenDisplay == 8:
      BossHealth = player1HealthFont.render(str(peteyPiranha.health), False, (255, 0, 0))
    if screenDisplay == 9:
      BossHealth = player1HealthFont.render(str(ridley.health), False, (255, 0, 0))
    if screenDisplay == 10:
      BossHealth = player1HealthFont.render(str(gigaBowser.health), False, (255, 0, 0))
        
    #Player
    player.changeHitbox()
    player.characterSetup()
    player.gravity2(ground, ground2, gravity,screenDisplay)
    player.attackLogic(player2,grounds)
    if player.y >= 500 or player.health <= 0:
      screenDisplay = 12

    #Draw players
    if player.facingRight == True:
        player.draw(screen)
    else:
        player.drawFlip(screen)

    ground.changeHitbox()
    ground.draw(screen)
    bigBorder.draw(screen)

    #Player damage meters
    damagePanel3.draw(screen)
    player1Health = player1HealthFont.render(str(player.health), False, (150, 75, 0))
    screen.blit(player1Health,(damagePanel3.x + 7,damagePanel3.y + 20))
    damagePanel4.draw(screen)
    screen.blit(BossHealth,(damagePanel4.x + 10,damagePanel4.y + 20))
    
  #Projectiles
  if screenDisplay == 4 or (screenDisplay >= 8 and screenDisplay <= 11):
    projectile.setUpProjectile(player,player2,screen)
    projectile2.setUpProjectile(player2,player,screen)
    
  if screenDisplay == 20:
    screen.fill((0,0,0))
    pygame.draw.rect(screen,[30,30,30],(25,75,950,400))
    back.draw(screen)
    back.selHover("Assets/MainAssets/EchoSwap/echoSwap.png","Assets/MainAssets/EchoSwap/echoSwap2.png")

    reset.draw(screen)
    reset.selHover("Assets/MainAssets/Reset/reset.png","Assets/MainAssets/Reset/reset2.png")

    gamesText = statFont.render("GAMES: " + str(games),False,[255,255,255])
    if games > 999:
      gamesText = statFont.render("GAMES: 999+",False,[255,255,255])

    bossRushGameText = statFont.render("BOSS RUSH WINS: " + str(bossRushGames),False,[255,255,0])
    if bossRushGames > 999:
      bossRushGameText = statFont.render("BOSS RUSH WINS: 999+",False,[255,255,0])

    p1ScoreText = statFont.render("PLAYER 1 WINS: " + str(p1Wins),False,[255,0,0])
    if p1Wins > 999:
      p1ScoreText = statFont.render("PLAYER 1 WINS: 999+",False,[255,0,0])

    p2ScoreText = statFont.render("PLAYER 2 WINS: " + str(p2Wins),False,[0,255,0])
    if p2Wins > 999:
      p2ScoreText = statFont.render("PLAYER 2 WINS: 999+",False,[0,255,0])

    screen.blit(gamesText,(50,100))
    screen.blit(bossRushGameText,(50,150))
    screen.blit(p1ScoreText,(50,200))
    screen.blit(p2ScoreText,(50,250))
    statText2.draw(screen)
    
  border.draw(screen)

  #Updates the screen
  pygame.display.update()

#Exits the program.
pygame.quit()
