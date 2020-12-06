#This is AN awesome tool :>

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
        os.system('clear')
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


    
    
#the program is initiated, so to speak, here
main()

