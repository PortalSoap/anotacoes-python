import math

degreesFahrenheit = int(input("Insira a temperatura em graus Fahrenheit: "))
degreesCelsius = 5 * ((degreesFahrenheit - 32) / 9)

print("Conversão (F° para C°):", math.trunc(degreesCelsius))