import heapq
import random

class FlightManager:
    def __init__(self):
        print("--- SYSTEM STARTUP ---")
        try:
            self.rows = int(input("How many rows? "))
            self.cols = int(input("How many columns? "))
        except ValueError:
            print("Invalid number. Using default 2 rows, 3 columns.")
            self.rows = 2
            self.cols = 3

        self.seats = []
        for r in range(self.rows):
            new_row = []
            for c in range(self.cols):
                new_row.append(None)
            self.seats.append(new_row)
        
        self.passenger_data = {}
        
        self.waiting_list = [] 
        self.ticket_number = 0 

        print(f"Seat map initialized: {self.rows} x {self.cols}")
        self.show_seats(show_names=False)

    def get_seat_name(self, row_index, col_index):
        row_string = str(row_index + 1)
        col_string = chr(65 + col_index) 
        return row_string + col_string

    def get_indices(self, seat_code):
        try:
            row_part = int(seat_code[:-1]) - 1
            col_part = ord(seat_code[-1]) - 65
            return row_part, col_part
        except:
            return None, None

    def get_empty_seats(self):
        empty_spots = []
        for r in range(self.rows):
            for c in range(self.cols):
                if self.seats[r][c] is None:
                    empty_spots.append(self.get_seat_name(r, c))
        return empty_spots

    def show_seats(self, show_names=False):
        print("\n--- SEAT MAP ---")
        for r in range(self.rows):
            line_display = []
            for c in range(self.cols):
                seat_code = self.get_seat_name(r, c)
                person = self.seats[r][c]

                if person is None:
                    line_display.append(f"{seat_code} (Available)")
                else:
                    if show_names:
                        line_display.append(f"{seat_code} ({person})") 
                    else:
                        line_display.append(f"{seat_code} (Occupied)") 
            
            print(" | ".join(line_display))
        print("\n")

    def add_passenger(self, first, last, birthday, address, wanted_seat=None):
        full_name = f"{first} {last}"
        
        if wanted_seat:
            r, c = self.get_indices(wanted_seat)
            
            if r is not None and 0 <= r < self.rows and 0 <= c < self.cols:
                if self.seats[r][c] is None:
                    self.save_booking(r, c, full_name, birthday, address)
                    return
                else:
                    print(f"Seat {wanted_seat} is already booked.")
                    available = self.get_empty_seats()
                    print(f"Available seats: {', '.join(available)}")
                    return 
            else:
                print("Invalid seat code.")
                return

        empty_indices = []
        for r in range(self.rows):
            for c in range(self.cols):
                if self.seats[r][c] is None:
                    empty_indices.append((r, c))

        if len(empty_indices) > 0:
            r, c = random.choice(empty_indices)
            self.save_booking(r, c, full_name, birthday, address)
        else:
            self.add_to_waitlist(first, last, birthday, address)

    def save_booking(self, r, c, name, birthday, address):
        self.seats[r][c] = name
        seat_code = self.get_seat_name(r, c)
        
        self.passenger_data[name] = {
            "dob": birthday,
            "address": address,
            "seat": seat_code,
            "status": "Booked"
        }
        print(f"Booking confirmed for {name} at {seat_code}.")

    def add_to_waitlist(self, first, last, birthday, address):
        name = f"{first} {last}"
        self.ticket_number += 1
        
        heapq.heappush(self.waiting_list, (self.ticket_number, {
            "first": first, "last": last, "dob": birthday, "addr": address
        }))
        
        self.passenger_data[name] = {
            "dob": birthday,
            "address": address,
            "seat": "Waitlist",
            "status": "Waiting"
        }
        print(f"All seats booked. {name} added to waitlist (Pos: {len(self.waiting_list)}).")

    def cancel_passenger(self, name, birthday):
        if name not in self.passenger_data:
            print("Error: Passenger not found.")
            return

        record = self.passenger_data[name]
        if record["dob"] != birthday:
            print("Error: Date of Birth does not match.")
            return

        current_seat = record["seat"]

        if current_seat == "Waitlist":
            print(f"Removed {name} from waitlist.")
            del self.passenger_data[name]
            return

        r, c = self.get_indices(current_seat)
        self.seats[r][c] = None 
        del self.passenger_data[name]
        print(f"Reservation for {name} at {current_seat} has been canceled.")

        if self.waiting_list:
            _, p_data = heapq.heappop(self.waiting_list)
            
            p_first = p_data["first"]
            p_last = p_data["last"]
            p_name = f"{p_first} {p_last}"
            
            print(f"Waitlisted passenger {p_name} assigned to {current_seat}.")
            self.save_booking(r, c, p_name, p_data["dob"], p_data["addr"])

    def find_passenger(self, name, dob):
        if name in self.passenger_data and self.passenger_data[name]["dob"] == dob:
            info = self.passenger_data[name]
            print(f"Found: {name} | Status: {info['status']} | Seat: {info['seat']}")
        else:
            print("Passenger details not found.")

    def simulate_scenarios(self):
        print("\n--- RUNNING SIMULATION ---")
        capacity = self.rows * self.cols
        
        for i in range(capacity + 2):
            fname = f"SimUser{i+1}"
            lname = "Bot"
            dob = "2000-01-01"
            addr = "Sim City"
            print(f"Processing booking for {fname} {lname}...")
            self.add_passenger(fname, lname, dob, addr)
        
        self.show_seats(show_names=True)
        
        target = "SimUser1 Bot"
        print(f"Simulating cancellation for {target}...")
        self.cancel_passenger(target, "2000-01-01")
        self.show_seats(show_names=True)

def start_program():
    sys = FlightManager()
    
    while True:
        print("\n=== FLIGHT RESERVATION SYSTEM ===")
        print("1. Admin")
        print("2. User")
        print("3. Exit")
        role = input("Enter Choice: ")

        match role:
            case "1":  
                key = input("Enter Passkey: ")
                if key == "admin123":  
                    while True:
                        print("\n[ADMIN DASHBOARD]")
                        print("1. Show Seat Map")        
                        print("2. View Waitlist")        
                        print("3. Cancel Reservation")   
                        print("4. Simulate Scenarios")  
                        print("5. Back")                 
                        opt = input("Select: ")

                        match opt:
                            case "1":
                                sys.show_seats(show_names=True)
                            case "2":
                                print(f"Waitlist Length: {len(sys.waiting_list)}")
                            case "3":
                                n = input("Name (First Last): ")
                                d = input("DOB (YYYY-MM-DD): ")
                                sys.cancel_passenger(n, d)
                            case "4":
                                sys.simulate_scenarios()
                            case "5":
                                break
                            case _:
                                print("Invalid.")
                else:
                    print("Access Denied.")

            case "2": 
                while True:
                    print("\n[USER DASHBOARD]")
                    print("1. Book a Seat")              
                    print("2. View Seat Map")            
                    print("3. Cancel Reservation")       
                    print("4. Find Passenger Details")   
                    print("5. Back")                     
                    opt = input("Select: ")

                    match opt:
                        case "1":
                            f = input("First Name: ")
                            l = input("Last Name: ")
                            d = input("DOB: ")
                            a = input("Address: ")
                            s = input("Preferred Seat (e.g. 1A) [Enter for Auto]: ").upper()
                            sys.add_passenger(f, l, d, a, s if s else None)
                        case "2":
                            sys.show_seats(show_names=False)
                        case "3":
                            n = input("Name (First Last): ")
                            d = input("DOB: ")
                            sys.cancel_passenger(n, d)
                        case "4":
                            n = input("Name (First Last): ")
                            d = input("DOB: ")
                            sys.find_passenger(n, d)
                        case "5":
                            break
                        case _:
                            print("Invalid.")

            case "3":
                print("Exiting.")
                break
            case _:
                print("Invalid selection.")

if __name__ == "__main__":
    start_program()

    