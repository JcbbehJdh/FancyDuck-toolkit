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
                      B: Zipcrack
                      C: DDOS
                      D: bruteforcessh
                      E: Dead mans switch/for twitter
                      F: portscanner : it sucks
                      Q: Quit/Log Out

                      Please enter your choice: """)

    if choice == "A" or choice =="a":
       os.system('python3 Decrypt.py')
    elif choice == "B" or choice =="b":
       os.system ('python3 zipcrack.py') 
    elif choice == "C" or choice =="c":
       os.system('python fancyddos.py')
    elif choice=="D" or choice=="d":
        os.system('python3 brutessh.py')
    elif choice== "E" or choice =="e":
       os.system('python3 deadswitch')
    elif choice == "F" or choice =="f":
       os.system('python3 portscanner.py')
    elif choice=="Q" or choice=="q":
        sys.exit
    else:
        print("You must only select an option retard")
        print("Please try again")
        menu()


main()

