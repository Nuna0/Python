# my_file = open('lesson13/file.txt', encoding='UTF-8')
# full_text = my_file.read()
# print(full_text)


# for line in my_file:
#     # print(line, end='')
#     print(line.rstrip('\n'))

# my_file.close()

with open('lesson13/file.txt', encoding='UTF-8') as my_file:
    text = my_file.read(10)
print(text)

with open('lesson13/file.txt','w', encoding='UTF-8') as my_file:
    my_file.write('Один\nДва\n')

with open('lesson13/file.txt','a', encoding='UTF-8') as my_file:
    my_file.write('Три\nЧетыре\n')


