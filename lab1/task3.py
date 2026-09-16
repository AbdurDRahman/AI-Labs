import random 

x = int(input("enter a number: ")) 

if x < 3 :
    print("minimum 3 characters required , generating a 3 character code")
    x = 3 

code = "" 

special_char_map = {
    1: '!',
    2: '@',
    3: '#',
    4: '$',
    5: '%'
}

lowercase_map = {
    1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 
    8: 'h', 9: 'i', 10: 'j', 11: 'k', 12: 'l', 13: 'm', 14: 'n', 
    15: 'o', 16: 'p', 17: 'q', 18: 'r', 19: 's', 20: 't', 21: 'u', 
    22: 'v', 23: 'w', 24: 'x', 25: 'y', 26: 'z'
}

num_special = random.randint(1,int(x/3)) 
num_uppercase = random.randint(1 , int(x/3))
num_numerics = random.randint(1 , int(x/3)) 
x -= (num_numerics + num_special + num_uppercase)

for i in range(x):

    random_number = random.randint(1,26) 
    code += lowercase_map[random_number]

for i in range(num_special):

    random_number = random.randint(1,5) 
    code += special_char_map[random_number]

for i in range(num_numerics):

    random_number = random.randint(1,9)
    code += str(random_number)    

for i in range(num_uppercase):

    random_number = random.randint(1,26)
    code += lowercase_map[random_number].upper()

code = "".join(random.sample(code, len(code)))
print(code)



