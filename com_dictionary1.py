basketball_score= {'Aayush':113,
        'King':110,
        'Queen':95,
        'Minister':82,
        'Army': 50
        }

high_score= {name: score for name, score in basketball_score.items() if score>80}
print(high_score)








# numbers= {1,2,3,4,5,6,7,8,9,10,11,12}

# # {key_expression: value_expression for item in iterable if condition}
# even= {x: x for x in range(1,15) if x%2==0}
# print(even)