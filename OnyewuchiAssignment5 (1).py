# # Class:	        	CSE 1321L
# # Section:		12         
# # Term:		Fall  
# # Instructor:	Kevin Markley 
# # Name:		Dexter Onyewuchi   
# # Assignment:	5

#MyRectangle


class MyRectangle:
    @staticmethod
    def isValid(rect):
        if sum(rect) > 30:
            return True
        else:
            return False

    def Area(self, rect):
        if self.isValid(rect):
            return rect[0]*rect[1]
    
    def Perimeter(self, rect):
        if self.isValid(rect):
            return 2*(rect[0] + rect[1])

class TestMyRectangle:
    @staticmethod
    def main():
        width = int(input('Enter width of rectangle: '))
        height = int(input('Enter height of rectangle: '))
        dimensions = [width, height]
        rectangle = MyRectangle()
        print(f'\nEntered width:\t{width}')
        print(f'Entered height:\t{height}')
        if rectangle.isValid(dimensions):
            print(f'Area:\t\t{rectangle.Area(dimensions)}')
            print(f'Perimeter:\t{rectangle.Perimeter(dimensions)}\n')
        else:
            print('This is invalid rectangle. Try again.\n')
check = TestMyRectangle()
check.main()

#FeetMeters

def feetTometer(feet):
    meter = .305 * feet
    return meter

def meterTofeet(meter):
    feet = 3.279 * meter
    return feet

def Conversionmain():
    vals = [1,2,3,19,20]
    print(25*'-')
    print('|{:^10} | {:^10}|'.format('Feet', 'Meter'))
    print(25*'-')
    for i in vals:
        print(f'|{i:^10} | {feetTometer(i):^10.3f}|')
    print(25*'-')
    print()
    print(25*'-')
    print('|{:10} | {:10}|'.format('Meter', 'Feet'))
    print(25*'-')
    for j in vals:
        print(f'|{j:^10} | {meterTofeet(j):^10.3f}|')
    print(25*'-')

Conversionmain()

#PrintTableSeries

def displaySums(n):
    print(21*'-')
    print('|{:^8} | {:^8}|'.format('i', 'Sum(i)'))
    print(21*'-')
    a, b = 0, 0
    for i in range(1,n+1):
        a = (i/(i+1))
        a, b = b, a + b
        print(f'|{i:^8} | {b:^8.3f}|')
    print(21*'-')
    
def Printmain():       
    n = int(input('\nEnter upper limit integer: '))
    print()
    displaySums(n)

Printmain()

#PalindromicPrime

def isPrime(num):
    if num == 2 or num == 3:
        return True
    if num < 2 or num%2 == 0: 
        return False
    if num < 9: 
        return True
    if num%3 == 0: 
        return False
    r = int(num**0.5)
    f = 5
    while f <= r:
        if num%f == 0: 
            return False
        if num%(f+2) == 0: 
            return False
        f +=6
    return True    

def isPalindrome(num):
    reverse = str(num)[::-1]
    return num == int(reverse)

def Palmain():
    print()
    d = 0
    for i in range(2,31000):
        if isPrime(i):
            if isPalindrome(i):
                d+=1
                print(f'{i:^7}',end='')
                if d%10 == 0:
                    print()
        if d == 50:
            break

Palmain()

#Password

def checkPassword(x):
    char = len(x) > 9
    alnum = all([i.isalnum() for i in x])
    numeric = len([i.isnumeric() for i in x if i.isnumeric() == True]) > 2
    if all([char, alnum, numeric]):
        return True
    else:
        return False

def Passwordmain():
    password = input('\nEnter password: ')
    print(f'\nEntered password:\t{password}')
    if checkPassword(password):
        print(f'Judgment:\t\tValid Password')
    else:
        print(f'Judgment:\t\tInvalid Password')

Passwordmain()