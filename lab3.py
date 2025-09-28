def main():
    students = {}
    while True:
        name = input("Введіть ім'я студента (або 'stop' для завершення): ")
        if name.lower() == "stop":         #нечутливість до регісту(можна писати капсом)
            break     #завершує цикл
        grade_str = input("Введіть оцінку за практичну роботу: ")
        if not grade_str.isdigit():      #перевіряє, чи складається рядок повністю з цифр
            continue
        grade = int(grade_str)
        students[name] = grade

    print("Список студентів та їх оцінки:")
    for name, grade in students.items():
        print(name + " - " + str(grade))     #склеюється в один рядок(+)

    if len(students) == 0:         #якщо список порожній
        print("Немає даних для обробки.")
        return

    total = sum(students.values())
    average = total / len(students)   #обчислююється середнє арифметичне

    excellent = [name for name, grade in students.items() if 10 <= grade <= 12]
    good = [name for name, grade in students.items() if 7 <= grade <= 9]
    average_students= [name for name, grade in students.items() if 4 <= grade <= 6]
    failed = [name for name, grade in students.items() if 1 <= grade <= 3]

    print("Середній бал по групі: " + str(average))
    print("Відмінники (" + str(len(excellent)) + "): " + ", ".join(excellent))
    print("Хорошисти (" + str(len(good)) + "): " + ", ".join(good))
    print("Відстаючі (" + str(len(average_students)) + "): " + ", ".join(average_students))
    print("Не здали (" + str(len(failed)) + "): " + ", ".join(failed))

if (__name__ == '__main__'):
    main()