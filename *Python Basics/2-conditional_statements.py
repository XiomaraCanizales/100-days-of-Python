dashes = '-----------------------------------'
# IF STATEMENT
print('IF STATEMENT:')

num1 = 5
if (num1 == 5):
    print('The number is equal to 5')
if num1 > 5:
    print('The number is greater than 5')

# conditions with logical operators
num2 = 12
if num2 % 2 == 0 and num2 % 3 == 0 and num2 == 0:
    print('Number is multiple of 2, 3 and 4')
if (num2 % 5 == 0 or num2 % 6 == 0):
    print('Number is multiple of 5 and/or 6')

# nested if statements
num3 = 63
if num3 >= 0 and num3 <= 100:
    if num3 >= 50 and num3 <= 75:
        if num3 >= 60 and num3 <= 70:
            print('Number is in the 60-70 range')

# creating and editing values
num4 = 10
if num4 > 5:
    num4 = 20
    new_num = num4 * 5
print(num4)
print(new_num)

print(dashes)

# IF-ELSE STATEMENT
print('IF-ELSE STATEMENT:')
num5 = 60
if num5 <= 50:
    print('Number less than of equal to 50')
else:
    print('Number greater thant 50')

# conditional expressions
output = 'Number less than of equal to 50' \
    if num5 <= 50 else 'Number greater thant 50'
print(output)

print(dashes)

# IF-ELIF-ELSE STATEMENT
print('IF-ELIF-ELSE STATEMENT:')
light = 'red'
if light == 'green':
    print('go')
elif light == 'yellow':
    print('caution')
elif light == 'red':
    print('stop')
else:
    print('incorrect light station')