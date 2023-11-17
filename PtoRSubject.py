from datetime import date
from EStartObserver import EStartObserver
from EEndObserver import EEndObserver
from MessageObserver import MessageObserver
class PtoRSubject:
    
    def __init__(self, eventStart: date, eventEnd: date, message: str):
        self.eventStart = eventStart
        self.eventEnd = eventEnd
        self.message = message
        
    # Getters for getting the observable information
    def geteventStart(self, eventStart):
        self.EStartObserver = EStartObserver(eventStart)
        return self.eventStart
        
    def geteventEnd(self, eventEnd):
        self.EEndObserver = EEndObserver(eventEnd)
        return self.eventEnd
        
    def getMessage(self, message):
        self.MessageObserver = MessageObserver(message)
        return self.message
    
    # Setters for setting the observable information
    def seteventStart(self, eventStart):
        self.eventStart = eventStart
    
    def seteventEnd(self, eventEnd):
        self.eventEnd = eventEnd
    
    def setMessage(self, message):
        self.message = message
    
    
