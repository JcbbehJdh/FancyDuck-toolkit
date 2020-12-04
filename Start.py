#Form Tutor Management System

import os
import sys #this allows you to use the sys.exit command to quit/logout of the application

os.system('clear')
def main():
    login()
    
def login():
    username="FancyDuck"
    password="1234567890"
    print("Enter username : ")
    answer1=input()
    print("Enter password : ")
    answer2=input()
    if answer1==username and answer2==password:
        print("Welcome - Access Granted")
        menu()

def menu():
    print("************MAIN MENU**************")
    #time.sleep(1)
    print()


    choice = input("""
                      A: Decrypt/encrypt files
                      B: Twitter hack
                      C: DDOS
                      D: FaceBook cracker
                      Q: Quit/Log Out

                      Please enter your choice: """)

    if choice == "A" or choice =="a":
       os.system('python3 Decrypt.py')
    elif choice == "B" or choice =="b":
       os.system ('sudo bash twithack.sh') 
    elif choice == "C" or choice =="c":
       os.system('python fancyddos.py')
    elif choice=="D" or choice=="d":
        os.system('python fbcracker.py')
    elif choice=="Q" or choice=="q":
        sys.exit
    else:
        print("You must only select either A,B,C, or D.")
        print("Please try again")
        menu()

def enterstudentdetails():
    pass
    #Teacher will enter student details manually
    #These will be appended to the csv file

def viewstudentdetails():
    pass
#Teacher can press a button to view all students at a glance

def searchbyid():
    pass
    #Teacher can input an ID number and display the relevant student's details

def producereports():
    pass
    #Teacher can produce clever reports such as:
    #a) list of names of males and email addresses (to email a reminder about boys football club)
    #b) list of names of females in specific postcode (to remind them of a girls coding club in the area)
    #c) list of all names, birthdays and addresses (to send out birthday cards!)
    
    
#the program is initiated, so to speak, here
main()

