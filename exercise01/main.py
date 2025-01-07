from datetime import datetime

def get_days_from_today(date):
    date_now = datetime.now().date()
    try:
        input_date = datetime.strptime(date, "%Y-%m-%d").date()
        return (date_now - input_date).days
    except ValueError:
        return "Invalid date"

print(get_days_from_today("2024-10-25"))