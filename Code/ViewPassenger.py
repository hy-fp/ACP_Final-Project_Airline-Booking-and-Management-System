from tkinter import *
from tkinter import ttk
from database_ import Database
from tkinter import messagebox
from tkcalendar import *


db = Database(host="localhost", user="root", password="", database="ABMS")

class ViewPList:
    def __init__(self, root):
        self.root = root

        self.search_entry = StringVar()

        self.ViewListFrame()
        self.tableOutputFrame()
        self.viewPassengerList()

    """Instructor Info Entries Frame"""

    def ViewListFrame(self):
        # Admin Control Frame Configurations
        self.entriesFrame = Frame(self.root, bg="#003b95")
        self.entriesFrame.pack(side=TOP, fill=BOTH)
        self.search_frame_title = Label(self.entriesFrame, text="Passenger List", font=("Goudy old style", 35),
                                       bg="#003b95",
                                       fg="white")
        self.search_frame_title.grid(row=0, columnspan=2, padx=10, pady=20, sticky="w")

        self.btnSearch = Button(self.entriesFrame, command=self.searchPassengers, text="Search", bd=0, cursor="hand2",
                                bg="#d5e7ff",
                                fg="#003b95", width=10, font=("Impact", 12))
        self.btnSearch.grid(row=1, column=1, padx=10, pady=5, sticky="w")
        self.txtSearch = Entry(self.entriesFrame, textvariable=self.search_entry, font=("Times New Roman", 15), width=20)
        self.txtSearch.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        
        self.btnBack = Button(self.entriesFrame, command=self.logOut, text="Back", bd=0, cursor="hand2",
                                bg="#d5e7ff",
                                fg="#003b95", width=15, font=("Impact", 15))
        self.btnBack.grid(row=0, column=6, padx=700, pady=5, sticky="e")
    """Sub Methods to be used in primary CTA methods"""

    def viewPassengerList(self):
        passenger_list = db.viewPassengerList()
        self.displayPassengers(passenger_list)

    def displayPassengers(self, passengers):
        # Clear the TreeView
        self.out.delete(*self.out.get_children())

        # Display the passenger list in the TreeView
        for row in passengers:
            self.out.insert("", END, values=row)

    def searchPassengers(self):
        search_term = self.search_entry.get()
        passenger_list = db.searchPassengerList(search_term)
        self.displayPassengers(passenger_list)

    # Method to redirect to the login frame
    def logOut(self):
        self.root.withdraw()

        from AdminPanel import AdminControls

        admin_window = Toplevel(self.root)
        admin_window.geometry(self.root.geometry())
        AdminControls(admin_window)

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
                                columns=(1, 2, 3, 4, 5, 6, 7), style="mystyle.Treeview")
        self.out.heading("1", text="PassengerID")
        self.out.column("1", width=20)
        self.out.heading("2", text="Username")
        self.out.column("2", width=40)
        self.out.heading("3", text="Name")
        self.out.column("3", width=80)
        self.out.heading("4", text="Email")
        self.out.column("4", width=30)
        self.out.heading("5", text="Gender")
        self.out.column("5", width=30)
        self.out.heading("6", text="CellNo")
        self.out.column("6", width=20)
        self.out.heading("7", text="FlightID")
        self.out.column("7", width=20)
        self.out['show'] = 'headings'

        # TreeView output layout configurations
        self.out.pack(fill=BOTH, expand=True)
        self.yScroll.config(command=self.out.yview)
