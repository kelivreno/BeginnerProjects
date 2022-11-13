#impossible to get an odd number

def even_num(num):
    number = 0
    for digit in num:
        if digit in [1 or 3 or 5 or 7 or 9]:
            number = number + 1
        else:
            number = num
    return number
print(even_num(input("Enter one digit: ")))