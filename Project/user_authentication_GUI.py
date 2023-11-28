import tkinter as tk
from tkinter import messagebox

class UserAuthenticationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("User Authentication")

        
        custom_font = ("Helvetica", 12)

        
        self.username_label = tk.Label(root, text="Username:", font=custom_font)
        self.username_label.pack(pady=10)
        self.username_entry = tk.Entry(root, font=custom_font)
        self.username_entry.pack(pady=10)

       
        self.password_label = tk.Label(root, text="Password:", font=custom_font)
        self.password_label.pack(pady=10)
        self.password_entry = tk.Entry(root, show="*", font=custom_font)
        self.password_entry.pack(pady=10)

        
        self.login_button = tk.Button(root, text="Login", command=self.authenticate, font=custom_font, bg="#4CAF50", fg="white")
        self.login_button.pack(pady=15)

    def authenticate(self):
        
        username = self.username_entry.get()
        password = self.password_entry.get()

        
        if username == "user" and password == "password":
            messagebox.showinfo("Authentication", "Login Successful!")
        else:
            messagebox.showerror("Authentication Error", "Invalid username or password")

if __name__ == "__main__":
    root = tk.Tk()
    app = UserAuthenticationApp(root)

    
    window_width = 300
    window_height = 200
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_position = int((screen_width - window_width) / 2)
    y_position = int((screen_height - window_height) / 2)
    root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

    
    root.configure(bg="#3498db")

    root.mainloop()
