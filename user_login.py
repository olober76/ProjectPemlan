import csv
import tkinter as tk
from tkinter import messagebox

def login_window():
   login_window = tk.Tk()
   login_window.title("Login System")

   username_label = tk.Label(login_window, text="Username")
   username_label.pack()

   username_entry = tk.Entry(login_window)
   username_entry.pack()

   password_label = tk.Label(login_window, text="Password")
   password_label.pack()

   password_entry = tk.Entry(login_window, show="*")
   password_entry.pack()

   def login():
       username = username_entry.get()
       password = password_entry.get()
       with open("users.csv") as csvfile:
           database = csv.DictReader(csvfile)
           for row in database:
               if row["username"] == username and row["password"] == password:
                  messagebox.showinfo("Login", "Login successful!")
                  login_window.destroy()
                  main_window()
                  break
           else:
               messagebox.showerror("Login", "Username or password incorrect. Please try again.")

   login_button = tk.Button(login_window, text="Login", command=login)
   login_button.pack()

   login_window.mainloop()

def main_window():
  main_window = tk.Tk()
  main_window.title("Main System")

  login_button = tk.Button(main_window, text="Login", command=login_window)
  login_button.pack()

  register_button = tk.Button(main_window, text="Register", command=register_window)
  register_button.pack()

  main_window.mainloop()


def register_window():
   register_window = tk.Tk()
   register_window.title("Register System")

   username_label = tk.Label(register_window, text="Username")
   username_label.pack()

   username_entry = tk.Entry(register_window)
   username_entry.pack()

   password_label = tk.Label(register_window, text="Password")
   password_label.pack()

   password_entry = tk.Entry(register_window, show="*")
   password_entry.pack()

   def register():
       username = username_entry.get()
       password = password_entry.get()
       with open("users.csv", "a", newline="") as csvfile:
           fieldnames = ["username", "password"]
           writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
           writer.writerow({"username": username, "password": password})
           messagebox.showinfo("Register", "Account created successfully!")
           register_window.destroy()
           login_window()

   register_button = tk.Button(register_window, text="Register", command=register)
   register_button.pack()

   register_window.mainloop()

main_window()
