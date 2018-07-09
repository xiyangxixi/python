'''
通过列表生成式，我们可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的。
而且，创建一个包含100万个元素的列表，不仅占用很大的存储空间，如果我们仅仅需要访问前面几个元素，那后面绝大多数元素占用的空间都白白浪费了。
生成器保存的是算法
所以，如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程
中不断推算出后续的元素呢？这样就不必创建完整的list，从而节省大量的空间。在Python中，这种一边循环一边计算的机制，称为生成器：generator。
通过next（）进行打印
'''
#g = (x * x for x in range(10))
#for n in g:
#    print(n)
g = fib(6)
while True:
    try:
        x = next(g)
        print('g:', x)
    except StopAsyncIteration as e:
        print('value:', e.value)
        break