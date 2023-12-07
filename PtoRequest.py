from datetime import date, timedelta
from random import random

from PtoStatus import PtoStatus
from CalendarEvent import CalendarEvent
class PtoRequest:

    def __init__(self, requestID: int, requestEmpName: str, recordID: int, startDate: date, endDate: date):
        self.requestID = requestID
        self.requestEmpName = requestEmpName
        self.recordID = recordID
        self.startDate = startDate
        self.endDate = endDate
        self.status = PtoStatus.Pending.name
        self.message = ""
        # source for time between days: https://www.geeksforgeeks.org/python-program-to-find-number-of-days-between-two-given-dates/
        self.numDays = (endDate-startDate).days

    def getId(self) -> int:
        return self.requestID

    def getStatus(self) -> PtoStatus:
        return self.status
    def getPTORequestString(self):
        return "ID: "+ str(self.requestID) +"\nEmployee Name: " +str(self.requestEmpName)+ "\nStart Date: "+ str(self.startDate.strftime("%x"))+"\nEnd Date: " + str(self.endDate.strftime("%x")) + "\n   Status: "+ str(self.status) + "\n   Message: " +str(self.message)

    def getNumDays(self):
        return int(self.numDays)

    def getEndDate(self):
        return self.endDate

    def getStartDate(self):
        return self.startDate

    def getMessage(self):
        return self.message

    def setMessage(self, newMessage: str):
        self.message = newMessage

    def approve(self, message: str) -> None:
        self.status = PtoStatus.Approved.name
        self.setMessage(message)

    def deny(self, message: str) -> None:
        # Setting the status
        self.status = PtoStatus.Denied.name
        # Setting the message
        self.setMessage(message)
