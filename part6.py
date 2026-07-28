language = 'python'

if language == 'python':
    print('hai isme')
elif language == 'java':
    print('java')
else:
    print('nhi h ')

# # Comparisons:
# Equal:            ==
# Not Equal:        !=
# Greater Than:     >
# Less Than:        <
# Greater or Equal: >=
# Less or Equal:    <=
# Object Identity:  is


# False Values:
    # False
    # None
    # Zero of any numeric type
    # Any empty sequence. For example, '', (), [].
    # Any empty mapping. For example, {}.
# yeh values pe condition false dega 

# condition = False

# if condition:
#     print('Evaluated to True')
# else:
#     print('Evaluated to False')

user = 'Admin'
logged_in = True

if user == 'Admin' and logged_in: # agar logged in true nhi hota to yeh nhi else wala chalata
    print('admin page')
else :
    print('bad credentials')

if not logged_in:
    print('hsbvhdbv') # agar yeh false hoga to yeh print ho jayega 

a = [1,2,3]
b = [1,2,3]
print(id(a)) # 126478582303168
print(id(b)) # 126478582305024
print(a is b ) # false
