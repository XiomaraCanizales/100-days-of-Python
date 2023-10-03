# other loops examples
print('** check for odd or even **')
for i in range(1, 11):
    if i % 2 == 0:
        print(i, " is even")
    else:
        print(i, " is odd")

# step
print('print a range with a step')
for i in range(1, 11, 3):
    print(i)

# nested for loop, using break
print('** print two elements whose sum is equal to 50 **')
n = 50
num_list = [10, 25, 4, 23, 6, 18, 27, 47]
found = False

for n1 in num_list:
    for n2 in num_list:
        if (n1 != n2):
            if (n1 + n2 == n):
                found = True
                break
    if found:
        print(n1, n2)
        break

# using continue
print('** skip when stateme is found **')
num_list = list(range(0, 10))
for num in num_list:
    if num == 3 or num == 6 or num == 8:
        continue
    print(num)
