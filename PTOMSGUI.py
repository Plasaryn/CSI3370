import random
import tkinter as tk
import datetime
from tkinter import messagebox
#from PTOMS import PTOMS
from PtoRecord import PtoRecord
from AuthorizationLevel import AuthorizationLevel
from PtoRequest import PtoRequest
from UserAuthenticationSystem import UserAuthenticationSystem
from User import User
from PtoStatus import PtoStatus
from PtoCalendar import PtoCalendar
from CalendarEvent import CalendarEvent

#class for the GUI of PTOMS system
class PTOMSGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("PTO Application")
        self.root.geometry("1200x800")
        self.pages = {}
        self.pto_records = []
        self.create_login_page()
        self.create_main_page_employee()
        self.create_main_page_manager()
        self.create_process_pto_landing_page()
        self.create_process_pto_prompt_page()
        self.create_pto_request_page()
        self.create_cancel_pto_page()
        self.create_pto_record_page()
        self.show_page("Login")

    # creates login page framework
    def create_login_page(self):
        page = tk.Frame(self.root)
        tk.Label(page, text="PTOMS", font=("Arial", 50, "bold"), bg='darkred', fg="white", height=3).pack(pady=(50,15))
        tk.Label(page, text="PAID TIME OFF MANAGEMENT SYSTEM", font=("Arial", 20, "bold")).pack(pady=(0,30))
        tk.Label(page, text="Username", font=("Arial", 14)).pack()
        self.username_entry = tk.Entry(page, font=("Arial", 12))
        self.username_entry.pack()
        tk.Label(page, text="Password", font=("Arial", 14)).pack()
        self.password_entry = tk.Entry(page, show="*", font=("Arial", 12))
        self.password_entry.pack()
        tk.Button(page, text="Login", command=lambda: final_PTOMS.login(app, userAuth), font=("Arial", 12), bg="darkred", fg="white").pack(pady=20)
        self.pages["Login"] = page

    #creates framework for employee main page
    def create_main_page_employee(self):
        page = tk.Frame(self.root)
        tk.Label(page, text="PTOMS", font=("Arial", 30, "bold"), bg='darkred', fg="white", width=50).pack(pady=(0, 15))
        tk.Label(page, text="Department Calendar", font=("Arial", 20, "bold")).pack()
        self.department_calendar_emp = tk.Text(page, height= 15, font=("Arial", 12))
        self.department_calendar_emp.pack()
        tk.Button(page, text="New PTO Request", font=("Arial", 12, 'bold'), bg='darkred', fg='white', width=20, relief=tk.RAISED, bd=5, command=lambda: final_PTOMS.prepare_request_pto_page(self)).pack(pady=10)
        tk.Button(page, text="View PTO Record", font=("Arial", 12, 'bold'), bg='darkred', fg='white', width=20, relief=tk.RAISED, bd=5, command=lambda: final_PTOMS.view_pto_record(self)).pack(pady=10)
        tk.Button(page, text="Log Out", font=("Arial", 12, 'bold'), bg='darkred', fg='white', width=20, relief=tk.RAISED, bd=5, command=lambda: self.show_page("Login")).pack(pady=10)
        self.pages["MainEmployee"] = page

    #creates framework for manager main page
    def create_main_page_manager(self):
        page = tk.Frame(self.root)
        tk.Label(page, text="PTOMS", font=("Arial", 30, "bold"), bg='darkred', fg="white", width=50).pack(pady=(0, 15))
        tk.Label(page, text="Department Calendar", font=("Arial", 20, "bold")).pack()
        self.department_calendar_mangr = tk.Text(page, height= 15, font=("Arial", 12))
        self.department_calendar_mangr.pack()
        tk.Button(page, text="Process Pending Requests", font=("Arial", 12, 'bold'), bg='darkred', fg='white', width=20, relief=tk.RAISED, bd=5, command=lambda: final_PTOMS.view_pending_requests(self)).pack(pady=10)
        tk.Button(page, text="Log Out", font=("Arial", 12, 'bold'), bg='darkred', fg='white', width=20, relief=tk.RAISED, bd=5, command=lambda: self.show_page("Login")).pack(pady=10)
        self.pages["MainManager"] = page

    # creates framework for process pto landing page
    def create_process_pto_landing_page(self):
        page = tk.Frame(self.root)
        tk.Label(page, text="PTOMS", font=("Arial", 30, "bold"), bg='darkred', fg="white", width=50).pack(pady=(0, 15))
        tk.Label(page, text="REQUESTS FOR REVIEW", font=("Arial", 18, "bold")).pack()
        self.requests_for_review = tk.Text(page, height=15, font=("Arial", 12))
        self.requests_for_review.pack()
        tk.Button(page, text="Process PTO Request", font=("Arial", 12, 'bold'), bg='darkred', fg='white', width=20, relief=tk.RAISED, bd=5, command=lambda: final_PTOMS.prepare_prompt_page(self)).pack(pady=10)
        tk.Button(page, text="Back", command=lambda: self.show_page("MainManager")).pack()
        self.pages["Process PTO Landing Page"] = page

    # creates framework for process pto prompting page
    def create_process_pto_prompt_page(self):
        page = tk.Frame(self.root)
        tk.Label(page, text="PTOMS", font=("Arial", 30, "bold"), bg='darkred', fg="white", width=50).pack(pady=(0, 15))
        tk.Label(page, text="REQUESTS FOR REVIEW", font=("Arial", 18, "bold")).pack()
        self.requests_list = tk.Text(page, height=10, font=("Arial", 12))
        self.requests_list.pack()
        tk.Label(page, text="Enter ID of Request to Process:", font=("Arial", 12)).pack(pady=(10,0))
        self.id_to_process_entry = tk.Entry(page, font=("Arial", 12))
        self.id_to_process_entry.pack()
        tk.Button(page, text="Get Request Data", font=("Arial", 12), command=lambda: final_PTOMS.view_request_to_process(self)).pack(pady=10)
        self.parent_record_title = tk.Text(page, height=1, font=("Arial", 12, "bold"))
        self.parent_record_title.pack()
        self.parent_record_info = tk.Text(page, height=3, font=("Arial", 12))
        self.parent_record_info.pack()
        self.request_in_review = tk.Text(page, height=6, font=("Arial", 12))
        self.request_in_review.pack()
        tk.Label(page, text="Enter Approval/Denial Message:", font=("Arial", 12)).pack(pady=(10,0))
        self.message_entry = tk.Entry(page, font=("Arial", 12))
        self.message_entry.pack()
        tk.Button(page, text="Approve Request", font=("Arial", 12, 'bold'), bg='darkred', fg='white', width=20, relief=tk.RAISED, bd=5, command=lambda: final_PTOMS.processPTORequest(self, PtoStatus.Approved)).pack(pady=(10,0))
        tk.Button(page, text="Deny Request", font=("Arial", 12, 'bold'), bg='darkred', fg='white', width=20, relief=tk.RAISED, bd=5, command=lambda: final_PTOMS.processPTORequest(self, PtoStatus.Denied)).pack(pady=(2, 10))
        tk.Button(page, text="Back", font=("Arial", 12, 'bold'), command=lambda: self.show_page("MainManager")).pack()
        self.pages["Process PTO Prompt Page"] = page

    # creates framework for cancel pto page
    def create_cancel_pto_page(self):
        page = tk.Frame(self.root)
        tk.Label(page, text="PTOMS", font=("Arial", 30, "bold"), bg='darkred', fg="white", width=50).pack(pady=(0, 15))
        self.cancel_pto_record_title = tk.Text(page, height=1, font=("Arial", 12, 'bold'))
        self.cancel_pto_record_title.pack()
        self.cancel_pto_record_text = tk.Text(page, height=3, font=("Arial", 12))
        self.cancel_pto_record_text.pack()
        self.cancel_pto_record_requests = tk.Text(page, height=15, font=("Arial", 12))
        self.cancel_pto_record_requests.pack()
        tk.Label(page, text="CANCEL PTO REQUEST", font=("Arial", 16, 'bold')).pack(pady=(10, 0))
        tk.Label(page, text="Enter Request ID:", font=("Arial", 12)).pack()
        self.cancel_request_id_entry = tk.Entry(page, font=("Arial", 12))
        self.cancel_request_id_entry.pack()
        tk.Button(page, text="Cancel PTO Request", font=("Arial", 12, 'bold'), bg='darkred', fg='white', width=20, relief=tk.RAISED, bd=5, command=lambda: final_PTOMS.cancelPTORequest(self)).pack(pady=10)
        tk.Button(page, text="Back", font=("Arial", 12), command=lambda: self.show_page("MainEmployee")).pack()
        self.pages["Cancel PTO"] = page

    # creates framework for new pto request page
    def create_pto_request_page(self):
        page = tk.Frame(self.root)
        tk.Label(page, text="PTOMS", font=("Arial", 30, "bold"), bg='darkred', fg="white", width=50).pack(pady=(0, 15))
        self.cr_pto_record_title = tk.Text(page, height=1, font=("Arial", 12, 'bold'))
        self.cr_pto_record_title.pack()
        self.cr_pto_record_text = tk.Text(page, height=3, font=("Arial", 12))
        self.cr_pto_record_text.pack()
        self.cr_pto_record_requests = tk.Text(page, height=15, font=("Arial", 12))
        self.cr_pto_record_requests.pack()
        tk.Label(page, text="NEW PTO REQUEST", font=("Arial", 16, 'bold')).pack(pady=(10, 0))
        tk.Label(page, text="Start Date (MM/DD/YYYY):", font=("Arial", 12)).pack(pady=(10,0))
        self.start_date_entry = tk.Entry(page, font=("Arial", 12))
        self.start_date_entry.pack()
        tk.Label(page, text="End Date (MM/DD/YYYY):", font=("Arial", 12)).pack()
        self.end_date_entry = tk.Entry(page, font=("Arial", 12))
        self.end_date_entry.pack(pady=(0,10))
        tk.Button(page, text="Submit", font=("Arial", 12, 'bold'), bg='darkred', fg='white', width=20, relief=tk.RAISED, bd=5, command=lambda: final_PTOMS.submitPTORequest(self)).pack(pady=10)
        tk.Button(page, text="Back", font=("Arial", 12), command=lambda: self.show_page("MainEmployee")).pack()
        self.pages["PTO Request"] = page

    # creates framework for pto record view page
    def create_pto_record_page(self):
        page = tk.Frame(self.root)
        tk.Label(page, text="PTOMS", font=("Arial", 30, "bold"), bg='darkred', fg="white", width=50).pack(pady=(0, 15))
        self.pto_record_title = tk.Text(page, height=1, font=("Arial", 12, 'bold'))
        self.pto_record_title.pack()
        self.pto_record_text = tk.Text(page, height=3, font=("Arial", 12))
        self.pto_record_text.pack()
        self.pto_record_requests = tk.Text(page, height= 15, font=("Arial", 12))
        self.pto_record_requests.pack()
        tk.Button(page, text="Cancel PTO Request", font=("Arial", 12, 'bold'), bg='darkred', fg='white', width=20, relief=tk.RAISED, bd=5, command=lambda: final_PTOMS.prepare_cancel_pto_page(self)).pack(pady=10)
        tk.Button(page, text="Back", command=lambda: self.show_page("MainEmployee")).pack()
        self.pages["PTO Record"] = page

    def show_page(self, page_name):
        page = self.pages[page_name]
        page.tkraise()


# class for main functionality of PTOMS system
class PTOMS:
    def __init__(self, company: str, department: str):
        self.company = company
        self.department = department
        self.records: list[PtoRecord] = []
        self.currentUserID = 0
        self.calendar = PtoCalendar()

    def getPtoRecord(self, id: int) -> PtoRecord:
        for ptorecord in self.records:
            if ptorecord.getId() == id:
                return ptorecord

    def login(self, currentGUI: PTOMSGUI, currentAuthSystem: UserAuthenticationSystem):

        username = currentGUI.username_entry.get()
        password = currentGUI.password_entry.get()
        matchedUser = currentAuthSystem.validateAuthentication(username, password)

        matchedUserID = 0

        #if there is a matched user found, assign user ID of found user to currentUserID
        if matchedUser:
            matchedUserID = matchedUser.userID
            self.setCurrentUserID(matchedUserID)

            if matchedUser.authLevel == "employee":
                currentGUI.show_page("MainEmployee")
            elif matchedUser.authLevel == "manager":
                currentGUI.show_page("MainManager")

        else:
            messagebox.showerror("LOGIN ERROR", "Incorrect username or password. Please try again.")

    def submitPTORequest(self, currentGUI: PTOMSGUI):

        start_date = currentGUI.start_date_entry.get()
        end_date = currentGUI.end_date_entry.get()

        sMonth = int(start_date[0:2])
        sDay = int(start_date[3:5])
        sYear = int(start_date[6:10])

        eMonth = int(end_date[0:2])
        eDay = int(end_date[3:5])
        eYear = int(end_date[6:10])

        sDate = datetime.datetime(sYear, sMonth, sDay)
        eDate = datetime.datetime(eYear, eMonth, eDay)

        #generate random request ID
        requestID = random.randint(1, 1000)

        #get current PTO record we are logged into
        chosenPTORecord = self.getPtoRecord(self.currentUserID)

        #create new PTORequest
        newPtoRequest = PtoRequest(requestID, chosenPTORecord.getEmpName(), chosenPTORecord.getId(), sDate, eDate)

        # add new request to current PTO record
        chosenPTORecord.addPtoRequest(newPtoRequest)
        messagebox.showinfo("MESSAGE", f"Your PTO request for {start_date} to {end_date} has been submitted for review.")
        currentGUI.show_page("MainEmployee")

    def prepare_cancel_pto_page(self, currentGUI: PTOMSGUI):
        chosenPTORecord = self.getPtoRecord(self.getCurrentUserID())
        PTORecordTitle = str(chosenPTORecord.empName).upper() + "'S PTO RECORD"
        PTORecordInfo = chosenPTORecord.getPTORecordInfoString()
        PTORequestsInfo = chosenPTORecord.getAllPTORequestsInfo()

        currentGUI.cancel_pto_record_title.delete(1.0, tk.END)
        currentGUI.cancel_pto_record_title.insert(tk.END, PTORecordTitle)

        currentGUI.cancel_pto_record_text.delete(1.0, tk.END)
        currentGUI.cancel_pto_record_text.insert(tk.END, PTORecordInfo)

        currentGUI.cancel_pto_record_requests.delete(1.0, tk.END)
        currentGUI.cancel_pto_record_requests.insert(tk.END, PTORequestsInfo)

        currentGUI.show_page("Cancel PTO")


    def prepare_request_pto_page(self, currentGUI: PTOMSGUI):
        chosenPTORecord = self.getPtoRecord(self.getCurrentUserID())
        PTORecordTitle = str(chosenPTORecord.empName).upper() + "'S PTO RECORD"
        PTORecordInfo = chosenPTORecord.getPTORecordInfoString()
        PTORequestsInfo = chosenPTORecord.getAllPTORequestsInfo()

        currentGUI.cr_pto_record_title.delete(1.0, tk.END)
        currentGUI.cr_pto_record_title.insert(tk.END, PTORecordTitle)

        currentGUI.cr_pto_record_text.delete(1.0, tk.END)
        currentGUI.cr_pto_record_text.insert(tk.END, PTORecordInfo)

        currentGUI.cr_pto_record_requests.delete(1.0, tk.END)
        currentGUI.cr_pto_record_requests.insert(tk.END, PTORequestsInfo)

        currentGUI.show_page("PTO Request")

    def cancelPTORequest(self, currentGUI: PTOMSGUI):

        request_id_to_cancel = int(currentGUI.cancel_request_id_entry.get())

        # get current PTO record we are logged into
        chosenPTORecord = self.getPtoRecord(self.getCurrentUserID())

        # get request to cancel
        requestToCancel = chosenPTORecord.getPtoRequest(request_id_to_cancel)
        numDays = requestToCancel.numDays

        chosenPTORecord.removePtoRequest(request_id_to_cancel)

        if requestToCancel.status == PtoStatus.Approved.name:
            chosenPTORecord.recalculateBalance(-numDays)
            self.calendar.removeEvent(request_id_to_cancel)
            DeptCalendarView = final_PTOMS.calendar.getCalendarEventsToString()
            currentGUI.department_calendar_emp.delete(1.0, tk.END)
            currentGUI.department_calendar_emp.insert(tk.END, DeptCalendarView)
            currentGUI.department_calendar_mangr.delete(1.0, tk.END)
            currentGUI.department_calendar_mangr.insert(tk.END, DeptCalendarView)

        self.view_pto_record(currentGUI)
        messagebox.showinfo("MESSAGE", f"PTO Request with ID: {request_id_to_cancel} cancelled successfully.")

        currentGUI.show_page("PTO Record")

    def view_pto_record(self, currentGUI: PTOMSGUI):

        chosenPTORecord = self.getPtoRecord(self.getCurrentUserID())

        #set strings to be put into textboxes
        PTORecordTitle = str(chosenPTORecord.empName).upper() + "'S PTO RECORD"
        PTORecordInfo = chosenPTORecord.getPTORecordInfoString()
        PTORequestsInfo = chosenPTORecord.getAllPTORequestsInfo()


        currentGUI.pto_record_title.delete(1.0, tk.END)
        currentGUI.pto_record_title.insert(tk.END, PTORecordTitle)

        currentGUI.pto_record_text.delete(1.0, tk.END)
        currentGUI.pto_record_text.insert(tk.END, PTORecordInfo)

        currentGUI.pto_record_requests.delete(1.0, tk.END)
        currentGUI.pto_record_requests.insert(tk.END, PTORequestsInfo)

        currentGUI.show_page("PTO Record")

    def view_pending_requests(self, currentGUI: PTOMSGUI):

        allPendingRequests: list[PtoRequest] = []
        for record in self.records:
            allPendingRequests.extend(record.getPendingRequests())

        stringPendingRequests = ""

        #source for checking if all strings empty: https://flexiple.com/python/check-if-list-is-empty-python
        if not allPendingRequests:
            stringPendingRequests = "No Pending Requests!"
        else:
            for request in allPendingRequests:
                stringPendingRequests = stringPendingRequests + request.getPTORequestString() + "\n-------------------------------\n"

        currentGUI.requests_for_review.delete(1.0, tk.END)
        currentGUI.requests_for_review.insert(tk.END, stringPendingRequests)

        currentGUI.show_page("Process PTO Landing Page")

    def prepare_prompt_page(self, currentGUI: PTOMSGUI):
        allPendingRequests: list[PtoRequest] = []
        for record in self.records:
            allPendingRequests.extend(record.getPendingRequests())

        stringPendingRequests = ""

        # source for checking if all strings empty: https://flexiple.com/python/check-if-list-is-empty-python
        if not allPendingRequests:
            stringPendingRequests = "No Pending Requests!"
        else:
            for request in allPendingRequests:
                stringPendingRequests = stringPendingRequests + request.getPTORequestString() + "\n-----------------------------------------------\n"

        currentGUI.requests_list.delete(1.0, tk.END)
        currentGUI.requests_list.insert(tk.END, stringPendingRequests)

        currentGUI.show_page("Process PTO Prompt Page")

    def view_request_to_process(self, currentGUI: PTOMSGUI):


        idToProcess = int(currentGUI.id_to_process_entry.get())

        searchResultsList: list[PtoRequest] = []

        stringRequestInReview = ""
        parentRecord = None

        for record in self.records:
            searchResultsList.append(record.getPtoRequest(idToProcess))

        for request in searchResultsList:
            if request is not None:
                stringRequestInReview = request.getPTORequestString()
                parentRecord = self.getPtoRecord(request.recordID)

        parentRecordString = parentRecord.getPTORecordInfoString()

        parentRecordTitle = str(parentRecord.empName).upper() + "'S PTO RECORD"

        currentGUI.parent_record_title.delete(1.0, tk.END)
        currentGUI.parent_record_title.insert(tk.END, parentRecordTitle)

        currentGUI.parent_record_info.delete(1.0, tk.END)
        currentGUI.parent_record_info.insert(tk.END, parentRecordString)

        currentGUI.request_in_review.delete(1.0, tk.END)
        currentGUI.request_in_review.insert(tk.END, stringRequestInReview)

        currentGUI.show_page("Process PTO Prompt Page")

    def processPTORequest(self, currentGUI: PTOMSGUI, status: PtoStatus):

        idToProcess = int(currentGUI.id_to_process_entry.get())
        requestMessage = currentGUI.message_entry.get()
        searchResultsList: list[PtoRequest] = []

        for record in self.records:
            searchResultsList.append(record.getPtoRequest(idToProcess))

        for request in searchResultsList:
            if request is not None:
                print("found request with id " +str(idToProcess))
                requestToProcess = request
                parentRecordID = request.recordID
                parentRecord = self.getPtoRecord(parentRecordID)
                numDays = requestToProcess.getNumDays()

                if status == PtoStatus.Approved:
                    requestToProcess.approve(requestMessage)
                    newCalEvent = CalendarEvent(requestToProcess.requestID, requestToProcess.startDate, requestToProcess.endDate, requestToProcess.requestEmpName)
                    self.calendar.addEvent(newCalEvent)
                    parentRecord.recalculateBalance(numDays)

                    DeptCalendarView = final_PTOMS.calendar.getCalendarEventsToString()
                    currentGUI.department_calendar_emp.delete(1.0, tk.END)
                    currentGUI.department_calendar_emp.insert(tk.END, DeptCalendarView)
                    currentGUI.department_calendar_mangr.delete(1.0, tk.END)
                    currentGUI.department_calendar_mangr.insert(tk.END, DeptCalendarView)
                    messagebox.showinfo("MESSAGE", f"Request ID: {idToProcess} was Approved successfully.")

                if status == PtoStatus.Denied:
                    requestToProcess.deny(requestMessage)
                    messagebox.showinfo("MESSAGE", f"Request ID: {idToProcess} was Denied successfully.")

        currentGUI.show_page("MainManager")

    def setCurrentUserID(self, newID: int):
        self.currentUserID = newID

    def getCurrentUserID(self):
        return self.currentUserID


# main method to start PTOMS and initialize it with users and employees.
if __name__ == "__main__":

    final_PTOMS = PTOMS("Company", "Accounting")
    # initialize PTO Records
    PTORec1 = PtoRecord(1, 20, 20, "Anderson")
    PTORec2 = PtoRecord(2, 22, 22, "Craig")
    PTORec3 = PtoRecord(3, 23, 23, "Scott")
    PTORec4 = PtoRecord(4, 21, 21, "Tyler")
    PTORec5 = PtoRecord(5, 19, 19, "Jared")

    # add PTO Records to PTO Record List in PTOMS
    final_PTOMS.records.extend([PTORec1, PTORec2, PTORec3, PTORec4, PTORec5])

    userAuth = UserAuthenticationSystem()
    # initialize Users
    User1 = User(1, "Anderson", "test123", AuthorizationLevel.employee.name)
    User2 = User(2, "Craig", "hello123", AuthorizationLevel.employee.name)
    User3 = User(3, "Scott", "testing123", AuthorizationLevel.employee.name)
    User4 = User(4, "Tyler", "password123", AuthorizationLevel.employee.name)
    User5 = User(5, "Jared", "password321", AuthorizationLevel.employee.name)
    User6 = User(6, "MikeManager", "managerpass", AuthorizationLevel.manager.name)
    # add users to Userlist in User Authentication System
    userAuth.usersList.extend([User1, User2, User3, User4, User5, User6])

    # to start the TKINTER GUI
    root = tk.Tk()
    app = PTOMSGUI(root)
    for page in app.pages.values():
      page.grid(row=0, column=0, sticky="nsew")
    root.mainloop()
