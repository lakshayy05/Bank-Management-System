import json
import random
import string
from pathlib import Path

class Bank:
    database = 'data.json'
    
    @classmethod
    def load_data(cls):
        if Path(cls.database).exists():
            with open(cls.database, 'r') as fs:
                try:
                    return json.load(fs)
                except json.JSONDecodeError:
                    return [] # Return empty if file is corrupt/empty
        return []

    @classmethod
    def save_data(cls, data):
        with open(cls.database, 'w') as fs:
            json.dump(data, fs, indent=4)

    @classmethod
    def generate_account_number(cls):
        chars = random.choices(string.ascii_letters, k=3) + \
                random.choices(string.digits, k=3) + \
                random.choices("!@#$%^&*", k=1)
        random.shuffle(chars)
        return ''.join(chars)

    @classmethod
    def CreateAccount(cls, name, age, email, pin):
        data = cls.load_data()
        if age < 18 or len(str(pin)) != 4:
            return None, "Age must be 18+ and PIN should be 4 digits"
        acc_no = cls.generate_account_number()
        
        # KEY STANDARDIZED HERE: 'account_no'
        user = {
            "name": name,
            "age": age,
            "email": email,
            "pin": pin,
            "account_no": acc_no, 
            "balance": 0
        }
        data.append(user)
        cls.save_data(data)
        return user, "Account created successfully"

    @classmethod
    def find_user(cls, acc_no, pin):
        data = cls.load_data()
        for user in data:
            # KEY STANDARDIZED HERE
            if user.get('account_no') == acc_no and user.get('pin') == pin:
                return user
        return None

    @classmethod
    def deposit(cls, acc_no, pin, amount):
        data = cls.load_data()
        for user in data:
            # KEY STANDARDIZED HERE
            if user.get('account_no') == acc_no and user.get('pin') == pin:
                if 0 < amount <= 10000:
                    user['balance'] += amount
                    cls.save_data(data)
                    return True, "Deposit successful"
                return False, "Amount must be between 1 and 10000"
        return False, "Invalid account or PIN"

    @classmethod
    def withdraw(cls, acc_no, pin, amount):
        data = cls.load_data()
        for user in data:
            # KEY STANDARDIZED HERE
            if user.get('account_no') == acc_no and user.get('pin') == pin:
                if user['balance'] >= amount:
                    user['balance'] -= amount
                    cls.save_data(data)
                    return True, "Withdrawal successful"
                return False, "Insufficient balance"
        return False, "Invalid account or PIN"

    @classmethod
    def update_user(cls, acc_no, pin, name=None, email=None, new_pin=None):
        data = cls.load_data()
        for user in data:
            # KEY STANDARDIZED HERE
            if user.get('account_no') == acc_no and user.get('pin') == pin:
                user['name'] = name or user['name']
                user['email'] = email or user['email']
                user['pin'] = int(new_pin) if new_pin else user['pin']
                cls.save_data(data)
                return True, "User details updated"
        return False, "User not found"

    @classmethod
    def delete_user(cls, acc_no, pin):
        data = cls.load_data()
        for i, user in enumerate(data):
            # KEY STANDARDIZED HERE
            if user.get('account_no') == acc_no and user.get('pin') == pin:
                data.pop(i)
                cls.save_data(data)
                return True, "Account deleted"
        return False, "Account not found"