import json
import random
import string
from pathlib import Path

class Bank:
    database = 'data.json'
    data = []

    try:
        if Path(database).exists():
            with open(database, 'r') as fs:
                data = json.loads(fs.read())
        else:
            print("No such files exist")
    
    except Exception as err:
        print(f"An error occured as {err}")

    @classmethod
    def __update(cls):
        with open(cls.database, 'w') as fs:
            fs.write(json.dumps(cls.data))

    @classmethod
    def __accountgenerate(cls):
        alpha = random.choices(string.ascii_uppercase + string.ascii_lowercase, k= 3)
        num = random.choices(string.digits, k = 4)
        spchar = random.choices('!@#$%^&', k = 2)
        id = alpha + num + spchar
        random.shuffle(id)
        return "".join(id)

    def CreateAccount(self):
        info = {
            "name" : input("Enter your name: "),
            "age"  : int(input("Enter your age: ")),
            "email" : input("Enter your email: "),
            "pin" : int(input("Enter your 4 digit pin: ")),
            "AccountNo" : Bank.__accountgenerate(),
            "balance" : 0
        }
        if info['age'] < 18 or len(str(info['pin'])) < 4:
            print("Sorry you cant create an account")
        else:
            print("Your account has been created successfully!")
            for i in info:
                print(f"{i} : {info[i]}")
            print("Please note down your Account Number")


            Bank.data.append(info)
            Bank.__update()
    
    def depositmoney(self):
        accnumber = input("Enter your account number: ")
        pin = int(input("Enter your account pin: "))

        userdata = [i for i in Bank.data if i['AccountNo'] == accnumber and i['pin'] == pin]

        if userdata == False:
            print("Sorry no data found")
        else:
            amount = int(input("Enter the amount you want to deposit: "))
            if amount > 10000 or amount < 0:
                print("Sorry, you can only deposit money between 0 and 10000")
            else:
                print(userdata)
                userdata[0]['balance'] += amount
                Bank.__update()
                print("Your money has been deposited successfully")
                print(f"Your balance is {userdata[0]['balance']}")

    def withdrawmoney(self):
        accnumber = input("Enter your account number: ")
        pin = int(input("Enter your account pin: "))

        userdata = [i for i in Bank.data if i['AccountNo'] == accnumber and i['pin'] == pin]

        if userdata == False:
            print("Sorry no data found")
        else:
            amount = int(input("Enter the amount you want to withdraw: "))
            if userdata[0]['balance'] < amount:
                print("Sorry, you cannot withdraw more than your balance")
            else:
                print(userdata)
                userdata[0]['balance'] -= amount
                Bank.__update()
                print("Your money has been withdrawn successfully")
                print(f"Your balance is {userdata[0]['balance']}")

    def showdetails(self):
        accnumber = input("Enter your account number: ")
        pin = int(input("Enter your account pin: "))

        userdata = [i for i in Bank.data if i['AccountNo'] == accnumber and i['pin'] == pin]
        print("Your account details are \n\n")

        for i in userdata[0]:
            print(f"{i} : {userdata[0][i]}")

    def updatedetails(self):
        accnumber = input("Enter your account number: ")
        pin = int(input("Enter your account pin: "))

        userdata = [i for i in Bank.data if i['AccountNo'] == accnumber and i['pin'] == pin]
        if userdata == False:
            print("Sorry no data found")
        
        else:
            print("You cant change your age, account number and balance")
            print("Fill the details you want to update")

        newdata = {
            "name" : input("Enter your name or enter to skip: "),
            "email" : input("Enter your email or enter to skip "),
            "pin" : input("Enter your pin or enter to skip: ")
        }

        if newdata['name'] == "":
            newdata['name'] = userdata[0]['name']
        if newdata['email'] == "":
            newdata['email'] = userdata[0]['email']
        if newdata['pin'] == "":
            newdata['pin'] = userdata[0]['pin']

        newdata['age'] = userdata[0]['age']
        newdata['AccountNo'] = userdata[0]['AccountNo']
        newdata['balance'] = userdata[0]['balance']
        
        if type(newdata['pin']) == str:
            newdata['pin'] = int(newdata['pin'])
        
        for i in newdata:
            if newdata[i] == userdata[0][i]:
                continue
            else:
                userdata[0][i] = newdata[i]

        Bank.__update()
        print("Account details updated successfully")

    def deleteaccout(self):
        accnumber = input("Enter your account number: ")
        pin = int(input("Enter your account pin: "))

        userdata = [i for i in Bank.data if i['AccountNo'] == accnumber and i['pin'] == pin]
        if userdata == False:
            print("Sorry no data found")
        else:
            print("Press y for account deletion otherwise press n")
            if check == 'n' or check == 'N':
                print("bypass")
            else:
                index = Bank.data.index(userdata[0])
                Bank.data.pop(index)
                Bank.__update()
                print("Account deleted successfully")

user = Bank()

print("Press 1 for creating new Bank Account")
print("Press 2 for depositing money")
print("Press 3 for withdrawing money")
print("Press 4 for showing details")
print("Press 5 for updating details")
print("Press 6 for deleting account")

check = int(input("Enter your choice: "))

if check == 1:
    user.CreateAccount()

if check ==2:
    user.depositmoney()

if check == 3:
    user.withdrawmoney()

if check == 4:
    user.showdetails()

if check == 5:
    user.updatedetails()

if check == 6:
    user.deleteaccount()