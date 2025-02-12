     Sample Test:
     
Output:
DEPOSIT of 1000 at 2025-02-12 15:12:16.712857
WITHDRAWAL of 200 at 2025-02-12 15:12:16.712857
Current balance: 800.0
Account 789012 - Tilekov Baktiar: Balance = 400.0

DEPOSIT of 500 at 2025-02-12 15:12:16.712857
WITHDRAWAL of 100 at 2025-02-12 15:12:16.712857
Account 123456 - Kurmanbek Abduraimov: Balance = 1100.0
Process finished with exit code 0

in this project i created 3 classes 
main, amount and personal account 

from datetime import datetime

class Amount:
    def __init__(self, amount, transaction_type):
        self.amount = amount
        self.timestamp = datetime.now()
        self.transaction_type = transaction_type

    def __str__(self):
        return f"{self.transaction_type} of {self.amount} at {self.timestamp}"

in personal account, i created 2 account 
from personal_account import PersonalAccount

account.deposit()
account.withdraw()
