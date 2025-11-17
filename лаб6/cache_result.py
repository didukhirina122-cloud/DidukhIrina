def cache_result(func):
    cache = {}   # тут зберігаються результати

    def wrapper(*args, **kwargs):
        key = (args, tuple(kwargs.items()))   # ключ для кешу

        if key in cache:
            print(">>> Беру результат з кешу")
            return cache[key]

        result = func(*args, **kwargs)
        cache[key] = result
        print(">>> Додаю результат у кеш")
        return result

    return wrapper