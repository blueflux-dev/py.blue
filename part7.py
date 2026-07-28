nums = [1,2,3,4,5]

for num in nums:
    if num == 3:
        print('found')
        break
    print(num)

print('sudcvudcvwcuwvudvc')

for num in nums:
    if num == 3:
        print('found')
        continue
    print(num)

# output :
# 1
# 2
# found
# sudcvudcvwcuwvudvc
# 1
# 2
# found
# 4
# 5

for num in nums:
    for letter in 'abc':
        print(num , letter)

# 1 a
# 1 b
# 1 c
# 2 a
# 2 b
# 2 c
# 3 a
# 3 b
# 3 c
# 4 a
# 4 b
# 4 c
# 5 a
# 5 b
# 5 c

for i in range(1 , 10): # not include 10
    print(i) # you know the output i guess

# WHILE LOOP

x = 0
while x < 10: # agar x < 10 ke jagah True likh doge to infinite looop ban jayega 
    # yaha bhi break statemrnt use kr sakte ho 
    print(x) # print krega 0 se 9
    x += 1