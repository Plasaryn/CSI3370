import tkinter as tk
from tkinter import messagebox
from pto_calendar_GUI import pto_calendar_GUI
from PtoRequest import PtoRequest

class PTORequestApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PTO Request")

        
        custom_font = ("Helvetica", 12)

        
        tk.Label(root, text="Reason for PTO:", font=custom_font, padx=10, pady=10).pack()
        self.pto_reason_entry = tk.Entry(root, font=custom_font, width=50)
        self.pto_reason_entry.pack(pady=10)

        
        submit_button = tk.Button(root, text="Submit PTO Request", font=custom_font, bg="#4CAF50", fg="white", command=self.submit_pto_request)
        submit_button.pack(pady=10)

    def submit_pto_request(self):
        pto_reason = self.pto_reason_entry.get()

        
        if not pto_reason:
            messagebox.showerror("Invalid PTO Request", "Please enter a reason for your PTO request.")
            return

        
        messagebox.showinfo("PTO Request Submitted", "Your PTO request has been submitted for review.")

       
        pto_calendar_app = pto_calendar_GUI(tk.Toplevel(self.root))
        pto_calendar_app.mainloop()
