import csv
import os
import tkinter as tk
from tkinter import messagebox

def load_movies():
  with open('movielist.csv', 'r') as csvfile:
      reader = csv.DictReader(csvfile)
      movies = [row['judul'] for row in reader]
  return movies

def confirm_selection(movie_vars):
  selected_movie = movie_vars.get()
  messagebox.showinfo("Confirmation", f"You selected: {selected_movie}")

def create_gui():
  window = tk.Tk()
  window.title("Movie Selection")
  window.geometry("300x400")

  frame = tk.Frame(window)
  frame.pack(padx=50, pady=50)

  movies = load_movies()
  movie_vars = tk.StringVar()
  for movie in movies:
      rb = tk.Radiobutton(frame, text=movie, variable=movie_vars, value=movie)
      rb.pack(anchor=tk.W)

  confirm_button = tk.Button(window, text="Confirm", command=confirm_selection(movie_vars))
  confirm_button.pack(pady=20)

  window.mainloop()

if __name__ == "__main__":
  create_gui()
