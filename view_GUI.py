import tkinter as tk
from tkinter import messagebox

class PTOApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PTO Application")
        self.root.geometry("625x425")
        self.root.configure(bg='lightgray')
        self.pages = {}
        self.pto_records = []
        self.create_login_page()
        self.create_main_page()
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
        tk.Button(page, text="Login", command=self.login, font=("Arial", 12), bg='darkred', fg='white').pack()
        self.pages["Login"] = page


    def create_main_page(self):
        page = tk.Frame(self.root, bg='lightgray')
        tk.Button(page, text="PTO Request", font=("Arial", 14, 'bold'), bg='darkred', fg='white', width=20, relief=tk.RAISED, bd=5, command=lambda: self.show_page("PTO Request")).pack(pady=10)
        tk.Button(page, text="PTO Record", font=("Arial", 14, 'bold'), bg='darkred', fg='white', width=20, relief=tk.RAISED, bd=5, command=self.show_pto_record).pack(pady=10)
        tk.Button(page, text="Cancel PTO", font=("Arial", 14, 'bold'), bg='darkred', fg='white', width=20, relief=tk.RAISED, bd=5, command=lambda: self.show_page("Cancel PTO")).pack(pady=10)
        self.pages["Main"] = page

    def create_cancel_pto_page(self):
        page = tk.Frame(self.root)
        tk.Label(page, text="Start Date").pack()
        self.cancel_start_date_entry = tk.Entry(page)
        self.cancel_start_date_entry.pack()
        tk.Label(page, text="End Date").pack()
        self.cancel_end_date_entry = tk.Entry(page)
        self.cancel_end_date_entry.pack()
        tk.Button(page, text="Cancel", command=self.cancel_pto).pack()
        tk.Button(page, text="Back", command=lambda: self.show_page("Main")).pack()
        self.pages["Cancel PTO"] = page

    def cancel_pto(self):
        start_date = self.cancel_start_date_entry.get()
        end_date = self.cancel_end_date_entry.get()
        pto_to_cancel = f"PTO from {start_date} to {end_date}"
        if pto_to_cancel in self.pto_records:
            self.pto_records.remove(pto_to_cancel)
        self.show_page("Main")


    def create_pto_request_page(self):
        page = tk.Frame(self.root)
        tk.Label(page, text="Start Date").pack()
        self.start_date_entry = tk.Entry(page)
        self.start_date_entry.pack()
        tk.Label(page, text="End Date").pack()
        self.end_date_entry = tk.Entry(page)
        self.end_date_entry.pack()
        tk.Button(page, text="Submit", command=self.submit_pto_request).pack()
        tk.Button(page, text="Back", command=lambda: self.show_page("Main")).pack()
        self.pages["PTO Request"] = page

    def create_pto_record_page(self):
        page = tk.Frame(self.root)
        self.pto_record_text = tk.Text(page)
        self.pto_record_text.pack()
        tk.Button(page, text="Back", command=lambda: self.show_page("Main")).pack()
        self.pages["PTO Record"] = page

    def show_page(self, page_name):
        page = self.pages[page_name]
        page.tkraise()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
       
        if username == "craig" and password == "testing":
            self.show_page("Main")
        else:
            messagebox.showerror("Login error", "Incorrect username or password")

    def submit_pto_request(self):
        start_date = self.start_date_entry.get()
        end_date = self.end_date_entry.get()
        self.pto_records.append(f"PTO from {start_date} to {end_date}")
        self.show_page("Main")

    def show_pto_record(self):
        self.pto_record_text.delete(1.0, tk.END)
        for record in self.pto_records:
            self.pto_record_text.insert(tk.END, record + "\n")
        self.show_page("PTO Record")

root = tk.Tk()
app = PTOApp(root)
for page in app.pages.values():
    page.grid(row=0, column=0, sticky="nsew")
root.mainloop()