file= open('C:/Users/aayus/OneDrive/Desktop/read.txt','r')

content=file.read()
print(content)
file.close()

#or
# with open('file.txt', 'r') as file:
#     content = file.read()
#     print(content)  # File is automatically closed after this block