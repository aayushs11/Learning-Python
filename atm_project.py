print('Welcome to Nepal Bank Limited ATM Service')

# PIN=2024

# user_pin= int(input('Enter your 4-digit PIN: '))
# if PIN==user_pin:
#     print('Welcome to ATM Service')
# else:
#     print('Your PIN is incorrect. Please Try Again!')

balance= 10000

while True:
    print('\nPlease select an option:')
    print('1. Check Balance')
    print('2. Deposit Money')
    print('3. Withdraw Money')
    print('4. Exit')

    user_input= int(input('Enter from (1-4): '))

    if user_input==1:
        print(f'Your current balance is Rs {balance}')

    elif user_input==2:
        amount= float(input('Enter amount to deposit:'))
        balance += amount
        print(f'Rs {amount} Deposit Successful. Your new balance is Rs',balance)
    
    elif user_input==3:
        amount= float(input('Enter amount to withdraw:'))
        if balance>=amount:
            balance -= amount
            print(f'Rs {amount} Withdraw Successful. Your new balance is',balance)
        else:
            print('Insufficient Balance')
    
    elif user_input==4:
        print('Thank you for using NBL Service. Goodbye!😊🙏')
        break

    else:
        print('Invalid Option. Please Try Again ⚠')