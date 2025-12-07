# Зберігаємо стан користувачів у пам'яті
user_states = {}


def set_state(user_id: int, state: str):
    """Встановити стан користувача"""
    user_states[user_id] = state


def get_state(user_id: int) -> str | None:
    """Отримати стан користувача"""
    return user_states.get(user_id)


def del_state(user_id: int):
    """Скинути стан користувача"""
    if user_id in user_states:
        del user_states[user_id]
