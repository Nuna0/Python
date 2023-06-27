
def fact_func(m):
    if m == 0:
        return 1
    return fact_func(m - 1) * m

print(fact_func(5))