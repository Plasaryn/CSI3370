from datetime import date

class Employee:
  def __init__(self, id: int, name:str, startDate:date):
    self.id = id
    self.name = name
    self.startDate = startDate