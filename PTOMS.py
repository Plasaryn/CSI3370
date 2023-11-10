from Employee import Employee
from PtoRecord import PtoRecord
from Calendar import Calendar
from PtoRule import PtoRule

class PTOMS:
    def __init__(self, company: str, department: str):
        self.company = company
        self.department = department
        self.ptoRecords = [] # list[PtoRecord]
        self.calendar = Calendar()
        self.ptoRule = PtoRule()

    def getPtoRecord(self, id: int) -> PtoRecord:
        # To Do return a pto record from a given ID
        pass

        for ptorecord in self.ptoRecords:
            if ptorecord.getId() == id:
                return ptorecord
            
    def newPtoRecord(self, 
            id: int,
            ptoDaysPermitted: int,
            sickDaysPermitted: int,
            employee: Employee) -> None:
        # Creates a new PtoRecord class and adds it to self.ptoRecords
        self.ptoRecords.append(
            PtoRecord(id, ptoDaysPermitted, sickDaysPermitted, employee)
        )

    
    
    def removePtoRecord(self, id: int) -> None:
        # Makes a matching list of the IDs for easy comparison
        # When after iterating through both the id list and record list
        # If the record id matches the target, the corresponding record
        # is removed from the pto list. 
        id_list = [x.getId() for x in self.ptoRecords]

        for record_ids, record in zip(id_list, self.ptoRecords):
            if id == record_ids:
                self.ptoRecords.remove(record)

    def newPtoRule(self, minDaysAway: int)-> None:
        self.ptoRule.setMinDatesAway(minDaysAway)

    def getPtoRule(self) -> PtoRule:
        return self.ptoRule
    
    def getCalendar(self) -> Calendar:
        return self.calendar




