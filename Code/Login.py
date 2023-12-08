from tkinter import *
from tkinter import messagebox
from PassengerPanel import SearchFlight
from database_ import Database
from adminlogin import AdminLogin
import mysql.connector

db = Database(host="localhost", user="root", password="", database="ABMS")

class PassengerLogin:
    def __init__(self, root):
        self.root = root

        self.username = StringVar()
        self.password = StringVar()

        self.root.config(bg="#003b95")

        self.loginControlFrame()

    def loginFunc(self):
        username = self.txtUsername.get()
        password = self.txtPassword.get()

        if not username or not password:
            messagebox.showinfo('Error!', 'Please provide both username and password.')
            return

        result = db.passengerLogin(username, password)

        if result:
            self.username = username
            self.root.withdraw()

            # Open the BookFlight window
            PassengerPanel = Toplevel(self.root)
            PassengerPanel.geometry(self.root.geometry())
            SearchFlight(PassengerPanel, self.username)
        else:
            messagebox.showinfo('Error!', 'Invalid Credentials')

    def passengerSignUp(self):
        username = self.txtUsername.get()
        password = self.txtPassword.get()

        if not username or not password:
            messagebox.showinfo('Error!', 'Please provide both username and password.')
            return

        result = db.passengerSignUp(username)

        if result:
            messagebox.showinfo('Error!', 'Username Already Taken!')
        else:
            db.insertPassengerAcc(username, password)
            messagebox.showinfo('Success!', 'Account Created!')

    def openAdminLogin(self):

        self.root.withdraw()
        admin_login_window = Toplevel(self.root)
        admin_login_window.geometry(self.root.geometry())
        AdminLogin(admin_login_window)

    def loginControlFrame(self):
        # Login Frame Configurations
        self.loginFrame = Frame(self.root, bg="white")
        self.loginFrame.pack(side=LEFT, fill=X, padx=60)
        self.login_frame_title = Label(self.loginFrame, text="Passenger", font=("Impact", 35), bg="white",
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

        self.btnLogin = Button(self.loginFrame, command=self.loginFunc, text="Login", bd=0, cursor="hand2",
                       fg="white", bg="#003b95", width=10, font=("Impact", 15))
        self.btnLogin.grid(row=3, column=1, padx=(15,30))

        self.btnSignUp = Button(self.loginFrame, command=self.passengerSignUp, text="Sign Up", bd=0, cursor="hand2",
                                fg="white", bg="#003b95", width=10, font=("Impact", 15))
        self.btnSignUp.grid(row=3, column=1, padx=(20,9), sticky="e")

        self.btnAdm = Button(self.loginFrame, command=self.openAdminLogin, text="Admin Login", bd=0, cursor="hand2",
                               fg="white", bg="#003b95", width=12, font=("Impact", 10))
        self.btnAdm.grid(row=4, column=1, padx=10, sticky="e")

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
