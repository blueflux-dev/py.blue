message = 'srijan is a fool'
print(message)
print(len(message)) #16
print(message[0]) #s
print(message[0:5]) #srija (excluding 5 index)
# so agar ratio ka aage ka chod diya then jaan jayega ki hum start se. krne wale h and as well as for end 

# want uppercase
print(message.upper()) #as well as for lower

print(message.count('i')) # kitna h ->  2
print(message.find('fool')) # kis index pe h -> 12

# replace characters 
new_msg = message.replace('fool','nice') # yeh reference nhi copy pass krta h jisse original ko koi dikkat nhi hogi
print(new_msg)

greet = 'hello'
name = 'srijan'
gteeying = greet + ' ' + name

print(gteeying)

#BETTER FORMAT FOR WRITING 
better_greet = '{} {} Welcome'.format(greet,name)
print(better_greet)

#SIMPLE FORMAT 
simple_greet = f'{greet} {name.upper()} Welcome'
print(simple_greet) # and humne name ko uppercase hi kr diya saath hi saath 
