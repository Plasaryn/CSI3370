from PtoRequest import PtoRequest
from PtoStatus import PtoStatus


class PtoRecord:
    def __init__(self, 
            id: int,
            ptoDaysPermitted: int,
            sickDaysPermitted: int,
            empName: str
            ):
        
        self.id = id
        self.ptoDaysPermitted = ptoDaysPermitted
        self.sickDaysPermitted = sickDaysPermitted
        self.ptoDaysConsumed = 0
        self.sickDaysConsumed = 0
        self.ptoDaysRemaining = ptoDaysPermitted
        self.sickDaysRemaining = sickDaysPermitted
        self.empName = empName
        self.requestList: list[PtoRequest] = []

    def __str__(self) -> str:
        return f"id: {self.id}"

    def getId(self) -> int:
        return self.id

    def addPtoRequest(self, request: PtoRequest) -> None:
        self.requestList.append(request)
    def getPTORecordInfoString(self):
        return "PTO Days Permitted: "+ str(self.ptoDaysPermitted) +"\nPTO Days Remaining: " + str(self.ptoDaysRemaining) + "\nPTO Days Consumed: "+ str(self.ptoDaysConsumed)

    def getAllPTORequestsInfo(self):
        requestListString = ""

        for request in self.requestList:
            requestListString = requestListString + request.getPTORequestString() + "\n-------------------------------\n"

        return requestListString
    def getSickDaysRemaining(self) -> int:
        return self.sickDaysRemaining
    
    def getPtoDaysRemaining(self) -> int:
        return self.ptoDaysRemaining
    
    def getSickDaysConsumed(self) -> int:
        return self.sickDaysConsumed
    
    def getPtoDaysConsumed(self) -> int:
        return self.ptoDaysConsumed
    
    def getSickDaysPermitted(self) -> int:
        return self.sickDaysPermitted
    
    def getPtoDaysPermitted(self) -> int:
        return self.ptoDaysPermitted
    
    def getEmpName(self) -> str:
        return self.empName
    
    def setPtoDaysPermitted(self, daysPermitted: int) -> None:
        self.ptoDaysPermitted = daysPermitted

    def setSickDaysPermitted(self, daysPermitted: int) -> None:
        self.sickDaysPermitted = daysPermitted

    def setPtoDaysConsumed(self, daysConsumed: int) -> None:
        self.ptoDaysConsumed = daysConsumed

    def setSickDaysConsumed(self, daysConsumed: int) -> None:
        self.sickDaysConsumed = daysConsumed

    def setPtoDaysRemaining(self, daysRemaining: int) -> None:
        self.ptoDaysRemaining = daysRemaining

    def setSickDaysRemaining(self, daysRemaining: int) -> None:
        self.sickDaysRemaining = daysRemaining



    def getPtoRequests(self) -> list[PtoRequest]:
        return self.requestList
    
    def getPtoRequest(self, id: int) -> PtoRequest:

        for request in self.requestList:
            if request.requestID == id:
                return request


    def getPendingRequests(self):
        pendingList: list[PtoRequest] = []

        print("PendingRequests called")
        for request in self.requestList:
            if request.status == "Pending":
                print("adding request with id" +str(request.requestID))
                pendingList.append(request)

        return pendingList

    def removePtoRequest(self, id: int):
        for request in self.requestList:
            if request.requestID == id:
                self.requestList.remove(request)
                print("Request with id: "+ str(id)+ "removed")
                

    def recalculateBalance(self, numDays: int):
        self.ptoDaysConsumed += numDays
        self.ptoDaysRemaining -= numDays

