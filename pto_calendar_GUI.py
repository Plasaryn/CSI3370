import tkinter as tk
from tkinter import messagebox
import calendar

class PTOCalendarApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PTO Calendar")

        
        custom_font = ("Helvetica", 12)

        
        self.calendar_frame = tk.Frame(root, bg="#f0f0f0", padx=10, pady=10)
        self.calendar_frame.pack(pady=20)

        
        self.day_var = tk.StringVar()
        self.month_var = tk.StringVar()
        self.year_var = tk.StringVar()

        
        self.day_entry = tk.Entry(self.calendar_frame, textvariable=self.day_var, font=custom_font, width=3)
        self.month_entry = tk.Entry(self.calendar_frame, textvariable=self.month_var, font=custom_font, width=3)
        self.year_entry = tk.Entry(self.calendar_frame, textvariable=self.year_var, font=custom_font, width=5)

        self.day_entry.grid(row=0, column=0, padx=5)
        tk.Label(self.calendar_frame, text=" / ", font=custom_font, bg="#f0f0f0").grid(row=0, column=1)
        self.month_entry.grid(row=0, column=2, padx=5)
        tk.Label(self.calendar_frame, text=" / ", font=custom_font, bg="#f0f0f0").grid(row=0, column=3)
        self.year_entry.grid(row=0, column=4, padx=5)

        
        self.submit_button = tk.Button(root, text="Submit PTO", command=self.submit_pto, font=custom_font, bg="#007AFF", fg="white")
        self.submit_button.pack(pady=10)

        
        self.update_calendar()

        
        self.calendar_frame.bind("<Button-1>", self.handle_day_click)

        
        tk.Label(root, text="PTO Info:", font=("Helvetica", 12), bg="#f0f0f0").pack(pady=10)
        self.pto_info_entry = tk.Entry(root, font=custom_font)
        self.pto_info_entry.pack(pady=10)

    def update_calendar(self):
        year = 2023  
        month_calendar = calendar.monthcalendar(year, 1)  

        for widget in self.calendar_frame.winfo_children():
            widget.destroy()

        for col, day in enumerate(['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']):
            tk.Label(self.calendar_frame, text=day, font=("Helvetica", 10, "bold"), bg="#f0f0f0").grid(row=1, column=col)

        for row, week in enumerate(month_calendar, start=2):
            for col, day in enumerate(week):
                if day == 0:
                    tk.Label(self.calendar_frame, text="", bg="#f0f0f0").grid(row=row, column=col)
                else:
                    
                    day_label = tk.Label(self.calendar_frame, text=str(day), font=("Helvetica", 12), bg="#f0f0f0", cursor="hand2")
                    day_label.grid(row=row, column=col)
                    day_label.bind("<Button-1>", lambda event, selected_day=day: self.handle_day_click(event, selected_day))

    def handle_day_click(self, event, selected_day):
        
        selected_year = 2023  
        selected_month = 1   

        
        self.day_var.set(selected_day)
        self.month_var.set(selected_month)
        self.year_var.set(selected_year)

    def submit_pto(self):
        
        selected_day = int(self.day_var.get())
        selected_month = int(self.month_var.get())
        selected_year = int(self.year_var.get())

        
        pto_info = self.pto_info_entry.get()

        messagebox.showinfo("PTO Submission", f"PTO submitted for {selected_month:02d}/{selected_day:02d}/{selected_year}.\nPTO Info: {pto_info}")

if __name__ == "__main__":
    root = tk.Tk()
    app = PTOCalendarApp(root)

   
    window_width = 320
    window_height = 450
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_position = int((screen_width - window_width) / 2)
    y_position = int((screen_height - window_height) / 2)
    root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

    
    root.configure(bg="#f0f0f0")

    root.mainloop()
