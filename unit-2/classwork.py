'''classmates = ["ross", "marcus", "flavio", "joseph", "maham", "vinay", "gungeet", "faris"]

#prints the number of items in a list 
print(len(classmates))

#prints the first item in the list

print(classmates[0])

#prints last element in list 
print(classmates[-3])

#adds element to the list  
classmates.append("john")

# insert function will take the location and what you wanna put 
classmates.insert(1, "jane")

#pop function can be used to remove soenthibg from the list from the end 
#classmates.pop(2)

#print all elements in the list 
for names in classmates:
    print(names)

#search for an item in the list --> linear search in the code

#for name in classmates:
    #if name == 'maham':
#        print('maham found in the list')

#another way to search

if 'maham' in classmates:
    print('found maham in the list')

#using indices in for loop, enumerate is a built in function that allows to access the positioning 
for idx, name in enumerate(classmates):
    #print(idx, name)
    if 'maham' in classmates:
        print('found maham in the list in position', idx)
      

#print your name backwards 
last_name = 'Jilani'
x = len(last_name)

for x in range(len(last_name) - 1, -1, -1):
    print(last_name[x])

#shortest way , 2 :: no start and end are specified and they ask you to go backwards with the -1 --> step 
print(last_name[: : -1])

#will print from the first to the third character 
print(last_name[1:3])
'''



