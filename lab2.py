list_main = [1, 4, 5, 7, 8, 3, 17, 22, 32,
             "Ріко", "Жан", "Ніл", "Аарон", "Ендрю",
             "Ваймак", "Елісон", "Кевін", "Рене"]
#розділяємо список на числа і слова
list_int = [x for x in list_main if isinstance(x, int)]
list_str = [x for x in list_main if isinstance(x, str)]

#сортуємо числа по зростанню
list_int.sort()
#сортуємо слова від "а" до "я"
list_str.sort()

#об’єднуємо спочатку числа, потім строки
sorted_list = list_int + list_str

#створюємо список чисел кратні 2(парні числа)
numbers_even = [x for x in list_int if x % 2 == 0]

#створюємо список де слова прописані капсом
str_caps = [s.upper() for s in list_str]

print("Основний відсортований список:", sorted_list)
print("Числа кратні 2:", numbers_even)
print("Слова прлпасані капсом:", str_caps)