import sys

args = sys.argv
accounts = []
while(True):
    print("\n**********************************************")
    print("What do you want to do?")
    print("==============================================\n")
    print("\t 1. Create account \n\t 2. View accounts \n\t 3. Deposit \n\t 4. Withdraw \n\t 5. Exit\n")
    action = input("Enter number: ")

    if(action == '1'):
        print("\nCreating account")
        number = input("Enter account number: ")
        accounts.append({'number': number, 'balance': 0})
        print(f"An account with number {number} has been created!")

    elif(action == '2'):
        print("\nViewing accounts")

        for account in accounts:
            print(f'Account Name: {account["number"]}, Balance: {account["balance"]} RWF')

        print("Done")

    elif(action == '3'):
        print("\nDepositing")
        account_number = input("Enter account number: ")
        amount_string = input("Enter deposit amount: ")

        try:
            amount = int(amount_string)
        except ValueError:
            print("Please enter a valid value")
            continue

        found = False
        if (amount < 0):
            print("Invalid amount")
            continue
        for account in accounts:
            if(account['number'] == account_number):
                found = True
                balance = int(account['balance']) + amount
                account['balance'] = balance
        
        if not found:
            print("Account does not exist")
        else:
            print("Operation successful")

    elif(action == '4'):
        print("\nWithdrawing")
        account_number = input("Enter account number: ")
        amount_string = input("Enter deposit amount: ")

        try:
            amount = int(amount_string)

        except ValueError:
            print("Please enter a valid value")
            continue
        
        found = False
        success = False

        if (amount < 0):
            print("Invalid amount")
            continue

        for account in accounts:

            if(account['number'] == account_number):
                found = True

                if(amount > int(account['balance'])):
                    print("Balance is less than withdrawal amount")

                else:
                    balance = int(account['balance']) - amount
                    account['balance'] = balance
                    success = True

        if not found:
            print("Account does not exist")

        if not success:
            continue

        else:
            print("Operation successful") 

    elif(action == '5'):
        print("\nExiting...")
        exit()
    else:
        print("Enter a valid action")