# Словник товарів і їх ціни
store = {
    "яблука": 57,
    "груші": 120,
    "помідори": 54,
    "чай": 86,
    "кава": 0  # немає в наявності
}

# Функція для показу ціни з 2 знаками після коми
def format_price(price):
    return  f"{price:.2f} грн"

# Перевірка наявності товарів
def check_items(items):
    result = {}
    for item in items:
        # якщо товар є в магазині і його кількість > 0
        if item in store and store[item] > 0:
            result[item] = True   # товар є
        else:
            result[item] = False  # товару немає
    return result  # повертаємо словник з результатами

# Функція покупки товарів
def buy_items(items):
    available = check_items(items)  # перевіряємо наявність товарів

    # збираємо товари, яких немає
    missing = [item for item in available if not available[item]]

    if missing:  # якщо є відсутні товари
        print("Не можна купити. Цих товарів немає:")
        for m in missing:
            print("-", m)
        return  # зупиняємо функцію

    total = 0  # загальна сума покупки
    for item in items:
        price = store[item]                # беремо ціну товару
        price_text = format_price(price)   # форматуємо ціну для виводу
        print("Товар:", item)              # показуємо назву товару
        print("Ціна цього товару:", price_text)  # показуємо ціну
        total += price                     # додаємо до загальної суми

    total_text = format_price(total)
    print("Загальна сума до оплати:", total_text)  # показуємо суму

# Функція перегляду наявності і цін товарів
def show_prices(items):
    available = check_items(items)  # перевіряємо наявність
    for item in items:
        status = "є" if available[item] else "немає"  # статус наявності
        price = store.get(item, 0)                     # беремо ціну, якщо товар є
        price_text = format_price(price)
        print("Товар:", item)
        print("Статус:", status)
        print("Ціна:", price_text)
        print("-" * 20)

# Функція показу усіх товарів у магазині
def show_all_products():
    print("Товари у магазині:")
    for item, price in store.items():
        status = "є" if price > 0 else "немає"  # перевіряємо, чи є товар
        print(f"{item} — {status}, ціна: {format_price(price)}")  # виводимо товар, статус і ціну

# Основна функція
def main():
    show_all_products()  # спершу показуємо усі товари

    action = input("Що робимо? (купити/перевірити): ")  # запитуємо дію
    items_input = input("Введіть товари через кому: ")   # вводимо список товарів
    items = [item.strip() for item in items_input.split(",")]  # розділяємо та прибираємо пробіли

    if action == "купити":
        buy_items(items)      # викликаємо функцію покупки
    elif action == "перевірити":
        show_prices(items)    # викликаємо функцію перевірки
    else:
        print("Невідома дія. Спробуйте ще раз.")  # якщо дія не зрозуміла

# Запуск програми
if __name__ == "main":
    main()  # запускаємо основну функцію