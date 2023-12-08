from tkinter import *
from tkinter import ttk
from database_ import Database
from tkinter import messagebox
from BookingPanel import BookFlight  
from BookedWindow import BookedFlight
import Login
from tkcalendar import *
from tkcalendar import DateEntry
from datetime import datetime

db = Database(host="localhost", user="root", password="", database="ABMS")

class SearchFlight:
    def __init__(self, root, username):
        self.root = root
        self.username = username

        # local variables
        self.Origin = StringVar()
        self.Destination = StringVar()
        self.FlightDate = StringVar()
        self.Class = StringVar()

        # Call the tkinter frames to the window
        self.searchFlightFrame()
        self.SFFrameButtons()
        self.tableOutputFrame()


    def searchFlightFrame(self):
        self.entriesFrame = Frame(self.root, bg="#003b95")
        self.entriesFrame.pack(side=TOP, fill=BOTH)
        self.search_frame_title = Label(self.entriesFrame, text="Passenger Panel", font=("Goudy old style", 35),
                                       bg="#003b95",
                                       fg="white")
        self.search_frame_title.grid(row=0, columnspan=2, padx=10, pady=20, sticky="w")

        #Origin
        self.labelOrigin = Label(self.entriesFrame, text="Origin", font=("Times New Roman", 16, "bold"),
                                bg="#003b95",
                                fg="white")
        self.labelOrigin.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.comboOrigin = ttk.Combobox(self.entriesFrame, textvariable=self.Origin, font=("Times New Roman", 15), width=57, state="readonly")
        self.comboOrigin['values'] = ("Ninoy Aquino International Airport (MNL) - Manila", "Mactan-Cebu International Airport (CEB) - Cebu", "Clark International Airport (CRK) - Angeles City, Pampanga", 
                                      "Iloilo International Airport (ILO) - Iloilo City", "Kalibo International Airport (KLO) - Kalibo, Aklan",
                                      "Bacolod-Silay International Airport (BCD) - Bacolod City", "Francisco Bangoy International Airport (DVO) - Davao City", 
                                      "Puerto Princesa International Airport (PPS) - Puerto Princesa, Palawan","Zamboanga International Airport (ZAM) - Zamboanga City" )
        self.comboOrigin.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        #Destination
        self.labelDestination = Label(self.entriesFrame, text="Destination", font=("Times New Roman", 16, "bold"), bg="#003b95",
                                fg="white")
        self.labelDestination.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.comboDestination = ttk.Combobox(self.entriesFrame, textvariable=self.Destination, font=("Times New Roman", 15), width=57, state="readonly")
        self.comboDestination['values'] = ("Ninoy Aquino International Airport (MNL) - Manila", "Mactan-Cebu International Airport (CEB) - Cebu", "Clark International Airport (CRK) - Angeles City, Pampanga", 
                                      "Iloilo International Airport (ILO) - Iloilo City", "Kalibo International Airport (KLO) - Kalibo, Aklan",
                                      "Bacolod-Silay International Airport (BCD) - Bacolod City", "Francisco Bangoy International Airport (DVO) - Davao City", 
                                      "Puerto Princesa International Airport (PPS) - Puerto Princesa, Palawan","Zamboanga International Airport (ZAM) - Zamboanga City" )
        self.comboDestination.grid(row=2, column=1, padx=10, pady=5, sticky="w")

        #Flight Date
        min_date = datetime.now().date()
        
        self.labelFlightDate= Label(self.entriesFrame, text="Flight Date", font=("Times New Roman", 16, "bold"),
                              bg="#003b95",
                              fg="white")
        self.labelFlightDate.grid(row=1, column=2, padx=10, pady=5, sticky="w")
        self.dateEntryFlightDate = DateEntry(self.entriesFrame, textvariable=self.FlightDate, font=("Times New Roman", 15),
                                             width=10, background='darkblue', foreground='white', borderwidth=2,
                                             mindate=min_date, state="readonly", date_pattern='mm/dd/yyyy')
        self.dateEntryFlightDate.grid(row=1, column=3, padx=10, pady=5, sticky="w")

        self.labelClass = Label(self.entriesFrame, text="Class", font=("Times New Roman", 16, "bold"), bg="#003b95", fg="white")
        self.labelClass.grid(row=2, column=2, padx=10, pady=5, sticky="w")
        self.comboClass = ttk.Combobox(self.entriesFrame, textvariable=self.Class, font=("Times New Roman", 15), width=10, state="readonly")
        self.comboClass['values'] = ("Economy", "Business")  # Add more classes as needed
        self.comboClass.grid(row=2, column=3, padx=10, pady=5, sticky="w")

    # event trigger Method to display the chosen data from the TreeView back in respective fields
    def getData(self, event=None):
            self.selectedRow = self.out.focus()
            self.selectedData = self.out.item(self.selectedRow)
            self.chosenRow = self.selectedData["values"]



    def viewBookedFlightsWindow(self):
        self.root.withdraw()

        # Open the BookFlight window
        booked_window = Toplevel(self.root)
        booked_window.geometry(self.root.geometry())
        BookedFlight(booked_window, self.username)

    def searchFlights(self):
        # Retrieve values from comboboxes
        flight_date = self.FlightDate.get()
        origin = self.Origin.get()
        destination = self.Destination.get()
        selected_class = self.Class.get()

        # Validate if any option is selected
        if not (origin and destination and selected_class):
            messagebox.showerror("Error!", "Please fill in all the search criteria.")
            return

        # Search for flights based on user selections
        flights = db.searchFlights(origin, destination, flight_date, selected_class)

        # Clear the TreeView
        self.out.delete(*self.out.get_children())

        # Display the search results in the TreeView
        for row in flights:
            # Check if there are available seats in the selected class
            if (selected_class == "Economy" and row[8] > 0) or (selected_class == "Business" and row[9] > 0):
                # Display only specific columns based on the selected class
                if selected_class == "Economy":
                    formatted_row = (
                        row[0], row[1], datetime.strftime(row[2], '%m/%d/%Y'), row[3], row[4], row[5], row[6], row[8], "")
                else:  # selected_class == "Business"
                    formatted_row = (
                        row[0], row[1], datetime.strftime(row[2], '%m/%d/%Y'), row[3], row[4], row[5], row[6], "", row[10])

                # Insert the formatted row into the TreeView
                self.out.insert("", END, values=formatted_row)

    def selectFlight(self):
        try:
            # Get the selected flight information
            selected_row = self.out.focus()
            selected_data = self.out.item(selected_row)
            chosen_row = selected_data["values"]

            # Store the selected flight information
            self.selectedFlightInfo = chosen_row

            selected_class = self.Class.get()

            self.root.withdraw()

            # Open the BookFlight window and pass the selected flight information and class
            BookingPanel = Toplevel(self.root)
            BookingPanel.geometry(self.root.geometry())
            BookFlight(BookingPanel, self.selectedFlightInfo, self.username, selected_class)
        except IndexError as error:
            pass


    # Method to reset all input widgets in the frame
    def resetForm(self):
        self.Origin.set("")
        self.Destination.set("")
        self.FlightDate.set("")
        self.Class.set("")

    # Method to redirect to the login frame
    def logOut(self):
        self.entriesFrame.destroy()
        self.buttonsFrame.destroy()
        self.tableFrame.destroy()
        Login.PassengerLogin(self.root)

    def SFFrameButtons(self):
        # Button Frame Configurations
        self.buttonsFrame = Frame(self.entriesFrame, bg="#003b95")
        self.buttonsFrame.grid(row=10, column=0, padx=10, pady=10, sticky="w", columnspan=8)

        self.btnSearch= Button(self.buttonsFrame, command=self.searchFlights, text="Search", bd=0, cursor="hand2",
                             bg="#d5e7ff",
                             fg="#003b95", width=20, font=("Impact", 15))
        self.btnSearch.grid(row=0, column=0, padx=10)

        self.btnSelect = Button(self.buttonsFrame, command=self.selectFlight, text="Select", bd=0, cursor="hand2",
                                bg="#d5e7ff", fg="#003b95", width=20, font=("Impact", 15))
        self.btnSelect.grid(row=0, column=1, padx=10)

        self.btnViewBookedFlights = Button(self.buttonsFrame, command=self.viewBookedFlightsWindow, text="View Booked Flights",
                                           bd=0, cursor="hand2",
                                           bg="#d5e7ff", fg="#003b95", width=20, font=("Impact", 15))
        self.btnViewBookedFlights.grid(row=0, column=2, padx=10)

        self.btnLogOut = Button(self.entriesFrame, command=self.logOut, text="Log Out", bd=0, cursor="hand2",
                                bg="#d5e7ff",
                                fg="#003b95", width=15, font=("Impact", 15))
        self.btnLogOut.grid(row=0, column=4, padx=(50, 15), sticky="e")

    def tableOutputFrame(self):
        # Treeview Frame Configurations
        self.tableFrame = Frame(self.root, bg="#DADDE6")
        self.tableFrame.place(x=0, y=239, width=1255, height=516)
        self.yScroll = Scrollbar(self.tableFrame)
        self.yScroll.pack(side=RIGHT, fill=Y)

        self.style = ttk.Style()
        self.style.configure("mystyle.Treeview", font=('Calibri', 12),
                            rowheight=50)
        self.style.configure("mystyle.Treeview.Heading", font=('Times New Roman', 14, "bold"), sticky="w")

        self.out = ttk.Treeview(self.tableFrame, yscrollcommand=self.yScroll.set,
                                columns=(1, 2, 3, 4, 5, 6, 7, 8, 9), style="mystyle.Treeview") 
        self.out.heading("1", text="Flight ID")
        self.out.column("1", width=10)
        self.out.heading("2", text="Airline")
        self.out.column("2", width=30)
        self.out.heading("3", text="Flight Date")
        self.out.column("3", width=30)
        self.out.heading("4", text="Departure")
        self.out.column("4", width=5)
        self.out.heading("5", text="Arrival")
        self.out.column("5", width=8)
        self.out.heading("6", text="Origin")
        self.out.column("6", width=10)
        self.out.heading("7", text="Destination")
        self.out.column("7", width=6)
        self.out.heading("8", text="Economy Fare")
        self.out.column("8", width=5)
        self.out.heading("9", text="Business Fare")
        self.out.column("9", width=5)
        

        self.out['show'] = 'headings'

        # Virtual Events to trigger methods
        self.out.bind("<ButtonRelease-1>", self.getData)

        # TreeView output layout configurations
        self.out.pack(fill=BOTH, expand=True)
        self.yScroll.config(command=self.out.yview)
