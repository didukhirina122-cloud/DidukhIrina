name = 'Ira'                                #тип даних str
age = 16                                    #тип даних int
height = 1.66                               #тип даних float
is_student = True                           #тип даних bool
hobbies = ['dance', 'books']                #тип даних list
friends = {"Саша", "Маша"}                  #тип даних set
birthday = (25, 5, 2009)                       #тип даних tuple
book =  {'aftg': 'allforthegame'}           #тип даних dict

#виведення кожної змінної та її типу

print('name', type(name),':', name)
print('age', type(age),':', age)
print('height', type(height),':', height)
print('is_student', type(is_student),':', is_student)
print('hobbies', type(hobbies),':', hobbies)
print('friends', type(friends),':', friends)
print('birthday', type(birthday),':', birthday)
print('book', type(book),':', book)

a = 52
b = 8

c = a + b                #додавання
print(c)

d = a - b                #віднімання
print(d)

n = a * b                 #множення
print(n)

f = a / b                 #діленння (результат завжди float)
print(f)

g = a // b                #ділення без остачі
print(g)

s = a % b                 #остача від ділення
print(s)

x = a ** b                #піднесення до степення
print(x)