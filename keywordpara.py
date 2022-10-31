def sample(a, b=10, *args, c, **kwargs):
    print('a', a)
    print('b', b)
    print('c', c)
    print('args', args)
    print('kwargs', kwargs)

sample(1, 2, 3, 4, c=5, d=6, e=7)