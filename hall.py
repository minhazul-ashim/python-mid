import datetime

class Star_Cinema :
    hall_list = [];

    @staticmethod
    def entryHall(rows, cols, hall_no) :
        hall = Hall(rows, cols, hall_no);
        Star_Cinema.hall_list.append(hall);
        return hall;


class Hall :
    def __init__(self, rows, cols, hall_no = (100 + len(Star_Cinema.hall_list))) -> None:
        self.seats = {};
        self.show_list = [];
        self.rows = rows;
        self.cols = cols;
        self.hall_no = hall_no;

    # Method to Entry a show to the Cinema Hall.
    def entry_show(self, id, movie_name, time) :

        x = (id, movie_name, time);
        self.show_list.append(x);

        y = [[0]*self.cols for _ in range(self.rows)];

        for i in range(0,self.rows) :
            for j in range(0, self.cols) :
                y[i][j] = 'Free';
    
        self.seats[id] = y;
    
    # Method to Book Seats in a show.
    def book_seats(self, id, seat) :
        target_show = None;
        x, y = seat;

        if(x >= self.rows or y >= self.cols) :
            print("Invalid Seats");
        
        for show in self.show_list :
            if(show[0] == id) :
                target_show = self.seats[id];
        
        if(target_show and target_show[x][y] == "Booked") :
            print("Sorry! The Seat is already Booked");

        if(target_show) :
            target_show[x][y] = 'Booked';
        else :
            print("Sorry, You provided wrong show ID.");
        

    # Method to view all the shows running in the hall;
    def view_show_list(self) :
        for show in self.show_list :
            id, movie_name, time = show;
            print(f'Movie Name: {movie_name}, Show ID: {id}, Time : {time}');

    # Method of view all the available seats of a show;
    def view_available_seats(self, id) :
        target_seats = None;
        for x in self.show_list :
            show_id, movie_name, time = x;
            if(show_id == id) :
                target_seats = self.seats[show_id];
        for i in range(0, self.rows) :
            for j in range(0, self.cols) :
                print(target_seats[i][j], end="\t");
            print('\n');


    # Representation class for the hall;
    def __repr__(self):
        print(f'Hall ID is {self.hall_no}, with Total Seats {self.rows * self.cols} and shows running {len(self.show_list)}');





# while True :
#     print('Welcome to the Star Cinema.');

hall = Star_Cinema.entryHall(5,5,100);

hall.entry_show("101", "Jawan", datetime.datetime.now());
# hall.view_show_list();
hall.book_seats("101", (1,1));
hall.view_available_seats("101");
hall.book_seats("101", (1,1));

