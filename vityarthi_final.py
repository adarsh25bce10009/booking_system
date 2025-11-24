def default_transport():
    try:
        open('transport_file', 'r')
    except:
        with open('transport_file', 'w') as f:
            f.write('T101,Delhi,Mumbai,08:00 AM\n')
            f.write('B101,Banglore,Mysore,10:30 AM\n')
            f.write('T102,Kanpur,Kolkata,04:00 PM\n')
            f.write('B102,Jaipur,Agra,01:00 Pm\n')

def signup():
    print("!!!SIGN UP!!!")
    username=input("enter new username: ")
    password=input("enter the password: ")
    with open('user_file','a') as f:
        f.write(username+','+password+'\n')
    print('!!signed up successfully!!')

def signin():
    print('!!!SIGN IN!!!')
    username=input("enter username: ")
    password=input("enter password: ")
    try:
        with open("user_file","r") as f:
            users=f.readlines()
            for i in users:
                line=i.strip()
                words=line.split(",")
                f_username=words[0]
                f_password=words[1]

                if f_username==username and f_password==password:
                    print("!!signed in successfuly!!!")
                    return username
    except:
        pass

    print("\nwrong details\n")
    return False

def show_transport():
    print("-----Available Transport-----")
    try:
        with open("transport_file","r") as f:
            for i in f:
                line=i.strip()
                words=line.split(",")
                t_num=words[0]
                frm=words[1]
                to=words[2]
                time=words[3]

                print(t_num," FROM ", frm," TO ", to," TIME ", time)
    except:
        print("no transport avalable")

    print()

def book_ticket(username):
    show_transport()
    t_num=input("enter vehicle number to book: ")

    try:
        found=False
        with open("transport_file","r") as f:
            for line in f:
                l=line.strip()
                if l.startswith(t_num):
                    found=True

        if found:
            with open("tickets_file","a") as f:
                f.write(username+","+t_num+"\n")
            print("!!ticket booked successfully!!")
        else:
            print("!!invalid vehicle number!!")
    except:
        print("!!error booking ticket!!")

def view_tickets(username):
    print("-----booked tickets-----")
    found=False
    try:
        with open("tickets_file","r") as f:
            for l in f:
                line=l.strip()
                words=line.split(",")
                f_username=words[0]
                t_num=words[1]
                if f_username==username:
                    found=True
                    print("Booked transport: ",t_num)

        if not found:
            print("no tickets booked")
    except:
        print("no tickets found")
    print()

def main_menu(username):
    while True:
        print("1. Show available transports")
        print("2. book ticket")
        print("3. view booked tickets")
        print("4. logout")
        ch=input("enter your choice: ")
        if ch=='1':
            show_transport()
        elif ch=='2':
            book_ticket(username)
        elif ch=='3':
            view_tickets(username)
        elif ch=='4':
            print("logging out...")
            break
        else:
            print("invalid choice")

def start():
    default_transport()
    while True:
        print("1. Sign up")
        print("2.sign in")
        print("3. exit")
        choice=input("enter your choice: ")
        if choice=='1':
            signup()
        elif choice=='2':
            username=signin()
            if username:
                main_menu(username)
        elif choice=='3':
            print("exiting...")
            break
        else:
            print("invalid choice, try again")

start()