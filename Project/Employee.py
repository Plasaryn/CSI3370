from datetime import date

class Employee:
  def __init__(self, id: int, name:str, startDate:date):
    self.id = id
    self.name = name
    self.startDate = startDate

  def getID(self, id: int):
    
    return self.id
  
  def setID(self, id):
    self.id = id

  def getName(self, name: str):
    return self.name
  
  def setName(self, name):
    self.name = name