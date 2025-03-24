from datetime import datetime 

now = datetime.now()
cur_date = now.strftime("%d/%m/%Y")
cur_hour = now.hour
cur_min = now.minute

class Bank:
    def openAcc(self,acno,cname,balance):
        self.ano = acno
        self.cname = cname
        self.bal = balance
        print("*"*50)
        print(cname+"Your Account Opened with Account number"+str(acno)+"and balance in your account is"+str(self.bal))
        file.write("\n"+cName+" Your Account opened with "+str(acno) + " number and balance is " + str(self.bal)+ "on" + str(cur_date)+ "and time"+ str(cur_hour)+"hours:"+str(cur_min)+" minutes")

    def deposit(self,amount):
        self.bal+=amount
        print("*"*50)
        print(self.cname+" your account deposited with "+str(amount)+" and your balance is "+str(self.bal))
        file.write("\n"+self.cname + " your account credited with "+ str(amount) + " your balance is "+ str(self.bal)+" Rs."+" on"+str(cur_date)+"and time "+str(cur_hour)+"hours:"+str(cur_min)+" minutes")

    def withdraw(self,amount):
        if(amount<=self.bal):
            self.bal-=amount
            print("*"*50)
            print(self.cname+" you taken money"+str(amount)+" from your account and your balance is "+str(self.bal))
            file.write("\n"+self.cname+ " Your account debited with "+ str(amount) + " Your balance is "+ str(self.bal) + " Rs."+" on"+str(cur_date)+" and time "+str(cur_hour)+"hours:"+str(cur_min)+" minutes")
        else:
            print("*"*50)
            print(self.cname+"for taking "+str(amount)+"from your account you need to add "+str(amount-self.bal)+" this amount in your acc first your balance is"+str(self.bal))
    def checkBal(self):
        print("*"*50)
        print("Balance in your account is "+ str(self.bal))

    def exit(self):
        print("*"*50)
        print("Thank you for using our services")
        print("*"*50)

cName = input("Enter Your Name : ")
acNo = int(input("Enter your AC no :"))
bal = int(input("Enter yout initial balance: "))

b1 = Bank()


file = open(cName+".txt","a")
file.close()

file = open(cName+".txt","a")
b1.openAcc(acNo,cName,bal)




while True:
    print("Please select your choices")
    print("1. for deposit amount")
    print("2. for withdraw amount")
    print("3. for check balance")
    print("4. for exit ")

    choice = int(input("Enter Your choice: "))

    if(choice == 1):
        amount = int(input("Enter deposit amount:"))
        b1.deposit(amount)
        print("*"*50)
    elif(choice == 2):
        amount = int(input("Enter withdraw amount: "))
        b1.withdraw(amount)
        print("*"*50)
    elif(choice == 3):
        b1.checkBal() #here b1 is self argument of checkBal so no need to give any argument as self self itself b1
        print("*"*50)
    elif(choice == 4):
        b1.exit()
        break
    else:
        print("Invalid input please try again")
        
        

file.close()
