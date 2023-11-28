from Employee import Employee

class PtoRecord:
    def __init__(self, 
            id: int,
            ptoDaysPermitted: int,
            sickDaysPermitted: int,
            employee: Employee
            ):
        
        self.id = id
        self.ptoDaysPermitted = ptoDaysPermitted
        self.sickDaysPermitted = sickDaysPermitted
        self.ptoDaysConsumed = 0
        self.sickDaysConsumed = 0
        self.ptoDaysRemaining = ptoDaysPermitted
        self.sickDaysRemaining = sickDaysPermitted
        self.employee = employee

    def __str__(self) -> str:
        return f"id: {self.id}"

    def getId(self) -> int:
        return self.id
    
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
    
    def getEmployeeName(self) -> str:
        return self.employee.getName()
    
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

<<<<<<< Updated upstream
=======
    def addPtoRequest(self, request: PtoRequest) -> None:
        self.requestList.append(request)

    def getPtoRequests(self) -> list[PtoRequest]:
        return self.requestList
    
    def getPtoRequest(self, id: int) -> None:
        id_ls = [x.getId() for x in self.requestList]
        for req_id,request in zip(id_ls, self.requestList):
            if req_id == id:
                return request
            
    def removePtoRequest(self,id): 
        id_ls = [x.getId() for x in self.requestList]
        for req_id,request in zip(id_ls, self.requestList):
            if req_id == id:
                self.requestList.remove(request)

>>>>>>> Stashed changes
    def getEmployee(self) -> None:
        return self.employee
