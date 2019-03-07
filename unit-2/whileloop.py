#print a message 10 times 
'''
count = 0
while count < 10:
    print ("inside while loop")
    count += 1 
'''
'''
# search for a value in a list 
nums = ['a', 'b', 'c', 'd', 'e']
found = False
key = 'd'
#just starting to look for something not found it yet, the not negates the variable, it is checking ot see if this value is true 
# if this things is true then we stop
'''
'''while not found:
        found = True
        break
    if nums[pos] == key'''

'''
# it doesnt work if you switch it 
for idx, item in enumerate(nums):
    print (item)
    print(idx)
    #print(nums[idx])
    if nums[idx] == key:
        print(f"Found {key} at position {idx}")

        break
#print (idx)
'''

'''
#continue 
my_nums = [1, 3, 15, 8, 7, 24, 6, 5, -1]

for num in my_nums:
    if num % 2 == 0:
        continue 
    print(f'{num} is odd')
'''

'''
# infinite true and then I break 
answer = 7 

while True:
    user_input = input ("Enter your number")
    x = int(user_input)
    if x > answer:
        print ("too big")
    elif x < answer:
        print("too small")
    else:
        print("correct")
        break

# other way of doing it 

x = 0 
while x != answer:
    user_input = input ("Enter your number")
    x = int(user_input)
    if x > answer:
        print ("too big")
    elif x < answer:
        print("too small")
    else:
        print("correct")
        break

# in to check if a value is in the list 

#input a number REMEMBER FOR DATA SCIENCE 
userr_inputt = 0
while user_input != answer:
    if user_input > answer:
        print('too big')
    elif user_input < answer:
        print ('too small')
    else: 
        print('correct')
        break 
    user_input = int(input('Enter the number: '))
    '''

# lets there is a list of numbers 
age = [25, 39, 45, 41, 27, 18, 33, 65, 11, 50]
total_age = 0 
for num in age:
    total_age = total_age + num  
    # sum += num
print(total_age)


