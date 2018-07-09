def test(n):
    return  test1(n, 1)
def test1(m, x):
    if m == 1:
        return  x
    return test1(m - 1, m * x)
print(test(5))