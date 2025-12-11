import json
import os


def load_json(filename):
    # Load data from JSON file
    # Завантаження даних з JSON файлу
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}


def save_json(filename, data):
    # Save data to JSON file
    # Збереження даних у JSON файл
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def get_user_list(user_id, filename):
    # Get list of manga for a specific user
    # Отримання списку манги для конкретного користувача
    data = load_json(filename)
    return data.get(str(user_id), [])


def add_to_list(user_id, manga_id, filename):
    # Add manga to user's list (Favorites or Read)
    # Додавання манги до списку користувача
    data = load_json(filename)
    user_key = str(user_id)

    if user_key not in data:
        data[user_key] = []

    if manga_id not in data[user_key]:
        data[user_key].append(manga_id)
        save_json(filename, data)
        return True  # Added successfully / Успішно додано

    return False  # Already exists / Вже існує