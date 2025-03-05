# def c_to_f (temp):
#     return (temp * 9/5) + 32
#
# celsius_temps = [0.0, 10.0, 20.0, 30.0, 40.0, 50.0]
#
# fahrenheit_temps = list(map(c_to_f, celsius_temps))
#
# print(fahrenheit_temps)
#
# for temp in fahrenheit_temps:
#     print(temp)

#Podemos usar uma função lambda

celsius_temps = [0.0, 10.0, 20.0, 30.0, 40.0, 50.0]

fahrenheit_temps = list(map(lambda temp: (temp * 9/5) + 32, celsius_temps))

print(fahrenheit_temps)