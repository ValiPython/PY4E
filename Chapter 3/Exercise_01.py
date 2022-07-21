# Exercise 1: Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.

hours = float(input('Enter Hours: '))
rate = float(input('Enter Rate: '))

pay1 = hours * rate
pay2 = pay1 + (hours - 40) * (rate * 0.5)

if hours <= 40:
    print('Pay:', pay1)
else:
    print('Pay:', pay2)