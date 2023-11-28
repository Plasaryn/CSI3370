from Employee import Employee
from PtoRecord import PtoRecord
from PtoCalendar import PtoCalendar
from PtoRule import PtoRule
from UserAuthentication import UserAuthentication

class PTOMS:
    def __init__(self, company: str, department: str):
        self.company = company
        self.department = department
        self.records: list[PtoRecord] = []
        self.calendar = PtoCalendar()
        self.ptoRule = PtoRule(0)
        self.sessions: list(UserAuthentication) = []

    def getPtoRecord(self, id: int) -> PtoRecord:
        # To Do return a pto record from a given ID
        pass

        for ptorecord in self.records:
            if ptorecord.getId() == id:
                return ptorecord
            
    def newPtoRecord(self, 
            id: int,
            ptoDaysPermitted: int,
            sickDaysPermitted: int,
            employee: Employee) -> None:
        # Creates a new PtoRecord class and adds it to self.records
        self.records.append(
            PtoRecord(id, ptoDaysPermitted, sickDaysPermitted, employee)
        )

    
    
    def removePtoRecord(self, id: int) -> None:
        # Makes a matching list of the IDs for easy comparison
        # When after iterating through both the id list and record list
        # If the record id matches the target, the corresponding record
        # is removed from the pto list. 
        id_list = [x.getId() for x in self.records]

        for record_ids, record in zip(id_list, self.records):
            if id == record_ids:
                self.records.remove(record)

    def newPtoRule(self, minDaysAway: int)-> None:
        self.ptoRule.setMinDaysAway(minDaysAway)

    def getPtoRule(self) -> PtoRule:
        return self.ptoRule
    
    def getCalendar(self) -> PtoCalendar:
        return self.calendar

    def setCompany(self, company: str) -> None:
        self.company = company

    def getCompany(self) -> str:
        return self.company
    
    def setDepartment(self, department: str) -> None:
        self.department = department

    def getDepartment(self) -> str:
        return self.department

    # REMOVING SESSION TRACKING FUNCTIONALITY
    # def addSession(self, session: UserAuthenticationSession) -> None:
    #         self.sessions.add(session)

    # def removeSession(self, id: int) -> None:
    #     session_ids = [x.getId() for x in self.sessions]
    #     for sess_id, session in zip(session_ids, self.sessions):
    #         if  sess_id == id:
    #             self.sessions.remove(session)
