from tkinter import *
from tkinter import messagebox
from AdminPanel import AdminControls 
from database_ import Database

db = Database(host="localhost", user="root", password="", database="ABMS")

class AdminLogin:
    def __init__(self, root):
        self.root = root

        self.username = StringVar()
        self.password = StringVar()

        # Background Color
        self.root.config(bg="#003b95")

        self.loginControlFrame()

    def adminloginFunc(self):
        if self.txtUsername.get() == 'admin' and self.txtPassword.get() == 'admin':
            self.root.withdraw()

            # Open the BookFlight window
            admin_controls_window = Toplevel(self.root)
            admin_controls_window.geometry(self.root.geometry())
            AdminControls(admin_controls_window)
        else:
            messagebox.showerror("Error!", "Check your credentials or Please Contact System Admin!")
            self.username.set("")
            self.password.set("")

    def backToPassengerLogin(self):
        self.root.withdraw()

        # Importing PassengerLogin inside the function to avoid circular import
        from Login import PassengerLogin

        # Open the PassengerLogin window
        passenger_login_window = Toplevel(self.root)
        passenger_login_window.geometry(self.root.geometry())
        PassengerLogin(passenger_login_window)

    def loginControlFrame(self):
        # Login Frame Configurations
        self.loginFrame = Frame(self.root, bg="white")
        self.loginFrame.pack(side=LEFT, fill=X, padx=60)
        self.login_frame_title = Label(self.loginFrame, text="Admin", font=("Impact", 35), bg="white",
                                       fg="#003b95")
        self.login_frame_title.grid(row=0, columnspan=2, padx=10, pady=20, sticky="w")

        self.labelUsername = Label(self.loginFrame, text="Username", font=("Times New Roman", 16, "bold"), bg="white",
                                   fg="#003b95")
        self.labelUsername.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.txtUsername = Entry(self.loginFrame, textvariable=self.username, font=("Times New Roman", 15), width=30,
                                 bd=5)
        self.txtUsername.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        self.labelPassword = Label(self.loginFrame, text="Password", font=("Times New Roman", 16, "bold"), bg="white",
                                   fg="#003b95")
        self.labelPassword.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.txtPassword = Entry(self.loginFrame, textvariable=self.password, font=("Times New Roman", 15), width=30,
                                 bd=5, show="*")
        self.txtPassword.grid(row=2, column=1, padx=10, pady=5, sticky="w")

        self.btnLogin = Button(self.loginFrame, command=self.adminloginFunc, text="Login", bd=0, cursor="hand2",
                               fg="white", bg="#003b95", width=10, font=("Impact", 15))
        self.btnLogin.grid(row=3, column=1, padx=10, sticky="e")

        self.btnBack = Button(self.loginFrame, command=self.backToPassengerLogin, text="Back", bd=0, cursor="hand2",
                              fg="white", bg="#003b95", width=10, font=("Impact", 10))
        self.btnBack.grid(row=4, column=1, padx=10, sticky="e")

        # empty label for spacing in grid
        self.emptyLabel = Label(self.loginFrame, font=("Times New Roman", 16, "bold"), bg="white",
                                fg="#003b95")
        self.emptyLabel.grid(row=4, column=1, padx=10, pady=5, sticky="w")

        # Right Side Frame as Welcome Message
        self.rightFrame = Frame(self.root, bg="#003b95")
        self.rightFrame.pack(side=RIGHT)

        self.labelCompanyName = Label(self.rightFrame, text="Travel Tours", font=("Impact", 80),
                                      bg="#003b95",
                                      fg="white")
        self.labelCompanyName.grid(row=0, column=1, columnspan=2, padx=10)
        self.labelDesc = Label(self.rightFrame, text="It's more fun in the Philippines!", font=("Times New Roman", 25, "italic"),
                               bg="#003b95",
                               fg="white")
        self.labelDesc.grid(row=1, column=1, columnspan=2, padx=10, pady=6)
