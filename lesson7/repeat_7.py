numbs = [5, 10, -2,3.1]
print(len(numbs))
print(min(numbs))
numbs.sort(key=lambda x: len(x))
print(numbs)