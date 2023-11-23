import csv
import tkinter as tk
from tkinter import messagebox

def choose_seat(selected_movie):
    filename = '{}.csv'.format(selected_movie)
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        seats = list(reader)

        root = tk.Tk()

        # Create a Frame for the first set of seats (ABC)
        frame_abc = tk.Frame(root)
        frame_abc.grid(row=0, column=0, padx=10)  # Adjust padx as needed

        seat_buttons_abc = [[None for _ in range(len(seats[0]))] for _ in range(len(seats))]

        for i in range(len(seats)):
            for j in range(len(seats[i]) // 2):  # Only use the first half of seats
                text = seats[i][j]
                seat_buttons_abc[i][j] = tk.Button(frame_abc, text=text, command=lambda i=i, j=j: book_seat(seats, selected_movie, seat_buttons_abc, i, j), width=5, height=2)
                seat_buttons_abc[i][j].grid(row=i, column=j)

        # Create a Frame for the second set of seats (DEF)
        frame_def = tk.Frame(root)
        frame_def.grid(row=0, column=1, padx=20)  # Adjust padx as needed

        seat_buttons_def = [[None for _ in range(len(seats[0]) // 2)] for _ in range(len(seats))]

        for i in range(len(seats)):
            for j in range(len(seats[i]) // 2, len(seats[i])):  # Use the second half of seats
                text = seats[i][j]
                seat_buttons_def[i][j - len(seats[i]) // 2] = tk.Button(frame_def, text=text, command=lambda i=i, j=j: book_seat(seats, selected_movie, seat_buttons_def, i, j - len(seats[i]) // 2), width=5, height=2)
                seat_buttons_def[i][j - len(seats[i]) // 2].grid(row=i, column=j - len(seats[i]) // 2)

        # Create a Canvas for the black box with padding
        canvas = tk.Canvas(root, bg='black', height=60)
        canvas.grid(row=1, columnspan=len(seats[0]) + 2, pady=10)  # Add padding to the bottom

        def save_and_confirm():
            confirmation = messagebox.askokcancel("Confirm", "Are you sure you want to confirm? Changes will be saved.")
            if confirmation:
                save_data(selected_movie, seats)
                root.destroy()

        confirm_button = tk.Button(root, text="Confirm", command=save_and_confirm, width=20, height=2)
        confirm_button.grid(row=2, columnspan=len(seats[0]) + 2, pady=10)  # Adjust pady as needed

        def on_closing():
            if messagebox.askokcancel("Confirm", "Are you sure you want to close? Changes will be saved."):
                root.destroy()
                save_data(selected_movie, seats)

        root.protocol("WM_DELETE_WINDOW", on_closing)
        root.mainloop()


# ... (fungsi save_data dan book_seat tetap sama)


        root.protocol("WM_DELETE_WINDOW", on_closing)
        root.mainloop()

# ... (fungsi save_data dan book_seat tetap sama)


def save_data(selected_movie, seats):
    with open('{}.csv'.format(selected_movie), 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(seats)

# Handle Seat Selection
def book_seat(seats, selected_movie, seat_buttons, i, j):
    seats[i][j] = 'X'
    seat_buttons[i][j].config(text='X')  # Update the button's text

if __name__ == "__main__":
    choose_seat('goat_documentary')
