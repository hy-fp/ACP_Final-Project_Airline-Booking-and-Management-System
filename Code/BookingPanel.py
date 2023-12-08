from tkinter import *
from tkinter import ttk
from database_ import Database
from tkinter import messagebox
from tkcalendar import *
from datetime import datetime
import mysql.connector

db = Database(host="localhost", user="root", password="", database="ABMS")



class BookFlight:
    def __init__(self, root, selected_flight_info, username, selected_class):
        
        self.root = root
        self.username = username
        self.selected_class = selected_class
        self.selectedFlightInfo = selected_flight_info
        
        # local variables
        self.Name = StringVar()
        self.Email = StringVar()
        self.Gender= StringVar()
        self.CellNo = StringVar()
        self.payment_type = StringVar()
        self.payment_entry = StringVar()
        
        self.bookFlightFrame()
        self.BFrameButtons()

        self.out = ttk.Treeview(self.root)

    """Instructor Info Entries Frame"""

    def bookFlightFrame(self):
        self.entriesFrame = Frame(self.root, bg="#003b95")
        self.entriesFrame.pack(side=TOP, fill=X)
        self.search_frame_title = Label(self.entriesFrame, text="Booking Panel", font=("Goudy old style", 35),
                                       bg="#003b95",
                                       fg="white")
        self.search_frame_title.grid(row=0, columnspan=2, padx=10, pady=20, sticky="w")

        self.labelName = Label(self.entriesFrame, text="Full Name", font=("Times New Roman", 16, "bold"), bg="#003b95",
                               fg="white")
        self.labelName.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.txtName = Entry(self.entriesFrame, textvariable=self.Name, font=("Times New Roman", 15), width=30)
        self.txtName.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        self.labelEmail = Label(self.entriesFrame, text="Email", font=("Times New Roman", 16, "bold"), bg="#003b95",
                               fg="white")
        self.labelEmail.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.txtEmail = Entry(self.entriesFrame, textvariable=self.Email, font=("Times New Roman", 15), width=30)
        self.txtEmail.grid(row=2, column=1, padx=10, pady=5, sticky="w")

        self.labelGender = Label(self.entriesFrame, text="Gender", font=("Times New Roman", 16, "bold"), bg="#003b95",
                                 fg="white")
        self.labelGender.grid(row=1, column=2, padx=10, pady=5, sticky="w")
        self.comboGender = ttk.Combobox(self.entriesFrame, textvariable=self.Gender, font=("Times New Roman", 15),
                                        width=28,
                                        state="readonly")
        self.comboGender['values'] = ("Male", "Female", "Other", "Prefer Not to Say")
        self.comboGender.grid(row=1, column=3, padx=10, pady=5, sticky="w") 

        self.labelCellNo = Label(self.entriesFrame, text="Contact Number", font=("Times New Roman", 16, "bold"),
                                bg="#003b95",
                                fg="white")
        self.labelCellNo.grid(row=2, column=2, padx=10, pady=5, sticky="w")
        self.txtCellNo = Entry(self.entriesFrame, textvariable=self.CellNo, font=("Times New Roman", 15), width=30)
        self.txtCellNo.grid(row=2, column=3, padx=10, pady=5, sticky="w")

    def validate_full_name(self):
        full_name = self.Name.get()
        if not full_name.replace(" ", "").isalpha():
            messagebox.showerror("Error!", "Full Name should only contain letters.")
            return False
        return True

    def validate_contact_number(self):
        contact_number = self.CellNo.get()
        if not contact_number.startswith("09") or not contact_number[2:].isdigit() or len(contact_number) != 11:
            messagebox.showerror("Error!", "Invalid Contact Number. It should start with '09' and have 11 digits.")
            return False
        return True

    def validate_email(self):
        email = self.Email.get()
        if not email.endswith(("@gmail.com", "@yahoo.com")):
            messagebox.showerror("Error!", "Invalid Email. It should end with '@gmail.com' or '@yahoo.com'.")
            return False
        return True

    def validate_inputs(self):

        is_full_name_valid = self.validate_full_name()
        is_email_valid = self.validate_email()
        is_contact_number_valid = self.validate_contact_number()

        if self.payment_type.get() == "gcash" and not self.payment_entry.get():
            messagebox.showerror("Error", "Please enter GCash number.")
            return False

        if self.payment_type.get() == "card" and not self.payment_entry.get():
            messagebox.showerror("Error", "Please enter Card number.")
            return False

        # Return False if any validation fails
        return all([is_full_name_valid, is_email_valid, is_contact_number_valid])

    def confirmMethod(self):
        selected_method = self.payment_type.get()

        # Hide GCash and and Card Entries and Confirm Buttons
        self.labelGcash.grid_remove()
        self.gcashEntry.grid_remove()
        self.btnConfirmGCash.grid_remove()
        self.labelCard.grid_remove()
        self.cardEntry.grid_remove()
        self.btnConfirmCard.grid_remove()

        if selected_method == "GCash":
            # Show GCash Label, Entry, and Confirm GCash Button
            self.labelGcash.grid(row=5, column=0, padx=10, pady=5, sticky="w")
            self.gcashEntry.grid(row=5, column=1, padx=10, pady=5, sticky="w")
            self.btnConfirmGCash.grid(row=5, column=2, padx=10, pady=5,sticky="w")
        elif selected_method == "Card":
            # Show Card Label, Entry, and Confirm Card Button
            self.labelCard.grid(row=5, column=0, padx=10, pady=5, sticky="w")
            self.cardEntry.grid(row=5, column=1, padx=10, pady=5, sticky="w")
            self.btnConfirmCard.grid(row=5, column=2, padx=10, pady=5, sticky="w")
        else:
            messagebox.showerror("Error", "Please select a payment method.")

    def confirmGCash(self):
        gcash_number = self.gcashEntry.get()

        if gcash_number.isdigit() and gcash_number.startswith("09") and len(gcash_number) == 11:
            # Proceed to book the flight after confirming GCash payment
            self.bookFlight()
        else:
            messagebox.showerror("Error", "Please enter a valid GCash number.")

    def confirmCard(self):
        card_number = self.cardEntry.get()

        if card_number.isdigit() and len(card_number) == 16:
            # Proceed to book the flight after confirming Card payment
            self.bookFlight()
        else:
            messagebox.showerror("Error", "Please enter a valid Card number.")

    # event trigger Method to display the chosen data from the TreeView back in respective fields
    def getData(self, event=None):
        try:
            self.selectedRow = self.out.focus()
            self.selectedData = self.out.item(self.selectedRow)
            self.chosenRow = self.selectedData["values"]
            self.Name.set(self.chosenRow[0])
            self.Email.set(self.chosenRow[1])
            self.Gender.set(self.chosenRow[2])
            self.CellNo.set(self.chosenRow[3])

        except IndexError as error:
            pass

    def bookFlight(self):
        if not self.validate_inputs():
            return

        flight_id = int(self.selectedFlightInfo[0])

        name = self.Name.get()
        email = self.Email.get()
        gender = self.Gender.get()
        cell_no = self.CellNo.get()

        passenger_id = db.insertPassengerAndBookedFlight(name, email, gender, cell_no, self.username, flight_id, self.selected_class)

        if passenger_id is not None:
            messagebox.showinfo("Success", "Flight booked successfully!")

        self.viewBookedFlights()

        self.root.withdraw()

        # Open the SearchFlight window
        from PassengerPanel import SearchFlight

        search_window = Toplevel(self.root)
        search_window.geometry(self.root.geometry())
        SearchFlight(search_window, self.username)

    def displayFlights(self, flights):
        # Clear the TreeView
        self.out.delete(*self.out.get_children())

        # Display the search results in the TreeView
        for row in flights:
            self.out.insert("", END, values=row)

    def viewBookedFlights(self):
        # Retrieve and display booked flights for the current passenger
        booked_flights = db.viewBookedFlights(self.username)
        self.displayFlights(booked_flights)


    def back(self):
        self.root.withdraw()

        from PassengerPanel import SearchFlight

        search_window = Toplevel(self.root)
        search_window.geometry(self.root.geometry())
        SearchFlight(search_window, self.username)

    def BFrameButtons(self):
        # Button Frame Configurations
        self.buttonsFrame = Frame(self.entriesFrame, bg="#003b95")
        self.buttonsFrame.grid(row=10, column=0, padx=10, pady=10, sticky="w", columnspan=8)

        self.labelPayment = Label(self.entriesFrame, text="Payment Method", font=("Times New Roman", 16, "bold"),
                            bg="#003b95", fg="white")
        self.labelPayment.grid(row=4, column=0, padx=10, pady=5, sticky="w")
        
        payment_methods = ["Select Payment Method", "GCash", "Card"]
        self.comboPayment = ttk.Combobox(self.entriesFrame, textvariable=self.payment_type,
                                         values=payment_methods, font=("Times New Roman", 15), state="readonly")
        self.comboPayment.grid(row=4, column=1, padx=10, pady=5, sticky="w")
        
        self.btnConfirmMethod = Button(self.entriesFrame, command=self.confirmMethod, text="Confirm Method", bd=0,
                                       cursor="hand2", bg="#d5e7ff", fg="#003b95", width=20, font=("Impact", 15))
        self.btnConfirmMethod.grid(row=4, column=2, padx=10, pady=5, sticky="w")

        self.labelGcash = Label(self.entriesFrame, text="Gcash Number", font=("Times New Roman", 16, "bold"),
                            bg="#003b95", fg="white")


        self.labelCard = Label(self.entriesFrame, text="Card Number", font=("Times New Roman", 16, "bold"),
                           bg="#003b95", fg="white")

        self.gcashEntry = Entry(self.entriesFrame, textvariable=self.payment_entry, font=("Times New Roman", 15),
                                width=20)

        self.btnConfirmGCash = Button(self.entriesFrame, command=self.confirmGCash, text="Confirm and Book", bd=0,
                                      cursor="hand2", bg="#d5e7ff", fg="#003b95", width=20, font=("Impact", 15))

        self.cardEntry = Entry(self.entriesFrame, textvariable=self.payment_entry, font=("Times New Roman", 15),
                               width=20)

        self.btnConfirmCard = Button(self.entriesFrame, command=self.confirmCard, text="Confirm and Book", bd=0,
                                     cursor="hand2", bg="#d5e7ff", fg="#003b95", width=20, font=("Impact", 15))
        
        self.btnBack = Button(self.entriesFrame, command=self.back, text="Back", bd=0, cursor="hand2",
                                bg="#d5e7ff",
                                fg="#003b95", width=15, font=("Impact", 15))
        self.btnBack.grid(row=0, column=4, padx=(10, 15), sticky="e")
