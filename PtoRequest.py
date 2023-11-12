from datetime import date, timedelta
from PTOMS import PTOMS
from PtoRecord import PtoRecord
from PtoStatus import PtoStatus
from PtoType import PtoType
from CalendarEvent import CalendarEvent
import datetime, timedelta
class PtoRequest:

    def __init__(self, eventStart: date, eventEnd: date, message: str):
        self.PtoStatus = PtoStatus()
        self.PtoType = PtoType()
        self.PtoRecord = PtoRecord()
        self.PTOMS = PTOMS()
        self.CalendarEvent = CalendarEvent()
        self.eventStart = eventStart
        self.eventEnd = eventEnd
        self.message = message

    def approve(self, app: str, message: str, eventStart: date, eventEnd: date) -> None:
        # Sets the decision of the PTO request
        #
        # Textual based for now until GUI
        newStatus = input("Choose the status of request:")

        if newStatus == 'Approve':
            app == 'Approve'
            message = input("Please specify your reason:")
            self.checkPtoRule(eventStart, eventEnd)
            self.CalendarEvent.append(CalendarEvent(app, eventStart, eventEnd))
        elif newStatus == 'Pending':
            app == 'Pending'
            message = input("Please specify your reason:")
            self.checkPtoRule(eventStart, eventEnd)
            self.CalendarEvent.append(CalendarEvent(app, eventStart, eventEnd))
    def deny(self, deny: str, message: str) -> None:
        # Textual based for now until GUI
        newStatus = input("Choose the status of request:")
        if newStatus == 'Deny':
            deny == 'Deny'
            message = input("Please specify your reason:")

    def getStatus(self) -> PtoStatus:
        return self.PtoStatus
    
    def setStatus(self, appStatus):

        self._status = appStatus
    def getType(self) -> PtoType:
        return self.PtoType
    
    def getEnd(self):
        return self.eventEnd
    
    def getStart(self):
        return self.eventStart
    
    def getMessage(self):
        return self.message
    
    def setMessage(self, message):
        self._message = message
    
    def checkPtoRule(self, ptoms: PTOMS) -> None:
        # Convert the PTORule to check how many days
        # from the current day when employee can take
        # time off
        time_rule = ptoms.getPtoRule
        day_convert = -time_rule
        current_day = datetime.datetime.today()
        next_day = datetime.timedelta(days = day_convert)

        total_time = current_day - next_day
        day_format = total_time.strftime("%d")
        #display the current pto rule, textual for now
        print("Cannot take time off within " + day_format)


        




        


     
    

        