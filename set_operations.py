#courses in colleges
prime= {'BIM','CSIT','BBA','BBM','BBS'}
nccs= {'BIM','BBS','BBA','BHM','BCA'}

#common courses
common_course= prime.intersection(nccs)
print(common_course)

#all available courses
courses= nccs.union(prime)
print(courses)

#course in prime but not in nccs
diff_course= prime.difference(nccs)
print(diff_course)

#course in nccs but not in prime
lol= nccs.difference(prime)
print(lol)

#course in either college but not in both
ok= nccs.symmetric_difference(prime)
print(ok)