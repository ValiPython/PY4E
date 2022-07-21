# Exercise 6: Rewrite your pay computation with time-and-a-half for overtime and create
# a function called 'computepay' which takes two parameters (hours and rate).

def computepay (hours, rate):
   if hours <= 40:
      print('Pay:', pay)
   else:
      print('Pay:', extra)
   return pay, extra

hours = float(input('Enter Hours: '))
rate = float(input('Enter Rate: '))

pay = hours * rate
extra = pay + (hours - 40) * (rate * 0.5)

computepay(hours, rate)


