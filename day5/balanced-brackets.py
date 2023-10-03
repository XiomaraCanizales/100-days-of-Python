def check_balance(brackets):
    check = 0
    for bracket in brackets:
        if bracket == '[':
            check += 1
        elif bracket == ']':
            check -= 1
        
        if check < 0:
            break
    return check == 0

print(check_balance("[[][][][]]"))
print(check_balance("[[[[][]]]]"))
print(check_balance("[[]]]]][[]"))
print(check_balance("[][[]]][[]"))


