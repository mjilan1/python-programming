#for i in range(10):
 #   print(i)
'''
square = []
for num in range(6):
    #sqr = num ** 2 
    sqr = num
    square.append(sqr)
    print(square)

this_list = ["apples", "oranages", "banana", "monkey"]
#for x in this_list:
 #   print(x)
#for name in range(len(this_list)):
 #   print(this_list[name])

for x in this_list:
    if x == "banana":
       # break
       continue
    print(x)

i = 1
while i < 7:
    print(i)
    i += 1

Fizz Buzz Test!!! 
for x in range(1, 101):
    if x % 3 == 0:
        print("Fizz")
    elif x % 5 == 0:
        print("Buzz")
    else:
        print(x)
    

def print_order(product):
    print("Thank you for purchasing the", product, ".")

print_order("Hanger")


def shipping_order(product, amount):
    if amount >= 30:
        print("its your lucky day! free shipping!")
    else:
        print("shipping charge is 5 dollars")


shipping_order("hanger", 55)
'''
def add_bonus(score):
    if score > 50:
        return score + 10 
    score += 20
    return score 

total_points = add_bonus(25)
print(total_points)