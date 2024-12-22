from datetime import datetime
def greet():
    today = datetime.now().date()
    print(today)
    return str(today)

