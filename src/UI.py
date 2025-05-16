import tkinter as tk
from operations import get_primary_key_column, delete_entry,messagebox

def view_specific_row_by_id(connection, table_name, primary_key_column):
    def get_row_by_id():
        row_id = row_id_entry.get()
        if row_id:
            sql = f"SELECT * FROM {table_name} WHERE {primary_key_column} = %s;"
            cursor = connection.cursor()
            cursor.execute(sql, (row_id,))
            row = cursor.fetchone()
            if row:
                result_label.config(text=f"Data for ID '{row_id}': {row}")
            else:
                result_label.config(text=f"No data found for {primary_key_column} = {row_id}")
        else:
            result_label.config(text="Please enter a valid ID.")

    view_window = tk.Toplevel()
    view_window.title(f"View Row by ID - {table_name}")
    tk.Label(view_window, text=f"Enter the ID value for {primary_key_column}:").pack(pady=5)
    row_id_entry = tk.Entry(view_window)
    row_id_entry.pack(pady=5)
    tk.Button(view_window, text="View Row", command=get_row_by_id).pack(pady=5)
    result_label = tk.Label(view_window, text="")
    result_label.pack(pady=10)

def sub_menu(connection, table_name):
    primary_key_column = get_primary_key_column(connection, table_name)

    if not primary_key_column:
        return

    # Create a new window for the sub-menu
    sub_menu_window = tk.Toplevel()
    sub_menu_window.title(f"Options for Table: {table_name}")

    # Title Label
    tk.Label(sub_menu_window, text=f"Table: {table_name}", font=("Arial", 16, "bold")).pack(pady=10)

    # Function to View Complete Table
    def on_view_table():
        try:
            cursor = connection.cursor()
            cursor.execute(f"SELECT * FROM {table_name};")
            rows = cursor.fetchall()

            # Create a new window to display data
            view_window = tk.Toplevel()
            view_window.title(f"Data in {table_name}")

            # Text widget to show the data
            text_widget = tk.Text(view_window, wrap=tk.WORD, width=100, height=30)
            text_widget.pack(expand=True, fill=tk.BOTH)

            # Fetch and display column names
            cursor.execute(f"DESCRIBE {table_name};")
            columns = [column[0] for column in cursor.fetchall()]
            text_widget.insert(tk.END, f"Columns: {', '.join(columns)}\n\n")

            # Fetch and display rows
            for row in rows:
                text_widget.insert(tk.END, f"{row}\n")
        except Exception as e:
            messagebox.showerror("Error", f"Error displaying table data: {e}")

    # Function to View a Specific Row
    def on_view_specific_row():
        def fetch_specific_row():
            row_id = primary_key_entry.get()
            if not row_id:
                result_label.config(text="Please enter a valid primary key value.")
                return
            try:
                cursor = connection.cursor()
                sql = f"SELECT * FROM {table_name} WHERE {primary_key_column} = %s;"
                cursor.execute(sql, (row_id,))
                row = cursor.fetchone()
                if row:
                    result_label.config(text=f"Data: {row}")
                else:
                    result_label.config(text="No data found for the given primary key.")
            except Exception as e:
                messagebox.showerror("Error", f"Error retrieving row data: {e}")

        # Create a new window for fetching a specific row
        specific_row_window = tk.Toplevel()
        specific_row_window.title(f"View Specific Row - {table_name}")
        tk.Label(specific_row_window, text=f"Enter {primary_key_column} value:").pack(pady=5)
        primary_key_entry = tk.Entry(specific_row_window)
        primary_key_entry.pack(pady=5)
        tk.Button(specific_row_window, text="Fetch Row", command=fetch_specific_row).pack(pady=10)
        result_label = tk.Label(specific_row_window, text="", font=("Arial", 12), fg="blue")
        result_label.pack(pady=10)

    # Function to Delete an Entry
    def on_delete_entry():
        delete_window = tk.Toplevel()
        delete_window.title(f"Delete Entry - {table_name}")

        tk.Label(delete_window, text=f"Enter {primary_key_column} to delete:").pack(pady=5)
        primary_key_entry = tk.Entry(delete_window)
        primary_key_entry.pack(pady=5)

        def perform_delete():
            primary_key_value = primary_key_entry.get()
            if primary_key_value:
                delete_entry(connection, table_name, primary_key_column, primary_key_value)
            else:
                messagebox.showwarning("Warning", "Please enter a valid primary key value.")

        tk.Button(delete_window, text="Delete", command=perform_delete).pack(pady=10)

    # Function to Insert an Entry
    def on_insert_entry():
        # Create a new window for inserting an entry
        insert_window = tk.Toplevel()
        insert_window.title(f"Insert Entry - {table_name}")

        cursor = connection.cursor()
        cursor.execute(f"DESCRIBE {table_name};")
        columns = [column[0] for column in cursor.fetchall()]

        entries = {}
        for column in columns:
            tk.Label(insert_window, text=f"Enter value for {column}:").pack(pady=5)
            entry = tk.Entry(insert_window)
            entry.pack(pady=5)
            entries[column] = entry

        def perform_insert():
            values = [entry.get() for entry in entries.values()]
            placeholders = ", ".join(["%s"] * len(values))
            columns_str = ", ".join(columns)
            sql = f"INSERT INTO {table_name} ({columns_str}) VALUES ({placeholders});"
            try:
                cursor = connection.cursor()
                cursor.execute(sql, values)
                connection.commit()
                messagebox.showinfo("Success", "Entry inserted successfully.")
                insert_window.destroy()
            except Exception as e:
                messagebox.showerror("Error", f"Error inserting entry: {e}")

        tk.Button(insert_window, text="Insert", command=perform_insert).pack(pady=10)

    # Add Buttons for Sub-Menu Options
    tk.Button(sub_menu_window, text="View Table Data", command=on_view_table, width=20).pack(pady=10)
    tk.Button(sub_menu_window, text="View Specific Row", command=on_view_specific_row, width=20).pack(pady=10)
    tk.Button(sub_menu_window, text="Insert Entry", command=on_insert_entry, width=20).pack(pady=10)
    tk.Button(sub_menu_window, text="Delete Entry", command=on_delete_entry, width=20).pack(pady=10)

    # Close Button
    tk.Button(sub_menu_window, text="Close", command=sub_menu_window.destroy, width=20).pack(pady=10)
