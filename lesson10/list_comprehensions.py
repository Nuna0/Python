num_list = [x for x in range(1,11) if x != 3]
print(num_list)

input_nums = [int(input()) for _ in range(4)]
print(input_nums)

input_numbs2 = [x ** 2 for x in input_nums if x >= 0]
print(input_numbs2)

input_numbs3 = [x ** 2 if x >= 0 else x ** 3 for x in input_nums ]
print(input_numbs3)