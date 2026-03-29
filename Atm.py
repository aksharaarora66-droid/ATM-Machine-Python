#        Made by OP




from dotenv import *
import os
env_path = os.path.join(os.getcwd(), ".env")
class Atm:
    def __init__(self):
      load_dotenv(override=True) 
      self.pin = int(os.getenv("Pin"))
      self.balance = int(os.getenv("Balance"))
      self.menu()
      
      
    def menu(self):
        print("""

                     Welcome to State Bank of India!

         """)
        while True:
         
         self.user_input=(input("""
                                 1.Press 1 to create a pin\n
                                 2.Press 2 to change pin\n
                                 3.Press 3 to withdraw money\n
                                 4.Press 4 to check balance\n
                                 5.Press any button to exit\n
                                 Enter Your Choice: (1/2/3/4/5)"""))
         if int(self.user_input)==1:
            if self.pin == 0:
               self.create_pin()
            else:
               print(" Your Pin is already been set! ")
               self.choice1=int(input(""" 1) Do You wanna Go to main menu!
                                 2) Do you wanna upgrade your pin! """))
               if self.choice1==1:
                  pass
               else :
                  self.change_pin()
         elif int(self.user_input)==2:
            self.change_pin()
         elif int(self.user_input)==3:
            self.withdraw_money()
         elif int(self.user_input)==4:
            self.check_balance()
         else:
            print("\nThank you for comming in our bank .Pls visit again! ")
            break
    
    
    def create_pin(self):
       self.pin2=int(input("Enter a pin"))
       set_key(env_path,"Pin",str(self.pin2))
       self.pin=self.pin2
       print("Pin created sucessfully! ")
       
   
   
    def change_pin(self):
       self.old_pin=int(input("Enter your old pin: "))
       if self.old_pin==self.pin:
         self.pin1=int(input("Pls enter a new pin: "))
         self.pin=self.pin1
         set_key(env_path,"Pin",str(self.pin1))
         print("Pin created successfully")
       else:
          print("Wrong Pin!! try again!")
          pass
    
    
    
    def withdraw_money(self):
       self.withdrawn_amount=int(input("Enter the amount you want to withdraw: "))
       self.pin3=int(input("Enter your pin: "))
       if self.pin3==self.pin:
          if self.withdrawn_amount<=self.balance:
             amount=self.balance-self.withdrawn_amount
             set_key(env_path,"Balance",str(amount))
             print(f"""Withdrawn Successfully!!
                   Remaining balance: {amount}""")
          else:
             print("There is insufficient amount in your bank")
       else:
          print("You have entered wrong pin. Try again!! ")
    
    
    def check_balance(self):
       print("your current amount is: ",os.getenv("Balance"))

State_Bank_of_India = Atm()


     

             

        


                             
                       
