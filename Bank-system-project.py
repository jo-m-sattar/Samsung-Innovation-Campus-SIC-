#This is the dictionary that will store the registered accounts
registered_accounts = {
    "first account": {
        "name": "jo",
        "email": "jo@gmail.com",
        'password': "1234",
        "phone": "123",
        'gender':'male',
        'age': 25,
        'city': 'cairo',
        "balance": 1000,
        'id': 1,
    },
    "second account": {
        "name": "Ahmed",
        "email": "Ahmed@gmail.com",
        'password': "5678",
        "phone": "12345678910",
        'gender':'male',
        'age': 26,
        'city': 'Giza',
        "balance": 500,
        'id': 2,
    },
    "third account": {
        "name": "mohamed",
        "email": "mohamed@gmail.com",
        'password': "456",
        "phone": "12345678910",
        'gender':'male',
        'age': 26,
        'city': 'Giza',
        "balance": 400,
        'id': 3,
    }

}

def register():
    
        user_name = input("please enter your name:  ")
        user_email = input("please enter your email:  ")
        user_password = input("please enter your password:  ")
        user_phone = input("please enter your phone number:  ")
        user_gender = input("please enter your gender:  ")
        user_age = int(input("please enter your age:  "))
        user_city = input("please enter your city:  ")
        account = f"{user_name}'s account"
        registered_accounts[account] = {
            
                "name": user_name,
                "email": user_email,
                'password': user_password,
                "phone": user_phone,
                'gender': user_gender,
                'age': user_age,
                'city': user_city,
                "balance": 0,
                'id': len(registered_accounts) + 1,
            
        }
        
        account_registered = True
        account = registered_accounts[f"{user_name}'s account"]
        
        if account_registered:
            print("account added suscessfully!")
            print('your account id is ' + str(len(registered_accounts)))

def deposit():
                deposited_amount = int(input("please enter the amount you want to deposit: "))
                depostited_currency = input("please enter the currency you want to deposit in:(EGP/USD/SAR) ").upper()
                if depostited_currency == "EGP":
                     registered_accounts[account]["balance"] += deposited_amount
                if depostited_currency == "USD":
                     registered_accounts[account]["balance"] += deposited_amount * 30  
                if depostited_currency == 'SAR':
                     registered_accounts[account]["balance"] += deposited_amount * 9  
                print('Your new balance is '+str(registered_accounts[account]['balance'])+ ' EGP')
                make_another_transaction = input("do you want to make another transaction? (yes/no) ").lower()
                if make_another_transaction == "yes":
                    transactions()
                else:
                    exit('ok, bye bye')
def withdraw():
                withdrawn_amount = int(input("please enter the amount you want to withdraw: "))
                withdrawn_currency = input("please enter the currency you want to deposit in:(EGP/USD/SAR) ").upper()
                if withdrawn_currency == "EGP":
                        if registered_accounts[account]["balance"] >= withdrawn_amount:
                            registered_accounts[account]["balance"] -= withdrawn_amount
                        else:
                            print("insufficient balance")
                if withdrawn_currency == "USD":
                        if registered_accounts[account]["balance"] >= withdrawn_amount * 30:
                            registered_accounts[account]["balance"] -= withdrawn_amount * 30 
                        else:
                            print("insufficient balance") 
                if withdrawn_currency == 'SAR':
                        if registered_accounts[account]["balance"] >= withdrawn_amount * 9:
                            registered_accounts[account]["balance"] -= withdrawn_amount * 9
                        else:
                            print("insufficient balance")
                print('Your new balance is ' + str(registered_accounts[account]['balance'])+ ' EGP')
                make_another_transaction = input("do you want to make another transaction? (yes/no) ").lower()
                if make_another_transaction == "yes":
                        transactions()
                else:
                        exit('ok, bye bye')
def transfer():
                receiver_account_id = int(input('please enter the id of the account you want to transfer money into it'))
                transferred_amount = float(input('please enter the amount you want to transfer'))
                if transferred_amount <= registered_accounts[account]['balance']:
                    # receiver_account_balance = registered_accounts[account]['balance'] + transferred_amount
                    registered_accounts[account]['balance'] -= transferred_amount
                    print(str(transferred_amount) + ' EGP has been transferred to account with id ' + str(receiver_account_id) + ' successfully')
                    print('Your new balance is ' + str(registered_accounts[account]['balance']) + ' EGP')
                    make_another_transaction = input("do you want to make another transaction? (yes/no) ").lower()
                if make_another_transaction == "yes":
                    transactions()
                else:
                    exit('ok, bye bye')
def currency_conversion():
                user_balance_currency_choice = input("please enter the currency you want to check your balance in:(EGP/USD/SAR) ").upper()
                if user_balance_currency_choice == "EGP":
                     print('your balance is')
                     print(str(registered_accounts[account]['balance'])+" EGP")
                if user_balance_currency_choice == "USD":
                        print('your balance is')
                        print(str(registered_accounts[account]['balance'] / 30)+" USD")
                if user_balance_currency_choice == 'SAR':
                        print('your balance is')
                        print(str(registered_accounts[account]['balance'] / 9)+" SAR")
                make_another_transaction = input("do you want to make another transaction? (yes/no) ").lower()
                if make_another_transaction == "yes":
                    transactions()
                else:
                    exit('ok, bye bye')

print('welcome to SIC bank')
#this for loop will ask the user whether he has account or not 
#if he had account it will ask him to enter his account id and password
#and if he didn't have account it will ask him to register an account with the bank
while True:
    account_found = False
    account_registered = False
    user_has_account = input("do you have an account with us? (yes/no) ").lower()

    if user_has_account == "yes":
        user_account_id = int(input("please enter your account id  "))
        user_account_password = input("please enter your account password  ")
        for account,password in registered_accounts.items():
            if user_account_id == registered_accounts[account]['id'] and user_account_password == registered_accounts[account]['password']:
                account_found = True
                break
        if account_found:
            print('hi ' + registered_accounts[account]['name'] + ', welcome back to SIC bank')
            break
        else:
            print('account not found')
            
                

    elif user_has_account == "no":
        print("please register an account with us")
        register()
        

            
    else:
        print("invalid input")

while True:
    #this is the function that that will handle transaction
    def transactions():
        choice = input("here are our services, please choose one:\n"
                        "1. Deposit\n"
                        "2. Withdraw\n"
                        "3. Transfer\n"
                        "4. Balance Inquiry\n"
                        "5. Exit\n"
                        "6. Account information\n")

        if choice == "1":
            #this will handle the deposit transaction
            #it will ask the user to enter the amount he wants to deposit and the currency he wants to deposit in
            deposit()
                    
                        

        if choice == "2":
            #this will handle the withdraw transaction
            #it will ask the user to enter the amount he wants to withdraw and the currency he wants to withdraw in
            withdraw() 


        if choice == "3":
            #this will handle the transfer transaction
            # it will ask the user to enter the id of the account he wants to transfer money into it
            # and the amount he wants to transfer
            # it will check if the amount he wants to transfer is less than or equal to his balance
            transfer()

        if choice == "4":
            #this will handle the balance inquiry transaction
            #it will print the balance of the user's account
            currency_conversion()
                
        if choice == "5":
                #this will handle the exit transaction
                #it will ask the user to confirm if he wants to exit or not
                confirm_exit = input("Are you sure you want to exit ? ").lower()
                if confirm_exit == "yes":
                    exit("ok, bye bye")

                else:
                     transactions()
    
        if choice == "6":
        #this will print the account information of the user
             for key, value in registered_accounts[account].items():
                 print(f"{key}: {value}")
    
    
    transactions()
