#Assignment2
#Dexter Onyewuchi
#CSE 1321L Section 12

#Cylinder
#This program calculates the volume of a cylinder
#Testing to see changes

radius = float(input('Enter radius: '))
length = float(input('Enter length: '))
pi = 3.14
area = radius * radius * pi
volume = area * length
print('The Volume is:', volume)
print('\n')

#SumDigits
#This program finds the sum of the digits in a number.

num = int(input('Enter number: '))
x = 0

while 1000 > num > 0:
    x += num % 10
    num = num//10
    
if 1000 > num >= 0:
    print('Sum of digits:', x)
else:
    print('You must enter a number between 0 and 1000.')

print('\n')

#Distance
#This program finds the distance between points

x1 = float(input('Enter X1: '))
y1 = float(input('Enter Y1: '))
x2 = float(input('Enter X2: '))
y2 = float(input('Enter Y2: '))
dist = (((x2 - x1)**2) + ((y2 - y1)**2))**(0.5)
print('Distance is:', dist)
print('\n')

#DrivingCost
#This program calculates the cost of a trip

dist = float(input('Distance travelled (miles): '))
mpg = float(input('Miles per gallon (mpg): '))
price = float(input('Price per gallon (dollars): '))
trip_cost = (dist/mpg) * price
print('Trip cost (dollars):', round(trip_cost, 2))
