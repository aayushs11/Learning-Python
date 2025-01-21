#Using with statement for file handling
with open('trimurti.csv','r') as file:
    content= file.read()
    print(content)