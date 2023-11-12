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
    
    def getEmployeeName(self) -> str:
        return self.employee.getName()