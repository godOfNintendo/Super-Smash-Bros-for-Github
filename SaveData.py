import pickle
import os
import pygame

class SaveData:
  #Saves data
  def saveData(self,data,name):
    dataFile = open("SavedData/" + name + ".game","wb")
    pickle.dump(data,dataFile)

  #Loads Data
  def loadData(self,name):
    dataFile = open("SavedData/" + name + ".game","rb")
    return pickle.load(dataFile)

  #If a file exists
  def checkForFile(self,name):
    return os.path.exists("SavedData/" + name + ".game")

  #Deletes a file
  def deleteFile(self,name):
    os.remove("SavedData/" + name + ".game")
