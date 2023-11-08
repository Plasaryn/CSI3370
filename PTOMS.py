class PTOMS:
    def __init__(self, company: str, department: str):
        self.company = company
        self.department = department
        self.ptoRecords = [] # list[PtoRecord]

    def getPtoRecord(self, id: int) -> PtoRecord:
        # To Do return a pto record from a given ID
        pass

class PtoRecord:
    def __init__(self, 
            id: int,
            ptoDaysPermitted: int,
            sickDaysPermitted: int):
        
        self.id = id
        self.ptoDaysPermitted = ptoDaysPermitted
        self.sickDaysPermitted = sickDaysPermitted
        self.ptoDaysConsumed = 0
        self.sickDaysConsumed = 0
        self.ptoDaysRemaining = ptoDaysPermitted
        self.sickDaysRemaining = sickDaysPermitted