grade= {'Aayush':70,
        'Ram':91,
        'Sita':50,
        'Krishna':83,
        'Shyam':32,
        'Gita':48
        }

#Syntax Method
# passed= {key:value for key, value in grade.items() if value>=50}
# print('Student who passed the exam are:', passed)

passed= {name:result for name, result in grade.items() if result>=50}
print(passed)

#Trails Dictionary Comprehension

# selection= {post:result for post, result in grade.items() if result>=40}
# print(selection)

# tired= {name:result for name, result in grade.items() if result>32}
# print(tired)
