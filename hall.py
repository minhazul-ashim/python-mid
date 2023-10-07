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
            return;
    
        for show in self.show_list :
            if(show[0] == id) :
                target_show = self.seats[id];
        
        if(target_show and target_show[x][y] == "Booked") :
            print("Sorry! The Seat is already Booked");
            return;

        if(target_show) :
            target_show[x][y] = 'Booked';
            print("Your Seats has been booked");
        else :
            print("Sorry, You provided wrong show ID.");
            return;
        

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


hall = Star_Cinema.entryHall(5,5,100);

hall.entry_show("101", "Avenger Endgame", datetime.datetime.now());
hall.entry_show("102", "Wonder Woman", datetime.datetime.now());

while True :
    print('\n \n');
    print('Welcome to the Star Cinema Dashboard');
    print("1 : Interact as User");
    print("2 : Interact as Counter");
    print("3 : Terminate Process");
    n = int(input());

    if(n == 1) :

        while True :
            
            print('\n \n Interacting as User');
            print("Choose your option.");
            print("1 : View Show List");
            print("2 : Book Seat");
            print("3 : Return to Dashboard");
            print("Go to ", end=" ");
            x = int(input());
            
            match x :
                case 1 :
                    hall.view_show_list();
                case 2 :
                    print("Enter Show ID", end=" ");
                    id = input();
                    print("Enter Row", end=" ");
                    x = int(input());
                    print("Enter Column", end = " ");
                    y = int(input());
                    hall.book_seats(id, (x, y));
                case 3: 
                    print('Process Terminated');
                    break;
    elif(n == 2) :
        
        print('\n \n Interacting as Counter');
        print("Choose your option.");
        print("1 : Entry Show");
        print("2 : View Show List");
        print("3 : View Available Seat");
        print("4 : Book Seat");
        print("5 : Return to Dashboard");
        print("Go to ", end=" ");
        x = int(input());
        
        match x :
            case 1 :
                print("Enter Movie Name", end=" ");
                x = input();
                print("Enter Show ID", end=" ");
                y = input();
                hall.entry_show(y, x, datetime.datetime.now());
                print("Show Entry Successful");
            case 2 :
                hall.view_show_list();
            case 3 :
                print("Enter Show ID", end=" ");
                x = input();
                hall.view_available_seats(x);
            case 4 :
                print("Enter Show ID", end=" ");
                id = input();
                print("Enter Row", end=" ");
                x = int(input());
                print("Enter Column", end = " ");
                y = int(input());
                hall.book_seats(id, (x, y));
            case 5: 
                print('Process Terminated');
                break;
    
    elif(n == 3) :
        print("Process Terminated");
        break;