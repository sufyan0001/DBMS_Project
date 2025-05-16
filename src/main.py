import tkinter as tk
from UI import sub_menu
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error
from tkinter import messagebox

def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="2n0a0e4m@8365",
            database="bankmanagement",
            auth_plugin='mysql_native_password'
        )
        if connection.is_connected():
            return connection
    except Error as e:
        messagebox.showerror("Error", f"Error connecting to MySQL: {e}")
        return None

def show_table_names(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("SHOW TABLES;")
        tables = cursor.fetchall()
        if not tables:
            messagebox.showwarning("Warning", "No tables found in the database.")
        return [table[0] for table in tables]
    except Error as e:
        messagebox.showerror("Error", f"Error retrieving table names: {e}")
        return []


def main():
    connection = connect_to_database()
    if not connection:
        return

    def on_table_select():
        table_name = table_listbox.get(tk.ACTIVE)
        if table_name:
            sub_menu(connection, table_name)  # Only pass connection and table_name


    root = tk.Tk()
    root.title("Bank Management System")
    table_names = show_table_names(connection)
    if not table_names:
        messagebox.showerror("Error", "No tables found in the database.")
        return

    tk.Label(root, text="Select a table to operate on:").pack(pady=10)
    table_listbox = tk.Listbox(root)
    for table_name in table_names:
        table_listbox.insert(tk.END, table_name)
    table_listbox.pack(pady=10)
    tk.Button(root, text="Select Table", command=on_table_select).pack(pady=20)
    tk.Button(root, text="Exit", command=root.quit).pack(pady=10)
    root.mainloop()

if __name__ == "__main__":
    main()
