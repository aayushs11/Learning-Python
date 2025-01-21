w = input('Enter any word: ')
 
word = w.lower()[0]

if word == 'a' or word == 'e' or word == 'i' or word == 'o' or word == 'u':
    print(f'The word {w} is vowel')
else:
    print(f'The word {w} is not vowel')