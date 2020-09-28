# Question 1 - Write a function to print "Hello_USERNAME"

def hello_name(user_name):
    print("Hello" + user_name.upper() + "!")

hello_name('Carlos')

# Question 2 - Print first odd numbers
def odd_number():
for i in range(0,101,2):
    print(i)

odd_numbers()

# Question 3 - Write a function return the max number in a given list

def max_num_in_list(a_list):
    max_num = max(a_list)
    return max_num

print(max_num_in_list([2,3,5,8,9]))

# Question 4 - write a function to return if the given year is aleap year

def is_leap_year(a_year):
    if a_year % 4 == 0 and a_year % 100 != 0:
        print(if'{a_year'} is a leap year')
    elif a_year % 400 == 0:
        print(f'{a_year} is a leap year')
    else:
        a_year = False

def is _leap(a_year):
    if a_year % 4== 0 and (a_year % 400 == 0 or a_year % 100 != 0):
        print(True)
    else:
        print(False)

# Question 5 - Write a function to check if all numbers in a list are consecutive

def is_consecutive(a_list):
    i = 0
    status = True
    while i < len(a_list) - 1:
        if a_list[i] + 1 == a_list[i+1]:
            i += 1
        else:
            status = False
            break
    print(status)
    







    
