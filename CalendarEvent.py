from datetime import date
class CalendarEvent:
    def __init__(self, 
                 id: int,
                 eventStart: date,
                 eventEnd: date,
                 eventName: str):
        self.id = id
        self.eventStart = eventStart
        self.eventEnd = eventEnd
        self.eventName = eventName

    def getCalEventToString(self):
        return f"{self.eventName}: {self.eventStart.strftime('%x')} to {self.eventEnd.strftime('%x')}"

    def getStartDate(self):
        return self.eventStart

    
