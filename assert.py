#Assert will test condition if condition is true,
# nothing happens, but if the condition is False, 
#it raises an AssertionError with an optional error message.

price = int(input('If soneone give you a gold for free, What is the cost of gold for you: '))

assert price==0, 'Gold is so expensive who will give it to you for free'

print('Bruh the price of gold per tola is Rs 1,80,000. Who will give it for free?')