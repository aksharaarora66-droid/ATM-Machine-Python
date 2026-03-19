class Atm:
    def __init__(self):
        self.__balance=0
        self.__pin=''
        self.menu()
    def menu(self):
        user_input=int(input("""
                                1.Press 1 to create a pin
                                2.Press 2 to change pin 
                                3.Press 3 to withdraw money
                                4.Press 4 to check balance
                                5.Press any button to exit
                                Enter Your Choice: """))
        if user_input==1:
         self.create_pin()
        elif user_input==2:
         self.change_pin()
 
        elif user_input==3:
           self.withdraw_money()
        elif user_input==4:
           self.check_balance
        else:
         print("Thank you for comming in our bank .Pls visit again")
    def create_pin(self):
       pin=input("Pls enter your pin: ")
       self.__pin=pin
       print("Pin created successfully")
       balance=input("Enter your balance:")
       self.__balance=balance
       print("You have successfully completed the process")
       self.menu()
    def change_pin(self):
       old_pin=input("Enter your old pin: ")
       if self.__pin==old_pin:
          new_pin=input("Enter your new pin: ")
          self.__pin=new_pin
          print("You have created your new_pin successfully!!")
          self.menu()
       else:
          print("Wrong pin!!")
          self.menu()
    def withdraw_money(self):
       pin=input("Enter your pin: ")
       if pin==self.__pin:
          withdrawn_amount=int(input("Enter the amount you want to withdraw: "))
          if withdrawn_amount<=self.__balance:
             amount=self.__balance-withdrawn_amount
             self.__balance=amount
             print("""Withdrawn Successfully!!
                   Remaining balance: {self.__balance}""")
             self.menu()
          else:
             print("There is insufficient amount in your bank")
             self.menu()
       else:
          print("You have entered wrong pin. Try again")
       self.menu()
    def check_balance(self):
       print("your current amount is: ",self.__balance)

sbi = Atm()


     

             
          
             
        

        


                             
                       
