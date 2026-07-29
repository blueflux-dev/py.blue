# FUNCTIONS

# def hello_func():
#     print('hello function')

# hello_func() # to call a function
def hello_func():
    return 'hello function'


print(hello_func().upper())

def hibro(greeting):
    return '{} bro how are you'.format(greeting)

print(hibro('hello')) # by passing the value to the function 

def helloc(greeting , name = 'srijan'): # so name as default srijan and you can also pass it the value 
    return '{},{}'.format(greeting , name)

print(helloc('hey baby'))

def student_info(*args , **kwargs): # 
    print(args)
    print(kwargs)

student_info('math','art',name = 'srijan',age = 22) # args are tuples and kwargs are dictionary just like mutable and immutable

courses = ['Math' , 'Art']
info = {'name': 'srijan' , 'age': 22}

student_info(courses , info)
# Number of days per month. First value placeholder for indexing purposes.
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_leap(year):
    """Return True for leap years, False for non-leap years."""

    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def days_in_month(year, month):
    """Return number of days in that month in that year."""

    if not 1 <= month <= 12:
        return 'Invalid Month'

    if month == 2 and is_leap(year):
        return 29

    return month_days[month]