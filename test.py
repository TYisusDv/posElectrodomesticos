from datetime import datetime, timedelta

def get_next_month_day(current_date, ts_days):
    new_date = current_date + timedelta(days=ts_days)
    
    if ts_days == 30:
        my_date = current_date
        my_date_day = my_date.day
        my_date_month = my_date.month
        my_date_year = my_date.year
        next_month = (my_date.month % 12) + 1
        
        try:
            if my_date_month >= 12:
                new_date = my_date.replace(year=my_date_year + 1, month = next_month, day=my_date_day)  
            else:
                new_date = my_date.replace(month = next_month, day=my_date_day)  
        except ValueError as e:
            new_date = my_date + timedelta(days=ts_days)                

    return new_date

current_date = datetime(2023, 12, 31)
ts_days = 30
next_month_date = get_next_month_day(current_date, ts_days)
print(next_month_date) 