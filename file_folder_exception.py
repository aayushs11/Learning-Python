import os

#Creating folder with try and except
try:
    os.mkdir('Do Not Open')
    print('Folder created!')

except:
    print('Folder already exists!')

finally:
    print('Looks like a place to hide all the... questionable choices💻🕵️‍♂️')