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

    def __init__(self, id: int, eventStart: date, eventEnd: date, message: str, status: str):
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
        self.message = message
        self.status = status

    def getId(self) -> int:
        return self.id

    def approve(self, eventStart: date, eventEnd: date) -> None:
        # Sets the decision of the PTO request
        #
        self.checkPtoRule(eventStart, eventEnd)
        parent = self.PtoRecord
        newStatus = PtoStatus.Approved
        CalendarEvent(
            id = parent.getId(),
            start = eventStart,
            end = eventEnd,
            eventName = str(PtoStatus.Approved)
        )
        PtoRequest.setStatus(str(newStatus))

    def deny(self) -> None:
        # Takes the literal of the 'Denied' variable in
        # the PtoStatus enumeration class.
        newStart = date
        newEnd = date
        self.eventStart = newStart.replace(year = 0, month = 0, day = 0)
        self.eventEnd = newEnd.replace(year = 0, month = 0, day = 0)
        newStatus = PtoStatus.Denied
        PtoRequest.setStatus(str(newStatus))
        
            
    def getStatus(self) -> PtoStatus:
        return self.PtoStatus
    
    def setStatus(self, newStatus: str):
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



    def checkPtoRule(self, ptoms: PTOMS) -> None:
        # Convert the PTORule to check how many days
        # from the current day when employee can take
        # time off.
        time_rule = ptoms.getPtoRule()
        day_convert = -time_rule
        current_day = date.today()
        next_day = timedelta(days = day_convert)

        total_time = current_day - next_day
        day_format = total_time.strftime("%d")

        


        




        


     
    

        