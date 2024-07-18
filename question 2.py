import re
from datetime import datetime
import jdatetime
def convert_to_jalali(date_str):
    patterns = [
        r'(\d{2})-(\d{2})-(\d{4})',  # 11-07-2024
        r'(\d{1,2})-(\d{1,2})-(\d{4})',  # 9-7-2024
        r'(\d{1,2})/(\d{1,2})/(\d{4})',  # 9/7/2024
        r'(\d{1,2})/(\d{1,2})/(\d{2})',  # 9/7/24
    ]
    for pattern in patterns:
        match = re.match(pattern, date_str)
        if match:
            day, month, year = match.groups()
            if len(year) == 2:
                year = '20' + year
            day = int(day)
            month = int(month)
            year = int(year)
            gregorian_date = datetime(year, month, day)
            jalali_date = jdatetime.date.fromgregorian(date=gregorian_date)
            return jalali_date.strftime('%Y/%m/%d')
    return "Invalid date format"
dates = ["11-07-2024", "9-7-2024", "9/7/2024", "9/7/24"]
for date in dates:
    print(f"{date} -> {convert_to_jalali(date)}")
