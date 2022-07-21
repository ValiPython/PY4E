# Exercise 2: Rewrite your pay program using try and except so that your program handles
# non-numeric input gracefully by printing a message and exiting the program.
# The following shows two executions of the program:

# Enter Hours: 20
# Enter Rate: nine
# Error, please enter numeric input

# Enter Hours: forty
# Error, please enter numeric input

try:
    hours = int(input('Enter Hours: '))
    rate = int(input('Enter Rate: '))

except:
    print('Error, please enter numeric input')
    quit()

pay1 = hours * rate
pay2 = pay1 + (hours - 40) * (rate * 0.5)


if hours <= 40:
    print('Pay:', int(pay1))
else:
    print('Pay:', int(pay2))