# Transport ticket management system

## Overview
This project is a simple python based program for booking tickets for trains and buses.
user can sign up, sign in, view transport availability, book tickets, and view the tickets already booked.
all records are stored in text files for storage and future use.

## Features
1. user signup and signin: the signup function lets the user create a new account on the system which gets stored in a text file of user details and the signin funtions checks if the details the user put are coreect or not, and if it is grants access to the system.
2. store user data in a text file: the text files 'users.txt', 'transports.txt', 'tickets.txt' are used to store data of users, transport vehicles and their details and tickets status respectively.
3. view available bus/train options: the programm lets us view the available bus/train and the details of the same.
4. book tickets using transport number: after signing in the user can book tickets for the bus or train.
5. view previously booked tickets: after booking we can also check the booked ticket and all the booked tickets.
6. simple command line interface: command line interface keeps everything simple so we dont get confused or have to find different features, it is all in front of us.

## Technology/Tools used
1. Python
2. File handling with '.txt' file: the '.txt' files are used to save the data of users transport and tickets to save it and for future refence.
3. standard input/output: the input output tools are used to input the details from the user like username password and the coice of what the user wants to do in the program, and output is used to show the desired data to the user.
4. Program structure and control: the whole program is modularised into functions so the flow is streamlined and no unnecessary part is running that can cause any error in the program.
5. data conversion tools: various tools used to convet data types in the program.

## Steps to Install & run the project
1. Install python
2. download or clone this github repository
3. open the project folder
4. run the python file transport_system.py: copy the code and paste it in a file with .py extension.
5. you must run this program interactively from command line.

## Instructions for testing
1. run the program
2. choose 'signup' option and create a new user
3. sign in using the same details
4. view transport list
5. enter thr transport ccode (ex- 'T101', 'B102') to book a ticket
6. view 'my tickets' to check bookings
7. logout and exit

# screenshots
screenshot 1-
<img width="1920" height="1080" alt="Screenshot (62)" src="https://github.com/user-attachments/assets/b8d0dec4-5948-44ea-a738-f787298b9790" />
screenshot 2-
<img width="1920" height="1080" alt="Screenshot (63)" src="https://github.com/user-attachments/assets/f467ad12-7a1c-4d8c-b412-4bf9760caef7" />
