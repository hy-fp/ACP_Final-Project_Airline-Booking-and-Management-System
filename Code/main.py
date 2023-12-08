from tkinter import *
import Login

#main method
def main():

    root = Tk()
    root.title("Travel Tours")
    root.geometry("1255x775")
    root.resizable(False, True)

    root.iconbitmap(r"C:\Users\Hannah\Downloads\airplanelogo.ico")


    Login.PassengerLogin(root)
    root.mainloop()

if __name__ == '__main__':

    main()
