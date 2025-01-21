from datetime import datetime

# Ask the user for their birthdate
birthdate_str = input("Enter your birthdate (YYYY-MM-DD): ")

try:
    # Convert the input to a date object
    birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d")
    today = datetime.today()
    
    # Calculate the age
    age = today.year - birthdate.year
    if (today.month, today.day) < (birthdate.month, birthdate.day):
        age -= 1
    
    print(f"You are {age} years old.")
except ValueError:
    print("Invalid date format. Please enter your birthdate in YYYY-MM-DD format.")
