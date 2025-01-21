#Open file in read mode
file= open('contact.txt','r')

#Read the file content
content= file.read()
print(content)

#close the file
file.close()

#OR, Directly read and display content
# file= open('contact.txt').read()
# print(file)