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

    