def check_sum(num_list):
    for n1 in num_list:
        for n2 in num_list:
            if (n1 + n2 == 0):
                return True
    return False

print(check_sum([10, -14, 26, -5, -3, 13, 5]))