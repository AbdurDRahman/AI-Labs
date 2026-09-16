
def check(num : int) -> bool :
    str_num = str(num)
    length = len(str_num)

    sum = 0 
    for digit in str_num :
        sum += int(digit) ** length 

    return sum == num 

print(check(1634))
print(check(153))
print(check(1234))