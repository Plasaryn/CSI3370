from datetime import datetime

from PtoRecord import PtoRecord
from ConversionReceipt import ConversionReceipt

class InvalidConversion(ValueError):
  def __init__(self, message: str) -> None:
    super().__init__(message)


class PtoConversion:
  def __init__(self, ptoRecord: PtoRecord) -> None:
    self.parentPtoRecord = ptoRecord
    self.__sickDaysToConvert = 0
    self.__ptoDaysToConvert = 0
    self.__sickDaysAfterConversion = 0
    self.__ptoDaysAfterConversion = 0
  
  def setSickDaysToConvert(self, days:int) -> None:
    parent = self.parentPtoRecord

    # Sets the new value and resets the other to 0
    self.__sickDaysToConvert = days
    self.__ptoDaysToConvert = 0

    # Sets the amount remaining after conversion
    self.__sickDaysAfterConversion = (
      parent.getSickDaysRemaining() - days
    )

    self.__ptoDaysAfterConversion = (
      parent.getPtoDaysRemaining() + days // 2
    )

  def setPtoDaysToConvert(self, days: int) -> None:
    parent = self.parentPtoRecord

    # Sets the new value and resets the other to 0
    self.__sickDaysToConvert = 0
    self.__ptoDaysToConvert = days

    # Sets the amount remaining after conversion
    self.__sickDaysAfterConversion = (
      parent.getSickDaysRemaining() + 2 * days
    )

    self.__ptoDaysAfterConversion = (
      parent.getPtoDaysRemaining() - days
    )

  def getSickDaysToConvert(self) -> int:
    return self.__sickDaysToConvert
  
  def getPtoDaysToConvert(self) -> int:
    return self.__ptoDaysToConvert
  
  def conmmitPtoConversion(self) -> None:
    # If both values are set to 0, then no action needs to be taken
    if not (self.__ptoDaysToConvert or self.__sickDaysToConvert):
      print("PtoConversion record is empty, no action taken")
      return
    
    if self.__isValidConversion():
      self.__createConversionReceipt()
      
      parent = self.parentPtoRecord
      parent.setSickDaysRemaining(self.__sickDaysAfterConversion)
      parent.setPtoDaysRemaining(self.__ptoDaysAfterConversion)
    else:
      raise InvalidConversion(
        f"Cannot commit PTO Conversion with the following values \n"
        + f"Sick Days to Convert: {self.__sickDaysToConvert} \n"
        + f"PTO Days to convert: {self.__ptoDaysToConvert}"
      )



  def __createConversionReceipt(self):
    parent = self.parentPtoRecord
    beforeSick = parent.getSickDaysRemaining()
    beforePto = parent.getPtoDaysRemaining()
    ConversionReceipt(
      createdOn = datetime.now(),
      createdFor = self.parentPtoRecord.getEmployeeName(),
      sickDaysBeforeConversion = beforeSick,
      ptoDaysBeforeConversion = beforePto,
      sickDaysAfterConversion = self.__sickDaysAfterConversion,
      ptoDaysAfterConversion = self.__ptoDaysAfterConversion
    )

  def __isValidConversion(self) -> bool:
    # Returns an exclusive or for the days to convert being greater than 0
    return (
      (self.__sickDaysToConvert > 0) ^ (self.__ptoDaysToConvert > 0)
    )
