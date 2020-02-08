from datetime import datetime , timedelta
birthyear = int(input("what is your birth: "))
current_time = datetime.now()
x = current_time.year - birthyear
print(str(x))