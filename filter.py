def odd(n):
    return n % 2 == 1
print(list(filter(odd, [1, 2, 4, 5, 6, 7, 8, 9])))