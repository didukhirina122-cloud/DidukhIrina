a = [1, 4, 5, 7, 8, 3, 17, 22, 32,
             "Ріко", "Жан", "Ніл", "Аарон", "Ендрю",
             "Ваймак", "Елісон", "Кевін", "Рене"]
#розділяємо список на числа і слова
ints= [x for x in a if isinstance(x, int)]
strs= [x for x in a if isinstance(x, str)]

#сортуємо числа по зростанню
ints.sort()
#сортуємо слова від "а" до "я"
strs.sort()

#об’єднуємо спочатку числа, потім строки
sorted_list = ints + strs

#створюємо список чисел кратні 2(парні числа)
numbers = [x for x in int if x % 2 == 0]

#створюємо список де слова прописані капсом
str_caps = [s.upper() for s in str]

print("Основний відсортований список:", sorted_list)
print("Числа кратні 2:", numbers)

print("Слова прописані капсом:", str_caps)
