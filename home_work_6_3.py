number = int(input("Enter number: "))

while number > 9:
    calc_num = 1
    for digit in str(number):
        calc_num *= int(digit)
    number = calc_num

print("Result:", number)