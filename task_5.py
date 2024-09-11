import tkinter as tk
from tkinter import messagebox

# Initialize the main window
root = tk.Tk()
root.title('Contact Book')

# Create a list to store contacts
contacts = []

# Function to add a contact
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()
    if name and phone and email and address:
        contacts.append({"Name": name, "Phone": phone, "Email": email, "Address": address})
        clear_entries()
        update_contact_list()
    else:
        messagebox.showerror("Error", "Please enter All entries  name,phone,email,address")
        
# Function to update the contact list
def update_contact_list():
    contact_list.delete(0, tk.END)
    for contact in contacts:
        contact_list.insert(tk.END, f"{contact['Name']} - {contact['Phone']} - {contact['Email']} - {contact['Address']}")
    
# Function to search for a contact
def search_contact():
    search_term = search_entry.get()
    contact_list.delete(0, tk.END)
    for contact in contacts:
        if search_term.lower() in contact['Name'].lower() or search_term.lower() in contact['Phone'].lower() or search_term.lower() in contact['Email'].lower() or search_term.lower() in contact['Address']:
            contact_list.insert(tk.END, f"{contact['Name']} - {contact['Phone']} - {contact['Email']} - {contact['Address']}")
            
# Function to update a contact
def update_selected_contact():
    selected_index = contact_list.curselection()
    if selected_index:
        selected_index = selected_index[0]
        name = name_entry.get()
        phone = phone_entry.get()
        email = email_entry.get()
        address = address_entry.get()
        if name and phone and email and address:
            contacts[selected_index] = {"Name":name, "Phone": phone, "Email": email, "Address": address}
            clear_entries()
            update_contact_list()
        else:
            messagebox.showerror("Error", "Please enter All entries  name,phone,email,address")
            
# Function to delete a contact
def delete_selected_contact():
    selected_index = contact_list.curselection()
    if selected_index:
        selected_index = selected_index[0]
        del contacts[selected_index]
        clear_entries()
        update_contact_list()
        
# Function to clear entry fields
def clear_entries():
    name_entry.delete (0, tk.END)
    phone_entry.delete (0, tk.END)
    email_entry.delete (0, tk.END)
    address_entry.delete (0, tk.END)
    
# Create labels and entry fields
name_label = tk.Label(root, text = "Name:")
name_label.grid(row = 0, column= 0)
name_entry = tk.Entry(root)
name_entry.grid(row = 0, column = 1)

phone_label = tk.Label(root, text = "Phone:")
phone_label.grid(row = 1, column = 0)
phone_entry = tk.Entry(root)
phone_entry.grid(row = 1, column = 1)

email_label = tk.Label(root, text = "Email:")
email_label.grid(row = 2, column = 0)
email_entry = tk.Entry(root)
email_entry.grid(row = 2, column = 1)

address_label = tk.Label(root, text = "Address:")
address_label.grid(row = 3, column = 0)
address_entry = tk.Entry(root)
address_entry.grid(row = 3, column = 1)

# Create buttons
add_button = tk.Button (root, text = "Add Contact", command = add_contact)
add_button.grid (row = 0, column=2)

update_button = tk.Button (root, text = "Update Contact", command= update_selected_contact)
update_button.grid(row=1, column=2)

delete_button = tk.Button (root, text = "Delete Contact", command= delete_selected_contact)
delete_button.grid(row = 2, column=2)

search_label = tk.Label(root, text = "Search:")
search_label.grid(row = 4, column = 0)

search_entry = tk.Entry(root)
search_entry.grid(row = 4, column = 1)

search_button = tk.Button(root, text = "Search", command=search_contact)
search_button.grid(row = 4, column=2)

# Create a listbox to display contact
contact_list = tk.Listbox(root, width = 80)
contact_list.grid(row = 5, column=0, columnspan=3)

# Run the Application
root.mainloop()