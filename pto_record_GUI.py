import tkinter as tk

class PTORecordApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PTO Record")

        
        custom_font = ("Helvetica", 12)

        
        self.pto_info_frame = tk.Frame(root, padx=10, pady=10)
        self.pto_info_frame.pack()

        
        tk.Label(self.pto_info_frame, text="Total PTO:", font=custom_font).pack(pady=5)
        tk.Label(self.pto_info_frame, text="PTO Used:", font=custom_font).pack(pady=5)
        tk.Label(self.pto_info_frame, text="PTO Available:", font=custom_font).pack(pady=5)

       
        self.total_pto_entry = tk.Entry(self.pto_info_frame, font=custom_font, state=tk.DISABLED)
        self.total_pto_entry.pack(pady=5)

        self.pto_used_entry = tk.Entry(self.pto_info_frame, font=custom_font, state=tk.DISABLED)
        self.pto_used_entry.pack(pady=5)

        self.available_pto_entry = tk.Entry(self.pto_info_frame, font=custom_font, state=tk.DISABLED)
        self.available_pto_entry.pack(pady=5)

        
        self.total_pto = 20
        self.pto_used = 5
        self.update_pto_display()

    def update_pto_display(self):
        self.available_pto = self.total_pto - self.pto_used

        self.total_pto_entry.delete(0, tk.END)
        self.total_pto_entry.insert(0, str(self.total_pto))

        self.pto_used_entry.delete(0, tk.END)
        self.pto_used_entry.insert(0, str(self.pto_used))

        self.available_pto_entry.delete(0, tk.END)
        self.available_pto_entry.insert(0, str(self.available_pto))

if __name__ == "__main__":
    root = tk.Tk()
    app = PTORecordApp(root)

    
    window_width = 300
    window_height = 150
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_position = int((screen_width - window_width) / 2)
    y_position = int((screen_height - window_height) / 2)
    root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

    
    root.configure(bg="#f0f0f0")

    root.mainloop()
