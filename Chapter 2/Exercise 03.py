# Exercise 3: Write a program to prompt the user for hours and rate per hour to compute gross pay.

# We won’t worry about making sure our pay has exactly two digits after the decimal place for now.

# If you want, you can play with the built-in Python round() function to
# properly round the resulting pay to two decimal places.

# Enter Hours: 35
# Enter Rate: 2.75
# Pay: 96.25

hours = input('Enter the hours: ')
rate = input('Enter the rate: ')

pay = float(hours) * float(rate)

print('The rate is:', pay)

# print('The rate is:', round(pay), '(rounded)')
