class Star_Ciname:
    __hall_list = []

    @classmethod
    def entry_hall(cls, hall):
        cls.__hall_list.append(hall)

class Hall(Star_Ciname):
    def __init__(self, rows, cols, hall_no):
        self.__rows = rows
        self.__cols = cols
        self.__hall_no = hall_no
        self.__seats = {}
        self.__show_list = []
        self.entry_hall(self)

    def entry_show(self, id, movie_name, time):
        show = (id, movie_name, time)
        self.__show_list.append(show)
        # self.__seats[id] = [[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        self.__seats[id] = [[0 for i in range(self.__rows)] for j in range(self.__cols)]

    def book_seats(self, id, seats):
        if id not in self.__seats:
            print("Invalid show ID.")
            return
        
        for (row, col) in seats:
            if row >= len(self.__seats[id]) or col >= len(self.__seats[id][0]):
                print(f"Seat ({row}, {col}) is invalid")
                continue

            if self.__seats[id][row][col] == 0:
                self.__seats[id][row][col] = 1
                print(f"Seat ({row}, {col}) booked")
            else:
                print(f"Seat ({row}, {col}) is already booked.")
        
    def view_show_list(self):
        print("View All Shows:")
        for show in self.__show_list:
            print(f"MOVIE NAME: {show[1]} SHOW ID: {show[0]} TIME: {show[2]}")
        
    def view_available_seats(self, id):   
        if id not in self.__seats:
            print("Invalid show ID.")
            return
        
        print(f"Available seats for show {id}:")
        for i, row in enumerate(self.__seats[id]):
            for j, seat in enumerate(row):
                if seat == 0:
                    print(f"\nseat ({i}, {j})", end=' ')
        print()

        print(f"\nSeat Matrix for show ID {id} in Hall {self.__hall_no}:")
        seats = self.__seats[id]
        for row in seats:
            print(" ".join(str(seat) for seat in row))

def ticket_system():
    hall = Hall(6, 6, 8)
    hall.entry_show(111, "Jawan Maji", "25/10/2023 11:00 AM")
    hall.entry_show(333, "Sujon Maji", "25/10/2023 2:00 AM")

    while True:
        print("\n1. VIEW ALL SHOW TODAY")
        print("2. VIEW AVAILABLE SEATS")
        print("3. BOOK TICKET")
        print("4. EXIT")
        ch = int(input("ENTER OPTION: "))

        if ch == 1:
            hall.view_show_list()
        elif ch == 2:
            id = int(input("ENTER SHOW ID: "))
            hall.view_available_seats(id)
        elif ch == 3:
            id = int(input("ENTER SHOW ID: "))
            number_of_seats = int(input("HOW MANY SEATS? "))
            booking = []
            for i in range(number_of_seats):
                row = int(input("ENTER ROW: "))
                col = int(input('ENTER COLUMN: '))
                booking.append((row, col))
            hall.book_seats(id, booking)
        elif ch == 4:
            break
        else:
            print("Invalid optional!")

if __name__ == "__main__":
    ticket_system()

