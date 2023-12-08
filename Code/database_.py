import mysql.connector
from tkinter import messagebox
from datetime import datetime

class Database:
    def __init__(self, host, user, password, database):
        # creating database connection
        self.con = mysql.connector.connect(host="localhost", user="root", password="", database="ABMS")
        self.cur = self.con.cursor()

        # SQL queries to create tables

        sql_flight_info = """
        CREATE TABLE IF NOT EXISTS FlightInfo (
            FlightID INT PRIMARY KEY,
            Airline VARCHAR(255),
            FlightDate DATE,
            DepartureTime VARCHAR(255),
            ArrivalTime VARCHAR(255),
            Origin VARCHAR(100),
            Destination VARCHAR(105),
            E_Seats INT,
            EconomyTotalFare INT,
            B_Seats INT,
            BusinessTotalFare INT
        )
        """

        sql_login_info = """
        CREATE TABLE IF NOT EXISTS LoginInfo (
            Username VARCHAR(20) PRIMARY KEY,
            Password VARCHAR(40)
        )
        """

        sql_passenger_info = """
        CREATE TABLE IF NOT EXISTS PassengerInfo (
            PassengerID INT AUTO_INCREMENT PRIMARY KEY,
            Username VARCHAR(20),
            Name VARCHAR(40),
            Email VARCHAR(40),
            Gender ENUM('Male', 'Female', 'Other', 'Prefer Not to Say'),
            CellNo VARCHAR(11)
        )
        """

        sql_booked_flights = """
        CREATE TABLE IF NOT EXISTS BookedFlights (
            BookingID INT AUTO_INCREMENT PRIMARY KEY,
            Username VARCHAR(20),
            FlightID INT,
            PassengerID INT, 
            Class ENUM('Economy', 'Business'),  -- Add this line for the booked class
            FOREIGN KEY(PassengerID) REFERENCES PassengerInfo(PassengerID),
            FOREIGN KEY(Username) REFERENCES LoginInfo(Username),
            FOREIGN KEY(FlightID) REFERENCES FlightInfo(FlightID)
        )
        """

        # cursor executions
        self.cur.execute(sql_flight_info)
        self.cur.execute(sql_login_info)
        self.cur.execute(sql_passenger_info)
        self.cur.execute(sql_booked_flights)
        self.con.commit()

    # Add Flight record to the table
    def insertFlight(self, FlightID, Airline, FlightDate, DepartureTime, ArrivalTime, Origin, Destination, E_Seats, EconomyTotalFare, B_Seats, BusinessTotalFare):
        try:
            # Check if FlightID already exists
            self.cur.execute("SELECT FlightID FROM FlightInfo WHERE FlightID=%s", (FlightID,))
            existing_flight_id = self.cur.fetchone()

            if existing_flight_id:
                return False  # FlightID already exists, insertion failed

            # Insert new flight record
            query = """
            INSERT INTO FlightInfo (
                FlightID, Airline, FlightDate, DepartureTime, ArrivalTime, Origin, Destination, 
                E_Seats, EconomyTotalFare, B_Seats, BusinessTotalFare
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            values = (
                FlightID, Airline, FlightDate, DepartureTime, ArrivalTime, Origin, Destination, 
                E_Seats, EconomyTotalFare, B_Seats, BusinessTotalFare
            )

            self.cur.execute(query, values)
            self.con.commit()

            return True
        except Exception as e:
            return False
    
    def searchPassengerList(self, search_term):
        query = """
            SELECT p.*, b.FlightID
            FROM PassengerInfo p
            LEFT JOIN BookedFlights b ON p.PassengerID = b.PassengerID
            WHERE p.Username LIKE %s OR b.FlightID LIKE %s
        """
        search_term_with_wildcard = f"%{search_term}%"
        self.cur.execute(query, (search_term_with_wildcard, search_term_with_wildcard))
        passengers = self.cur.fetchall()
        return passengers

    # Display Flight List from table
    def viewFlight(self):
        self.cur.execute("SELECT * FROM FlightInfo")
        rows = self.cur.fetchall()
        return rows

    # Delete Flight Entry from table
    def removeFlight(self, FlightID):
        try:
            # Check if the flight is already booked
            self.cur.execute("SELECT * FROM BookedFlights WHERE FlightID=%s", (FlightID,))
            booked_flight = self.cur.fetchone()

            if booked_flight:
                # Flight is already booked, can't be deleted
                return False

            # If the flight is not booked, proceed with deletion
            self.cur.execute("DELETE FROM FlightInfo WHERE FlightID=%s", (FlightID,))
            self.con.commit()
            
            return True  # Successfully deleted
        except Exception as e:
            return False  # Failed to delete
        
    def getPassengerID(self, username, flight_id):
        # Retrieve Passenger ID based on username and flight ID
        sql_query = "SELECT PassengerID FROM BookedFlights WHERE Username = %s AND FlightID = %s"
        self.cur.execute(sql_query, (username, flight_id))
        result = self.cur.fetchone()
        if result:
            return result[0]
        else:
            return None

    def insertPassengerAndBookedFlight(self, Name, Email, Gender, CellNo, username, flight_id, selected_class):
        try:
            # Insert a new passenger
            self.cur.execute(
                "INSERT INTO PassengerInfo (Username, Name, Email, Gender, CellNo) VALUES (%s,%s,%s,%s,%s)",
                (username, Name, Email, Gender, CellNo)
            )
            self.con.commit()

            # Retrieve the auto-generated PassengerID
            self.cur.execute("SELECT LAST_INSERT_ID()")
            passenger_id = self.cur.fetchone()[0]

            # Insert booked flight details with the auto-generated PassengerID
            sql_query = "INSERT INTO BookedFlights (Username, FlightID, PassengerID, Class) VALUES (%s, %s, %s, %s)"
            self.cur.execute(sql_query, (username, flight_id, passenger_id, selected_class))
            self.con.commit()

            # Update available seats based on the selected class
            if selected_class == "Economy":
                self.cur.execute("UPDATE FlightInfo SET E_Seats = E_Seats - 1 WHERE FlightID = %s", (flight_id,))
            elif selected_class == "Business":
                self.cur.execute("UPDATE FlightInfo SET B_Seats = B_Seats - 1 WHERE FlightID = %s", (flight_id,))
            self.con.commit()

        except Exception as e:
            return False

        return True




    def viewBookedFlights(self, username):
        # Retrieve booked flights for the given username
        sql_query = """
        SELECT b.FlightID, f.Airline, f.FlightDate, f.DepartureTime, f.ArrivalTime, f.Origin, f.Destination, b.Class,
            CASE
                WHEN b.Class = 'Economy' THEN f.EconomyTotalFare
                WHEN b.Class = 'Business' THEN f.BusinessTotalFare
                ELSE NULL
            END AS Fare
        FROM FlightInfo f
        JOIN BookedFlights b ON f.FlightID = b.FlightID
        WHERE b.Username = %s
        """
        self.cur.execute(sql_query, (username,))
        rows = self.cur.fetchall()
        return rows

    def viewPassengerList(self):
        # Retrieve passenger information with booked flights
        sql_query = """
        SELECT p.PassengerID, p.Username, p.Name, p.Email, p.Gender, p.CellNo,
            b.FlightID, f.Airline, f.FlightDate, f.DepartureTime, f.ArrivalTime, f.Origin, f.Destination,
            CASE
                WHEN b.Class = 'Economy' THEN f.EconomyTotalFare
                WHEN b.Class = 'Business' THEN f.BusinessTotalFare
                ELSE NULL
            END AS Fare
        FROM PassengerInfo p
        LEFT JOIN BookedFlights b ON p.PassengerID = b.PassengerID
        LEFT JOIN FlightInfo f ON b.FlightID = f.FlightID
        """
        self.cur.execute(sql_query)
        rows = self.cur.fetchall()
        return rows


    def searchFlights(self, origin, destination, flight_date, selected_class):
        if not (origin and destination and flight_date and selected_class):
            return []

        formatted_date = datetime.strptime(flight_date, '%m/%d/%Y').strftime('%Y-%m-%d')

        if selected_class == "Economy":
            sql_query = "SELECT * FROM FlightInfo WHERE Origin=%s AND Destination=%s AND FlightDate=%s AND E_Seats > 0"
        elif selected_class == "Business":
            sql_query = "SELECT * FROM FlightInfo WHERE Origin=%s AND Destination=%s AND FlightDate=%s AND B_Seats > 0"
        else:
            sql_query = "SELECT * FROM FlightInfo WHERE Origin=%s AND Destination=%s AND FlightDate=%s"

        self.cur.execute(sql_query, (origin, destination, formatted_date))
        flights = self.cur.fetchall()
        return flights

    def searchBookedFlights(self, username, search_term):
        query = """
            SELECT b.FlightID, f.Airline, f.FlightDate, f.DepartureTime, f.ArrivalTime, f.Origin, f.Destination,
                CASE
                    WHEN b.Class = 'Economy' THEN f.EconomyTotalFare
                    WHEN b.Class = 'Business' THEN f.BusinessTotalFare
                    ELSE NULL
                END AS Fare
            FROM FlightInfo f
            JOIN BookedFlights b ON f.FlightID = b.FlightID
            WHERE b.Username = %s
                AND (
                    f.FlightID LIKE %s OR
                    f.Airline LIKE %s OR
                    f.FlightDate LIKE %s OR
                    f.DepartureTime LIKE %s OR
                    f.ArrivalTime LIKE %s OR
                    f.Origin LIKE %s OR
                    f.Destination LIKE %s OR
                    CASE
                        WHEN b.Class = 'Economy' THEN f.EconomyTotalFare
                        WHEN b.Class = 'Business' THEN f.BusinessTotalFare
                        ELSE NULL
                    END LIKE %s
                )
        """
        search_term_with_wildcard = f"%{search_term}%"
        params = (username,) + tuple([search_term_with_wildcard] * 8)
        self.cur.execute(query, params)
        flights = self.cur.fetchall()
        return flights
    
    def passengerLogin(self, username, password):
        sql_query = "SELECT * FROM LoginInfo WHERE Username=%s AND Password=%s"
        self.cur.execute(sql_query, (username, password))
        result = self.cur.fetchall()
        return result

    def passengerSignUp(self, username):
        sql_query = "SELECT * FROM LoginInfo WHERE Username=%s"
        self.cur.execute(sql_query, (username,))
        result = self.cur.fetchall()
        return result

    def insertPassengerAcc(self, username, password):
        sql_query = "INSERT INTO LoginInfo (Username, Password) VALUES (%s, %s)"
        self.cur.execute(sql_query, (username, password))
        self.con.commit()