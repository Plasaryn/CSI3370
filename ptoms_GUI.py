import tkinter as tk
from tkinter import ttk

def create_request_pto_window():
    request_pto_window = tk.Toplevel(window)
    request_pto_window.title("Request PTO")
    request_pto_window.geometry("400x200")  # Set the size of the window
    request_pto_window.configure(bg='#333333')  # Set the background color

    ttk.Label(request_pto_window, text="Start Date:", font=('Helvetica', 12, 'bold'), foreground='#3366cc', background='#333333').pack(pady=5)
    start_date_entry = ttk.Entry(request_pto_window, font=('Helvetica', 10))
    start_date_entry.pack(pady=5)

    ttk.Label(request_pto_window, text="End Date:", font=('Helvetica', 12, 'bold'), foreground='#3366cc', background='#333333').pack(pady=5)
    end_date_entry = ttk.Entry(request_pto_window, font=('Helvetica', 10))
    end_date_entry.pack(pady=5)

    submit_button = ttk.Button(request_pto_window, text="Submit", style="Colorful.TButton")
    submit_button.pack(pady=10)

def create_cancel_pto_window():
    cancel_pto_window = tk.Toplevel(window)
    cancel_pto_window.title("Cancel PTO")
    cancel_pto_window.geometry("400x150")  # Set the size of the window
    cancel_pto_window.configure(bg='#333333')  # Set the background color

    ttk.Label(cancel_pto_window, text="PTO Date:", font=('Helvetica', 12, 'bold'), foreground='#cc3366', background='#333333').pack(pady=5)
    pto_date_entry = ttk.Entry(cancel_pto_window, font=('Helvetica', 10))
    pto_date_entry.pack(pady=5)

    submit_button = ttk.Button(cancel_pto_window, text="Submit", style="Colorful.TButton")
    submit_button.pack(pady=10)

def create_view_pto_window():
    view_pto_window = tk.Toplevel(window)
    view_pto_window.title("View PTO")
    view_pto_window.geometry("400x300")  # Set the size of the window
    view_pto_window.configure(bg='#333333')  # Set the background color

    ttk.Label(view_pto_window, text="PTO Requests:", font=('Helvetica', 12, 'bold'), foreground='#33cc66', background='#333333').pack(pady=5)
    pto_list = tk.Listbox(view_pto_window, font=('Helvetica', 10), selectbackground='#ffcc00', bg='#333333', fg='#ffffff')
    pto_list.pack(pady=10)

def handle_click():
    selected_option = selected_option_var.get()

    if selected_option == 1:
        create_request_pto_window()
    elif selected_option == 2:
        create_cancel_pto_window()
    elif selected_option == 3:
        create_view_pto_window()

window = tk.Tk()
window.title("PTO Management System")
window.geometry("500x300")
window.configure(bg='#333333')  # Set the background color

# Use IntVar to represent the selected value
selected_option_var = tk.IntVar()

style = ttk.Style()
style.configure("TButton", padding=(10, 5), font=('Helvetica', 12))
style.configure("Colorful.TButton", background='#ffcc00', foreground='#3366cc', font=('Helvetica', 12, 'bold'))

request_pto_button = ttk.Radiobutton(window, text="Request PTO", value=1, variable=selected_option_var, style="Colorful.TButton")
cancel_pto_button = ttk.Radiobutton(window, text="Cancel PTO", value=2, variable=selected_option_var, style="Colorful.TButton")
view_pto_button = ttk.Radiobutton(window, text="View PTO", value=3, variable=selected_option_var, style="Colorful.TButton")

request_pto_button.pack(pady=10)
cancel_pto_button.pack(pady=10)
view_pto_button.pack(pady=10)

# Use command instead of binding to handle the click event
request_pto_button.config(command=handle_click)
cancel_pto_button.config(command=handle_click)
view_pto_button.config(command=handle_click)

window.mainloop()
