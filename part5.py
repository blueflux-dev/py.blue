# DICTIONARIES

student = {'name': 'Srijan','age': 25,'courses': ['Math','cse']}

print(student['courses']) # access krne ke liye apna documentary
# so agar koi aesi values ko access krna h jo h nhi to error aayega 

# ek aur function h jisse ise matlab documentary ko access kr sakte h 
print(student.get('courses')) # so isse bhi access ho jayega 
# and agar ek aesi values ko access krne ki koshish krenge jo h nhi to error nhi default value none return krega 

# now if i want to change the default from none to something else then 
print(student.get('phone','Not found'))
# so default none changes to Not found

# agar explicitily assign krna h then 
student['phone'] = '555-55555'
student['name'] = 'Sijju' # now name is updated

# agar ek saath kafi update krna h then 
# student.update[{'name': 'sijju' , 'age': 26 , 'phone': '555-5555'}]

age = student.pop('age') # agar hum pop krenge to value delete krke return bhi krega 
# del student['age'] # agar age key ko delete krna h to 

print(student)
print(age)

# also len(student) se uska length aa jayega 
print(student.keys()) # so isse dictionaries ke saare keys mil jaye 
# aesi hi agar values chaiye to print(student.values()) jissse values mil jayegi saari 

print(student.items()) # dict_items([('name', 'Sijju'), ('courses', ['Math', 'cse']), ('phone', '555-55555')])

for key in student:
    print(key)

for key,value in student.items():
    print(key , value)