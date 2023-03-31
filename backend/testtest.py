# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from tkinter import *
from PIL import ImageTk, Image
import sqlite3


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f"Hi, {name}")  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    print_hi("PyCharm")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

root = Tk()
root.title("Test CSIT 314")
root.geometry("400x400")

# Databases

# Create a database or connect to one
conn = sqlite3.connect("address_book.db")

# Create cursor
c = conn.cursor()

'''
# Create table
c.execute("""CREATE TABLE addresses(
            first_name text,
            last_name text
            )""")
'''
# Create Submit Function
def submit():
    # Create a database or connect to one
    conn = sqlite3.connect("address_book.db")

    # Create cursor
    c = conn.cursor()

    # Insert into table
    c.execute("INSERT INTO addresses VALUES (:f_name, :l_name)", {"f_name": f_name.get(), "l_name": l_name.get()})

    # Commit changes
    conn.commit()

    # Close connection
    conn.close()

    # Clear the text box
    f_name.delete(0, END)
    l_name.delete(0, END)


# Create query Function
def query():
    # Create a database or connect to one
    conn = sqlite3.connect("address_book.db")

    # Create cursor
    c = conn.cursor()

    # Select into table
    c.execute("SELECT * FROM addresses")

    records = c.fetchall()

    c.execute("SELECT rowid FROM addresses")
    oid = c.fetchall()
    # print(records)

    # Loop through the results
    print_records = ""
    index = 0
    for index1, record in enumerate(records):
        print_records += "oid: " + str(oid[index1]) + "\t"
        print_records += "first name: " + str(record[0]) + "\n"
        index += 1
    """
    records = c.fetchall()
    for row in records:
        print("first name:", row[0])
        print("last name:", row[1])
    """

    root1 = Tk()
    root1.title("Test CSIT 314")
    root1.geometry("400x400")

    query_label = Label(root, text=print_records)
    query_label.grid(row=6, column=0, columnspan=2)

    # Commit changes
    conn.commit()

    # Close connection
    conn.close()


# Create delete function
def delete():

    # Create a database or connect to one
    conn = sqlite3.connect("address_book.db")

    # Create cursor
    c = conn.cursor()

    # Delete from table
    c.execute("DELETE FROM addresses")

    # Commit changes
    conn.commit()

    # Close connection
    conn.close()


# Create textbox
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1)

l_name = Entry(root, width=30)
l_name.grid(row=1, column=1)

# Create Text box labels
f_name_label = Label(root, text="First name")
f_name_label.grid(row=0, column=0)
l_name_label = Label(root, text="Last name")
l_name_label.grid(row=1, column=0)

# Create Submit button
submit_btn = Button(root, text="Add record into the database", command=submit)
submit_btn.grid(row=3, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# Create Submit button
query_btn = Button(root, text="Show records", command=query)
query_btn.grid(row=4, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# Create Delete button
delete_btn = Button(root, text="Delete records", command=delete)
delete_btn.grid(row=5, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# Commit changes
conn.commit()

# Close connection
conn.close()

root.mainloop()
