# Calculating Circle

import math

radius = float(input("Enter radius of circle: "))
circumference = 2 * math.pi * radius
area = math.pi * pow(radius, 2)


# round(value, decimals) round to X decimal places round circumference to 2 decimals, round area to 2 decimals
print(f"The circumference of the circle is {round(circumference, 2)} cm" 
      f" and the area of the circle is {round(area, 2)}cm²" )
