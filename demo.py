print("This is my first line of code today")
first_name = "Ayobamidele"
last_name = "Ewetuga"
# output = "Hello, {} {}".format(first_name ,last_name)
output = f"Hello, {first_name} {last_name}"
print(output)
my_num = 96.5
print(str(my_num) + " is my number")
print(f"my number is {my_num}")
print(f"{my_num} is my number")
# This code below uses the int function before the input function.  
# Therefore allowing it to turn into a string
# It can also be written in the print function so as to turn it into an "int" or 'float' 
# # first_num = int(input("What is your first number: "))
# # second_num = int(input("What is your second number: "))
# # print(f"The number is {first_num + second_num}")

#Here i call the datetime and deltatime module and import it into the file
from datetime import datetime , timedelta
#collect the input in dd/mm/yy
birthday = input("what is your birthday (dd/mm/yy): ")
#transfer into a new variable, which converts it into a datetime object 
birthday_date = datetime.strptime(birthday, '%d/%m/%Y')
#here i have it printed out and turned into a string

print(str(birthday_date))

one_day = timedelta(days=5) 
birthday_eve = birthday_date - one_day
print("This is the day before my birthday " + str(birthday_eve) )
# current_time = datetime.now()

# print("Today is: " + str(current_time.minute))

print(numbers < 10)