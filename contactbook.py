import tkinter as tk
from tkinter import messagebox

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email, address):
        contact = {
            'name': name,
            'phone': phone,
            'email': email,
            'address': address
        }
        self.contacts.append(contact)

    def view_contacts(self):
        for contact in self.contacts:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}")

    def search_contact(self, keyword):
        results = [contact for contact in self.contacts if keyword.lower() in contact['name'].lower() or keyword in contact['phone']]
        return results

    def update_contact(self, old_phone, new_name, new_phone, new_email, new_address):
        for contact in self.contacts:
            if contact['phone'] == old_phone:
                contact['name'] = new_name
                contact['phone'] = new_phone
                contact['email'] = new_email
                contact['address'] = new_address
                return True
        return False

    def delete_contact(self, phone):
        for contact in self.contacts:
            if contact['phone'] == phone:
                self.contacts.remove(contact)
                return True
        return False


class ContactBookApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")

        self.contact_book = ContactBook()

        self.label = tk.Label(root, text="Contact Book")
        self.label.pack()

        self.frame = tk.Frame(root)
        self.frame.pack()

        self.name_label = tk.Label(self.frame, text="Name:")
        self.name_label.grid(row=0, column=0)
        self.name_entry = tk.Entry(self.frame)
        self.name_entry.grid(row=0, column=1)

        self.phone_label = tk.Label(self.frame, text="Phone:")
        self.phone_label.grid(row=1, column=0)
        self.phone_entry = tk.Entry(self.frame)
        self.phone_entry.grid(row=1, column=1)

        self.email_label = tk.Label(self.frame, text="Email:")
        self.email_label.grid(row=2, column=0)
        self.email_entry = tk.Entry(self.frame)
        self.email_entry.grid(row=2, column=1)

        self.address_label = tk.Label(self.frame, text="Address:")
        self.address_label.grid(row=3, column=0)
        self.address_entry = tk.Entry(self.frame)
        self.address_entry.grid(row=3, column=1)

        self.add_button = tk.Button(self.frame, text="Add Contact", command=self.add_contact)
        self.add_button.grid(row=4, column=0, columnspan=2)

        self.view_button = tk.Button(self.frame, text="View Contacts", command=self.view_contacts)
        self.view_button.grid(row=5, column=0, columnspan=2)

        self.search_button = tk.Button(self.frame, text="Search Contact", command=self.search_contact)
        self.search_button.grid(row=6, column=0, columnspan=2)

        self.update_button = tk.Button(self.frame, text="Update Contact", command=self.update_contact)
        self.update_button.grid(row=7, column=0, columnspan=2)

        self.delete_button = tk.Button(self.frame, text="Delete Contact", command=self.delete_contact)
        self.delete_button.grid(row=8, column=0, columnspan=2)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        if name and phone:
            self.contact_book.add_contact(name, phone, email, address)
            messagebox.showinfo("Success", "Contact added successfully")
        else:
            messagebox.showerror("Error", "Name and Phone are required")

    def view_contacts(self):
        self.contact_book.view_contacts()

    def search_contact(self):
        keyword = simpledialog.askstring("Search", "Enter name or phone number:")
        results = self.contact_book.search_contact(keyword)
        if results:
            for contact in results:
                print(f"Name: {contact['name']}, Phone: {contact['phone']}")
        else:
            messagebox.showinfo("Not Found", "No contacts found")

    def update_contact(self):
        old_phone = simpledialog.askstring("Update", "Enter the phone number of the contact to update:")
        if not old_phone:
            return

        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        success = self.contact_book.update_contact(old_phone, name, phone, email, address)
        if success:
            messagebox.showinfo("Success", "Contact updated successfully")
        else:
            messagebox.showerror("Error", "Contact not found")

    def delete_contact(self):
        phone = simpledialog.askstring("Delete", "Enter the phone number of the contact to delete:")
        if not phone:
            return

        success = self.contact_book.delete_contact(phone)
        if success:
            messagebox.showinfo("Success", "Contact deleted successfully")
        else:
            messagebox.showerror("Error", "Contact not found")


if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBookApp(root)
    root.mainloop()
