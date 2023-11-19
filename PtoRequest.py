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

    def __init__(self, eventStart: date, eventEnd: date, message: str):
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
        

    def approve(self, app: str, eventStart: date, eventEnd: date) -> None:
        # Sets the decision of the PTO request
        #
        # Textual based for now until GUI
        newStatus = input("Choose the status of request:")
        # Takes the literal of the 'Approved' variable in
        # the PtoStatus enumeration class and compares it to
        # the input. It also compares the 'Pending' literal
        # inside the same class.
        if newStatus == str(PtoStatus.Approved):
            app = str(PtoStatus.Approved)
            self.checkPtoRule(eventStart, eventEnd)
            self.CalendarEvent.append(CalendarEvent(app, eventStart, eventEnd))
        elif newStatus == str(PtoStatus.Pending):
            app = str(PtoStatus.Pending)
            self.checkPtoRule(eventStart, eventEnd)
            self.CalendarEvent.append(CalendarEvent(app, eventStart, eventEnd))

    def deny(self, deny: str) -> None:
        # Textual based for now until GUI
        # Takes the literal of the 'Denied' variable in
        # the PtoStatus enumeration class and compares it to
        # the input.
        newStatus = input("Choose the status of request:")
        if newStatus == str(PtoStatus.Denied):
            deny = str(PtoStatus.Denied)
            
    def getStatus(self) -> PtoStatus:
        return self.PtoStatus
    
    def setStatus(self, appStatus):

        self.status = appStatus
    def getType(self) -> PtoType:
        return self.PtoType
    
    def getEnd(self):
        return self.eventEnd
    
    def getStart(self):
        return self.eventStart
    
    def getMessage(self):
        return self.message
    
    def setMessage(self, message):
        self.message = message
    
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
        # time off
        time_rule = ptoms.getPtoRule
        day_convert = -time_rule
        current_day = date.today()
        next_day = timedelta(days = day_convert)

        total_time = current_day - next_day
        day_format = total_time.strftime("%d")
        #display the current pto rule, textual for now
        print("Cannot take time off until the " + day_format)
        


        




        


     
    

        