from datetime import date, timedelta
from PTOMS import PTOMS
from PtoRecord import PtoRecord
from PtoStatus import PtoStatus
from PtoType import PtoType
from CalendarEvent import CalendarEvent
from EEndObserver import EEndObserver
from EStartObserver import EStartObserver
from MessageObserver import MessageObserver
from PtoRSubject import PtoRSubject
class PtoRequest:

    def __init__(self, id: int, eventStart: date, eventEnd: date, status: str):
        self.id = id
        self.PtoStatus = PtoStatus()
        self.PtoType = PtoType()
        self.PtoRecord = PtoRecord()
        self.PTOMS = PTOMS()
        self.CalendarEvent = CalendarEvent()
        self.EEndObserver = EEndObserver()
        self.EStartObserver = EStartObserver()
        self.MessageObserver = MessageObserver()
        self.PtoRSubject = PtoRSubject()
        self.eventStart = eventStart
        self.eventEnd = eventEnd
        self.status = status

    def getId(self) -> int:
        return self.id

    def approve(self, eventStart: date, eventEnd: date) -> None:
        # Sets the decision of the PTO request
        #
        self.eventStart = input()
        self.eventEnd = PtoRequest.checkPtoRule()
        parent = self.PtoRecord

        newStatus = PtoStatus.Approved
        #newStatus = PtoRequest.setStatus()
        CalendarEvent(
            empId = parent.getId(),
            start = eventStart,
            end = eventEnd,
            eventName = str(PtoStatus.Approved)
        )
        PtoRequest.setStatus(str(newStatus))
        message = input()
        PtoRequest.setMessage(message)

    def deny(self) -> None:
        # Takes the literal of the 'Denied' variable in
        # the PtoStatus enumeration class.
        self.eventEnd = PtoRequest.checkPtoRule()
        newStart = date.today()
        newEnd = date.today()
        self.eventStart = newStart.replace(newStart.year, newStart.month, newStart.day)
        self.eventEnd = newEnd.replace(newEnd.year, newEnd.month, newEnd.day)
        newStatus = PtoStatus.Denied
        PtoRequest.setStatus(str(newStatus))
        message = input()
        PtoRequest.setMessage(message)
            
    def getStatus(self) -> PtoStatus:
        return self.PtoStatus
    
    def setStatus(self, newStatus: str):
        newStatus = input()
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
    
    def PtoObservers(self, eEnd: EEndObserver, eStart: EStartObserver, MessObs: MessageObserver):
        sub = PtoRSubject()
        self.eEnd = eEnd
        self.eStart = eStart
        self.MessObs = MessObs
        sub.addObserver(eEnd)
        sub.addObserver(eStart)
        sub.addObserver(MessObs)



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

        


        




        


     
    

        