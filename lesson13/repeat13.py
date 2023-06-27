def ismmple_func(*args, **kwargs):
    print(args)
    print(kwargs)

ismmple_func(1,2,3, x='qwerty', y= 'йцуке')

num_list = [1,2,3]
print(list(filter(lambda x: x>2, num_list)))
print(list(map(lambda x: x + 1, num_list)))