# # Class:	        	CSE 1321L
# # Section:		12         
# # Term:		Fall  
# # Instructor:	Kevin Markley 
# # Name:		Dexter Onyewuchi   
# # Assignment:	3

#PhoneBill

account = input('Enter your account number: ')
serv_code = input('Enter your service code (r or p): ')

if serv_code == 'r':
    serv_code = 'Regular'
    amount = 15
    minutes = int(input('Enter number of minutes of service use: '))
    if minutes > 50:
	    amount += (minutes-50)/2
    print('\n')
    print('Account number:', account)
    print('Service type:', serv_code)
    print('Total minutes:', minutes)
    print('Amount due:\t$',amount,'\n',sep='')

elif serv_code == 'p':
    serv_code = 'Premium'
    amount = 25
    daytime = int(input('Enter daytime minutes used: '))
    night = int(input('Enter nighttime minutes used: '))
    if daytime > 50:
	    amount += (daytime-50)/5
    if night > 100:
	    amount += (night-100)/10
    print('\nAccount number:', account)
    print('Service type:', serv_code)
    print('Daytime minutes:', daytime)
    print('Nighttime minutes:', night)
    print('Amount due:\t$', amount,'\n', sep='')
#FiveDigitPalindrome

num_list = []
number = int(input('Enter five-digit number: '))

if 11111 < number < 99999:
    while number != 0:
	    items = number % 10
	    number = number // 10
	    num_list.append(items)
    
    if num_list == num_list[::-1]:
        print('Valid 5-digit palindrome.\n')
    else:
        print('Invalid 5-digit palindrome.\n')
else:
    print('Invalid 5-digit number. Try again.\n')

#BestDeal

small_app = int(input('Enter weight of small apple box: '))
small_price = int(input('Enter price of small apple box: '))
large_app = int(input('Enter weight of large apple box: '))
large_price = int(input('Enter price of large apple box: '))
print('\nSmall box weight:', small_app, sep='\t')
print('Small box price:', small_price, sep='\t')
print('Large box weight:', large_app, sep='\t')
print('Large box price:', large_price, sep='\t')
if small_price/small_app > large_price/large_app:
    print('Judgment:\tThe large box is a better deal.\n')
elif small_price/small_app < large_price/large_app:
    print('Judgment:\tThe smaller box is a better deal.\n')
else:
    print('Judgment:\tBoth boxes are of the same value.\n')

#Circles

circle1 = [int(x) for x in input('Circle one coordinates and radius, separated by spaces: ').split()]
circle2 = [int(x) for x in input('Circle two coordinates and radius, separated by spaces: ').split()]
if len(circle1) != 3 or len(circle2) != 3:
    print('Please enter valid coordinates')
else:
    distance = ((circle1[0]-circle1[1])**2 + (circle2[0]-circle2[1])**2)**0.5
    center1 = circle1[0:2]
    center2 = circle2[0:2]
    print('\nCircle 1 center is:\t', center1)
    print('Circle 1 radius is:\t', circle1[2])
    print('Circle 2 center is:\t', center2)
    print('Circle 2 radius is:\t', circle2[2])
    if distance <= circle1[2]-circle2[2]:
        print('Judgment:\tCircle 2 is completely inside circle 1\n')
    elif distance > circle1[2]+circle2[2]:
        print('Judgment:\tCircle 2 is completely outside circle 1\n')
    else:
        print('Judgment:\tCircle 2 is overlapping with circle 1\n')

#IncomeTax

ann_income = int(input('Enter annual income: '))
tax_due = []
brackets = [[0, 50000, 5], [50000,200000,10],[200000,400000,15],
[400000,900000, 25],[900000,ann_income,35]]
for i in brackets:
    if i[0] < ann_income > i[1]:
        tax_due.append((i[1] - i[0]) * i[2]/100)
    elif i[0] < ann_income <= i[1]:
        tax_bracket = i[2]
        tax_due.append((ann_income - i[0]) * i[2]/100)
tax_due = sum(tax_due)
print('\nAnnual Income:\t', ann_income)
print('Tax Bracket:\t', str(tax_bracket)+'%')
print('Tax due amount:\t', tax_due)