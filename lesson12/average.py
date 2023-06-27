# def avg_func(num_list):
#     return sum(num_list)/ len(num_list)

# print(avg_func({3,4,6,9}))

def avg_func(*args):
    return sum(args)/len(args)

print(avg_func(2,5,7,9,1))