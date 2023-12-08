from tkinter import *
from tkinter import ttk
from database_ import Database
from tkinter import messagebox
from BookingPanel import BookFlight  
from tkcalendar import *

db = Database(host="localhost", user="root", password="", database="ABMS")

class BookedFlight:
    def __init__(self, root, username):
        self.root = root
        self.username = username

        self.search_entry = StringVar()

        self.BookedFlightFrame()
        self.tableOutputFrame()
        self.viewBookedFlights()

    """Instructor Info Entries Frame"""

    def BookedFlightFrame(self):
        # Admin Control Frame Configurations
        self.entriesFrame = Frame(self.root, bg="#003b95")
        self.entriesFrame.pack(side=TOP, fill=BOTH)
        self.search_frame_title = Label(self.entriesFrame, text="Booked Flights", font=("Goudy old style", 35),
                                       bg="#003b95",
                                       fg="white")
        self.search_frame_title.grid(row=0, columnspan=2, padx=10, pady=20, sticky="w")

        self.btnSearch = Button(self.entriesFrame, command=self.searchInfo, text="Search", bd=0, cursor="hand2",
                                bg="#d5e7ff",
                                fg="#003b95", width=10, font=("Impact", 12))
        self.btnSearch.grid(row=1, column=1, padx=10, pady=5, sticky="w")
        self.txtSearch = Entry(self.entriesFrame, textvariable=self.search_entry, font=("Times New Roman", 15), width=40)
        self.txtSearch.grid(row=1, column=0, padx=10, pady=5, sticky="w")

        self.btnViewDetails = Button(self.entriesFrame, command=self.viewDetails, text="View Details", bd=0, cursor="hand2",
                                     bg="#d5e7ff",
                                     fg="#003b95", width=15, font=("Impact", 15))
        self.btnViewDetails.grid(row=1, column=3, padx=10, sticky="e")
        
        self.btnBack = Button(self.entriesFrame, command=self.back, text="Back", bd=0, cursor="hand2",
                                bg="#d5e7ff",
                                fg="#003b95", width=15, font=("Impact", 15))
        self.btnBack.grid(row=0, column=4, padx=(340, 15), sticky="e")

    def getData(self, event=None):
            self.selectedRow = self.out.focus()
            self.selectedData = self.out.item(self.selectedRow)
            self.chosenRow = self.selectedData["values"]

    def viewDetails(self):
        try:
            # Get the selected row
            selected_row = self.out.focus()
            selected_data = self.out.item(selected_row)
            chosen_row = selected_data["values"]

            # Display details in a prompt
            flight_details = f"Flight ID: {chosen_row[0]}\n" \
                            f"Airline: {chosen_row[1]}\n" \
                            f"Flight Date: {chosen_row[2]}\n" \
                            f"Departure Time: {chosen_row[3]}\n" \
                            f"Arrival Time: {chosen_row[4]}\n" \
                            f"Origin: {self.get_terminal_info(chosen_row[5])}\n" \
                            f"Destination: {self.get_terminal_info(chosen_row[6], destination=True)}\n" \
                            f"Class: {chosen_row[7]}\n" \
                            f"Fare: {chosen_row[8]}\n"

            # Add terminal and hotel information based on origin and destination
            terminal_info = self.get_terminal_info(chosen_row[5])  # Origin
            terminal_info += self.get_terminal_info(chosen_row[6], destination=True)  # Destination

            hotel_info = self.get_hotel_info(chosen_row[5])  # Origin
            hotel_info += "\n" + self.get_hotel_info(chosen_row[6], destination=True)  # Destination

            details_prompt = f"{flight_details}\n\n{hotel_info}"

            messagebox.showinfo("Flight Details", details_prompt)

        except IndexError:
            messagebox.showerror("Error!", "Please Choose a Flight Record to View Details!")

    def get_terminal_info(self, location, destination=False):
        if location in ["Ninoy Aquino International Airport (MNL) - Manila", "Mactan-Cebu International Airport (CEB) - Cebu", "Clark International Airport (CRK) - Angeles City, Pampanga"]:
            terminal = "Terminal 1"
        elif location in ["Bacolod-Silay International Airport (BCD) - Bacolod City", "Iloilo International Airport (ILO) - Iloilo City"]:
            terminal = "Terminal 2"
        elif location in ["Kalibo International Airport (KLO) - Kalibo, Aklan","Francisco Bangoy International Airport (DVO) - Davao City"]:
            terminal = "Terminal 3"
        elif location in ["Puerto Princesa International Airport (PPS) - Puerto Princesa, Palawan", "Zamboanga International Airport (ZAM) - Zamboanga City"]:
            terminal = "Terminal 4"
        else:
            terminal = "Not specified"

        location_type = "Destination" if destination else "Origin"
        return f"{location} | {terminal}"

    def get_hotel_info(self, location, destination=False):

        if location == "Ninoy Aquino International Airport (MNL) - Manila":
            hotel = "Manila Marriott Hotel"
        elif location == "Mactan-Cebu International Airport (CEB) - Cebu":
            hotel = "Shangri-La's Mactan Resort and Spa"
        elif location == "Clark International Airport (CRK) - Angeles City, Pampanga":
            hotel = "Midori Clark Hotel and Casino"
        elif location == "Iloilo International Airport (ILO) - Iloilo City":
            hotel = "Richmonde Hotel Iloilo"
        elif location == "Kalibo International Airport (KLO) - Kalibo, Aklan":
            hotel = "Discover Boracay Hotel"
        elif location == "Bacolod-Silay International Airport (BCD) - Bacolod City":
            hotel = "L'Fisher Hotel"
        elif location == "Francisco Bangoy International Airport (DVO) - Davao City":
            hotel = "Marco Polo Davao"
        elif location == "Puerto Princesa International Airport (PPS) - Puerto Princesa, Palawan":
            hotel = "Astoria Palawan"
        elif location == "Zamboanga International Airport (ZAM) - Zamboanga City":
            hotel = "Grand Astoria Hotel"
        else:
            hotel = "Hotel information not available"

        location_type = "Destination" if destination else "Origin"
        return f"Recommended Hotel Near {location}: {hotel}"

    def searchInfo(self):
        search_term = self.search_entry.get()
        if search_term:
            # Search for flights based on the entered search term
            flights = db.searchBookedFlights(self.username, search_term)
            self.displayFlights(flights)
        else:
            self.viewBookedFlights()

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

    # Method to redirect to the login frame
    def back(self):
        self.root.withdraw()

        from PassengerPanel import SearchFlight

        search_window = Toplevel(self.root)
        search_window.geometry(self.root.geometry())
        SearchFlight(search_window, self.username)

    """CTA Buttons Frame"""

    def tableOutputFrame(self):
        # Treeview Frame Configurations
        self.tableFrame = Frame(self.root, bg="#DADDE6")
        self.tableFrame.place(x=0, y=140, width=1255, height=650)
        self.yScroll = Scrollbar(self.tableFrame)
        self.yScroll.pack(side=RIGHT, fill=Y)

        self.style = ttk.Style()
        self.style.configure("mystyle.Treeview", font=('Calibri', 12),
                             rowheight=50)
        self.style.configure("mystyle.Treeview.Heading", font=('Times New Roman', 14, "bold"), sticky="w")

        self.out = ttk.Treeview(self.tableFrame, yscrollcommand=self.yScroll.set,
                                columns=(1, 2, 3, 4, 5, 6, 7, 8, 9), style="mystyle.Treeview")
        self.out.heading("1", text="Flight ID")
        self.out.column("1", width=1)
        self.out.heading("2", text="Airline")
        self.out.column("2", width=30)
        self.out.heading("3", text="Flight Date")
        self.out.column("3", width=3)
        self.out.heading("4", text="Departure")
        self.out.column("4", width=1)
        self.out.heading("5", text="Arrival")
        self.out.column("5", width=1)
        self.out.heading("6", text="Origin")
        self.out.column("6", width=170)
        self.out.heading("7", text="Destination")
        self.out.column("7", width=170)
        self.out.heading("8", text="Class")
        self.out.column("8", width=1)
        self.out.heading("9", text="Fare")
        self.out.column("9", width=1)
        self.out['show'] = 'headings'

        # Virtual Events to trigger methods
        self.out.bind("<ButtonRelease-1>", self.getData)

        # TreeView output layout configurations
        self.out.pack(fill=BOTH, expand=True)
        self.yScroll.config(command=self.out.yview)