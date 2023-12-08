from tkinter import *
from tkinter import ttk
from database_ import Database
from tkinter import messagebox
from ViewPassenger import ViewPList
import Login
from tkcalendar import DateEntry
from datetime import datetime

db = Database(host="localhost", user="root", password="", database="ABMS")

class AdminControls:
    def __init__(self, root):
        self.root = root

        self.insFlightID = StringVar()
        self.Airline = StringVar()
        self.FlightDate = StringVar()
        self.insDepartureTime = StringVar()
        self.ArrivalTime = StringVar()
        self.Origin = StringVar()
        self.Destination = StringVar()
        self.EconomyAvailableSeats = StringVar()
        self.BusinessAvailableSeats = StringVar()

        self.adminControlsFrame()
        self.adminFrameButtons()
        self.tableOutputFrame()

    def adminControlsFrame(self):
        # Admin Control Frame Configurations
        self.entriesFrame = Frame(self.root, bg="#003b95")
        self.entriesFrame.pack(side=TOP, fill=X)
        self.admin_frame_title = Label(self.entriesFrame, text="Admin Management", font=("Goudy old style", 35),
                                       bg="#003b95",
                                       fg="white")
        self.admin_frame_title.grid(row=0, columnspan=2, padx=10, pady=20, sticky="w")

        self.labelFlightID = Label(self.entriesFrame, text="Flight ID", font=("Times New Roman", 16, "bold"), bg="#003b95",
                               fg="white")
        self.labelFlightID.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.txtFlightID = Entry(self.entriesFrame, textvariable=self.insFlightID, font=("Times New Roman", 15), width=30)
        self.txtFlightID.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        self.labelDepartureTime = Label(self.entriesFrame, text="Departure Time", font=("Times New Roman", 16, "bold"), bg="#003b95",
                                 fg="white")
        self.labelDepartureTime.grid(row=1, column=2, padx=10, pady=5, sticky="w")
        self.comboDepartureTime = ttk.Combobox(self.entriesFrame, textvariable=self.insDepartureTime, font=("Times New Roman", 15),
                                        width=28,
                                        state="readonly")
        self.comboDepartureTime['values'] = ("12:00 AM", "1:00 AM","2:00 AM", "3:00 AM", "4:00 AM", "5:00 AM","6:00 AM","7:00 AM", "8:00 AM", "9:00 AM", "10:00 AM", "11:00 AM", "12:00 PM", "1:00 PM","2:00 PM", "3:00 PM", "4:00 PM", "5:00 PM","6:00 PM","7:00 PM", "8:00 PM", "9:00 PM", "10:00 PM", "11:00 PM")
        self.comboDepartureTime.grid(row=1, column=3, padx=10, pady=5, sticky="w")

        self.labelAirline = Label(self.entriesFrame, text="Airline", font=("Times New Roman", 16, "bold"),
                                 bg="#003b95",
                                 fg="white")
        self.labelAirline.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.comboAirline = ttk.Combobox(self.entriesFrame, textvariable=self.Airline, font=("Times New Roman", 15),
                                       width=28,
                                       state="readonly")
        self.comboAirline['values'] = ("Philippine Airlines", "Cebu Pacific Air", "AirAsia")
        self.comboAirline.grid(row=2, column=1, padx=10, pady=5, sticky="w")

        self.labelArrivalTime = Label(self.entriesFrame, text="Arrival Time", font=("Times New Roman", 16, "bold"), bg="#003b95",
                                 fg="white")
        self.labelArrivalTime.grid(row=2, column=2, padx=10, pady=5, sticky="w")
        self.comboArrivalTime = ttk.Combobox(self.entriesFrame, textvariable=self.ArrivalTime, font=("Times New Roman", 15),
                                        width=28,
                                        state="readonly")
        self.comboArrivalTime['values'] = ("12:00 AM", "1:00 AM","2:00 AM", "3:00 AM", "4:00 AM", "5:00 AM","6:00 AM","7:00 AM", "8:00 AM", "9:00 AM", "10:00 AM", "11:00 AM", "12:00 PM", "1:00 PM","2:00 PM", "3:00 PM", "4:00 PM", "5:00 PM","6:00 PM","7:00 PM", "8:00 PM", "9:00 PM", "10:00 PM", "11:00 PM")
        self.comboArrivalTime.grid(row=2, column=3, padx=10, pady=5, sticky="w")

        self.labelOrigin = Label(self.entriesFrame, text="Origin", font=("Times New Roman", 16, "bold"), bg="#003b95",
                                 fg="white")
        self.labelOrigin.grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.comboOrigin = ttk.Combobox(self.entriesFrame, textvariable=self.Origin, font=("Times New Roman", 15),
                                        width=28,
                                        state="readonly")
        self.comboOrigin['values'] = ("Ninoy Aquino International Airport (MNL) - Manila", "Mactan-Cebu International Airport (CEB) - Cebu", "Clark International Airport (CRK) - Angeles City, Pampanga", 
                                      "Iloilo International Airport (ILO) - Iloilo City", "Kalibo International Airport (KLO) - Kalibo, Aklan",
                                      "Bacolod-Silay International Airport (BCD) - Bacolod City", "Francisco Bangoy International Airport (DVO) - Davao City", 
                                      "Puerto Princesa International Airport (PPS) - Puerto Princesa, Palawan","Zamboanga International Airport (ZAM) - Zamboanga City" )
        self.comboOrigin.grid(row=3, column=1, padx=10, pady=5, sticky="w")

        self.labelDestination = Label(self.entriesFrame, text="Destination", font=("Times New Roman", 16, "bold"), bg="#003b95",
                                 fg="white")
        self.labelDestination.grid(row=4, column=0, padx=10, pady=5, sticky="w")
        self.comboDestination = ttk.Combobox(self.entriesFrame, textvariable=self.Destination, font=("Times New Roman", 15),
                                        width=28,
                                        state="readonly")
        self.comboDestination['values'] = ("Ninoy Aquino International Airport (MNL) - Manila", "Mactan-Cebu International Airport (CEB) - Cebu", "Clark International Airport (CRK) - Angeles City, Pampanga", 
                                      "Iloilo International Airport (ILO) - Iloilo City", "Kalibo International Airport (KLO) - Kalibo, Aklan",
                                      "Bacolod-Silay International Airport (BCD) - Bacolod City", "Francisco Bangoy International Airport (DVO) - Davao City", 
                                      "Puerto Princesa International Airport (PPS) - Puerto Princesa, Palawan","Zamboanga International Airport (ZAM) - Zamboanga City" )
        self.comboDestination.grid(row=4, column=1, padx=10, pady=5, sticky="w")

        min_date = datetime.now().date()
        self.labelFlightDate= Label(self.entriesFrame, text="Flight Date", font=("Times New Roman", 16, "bold"),
                              bg="#003b95",
                              fg="white")
        self.labelFlightDate.grid(row=5, column=0, padx=10, pady=5, sticky="w")
        self.dateEntryFlightDate = DateEntry(self.entriesFrame, textvariable=self.FlightDate, font=("Times New Roman", 15),
                                             width=28, background='darkblue', foreground='white', borderwidth=2,
                                             mindate=min_date, state="readonly", date_pattern='mm/dd/yyyy')
        self.dateEntryFlightDate.grid(row=5, column=1, padx=10, pady=5, sticky="w")

        self.labelEconomyAvailableSeats = Label(self.entriesFrame, text="Economy Available Seats",
                                                font=("Times New Roman", 16, "bold"), bg="#003b95",
                                                fg="white")
        self.labelEconomyAvailableSeats.grid(row=3, column=2, padx=10, pady=5, sticky="w")
        self.comboEconomyAvailableSeats = ttk.Combobox(self.entriesFrame, textvariable=self.EconomyAvailableSeats,
                                                       font=("Times New Roman", 15), width=28, state="readonly")
        self.comboEconomyAvailableSeats['values'] = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10")
        self.comboEconomyAvailableSeats.grid(row=3, column=3, padx=10, pady=5, sticky="w")

        self.labelBusinessAvailableSeats = Label(self.entriesFrame, text="Business Available Seats",
                                                 font=("Times New Roman", 16, "bold"), bg="#003b95",
                                                 fg="white")
        self.labelBusinessAvailableSeats.grid(row=4, column=2, padx=10, pady=5, sticky="w")
        self.comboBusinessAvailableSeats = ttk.Combobox(self.entriesFrame, textvariable=self.BusinessAvailableSeats,
                                                        font=("Times New Roman", 15), width=28, state="readonly")
        self.comboBusinessAvailableSeats['values'] = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10")
        self.comboBusinessAvailableSeats.grid(row=4, column=3, padx=10, pady=5, sticky="w")


    def getData(self, event=None):
        try:
            self.selectedRow = self.out.focus()
            self.selectedData = self.out.item(self.selectedRow)
            self.chosenRow = self.selectedData["values"]
            self.insFlightID.set(self.chosenRow[0])
            self.Airline.set(self.chosenRow[1])
            self.FlightDate.set(self.chosenRow[2])
            self.insDepartureTime.set(self.chosenRow[3])
            self.ArrivalTime.set(self.chosenRow[4])
            self.Origin.set(self.chosenRow[5])
            self.Destination.set(self.chosenRow[6])
            self.EconomyAvailableSeats.set(self.chosenRow[7])
            self.BusinessAvailableSeats.set(self.chosenRow[8])
            
        except IndexError as error:
            pass

    def addFlight(self):
        if (
            self.txtFlightID.get() == ""
            or self.comboDepartureTime.get() == ""
            or self.comboAirline.get() == ""
            or self.comboArrivalTime.get() == ""
            or self.comboOrigin.get() == ""
            or self.comboDestination.get() == ""
            or self.comboEconomyAvailableSeats.get() == ""
            or self.comboBusinessAvailableSeats.get() == ""
        ):
            messagebox.showerror("Error!", "Please fill all the fields!")
            return

        # Check if Origin and Destination are the same
        if self.comboOrigin.get() == self.comboDestination.get():
            messagebox.showerror("Error!", "Origin and Destination cannot be the same.")
            return

        # Check if Departure Time and Arrival Time are the same
        if self.comboDepartureTime.get() == self.comboArrivalTime.get():
            messagebox.showerror(
                "Error!", "Departure Time and Arrival Time cannot be the same."
            )
            return

        flight_date = datetime.strptime(self.FlightDate.get(), "%m/%d/%Y")

        # Calculate Economy Total Fare
        economy_total_fare = (
            self.getFixedFare(self.comboOrigin.get(), self.comboDestination.get())
            + self.getAirlineFare(self.comboAirline.get())
            + self.getClassFare("Economy")
        )

        # Calculate Business Total Fare
        business_total_fare = (
            self.getFixedFare(self.comboOrigin.get(), self.comboDestination.get())
            + self.getAirlineFare(self.comboAirline.get())
            + self.getClassFare("Business")
        )

        # Perform the insertion
        if not db.insertFlight(
            self.txtFlightID.get(),
            self.comboAirline.get(),
            flight_date,
            self.comboDepartureTime.get(),
            self.comboArrivalTime.get(),
            self.comboOrigin.get(),
            self.comboDestination.get(),
            self.comboEconomyAvailableSeats.get(),
            economy_total_fare,
            self.comboBusinessAvailableSeats.get(),
            business_total_fare,
        ):
            messagebox.showerror(
                "Error!",
                f"Flight ID '{self.txtFlightID.get()}' is already registered. Please choose a unique one.",
            )
            return

    # If all checks pass, proceed with the insertion
        messagebox.showinfo("Success!", "Record Successfully Inserted!")

        self.resetForm()
        self.viewFlight()

    # Method to remove selected flight from the database
    def deleteFlight(self):
        try:
            success = db.removeFlight(self.chosenRow[0])

            if success:
                messagebox.showinfo("Success!", "Flight successfully deleted!")
                self.resetForm()
                self.viewFlight()
            else:
                messagebox.showwarning("Warning", "Cannot delete the flight because it is already booked.")
        except AttributeError as error:
            messagebox.showerror("Error!", "Please Choose a Flight Record to Remove!")

    def getFixedFare(self, origin, destination):
        fixed_fares = {
            ("Ninoy Aquino International Airport (MNL) - Manila", "Mactan-Cebu International Airport (CEB) - Cebu"): 8000,
            ("Ninoy Aquino International Airport (MNL) - Manila", "Clark International Airport (CRK) - Angeles City, Pampanga"): 1200,
            ("Ninoy Aquino International Airport (MNL) - Manila", "Zamboanga International Airport (ZAM) - Zamboanga City"): 8000,
            ("Ninoy Aquino International Airport (MNL) - Manila", "Kalibo International Airport (KLO) - Kalibo, Aklan"): 6000,
            ("Ninoy Aquino International Airport (MNL) - Manila", "Iloilo International Airport (ILO) - Iloilo City"): 6500,
            ("Ninoy Aquino International Airport (MNL) - Manila", "Bacolod-Silay International Airport (BCD) - Bacolod City"): 7000,
            ("Ninoy Aquino International Airport (MNL) - Manila", "Francisco Bangoy International Airport (DVO) - Davao City"): 9000,
            ("Ninoy Aquino International Airport (MNL) - Manila", "Puerto Princesa International Airport (PPS) - Puerto Princesa, Palawan"): 2500,
            ("Mactan-Cebu International Airport (CEB) - Cebu", "Ninoy Aquino International Airport (MNL) - Manila"): 8000,
            ("Mactan-Cebu International Airport (CEB) - Cebu", "Clark International Airport (CRK) - Angeles City, Pampanga"): 8400,
            ("Mactan-Cebu International Airport (CEB) - Cebu", "Zamboanga International Airport (ZAM) - Zamboanga City"): 2000,
            ("Mactan-Cebu International Airport (CEB) - Cebu", "Kalibo International Airport (KLO) - Kalibo, Aklan"): 2000,
            ("Mactan-Cebu International Airport (CEB) - Cebu", "Iloilo International Airport (ILO) - Iloilo City"): 1200,
            ("Mactan-Cebu International Airport (CEB) - Cebu", "Bacolod-Silay International Airport (BCD) - Bacolod City"): 1100,
            ("Mactan-Cebu International Airport (CEB) - Cebu", "Francisco Bangoy International Airport (DVO) - Davao City"): 2500,
            ("Mactan-Cebu International Airport (CEB) - Cebu", "Puerto Princesa International Airport (PPS) - Puerto Princesa, Palawan"): 1200,
            ("Clark International Airport (CRK) - Angeles City, Pampanga", "Ninoy Aquino International Airport (MNL) - Manila"): 1200,
            ("Clark International Airport (CRK) - Angeles City, Pampanga", "Mactan-Cebu International Airport (CEB) - Cebu"): 8400,
            ("Clark International Airport (CRK) - Angeles City, Pampanga", "Zamboanga International Airport (ZAM) - Zamboanga City"): 8200,
            ("Clark International Airport (CRK) - Angeles City, Pampanga", "Kalibo International Airport (KLO) - Kalibo, Aklan"): 6200,
            ("Clark International Airport (CRK) - Angeles City, Pampanga", "Iloilo International Airport (ILO) - Iloilo City"): 6700,
            ("Clark International Airport (CRK) - Angeles City, Pampanga", "Bacolod-Silay International Airport (BCD) - Bacolod City"): 7200,
            ("Clark International Airport (CRK) - Angeles City, Pampanga", "Francisco Bangoy International Airport (DVO) - Davao City"): 9200,
            ("Clark International Airport (CRK) - Angeles City, Pampanga", "Puerto Princesa International Airport (PPS) - Puerto Princesa, Palawan"): 2700,
            ("Zamboanga International Airport (ZAM) - Zamboanga City", "Ninoy Aquino International Airport (MNL) - Manila"): 8000,
            ("Zamboanga International Airport (ZAM) - Zamboanga City", "Mactan-Cebu International Airport (CEB) - Cebu"): 2000,
            ("Zamboanga International Airport (ZAM) - Zamboanga City", "Clark International Airport (CRK) - Angeles City, Pampanga"): 8400,
            ("Zamboanga International Airport (ZAM) - Zamboanga City", "Kalibo International Airport (KLO) - Kalibo, Aklan"): 4500,
            ("Zamboanga International Airport (ZAM) - Zamboanga City", "Iloilo International Airport (ILO) - Iloilo City"): 4000,
            ("Zamboanga International Airport (ZAM) - Zamboanga City", "Bacolod-Silay International Airport (BCD) - Bacolod City"): 3500,
            ("Zamboanga International Airport (ZAM) - Zamboanga City", "Francisco Bangoy International Airport (DVO) - Davao City"): 1200,
            ("Zamboanga International Airport (ZAM) - Zamboanga City", "Puerto Princesa International Airport (PPS) - Puerto Princesa, Palawan"): 5000,
            ("Kalibo International Airport (KLO) - Kalibo, Aklan", "Ninoy Aquino International Airport (MNL) - Manila"): 6000,
            ("Kalibo International Airport (KLO) - Kalibo, Aklan", "Mactan-Cebu International Airport (CEB) - Cebu"): 2000,
            ("Kalibo International Airport (KLO) - Kalibo, Aklan", "Clark International Airport (CRK) - Angeles City, Pampanga"): 6200,
            ("Kalibo International Airport (KLO) - Kalibo, Aklan", "Zamboanga International Airport (ZAM) - Zamboanga City"): 4500,
            ("Kalibo International Airport (KLO) - Kalibo, Aklan", "Iloilo International Airport (ILO) - Iloilo City"): 1000,
            ("Kalibo International Airport (KLO) - Kalibo, Aklan", "Bacolod-Silay International Airport (BCD) - Bacolod City"): 1300,
            ("Kalibo International Airport (KLO) - Kalibo, Aklan", "Francisco Bangoy International Airport (DVO) - Davao City"): 7000,
            ("Kalibo International Airport (KLO) - Kalibo, Aklan", "Puerto Princesa International Airport (PPS) - Puerto Princesa, Palawan"): 4000,
            ("Iloilo International Airport (ILO) - Iloilo City", "Ninoy Aquino International Airport (MNL) - Manila"): 6500,
            ("Iloilo International Airport (ILO) - Iloilo City", "Mactan-Cebu International Airport (CEB) - Cebu"): 1200,
            ("Iloilo International Airport (ILO) - Iloilo City", "Clark International Airport (CRK) - Angeles City, Pampanga"): 6700,
            ("Iloilo International Airport (ILO) - Iloilo City", "Zamboanga International Airport (ZAM) - Zamboanga City"): 4000,
            ("Iloilo International Airport (ILO) - Iloilo City", "Kalibo International Airport (KLO) - Kalibo, Aklan"): 1000,
            ("Iloilo International Airport (ILO) - Iloilo City", "Bacolod-Silay International Airport (BCD) - Bacolod City"): 800,
            ("Iloilo International Airport (ILO) - Iloilo City", "Francisco Bangoy International Airport (DVO) - Davao City"): 5000,
            ("Iloilo International Airport (ILO) - Iloilo City", "Puerto Princesa International Airport (PPS) - Puerto Princesa, Palawan"): 3500,
            ("Bacolod-Silay International Airport (BCD) - Bacolod City", "Ninoy Aquino International Airport (MNL) - Manila"): 7000,
            ("Bacolod-Silay International Airport (BCD) - Bacolod City", "Mactan-Cebu International Airport (CEB) - Cebu"): 1100,
            ("Bacolod-Silay International Airport (BCD) - Bacolod City", "Clark International Airport (CRK) - Angeles City, Pampanga"): 7200,
            ("Bacolod-Silay International Airport (BCD) - Bacolod City", "Zamboanga International Airport (ZAM) - Zamboanga City"): 3500,
            ("Bacolod-Silay International Airport (BCD) - Bacolod City", "Kalibo International Airport (KLO) - Kalibo, Aklan"): 1300,
            ("Bacolod-Silay International Airport (BCD) - Bacolod City", "Iloilo International Airport (ILO) - Iloilo City"): 800,
            ("Bacolod-Silay International Airport (BCD) - Bacolod City", "Francisco Bangoy International Airport (DVO) - Davao City"): 4500,
            ("Bacolod-Silay International Airport (BCD) - Bacolod City", "Puerto Princesa International Airport (PPS) - Puerto Princesa, Palawan"): 4000,
            ("Francisco Bangoy International Airport (DVO) - Davao City", "Ninoy Aquino International Airport (MNL) - Manila"): 9000,
            ("Francisco Bangoy International Airport (DVO) - Davao City", "Mactan-Cebu International Airport (CEB) - Cebu"): 2500,
            ("Francisco Bangoy International Airport (DVO) - Davao City", "Clark International Airport (CRK) - Angeles City, Pampanga"): 9200,
            ("Francisco Bangoy International Airport (DVO) - Davao City", "Zamboanga International Airport (ZAM) - Zamboanga City"): 1200,
            ("Francisco Bangoy International Airport (DVO) - Davao City", "Kalibo International Airport (KLO) - Kalibo, Aklan"): 7000,
            ("Francisco Bangoy International Airport (DVO) - Davao City", "Iloilo International Airport (ILO) - Iloilo City"): 5000,
            ("Francisco Bangoy International Airport (DVO) - Davao City", "Bacolod-Silay International Airport (BCD) - Bacolod City"): 4500,
            ("Francisco Bangoy International Airport (DVO) - Davao City", "Puerto Princesa International Airport (PPS) - Puerto Princesa, Palawan"): 5000,
            ("Puerto Princesa International Airport (PPS) - Puerto Princesa, Palawan", "Ninoy Aquino International Airport (MNL) - Manila"): 2500,
            ("Puerto Princesa International Airport (PPS) - Puerto Princesa, Palawan", "Mactan-Cebu International Airport (CEB) - Cebu"): 1200,
            ("Puerto Princesa International Airport (PPS) - Puerto Princesa, Palawan", "Clark International Airport (CRK) - Angeles City, Pampanga"): 2700,
            ("Puerto Princesa International Airport (PPS) - Puerto Princesa, Palawan", "Zamboanga International Airport (ZAM) - Zamboanga City"): 5000,
            ("Puerto Princesa International Airport (PPS) - Puerto Princesa, Palawan", "Kalibo International Airport (KLO) - Kalibo, Aklan"): 4000,
            ("Puerto Princesa International Airport (PPS) - Puerto Princesa, Palawan", "Iloilo International Airport (ILO) - Iloilo City"): 3500,
            ("Puerto Princesa International Airport (PPS) - Puerto Princesa, Palawan", "Bacolod-Silay International Airport (BCD) - Bacolod City"): 4000,
            ("Puerto Princesa International Airport (PPS) - Puerto Princesa, Palawan", "Francisco Bangoy International Airport (DVO) - Davao City"): 5000
        }

        key = (origin, destination)
        return fixed_fares.get(key, 0)  

    def getAirlineFare(self, airline):
        airline_fares = {"Philippine Airlines": 200, "Cebu Pacific Air": 80, "AirAsia": 120}

        return airline_fares.get(airline, 0) 

    def getClassFare(self, selected_class):

        class_fares = {"Economy": 100, "Business": 200}

        return class_fares.get(selected_class, 0)

    def viewFlight(self):
        self.out.delete(*self.out.get_children())  
        for row in db.viewFlight():
            formatted_row = list(row)
            if formatted_row[2] is not None:
                formatted_row[2] = formatted_row[2].strftime('%m/%d/%Y')
            self.out.insert("", END, values=tuple(formatted_row))

    def resetForm(self):
        self.insFlightID.set("")
        self.insDepartureTime.set("")
        self.Airline.set("")
        self.ArrivalTime.set("")
        self.Origin.set("")
        self.Destination.set("")
        self.EconomyAvailableSeats.set("")
        self.BusinessAvailableSeats.set("")

    # Method to redirect to the login frame
    def logOut(self):
        self.entriesFrame.destroy()
        self.buttonsFrame.destroy()
        self.tableFrame.destroy()
        
        Login.PassengerLogin(self.root)

    """CTA Buttons Frame"""

    def openPassengerListWindow(self):

        self.root.withdraw()
        # Open the ViewPassengerList window
        passenger_list_window = Toplevel(self.root)
        passenger_list_window.geometry(self.root.geometry())
        ViewPList(passenger_list_window)

    def adminFrameButtons(self):
        # Button Frame Configurations
        self.buttonsFrame = Frame(self.entriesFrame, bg="#003b95")
        self.buttonsFrame.grid(row=10, column=0, padx=10, pady=10, sticky="w", columnspan=8)

        self.btnAdd = Button(self.buttonsFrame, command=self.addFlight, text="Add Flight", bd=0, cursor="hand2",
                             bg="#d5e7ff",
                             fg="#003b95", width=20, font=("Impact", 15))
        self.btnAdd.grid(row=0, column=0, padx=10)

        self.btnDlt = Button(self.buttonsFrame, command=self.deleteFlight, text="Remove Flight", bd=0,
                             cursor="hand2",
                             bg="#d5e7ff",
                             fg="#003b95", width=20, font=("Impact", 15))
        self.btnDlt.grid(row=0, column=1, padx=10)

        self.btnView = Button(self.buttonsFrame, command=self.viewFlight, text="View Flight List", bd=0,
                              cursor="hand2",
                              bg="#d5e7ff",
                              fg="#003b95", width=20, font=("Impact", 15))
        self.btnView.grid(row=0, column=2, padx=10)

        self.btnViewPassengerList = Button(self.buttonsFrame, command=self.openPassengerListWindow,
                                       text="View Passenger List", bd=0, cursor="hand2",
                                       bg="#d5e7ff",
                                       fg="#003b95", width=20, font=("Impact", 15))
        self.btnViewPassengerList.grid(row=0, column=3, padx=10)

        self.btnLogOut = Button(self.entriesFrame, command=self.logOut, text="Log Out", bd=0, cursor="hand2",
                                bg="#d5e7ff",
                                fg="#003b95", width=15, font=("Impact", 15))
        self.btnLogOut.grid(row=0, column=4, padx=(50, 15), sticky="e")


    def tableOutputFrame(self):
        # Treeview Frame Configurations
        self.tableFrame = Frame(self.root, bg="#DADDE6")
        self.tableFrame.place(x=0, y=359, width=1255, height=415)
        self.yScroll = Scrollbar(self.tableFrame)
        self.yScroll.pack(side=RIGHT, fill=Y)

        self.style = ttk.Style()
        self.style.configure("mystyle.Treeview", font=('Calibri', 12),
                             rowheight=50)
        self.style.configure("mystyle.Treeview.Heading", font=('Times New Roman', 14, "bold"), sticky="w")

        self.out = ttk.Treeview(self.tableFrame, yscrollcommand=self.yScroll.set,
                                columns=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11), style="mystyle.Treeview")
        self.out.heading("1", text="Flight ID")
        self.out.column("1", width=1)
        self.out.heading("2", text="Airline")
        self.out.column("2", width=15)
        self.out.heading("3", text="Flight Date")
        self.out.column("3", width=1)
        self.out.heading("4", text="Departure")
        self.out.column("4", width=1)
        self.out.heading("5", text="Arrival")
        self.out.column("5", width=1)
        self.out.heading("6", text="Origin")
        self.out.column("6", width=30)
        self.out.heading("7", text="Destination")
        self.out.column("7", width=30)
        self.out.heading("8", text="E. Seats")
        self.out.column("8", width=1)
        self.out.heading("9", text="E. Fare")
        self.out.column("9", width=1)
        self.out.heading("10", text="B. Seats")
        self.out.column("10", width=1)
        self.out.heading("11", text="B. Fare")
        self.out.column("11", width=1)

        self.out['show'] = 'headings'

        # Virtual Events to trigger methods
        self.out.bind("<ButtonRelease-1>", self.getData)

        # TreeView output layout configurations
        self.out.pack(fill=BOTH, expand=True)
        self.yScroll.config(command=self.out.yview)
