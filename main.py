import json
import random
import string
from pathlib import Path

class Bank:
    data = []
    database = 'data.json'

    try:
        if Path(database).exists():
            with open(database, 'r') as fs:
                data = json.load(fs)
        else:
            print('file not found, creating new file...')
    except Exception as err:
        print(err)

    @classmethod
    def update(cls):
        with open(cls.database, 'w') as fs:
            json.dump(cls.data, fs, indent=4)

    @classmethod 
    def generate_account_no(cls):
        alpha = random.choices(string.ascii_letters, k=3)
        num = random.choices(string.digits, k=3)
        sp_chara = random.choices("!@#$%^&", k=3)
        id = alpha + num + sp_chara
        random.shuffle(id)
        return "".join(id)

    def create_account(self):
        info = {
            "name": input("enter your name: "),
            "age": int(input("enter your age: ")),
            "email": input("enter your email: "),
            "pin": input("enter your pin: "),
            "accountNo": Bank.generate_account_no(),
            "balance": 0
        }
        if info['age'] < 18 or len(str(info["pin"])) != 4:
            print("not eligible to create account")
        else:
            print("account created successfully with below details")
            for i in info:
                print(f"{i}: {info[i]}")
            Bank.data.append(info)
            Bank.update()

    def deposit_money(self):
        account = input("enter your account no: ")
        userAcc = next((i for i in Bank.data if i["accountNo"] == account), None)
        if userAcc is None:
            print("account not found")
        else:
            amount = int(input("enter amount you want to deposit: "))
            if 0 < amount <= 10000:
                userAcc["balance"] += amount
                Bank.update()
                print("Amount deposited successfully")
            else:
                print("you can deposit below 10000 only and greater than 0")

    def withdraw_money(self):
        account = input("enter your account no: ")
        pin = input("enter your pin no: ")
        userAcc = next((i for i in Bank.data if i["accountNo"] == account and i['pin']==pin), None)
        if userAcc is None:
            print("account not found")
        else:
            amount = int(input("enter amount you want to withdraw: "))
            if userAcc["balance"] <amount:
               print("insufficient balance") 
            elif 0 < amount <= 10000:
                userAcc["balance"] -= amount
                Bank.update()
                print("Amount withdrawn successfully")
            else:
                print("you can withdraw below 10000 only and greater than 0")

    def account_details(self):
        account = input("enter your account no: ")
        pin = input("enter your pin no: ")
        userAcc=next((i for i in Bank.data if i["accountNo"]==account and i["pin"]==pin),None)
        if userAcc is None:
            print("account not found")
        else:
            print("account details are as follows:")
            for i in userAcc:
                print(f"{i}: {userAcc[i]}")


    def account_update(self):
        account = input("enter your account no: ")
        pin = input("enter your pin no: ")
        userAcc=next((i for i in Bank.data if i["accountNo"]==account and i["pin"]==pin),None)
        if userAcc is None:
            print("account not found")
        else:
           print("account nunmber and balance cant be changed")
           new_email = input("enter new email ")
           new_name= input("enter new name")
           new_age = input("enter new aage ")
           new_pin = input("enter new pin ")
           userAcc.update({
                "email": new_email,
                "name": new_name,
                "age": new_age,
                "pin": new_pin
            })
           Bank.update()

    def account_delete(self):
        account = input("enter your account no: ")
        pin = input("enter your pin no: ")
        Bank.data= [i for i in Bank.data if not (i["accountNo"]== account and i["pin"]==pin)]
        Bank.update()


# --- Main ---
user = Bank()

print("press 1 for creating account")
print("press 2 for depositing money in the bank")
print("press 3 for withdrawing money")
print("press 4 for account details")
print("press 5 for updating account")
print("press 6 for deleting account")

check = int(input("enter your choice: "))

if check == 1:
    user.create_account()
elif check == 2:
    user.deposit_money()
elif check == 3:
    user.withdraw_money()
elif check == 4:
    user.account_details()
elif check == 5:
    user.account_update()
else:
    user.account_delete()
