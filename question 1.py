import re
def validate_email(email):
    # الگوی عبارت منظم برای اعتبارسنجی آدرس ایمیل
    regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    # بررسی مطابقت آدرس ایمیل با الگو
    if re.match(regex, email):
        return True
    else:
        return False
# مثال‌ها
emails = ["test@example.com", "invalid-email", "user@domain", "user@domain.c"]
for email in emails:
    if validate_email(email):
        print(f"{email} is a valid email address.")
    else:
        print(f"{email} is not a valid email address.")
