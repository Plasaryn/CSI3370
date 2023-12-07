from datetime import datetime

class ConversionReceipt:
  def __init__(self,
      createdOn: datetime,
      createdFor: str,
      sickDaysBeforeConversion: int,
      ptoDaysBeforeConversion: int,
      sickDaysAfterConversion: int,
      ptoDaysAfterConversion: int) -> None:
    
    # Defining pertinent fields of a Conversion Receipt
    self.createdOn = createdOn
    self.createdFor = createdFor
    self.sickDaysBeforeConversion = sickDaysBeforeConversion
    self.ptoDaysBeforeConversion = ptoDaysBeforeConversion
    self.sickDaysAfterConversion = sickDaysAfterConversion
    self.ptoDaysAfterConversion = ptoDaysAfterConversion


    # During the creation of the object, we log that the conversion was done
    self.__logConversion(message = self.__defineConversionMessage(), logName="log.txt")

  def __defineConversionMessage(self) -> str:
    return f"""
    Created on {self.createdOn}
    Created for {self.createdFor}
    Sick days remaining before converting: {self.sickDaysBeforeConversion}
    Sick days remaining after converting:  {self.sickDaysAfterConversion}
    PTO days remaining before converting: {self.ptoDaysBeforeConversion}
    PTO days remaining after converting: {self.ptoDaysAfterConversion}"""
  
  def __logConversion(self, message: str, logName: str) -> None:
    with open(logName, "a") as log:
      log.write(message)

    