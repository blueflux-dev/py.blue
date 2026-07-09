# LISTS , TUPLES AND SETS
courses = ['srijan ', 'ishna','rahut','samosa']
# access by courses[0] = srijan
# courses[0][0] = s
# courses[-1] = samosa   -1 is always be the last 
# courses[4] = error
# courses[0:2] = ['srijan' , 'ishna'] so its excluding index 2
# courses.append('art')  art add ho jayega humare list ke ending me 
# courses.insert(0,'art') art index 0 pe add ho jaega and sabko aage push kr dega 
courses_2 = ['art','Education']
# courses.insert(0,courses_2) pura courses2 ho jayga

# courses.extend(course_2) add ho jayega course me 
# courses.remove('srijan') hat jayega 
# courses.pop() last value delete krke return kr dega 


# courses.reverse() reverse ho jayega apna list 
# courses.sort() ab list sort ho jayega alphabetically and yeh numbers ke liye bhi work krega for ascending order

# courses.sort(reverse = True) ab sort hoke reverse bhi ho jayega 

# sorted(courses) -> yeh course ko affect nhi krega bus sorted version return krega 

nums = [1,8,3,6,2]
# max(nums) return krega max number 
# sum(nums) list ke saare number ko sum krke return krega 

# courses.index('samosa') kis index pe h samosa

# 'art' in course -> return krega boolean ki courses me yeh h ya nhi 

for item in courses:
    print(item) # for loop and yeh ek priint krne ke baad line change krega 

course_str = ', '.join(courses)
# srijan,ishna,rahut,samosa aesa ho jayega 

# TUPLES are like list but not modifiable 


Mutable
list_1 = ['History', 'Math', 'Physics', 'CompSci']
list_2 = list_1

print(list_1)
print(list_2) 

list_1[0] = 'Art' now yeh list 1 me bhi change ho jayega coz by reference conneect h 


print(list_1)
print(list_2)


Immutable
tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
tuple_2 = tuple_1

print(tuple_1)
print(tuple_2)

tuple_1[0] = 'Art'

print(tuple_1)
print(tuple_2)

# Sets
cs_courses = {'History', 'Math', 'Physics', 'CompSci'}

print(cs_courses)

# bas antar yeh h isme curly brackey use ho rha h and sets me double value ko remove kr deta h 
art_courses = {'History', 'Math', 'art', 'design'}
# cs_courses.intersection(art_courses) return krega jo value common h dono taraf and interection ke jagah difference lagau to cs_course me se common value nikal ke jo value bachega wo return krega 
# and intersection ke jagah union lagaoge to mix ho jayega 


# Empty Lists
empty_list = []
empty_list = list()

# Empty Tuples
empty_tuple = ()
empty_tuple = tuple()

# Empty Sets
empty_set = {} # This isn't right! It's a dict
empty_set = set()