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

class PTOMSGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("PTO Application")
        self.root.geometry("650x800")
        self.root.configure(bg='lightgray')
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

    def create_login_page(self):
        page = tk.Frame(self.root, bg='lightgray')
        tk.Label(page, text="Username", font=("Arial", 14), bg='lightgray').pack()
        self.username_entry = tk.Entry(page, font=("Arial", 12))
        self.username_entry.pack()
        tk.Label(page, text="Password", font=("Arial", 14), bg='lightgray').pack()
        self.password_entry = tk.Entry(page, show="*", font=("Arial", 12))
        self.password_entry.pack()
        tk.Button(page, text="Login", command=lambda: final_PTOMS.login(app, userAuth), font=("Arial", 12), bg="darkred", fg="white").pack()
        self.pages["Login"] = page


    def create_main_page_employee(self):
        page = tk.Frame(self.root, bg='lightgray')
        tk.Button(page, text="PTO Request", font=("Arial", 14, 'bold'), bg='darkred', fg='white', width=20, relief=tk.RAISED, bd=5, command=lambda: self.show_page("PTO Request")).pack(pady=10)
        tk.Button(page, text="PTO Record", font=("Arial", 14, 'bold'), bg='darkred', fg='white', width=20, relief=tk.RAISED, bd=5, command=lambda: final_PTOMS.view_pto_record(self)).pack(pady=10)
        tk.Button(page, text="Log Out", font=("Arial", 14, 'bold'), bg='darkred', fg='white', width=20, relief=tk.RAISED, bd=5, command=lambda: self.show_page("Login")).pack(pady=10)
        self.pages["MainEmployee"] = page

    def create_main_page_manager(self):
        page = tk.Frame(self.root, bg='lightgray')
        tk.Button(page, text="Process Pending Requests", font=("Arial", 14, 'bold'), bg='darkred', fg='white', width=20, relief=tk.RAISED, bd=5, command=lambda: final_PTOMS.view_pending_requests(self)).pack(pady=10)
        tk.Button(page, text="Log Out", font=("Arial", 14, 'bold'), bg='darkred', fg='white', width=20, relief=tk.RAISED, bd=5, command=lambda: self.show_page("Login")).pack(pady=10)
        self.pages["MainManager"] = page

    def create_process_pto_landing_page(self):
        page = tk.Frame(self.root)
        self.process_pto_title = tk.Text(page, height=1)
        self.process_pto_title.pack()
        self.requests_for_review = tk.Text(page)
        self.requests_for_review.pack()
        tk.Button(page, text="Process PTO Request", font=("Arial", 14, 'bold'), bg='darkred', fg='white', width=20, relief=tk.RAISED, bd=5, command=lambda: self.show_page("Process PTO Prompt Page")).pack(pady=10)
        tk.Button(page, text="Back", command=lambda: self.show_page("MainManager")).pack()
        self.pages["Process PTO Landing Page"] = page

    def create_process_pto_prompt_page(self):
        page = tk.Frame(self.root)
        tk.Label(page, text="Enter ID of Request to Process:").pack()
        self.id_to_process_entry = tk.Entry(page)
        self.id_to_process_entry.pack()
        tk.Button(page, text="Get Data", command=lambda: final_PTOMS.view_request_to_process(self)).pack()
        self.request_in_review = tk.Text(page)
        self.request_in_review.pack()
        tk.Label(page, text="Enter Approval/Denial Message:").pack()
        self.message_entry = tk.Entry(page)
        self.message_entry.pack()
        tk.Button(page, text="Approve Request", font=("Arial", 14, 'bold'), bg='darkred', fg='white', width=20, relief=tk.RAISED, bd=5, command=lambda: final_PTOMS.processPTORequest(self, PtoStatus.Approved)).pack(pady=10)
        tk.Button(page, text="Deny Request", font=("Arial", 14, 'bold'), bg='darkred', fg='white', width=20, relief=tk.RAISED, bd=5, command=lambda: final_PTOMS.processPTORequest(self, PtoStatus.Denied)).pack(pady=10)
        tk.Button(page, text="Back", command=lambda: self.show_page("MainManager")).pack()
        self.pages["Process PTO Prompt Page"] = page

    def create_cancel_pto_page(self):
        page = tk.Frame(self.root)
        tk.Label(page, text="Enter Request ID").pack()
        self.cancel_request_id_entry = tk.Entry(page)
        self.cancel_request_id_entry.pack()
        tk.Button(page, text="Cancel PTO Request", command=lambda: final_PTOMS.cancelPTORequest(self)).pack()
        tk.Button(page, text="Back", command=lambda: self.show_page("MainEmployee")).pack()
        self.pages["Cancel PTO"] = page


    def create_pto_request_page(self):
        page = tk.Frame(self.root)
        tk.Label(page, text="Start Date (MM/DD/YYYY)").pack()
        self.start_date_entry = tk.Entry(page)
        self.start_date_entry.pack()
        tk.Label(page, text="End Date (MM/DD/YYYY)").pack()
        self.end_date_entry = tk.Entry(page)
        self.end_date_entry.pack()
        tk.Button(page, text="Submit", command=lambda: final_PTOMS.submitPTORequest(self)).pack()
        tk.Button(page, text="Back", command=lambda: self.show_page("MainEmployee")).pack()
        self.pages["PTO Request"] = page

    def create_pto_record_page(self):
        page = tk.Frame(self.root)
        self.pto_record_title = tk.Text(page, height=1)
        self.pto_record_title.pack()
        self.pto_record_text = tk.Text(page, height=3)
        self.pto_record_text.pack()
        self.pto_record_requests = tk.Text(page)
        self.pto_record_requests.pack()
        tk.Button(page, text="Cancel PTO", font=("Arial", 14, 'bold'), bg='darkred', fg='white', width=20, relief=tk.RAISED, bd=5, command=lambda: self.show_page("Cancel PTO")).pack(pady=10)
        tk.Button(page, text="Back", command=lambda: self.show_page("MainEmployee")).pack()
        self.pages["PTO Record"] = page

    def show_page(self, page_name):
        page = self.pages[page_name]
        page.tkraise()



class PTOMS:
    def __init__(self, company: str, department: str):
        self.company = company
        self.department = department
        self.records: list[PtoRecord] = []
        self.currentUserID = 0

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

    # def placePTORequest(self):
    #     test
    #

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

    def cancelPTORequest(self, currentGUI: PTOMSGUI):

        request_id_to_cancel = int(currentGUI.cancel_request_id_entry.get())
        print(request_id_to_cancel)
        # get current PTO record we are logged into
        chosenPTORecord = self.getPtoRecord(self.getCurrentUserID())

        chosenPTORecord.removePtoRequest(request_id_to_cancel)
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

        currentGUI.process_pto_title.delete(1.0, tk.END)
        currentGUI.process_pto_title.insert(tk.END, "REQUESTS FOR REVIEW")

        currentGUI.requests_for_review.delete(1.0, tk.END)
        currentGUI.requests_for_review.insert(tk.END, stringPendingRequests)

        currentGUI.show_page("Process PTO Landing Page")

    def view_request_to_process(self, currentGUI: PTOMSGUI):

        idToProcess = int(currentGUI.id_to_process_entry.get())

        searchResultsList: list[PtoRequest] = []

        stringRequestInReview = ""

        for record in self.records:
            searchResultsList.append(record.getPtoRequest(idToProcess))

        for request in searchResultsList:
            if request is not None:
                stringRequestInReview = request.getPTORequestString()

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
                    parentRecord.recalculateBalance(numDays)
                    messagebox.showinfo("MESSAGE", f"Request ID: {idToProcess} was Approved successfully.")

                if status == PtoStatus.Denied:
                    requestToProcess.deny(requestMessage)
                    messagebox.showinfo("MESSAGE", f"Request ID: {idToProcess} was Denied successfully.")

            # else:
            #     messagebox.showerror("ERROR","The Request you selected is not Pending. Please try again.")

        currentGUI.show_page("MainManager")


    def setCurrentUserID(self, newID: int):
        self.currentUserID = newID

    def getCurrentUserID(self):
        return self.currentUserID
    #
    # def startPTOMS(self):
    #
    # def processPendingRequests(self):
    #
    # def getPendingRequests(self):
    #
    # def selectRequestToProcess(self):
    #
    # def approvePTORequest(self):




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

    root = tk.Tk()
    app = PTOMSGUI(root)
    for page in app.pages.values():
      page.grid(row=0, column=0, sticky="nsew")
    root.mainloop()
