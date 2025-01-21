grade = int(input('Enter the grade you secured: '))

if grade>=90:
    print('A+ ⭐⭐⭐⭐⭐ Outstanding')
elif grade>=80:
    print('A Excellent ⭐⭐⭐⭐')
elif grade>=70:
    print('B+ Very Good ⭐⭐⭐')
elif grade>=60:
    print('B Good ⭐⭐')
elif grade>=50:
    print('C+ Satisfactory ⭐')
else:
    print('Fail* Try Again')