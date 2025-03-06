class ATM:
    def __init__(self,user,pwd,Balance_Amount):
        self.user=user
        self.pwd=pwd
        self.Balance_Amount=Balance_Amount
        user=input("Enter Your Name:")
        pwd=int(input("Enter Your Pin Number:"))
        if user==user and pwd==1234:
            print("1-Withdrawal_Amount")
            print("2-Credited_Amount")
            print("Balance_Amount=5000")

            select=int(input("select:"))
            match (select):
                case 1:
                    Withdrawal_Amount=int(input("Withdrawal Amount:"))
                    if Withdrawal_Amount>=Withdrawal_Amount:
                        print(f"Balance_Amount_Total:{self.Balance_Amount-Withdrawal_Amount}")
                        print("Successfull")
                    else:
                        print("Invaild Balance")
                case 2:
                    Credited_Amount=int(input("Credited Amount:"))
                    print(f"Balance_Amount_Total:{self.Balance_Amount+Credited_Amount}")
                    print("Successfull")
        else:
            print("Invaild Number")
                
                
                   
                           
var=ATM("saravanan",1234,5000)

