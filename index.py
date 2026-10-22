from datetime import datetime

DATE_FORMAT = "%Y-%m-%d"


def get_days_from_today(date: str) -> int | None:
    """
    Return the number of days from the given date to today.

    Only calendar days are counted; the time of day is ignored.
    The result is negative if the given date is in the future.

    :param date: date string in 'YYYY-MM-DD' format, e.g. '2020-10-09'
    :return: number of days as int, or None if the input is invalid
    """
    try:
        given_date = datetime.strptime(date, DATE_FORMAT).date()
    except (ValueError, TypeError):
        print(f"Invalid date: {date!r}. Expected format is 'YYYY-MM-DD'.")
        return None

    today = datetime.today().date()
    return (today - given_date).days


if __name__ == "__main__":
    print(get_days_from_today("2021-10-09"))
    print(get_days_from_today("2030-01-01"))
    print(get_days_from_today(datetime.today().strftime(DATE_FORMAT)))
    print(get_days_from_today("09.10.2021"))
    print(get_days_from_today("2021-02-30"))
    print(get_days_from_today(None))
