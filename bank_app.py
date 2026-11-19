# A structured list of saved recipients with their bank details and current balances
recipients = [
    {
        "name": "Amina Bello",
        "account_number": "1012345678",
        "bank": "Zenith Bank",
        "account_balance": 15000.00
    },
    {
        "name": "Chidi Okafor",
        "account_number": "2087654321",
        "bank": "Access Bank",
        "account_balance": 2500.00
    },
    {
        "name": "Tunde Adeniran",
        "account_number": "0099887766",
        "bank": "GTBank",
        "account_balance": 500.00
    },
    {
        "name": "Blessing Okon",
        "account_number": "3045566778",
        "bank": "United Bank for Africa (UBA)",
        "account_balance": 48250.75
    },
    {
        "name": "Musa Ibrahim",
        "account_number": "0122334455",
        "bank": "First Bank of Nigeria",
        "account_balance": 9100.00
    }
]



account_balance = 5000.00



def welcome_msg():
    print("Welcome to Trust Bank")
    print()
    print("What would you like to do today..")
    print()
    print("Would you like to tranfer or check your balance")
    print()
    
    
    
def show_recipient():
    print("Who would you like to transfer to.")
    print()
    for recipient in recipients:
        print()
        print(f"Name:              {recipient["name"]}")
        print(f"Account Number:    {recipient["account_number"]}")
        print(f"Bank Name:         {recipient["bank"]}")
        print()
    





def get_recipient(account_no):
    for recipient in recipients:
        if recipient["account_number"] == account_no:
            return recipient





def balance_check(amount):
    if amount <= account_balance:
        return True
    else:
        return False
    
    
    
    
    
    
def transfer(amount, recipient):
    global account_balance
    account_balance -= amount
    recipient["account_balance"] += amount
    print(f"Transfer of {amount} to {recipient["name"]} is Successful.")





while True:
    welcome_msg()
    response = input("Type TF or AB:   ").strip()
    if response == "TF":
        show_recipient()
        account_no = input("Please enter recipient account number:   ").strip()
        found_recipient = get_recipient(account_no)
        if found_recipient:
            amount = float(input("Enter the amount:   ").strip())
            can_transfer = balance_check(amount)
            if can_transfer:
                transfer(amount, found_recipient)
                continue
            else:
                print("Insufficient Funds.")
                continue
        else:
            print("Recipient nor found")
            continue
    elif response == "AB":
        print()
        print(f"Your account balance is {account_balance}")
        print()
        continue
    else:
        print("Select a correct option.")