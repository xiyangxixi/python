def test(*name):
    sum = 0
    for i in name:
        sum = sum + i * i
    return  sum
print(test(1, 2, 3))