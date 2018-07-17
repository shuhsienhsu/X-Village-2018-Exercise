import datetime
def print_next_day():
    print((datetime.date.today() + datetime.timedelta(days = 1)).isoformat())

print_next_day()