from tkinter import messagebox

def get_primary_key_column(connection, table_name):
    try:
        cursor = connection.cursor()
        cursor.execute(f"SHOW KEYS FROM {table_name} WHERE Key_name = 'PRIMARY';")
        result = cursor.fetchall()
        if result:
            return result[0][4]  # Return the primary key column name
        else:
            messagebox.showwarning("Warning", f"No primary key found for table '{table_name}'.")
            return None
    except Exception as e:
        messagebox.showerror("Error", f"Error retrieving primary key column: {e}")
        return None

def delete_entry(connection, table_name, primary_key_column, primary_key_value):
    try:
        cursor = connection.cursor()
        cursor.execute(f"DELETE FROM {table_name} WHERE {primary_key_column} = %s", (primary_key_value,))
        connection.commit()
        messagebox.showinfo("Success", f"Entry with {primary_key_column}={primary_key_value} deleted successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"Error deleting entry: {e}")

