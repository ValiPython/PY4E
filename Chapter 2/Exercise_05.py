# Exercise 5: Write a program which prompts the user for a Celsius temperature, convert the temperature to Fahrenheit,
# and print out the converted temperature.

temp = input('Please enter the temperature in ºC: ')

fahr = (9 / 5 * int(temp)) + 32

print('The temperature is:', int(fahr))
