import csv
import tkinter as tk


def choose_seat(selected_movie):
    filename = '{}.csv'.format(selected_movie)
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        seats = list(reader)

        root = tk.Tk()
        seat_buttons = [[None for _ in range(len(seats[0]))] for _ in range(len(seats))]

        # Create a Seat Selection GUI
        for i in range(len(seats)):
            for j in range(len(seats[i])):
                text = seats[i][j]
                seat_buttons[i][j] = tk.Button(root, text=text, command=lambda i=i, j=j: book_seat(seats,selected_movie,i, j))
                seat_buttons[i][j].grid(row=i, column=j)

        root.mainloop()

# Handle Seat Selection
def book_seat(seats,selected_movie, i, j):
    seats[i][j] = 'X'
    with open('{}.csv'.format(selected_movie), 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(seats)
    seats[i][j].config(text='X')


if __name__ == "__main__":
    choose_seat('barbie')