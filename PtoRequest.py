from datetime import date, timedelta
from PTOMS import PTOMS
from PtoRecord import PtoRecord
from PtoStatus import PtoStatus
from PtoType import PtoType
from CalendarEvent import CalendarEvent
class PtoRequest:

    def __init__(self, id: int, eventStart: date, eventEnd: date, status: str, types: str):
        self.id = id
        self.PtoStatus = PtoStatus()
        self.PtoType = PtoType()
        self.PtoRecord = PtoRecord()
        self.PTOMS = PTOMS()
        self.CalendarEvent = CalendarEvent()
        self.eventStart = eventStart
        self.eventEnd = eventEnd
        self.status = status
        self.types = types

    def getId(self) -> int:
        return self.id

    def approve(self, eventStart: date, eventEnd: date) -> None:
        # Sets the decision of the PTO request
        #
        # Initialize Pto Type
        newType = input() 
        if(newType == "PTO"):
            self.types = str(PtoType.PTO)
        elif(newType == "Sick"):
            self.types = str(PtoType.Sick)
        parent = self.PtoRecord
        # Initialize Pto Status
        newStatus = input()
        if(newStatus == "Approved"):
            PtoRequest.setStatus(newStatus)
        elif(newStatus == "Pending"):
            PtoRequest.setStatus(newStatus)
        # Initialize start
        eventStart = input()
        # Initialize end
        eventEnd = input()
        # Sending the data through to CalendarEvent
        CalendarEvent(
            empId = parent.getId(),
            start = eventStart,
            end = eventEnd,
            eventName = self.status
        )
        # Setting the status
        PtoRequest.setStatus(str(newStatus))
        message = input()
        # Setting the reason
        PtoRequest.setMessage(message)

    def deny(self) -> None:
        # Takes the literal of the 'Denied' variable in
        # the PtoStatus enumeration class.

        # Defining the status as denied
        newStatus = PtoStatus.Denied
        # Setting the status
        PtoRequest.setStatus(str(newStatus))
        # Setting the reason
        message = input()
        PtoRequest.setMessage(message)
            
    def getStatus(self) -> PtoStatus:
        return self.PtoStatus
    
    def setStatus(self, newStatus: str):
        # Decision of status is made
        if(newStatus == "Approved"):
            newStatus = str(PtoStatus.Approved)
            return newStatus
        elif(newStatus == "Denied"):
            newStatus = str(PtoStatus.Denied)
            return newStatus
        elif(newStatus == "Pending"):
            newStatus = str(PtoStatus.Pending)
            return newStatus
        self.status = newStatus

    def getType(self) -> PtoType:
        return self.PtoType
    
    def getEnd(self):
        return self.eventEnd
    
    def getStart(self):
        return self.eventStart
    
    def getMessage(self):
        return self.message
    
    def setMessage(self, newMessage: str):
        self.message = newMessage


    def checkPtoRule(self, newDay: date) -> None:
        # Convert the PTORule to check how many days
        # from the current day when employee can take
        # time off.
        time_rule = PTOMS.getPtoRule()
        day_convert = -time_rule
        current_day = date.today()
        next_day = timedelta(days = day_convert)

        total_time = current_day - next_day
        newDay = total_time
        return total_time

        


        




        


     
    

        