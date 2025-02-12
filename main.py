#we will import personal account here:
from personal_account import PersonalAccount

# account users:
if __name__ == "__main__":

    account = PersonalAccount(123456, "Kurmanbek Abduraimov")
    account.deposit(1000)
    account.withdraw(200)
    account.print_transaction_history()
    print(f"Current balance: {account.get_balance()}")


    #Baktiar's bank balance
    account2 = PersonalAccount(789012, "Tilekov Baktiar")
    account2.deposit(500)
    account2.withdraw(100)
    print(account2)
    account2.print_transaction_history()

    # Using operator deposit and withdraw
    account + 500
    account - 200
    print(account)

