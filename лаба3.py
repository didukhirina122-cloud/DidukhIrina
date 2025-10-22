# Створюємо порожній словник для збереження результатів студентів
results = {}
# Безкінечний цикл для введення даних
while True:
    name = input("Введіть ім'я: ")  # Запитуємо ім'я студента
    if name == "stop":              # Якщо введено "stop", завершуємо цикл
        break

    while True:
      grade = int(input("Введіть оцінку: ")) # Запитуємо оцінку студента
      if 0 <= grade <= 12:
        break
      else:
        print("Неправильно введено оцінку, спробуйте ще раз.")

    results[name] = grade                   # Зберігаємо ім'я та оцінку в словнику
# Виводимо список усіх студентів та їхні оцінки
print("Студенти:")
for n in results:
    print(n, results[n])
# Обчислюємо та виводимо середній бал
print("Середній бал:", round(sum(results.values()) / len(results), 2))

exelent = [n for n in results if 10 <= results[n] <= 12]
good = [n for n in results if 7 <= results[n] <= 9]
weak = [n for n in results if 4 <= results[n] <= 6]
fail = [n for n in results if 1 <= results[n] <= 3]
# Виводимо кількість і список студентів у кожній категорії
print("Відмінники:", len(exelent))
print("Хорошисти:", len(good))
print("Відстаючі:", len(weak))
print("Не здали:", len(fail))