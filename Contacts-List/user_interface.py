from tkinter import *
from tkinter import messagebox
import contacts_database


# Class for user interface
class UserInterface:
    def __init__(self):
        self.root = Tk()
        self.root.title("Contacts")
        self.root.config(padx=100, pady=100)
        self.contacts_list = contacts_database.view_contacts()
        self.contacts_listbox = Listbox(selectmode="single", height=4)
        self.contacts_listbox.grid(row=2, column=2, padx=10, pady=10, rowspan=4)
        self.contacts_listbox.bind("<<ListboxSelect>>", self.show_details)
        self.scrollbar = Scrollbar(command=self.contacts_listbox.yview)
        self.contacts_listbox.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.grid(row=2, column=2, rowspan=4, sticky="ns")
        self.add_button = Button(text="Add contact", command=self.new_contact)
        self.add_button.grid(row=9, column=0, padx=10, pady=10)
        self.display_contacts()
        self.root.mainloop()

    # Display all the list of contacts saved in database
    def display_contacts(self):
        self.contacts_listbox.delete(0, END)
        self.contacts_list = contacts_database.view_contacts()
        for i in range(len(self.contacts_list)):
            contact_name = self.contacts_list[i].name
            self.contacts_listbox.insert("end", contact_name)

    # Display the details of a person
    def show_details(self, event):
        selected = self.contacts_listbox.curselection()
        if selected:
            name = self.contacts_listbox.get(selected[0])
            details = contacts_database.contact_details(name)
            self.details_label = Label(
                text=f"Name: {details.name}\n"
                     f"Phone number: {details.phone}\n"
                     f"Email: {details.email_id}\n"
                     f"City: {details.city}",
            )
            self.details_label.grid(row=2, column=1, padx=10, pady=10, rowspan=4)
            self.edit_button = Button(text="Edit", command=lambda: self.update_contact_details(details))
            self.edit_button.grid(row=7, column=0)
            self.delete_button = Button(text="Delete", command=lambda: self.remove_contact(details))
            self.delete_button.grid(row=8, column=0)

    # New widgets to be displayed during insertion or updation
    def additional_widgets(self):
        self.name_label = Label(text="Name: ")
        self.name_label.grid(row=2, column=0)
        self.name_entry = Entry(width=30)
        self.name_entry.grid(row=2, column=1)
        self.phone_label = Label(text="Phone number: ")
        self.phone_label.grid(row=3, column=0)
        self.phone_entry = Entry(width=30)
        self.phone_entry.grid(row=3, column=1)
        self.email_label = Label(text="Email: ")
        self.email_label.grid(row=4, column=0)
        self.email_entry = Entry(width=30)
        self.email_entry.grid(row=4, column=1)
        self.city_label = Label(text="City: ")
        self.city_label.grid(row=5, column=0)
        self.city_entry = Entry(width=30)
        self.city_entry.grid(row=5, column=1)

    # Create a new contact
    def new_contact(self):
        self.additional_widgets()
        self.ok_button = Button(text="OK", command=self.insert_contact)
        self.ok_button.grid(row=6, column=0)

    # Contact will be inserted on pressing OK button
    def insert_contact(self):
        c_name = self.name_entry.get()
        c_phone = self.phone_entry.get()
        c_email = self.email_entry.get()
        c_city = self.city_entry.get()
        contacts_database.add_contact(c_name, c_phone, c_email, c_city)
        messagebox.showinfo(title="Success", message="New contact added successfully!!!")
        self.destroy_widgets()
        self.display_contacts()

    # Update a contact
    def update_contact_details(self, data_obj):
        self.details_label.destroy()
        self.edit_button.destroy()
        self.additional_widgets()
        self.name_entry.insert(0, data_obj.name)
        self.phone_entry.insert(0, data_obj.phone)
        self.email_entry.insert(0, data_obj.email_id)
        self.city_entry.insert(0, data_obj.city)
        self.ok_button = Button(text="OK", command=lambda: self.change_details(data_obj))
        self.ok_button.grid(row=6, column=0)

    # Details will be updated when OK button
    def change_details(self, data_obj):
        yes_no_message = messagebox.askyesno(title="Change Details?",
                                             message="Are you sure that you want to save the changes made in the details?")

        c_name = self.name_entry.get()
        c_phone = self.phone_entry.get()
        c_email = self.email_entry.get()
        c_city = self.city_entry.get()
        contacts_database.edit_contact(data_obj, c_name, c_phone, c_email, c_city)
        messagebox.showinfo(title="Success", message="Contact modified successfully!!!")
        messagebox.showinfo(title="Ok", message="Contact details not changed!!!")
        self.destroy_widgets()
        self.display_contacts()

    # Delete a contact
    def remove_contact(self, data_obj):
        contacts_database.delete(data_obj)
        self.details_label.destroy()
        self.edit_button.destroy()
        self.delete_button.destroy()
        self.display_contacts()

    # Destroy the widgets
    def destroy_widgets(self):
        self.name_label.destroy()
        self.name_entry.destroy()
        self.city_label.destroy()
        self.city_entry.destroy()
        self.email_label.destroy()
        self.email_entry.destroy()
        self.phone_label.destroy()
        self.phone_entry.destroy()
        self.ok_button.destroy()


interface = UserInterface()
