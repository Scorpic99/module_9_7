def is_prime(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result > 1:
            if (result % 2 == 0 or result % 3 == 0 or result % 5 == 0) and (result > 5  or result == 4):
                print("Составное")
            else:
                print("Простое")
        return result
    return wrapper

@is_prime
def sum_three(firs, second, third):
    return firs + second + third

result = sum_three(2, 3, 6)#2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71
print(result)
"""for i in range(50):
    print(f'{i}: {sum_three(i)}')"""