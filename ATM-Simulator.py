import random

class ATM_Simulator:
    def __init__(self) :
        self.username = "abc" 
        self.password = "abc123" 
        self.amount = 1000
    
    def Balance (self) :
        print( f"Your balance is {self.amount}") 
        
    def Withdraw (self) :
        if self.amount > 0 :
            withdraw_amount = int(input (" Enter Withdrawal Amount :")) 
            if withdraw_amount > 0 and self.amount > withdraw_amount :
                self.amount -= withdraw_amount 
                print (f" Rs.{withdraw_amount} is Debited.") 
            else :
                print (" Un sufficient amount ")
                 
    
    def Deposit (self) :
        deposit_amount = int(input("Enter Deposit Amount :"))
        if deposit_amount > 0 :
            print (f"Rs.{deposit_amount} is Credited. ") 
            self.amount += deposit_amount
        else :
            print ("Invalid") 
            
    def Option (self) :
        while True:
            print ("""
                        OPTIONS:
                        1.Balance Enquiry
                        2.Withdraw
                        3.Deposit
                        4.Exit
                       """)
            Option = int(input("Enter Option:"))
            if Option == 1 :
                self.Balance()
            elif Option == 2 :
                self.Withdraw ()
            elif Option == 3 :
                self.Deposit() 
            elif Option == 4 :
                break
            else :
                print ("Invalid Option") 
                continue

            
    def ATM (self) :
        n = 3
        while (n>0) :
            username = input("Enter Username:") 
            password = input ("Enter Password :") 
            
            if (username == self.username) and (password == self.password):
                otp = random.randint(100000, 999999)
                print (f"Your Otp is {otp} ")
                Enter_otp = int(input("Enter OTP :")) 
                if Enter_otp == otp : 
                    self.Option() 
                    break
                else :
                    print ("Wrong OTP.") 
                    continue 
                    
            else :
                n -= 1
                print (f"Invalid Credentials and You have only {n} chance left. ") 
                continue
 
            
Obj=ATM_Simulator()
Obj.ATM()
