balance=1000

print('\nWelcome to Central Bank of Nepal ATM Service')

while True:
    print('\nPlease choose an option:')
    print('1. Check Balance')
    print('2. Deposit Money')
    print('3. withdraw Money') 
    print('4. Exit')  

    user_input= int(input('Enter any number from (1-4): '))

    if user_input==1:
        print(f'Your balance is Rs {balance}')
    
    elif user_input==2:
        amount= float(input('Enter amount to diposit: '))
        balance= balance + amount
        print(f'Rs {amount} has been deposited. Your new balance is Rs {balance}')
    
    elif user_input==3:
        amount= float(input('Enter amount to withdraw: '))
        if balance>=amount:
            balance= balance - amount
            print(f'Rs {amount} has been withdrawn. Your new balance is Rs {balance}')
        else:
            print(f'Inusufficient Balance. Please enter less amount')

    elif user_input==4:
        print('Thank you for choosing CBN ATM Service. Have a nice day!')
        break

    else:
        print('Invalid Optuon. Please enter any number from (1-4)')