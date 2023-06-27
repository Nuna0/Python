import math

# access_level = input("Введите ваш уровень доступа. ")

# if access_level in check_list:
#     print("Доступ разрешен")
# else:
#     print("В доступе отказано")
check_list = ['админ','superuser']

def acces_check():
    access_level = input("Введите ваш уровень доступа. ")

    if access_level in check_list:
      print("Доступ разрешен")
    else:
        print("В доступе отказано")

acces_check()

def sqrt_with_check(num):
   if num >= 0 :
      return math.sqrt(num)
   else:
      return 0
   
print(f'{sqrt_with_check(15):.2f}')

def greeting(name, sername):
   print(f'Здравствуйте, {sername} {name}')

greeting("A","T")

def incr(num):
    #return num + 1
    num_list.append(num +1)
    #num_list = [1,2]

num_list = [1,2,3]
incr(3)
print(num_list)
# print(num)
