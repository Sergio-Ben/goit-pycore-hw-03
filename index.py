from datetime import datetime, timedelta
import random
import re

 #1
def get_days_from_today(date: str) -> int | None:
    try:
        given_date = datetime.fromisoformat(date).date()
    except (ValueError, TypeError):
        print(f"Invalid date: {date!r}. Expected format is 'YYYY-MM-DD'.")
        return None

    today = datetime.today().date()
    return (today - given_date).days

print(f"First task: {get_days_from_today('2021-10-09')}")

 #2
def get_numbers_ticket(min: int, max: int, quantity: int) -> list[int]:
    if (min < 1 or max > 1000 or quantity > (max - min + 1)):
        return []
    
    return sorted(random.sample(range(min, max + 1), quantity))


lottery_numbers = get_numbers_ticket(1, 5, 5)
print("Ваші лотерейні числа:", lottery_numbers)

 #3
def normalize_phone(phone_number: str) -> str:
    phone_number = phone_number.strip()
    digits = re.sub(r"\D", "", phone_number)

    if phone_number.startswith("+"):
        return "+" + digits
    if digits.startswith("380"):
        return "+" + digits
    return "+38" + digits


raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)

 #4
BIRTHDAY_FORMAT = "%Y.%m.%d"

def get_upcoming_birthdays(users: list[dict]) -> list[dict]:
    current_date = datetime.today().date()
    usersToCongratulate = []
    for user in users:
        try:
            user_birthday = datetime.strptime(user["birthday"], BIRTHDAY_FORMAT).date()
        except (ValueError, TypeError):
            print(f"Invalid birthday format for user {user['name']}: {user['birthday']!r}. Expected format is 'YYYY.MM.DD'.")
            continue
        try:
            birthday_this_year = user_birthday.replace(year=current_date.year)
        except ValueError:  # 29 February in a non-leap year
            birthday_this_year = user_birthday.replace(year=current_date.year, day=28)

        if birthday_this_year < current_date:
            try:
                birthday_this_year = user_birthday.replace(year=current_date.year + 1)
            except ValueError:
                birthday_this_year = user_birthday.replace(year=current_date.year + 1, day=28)

        if (birthday_this_year - current_date).days > 7:
            continue

        congratulation_date = birthday_this_year
        if congratulation_date.weekday() >= 5:  # Saturday or Sunday
            congratulation_date += timedelta(days=7 - congratulation_date.weekday())

        usersToCongratulate.append({
            "name": user["name"],
            "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
        })

    return usersToCongratulate

users = [
    {"name": "John Doe", "birthday": "1985.10.25"},
    {"name": "Jane Smith", "birthday": "1990.10.31"},
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
