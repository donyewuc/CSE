#Words

x = input('Enter a sentence: ')
y = x.split()
print('Entered String: ', x, '\n')
for num, i in enumerate(y,1):
    print('Word #{}:'.format(num), i)

# # SandClockAlternate

# stars = '* '
# space = ' '
# for i in range(9,0,-2):
#     print((9-i)*space + (i*stars))
# for i in range(3,10,2):
#     print((9-i)*space + (i*stars))

#SandClock

stars = '* '
space = ' '
for i in range(9,2,-2):
    for j in range(0,i):
        if j == 0:
            print((9-i)*space,end='')
        print(stars,end='')
    print()

for i in range(1,10,2):
    for j in range(0,i):
        if j == 0:
            print((9-i)*space,end='')
        print(stars,end='')
    print()

#Pattern

for i in range(6,0,-1):
    x = 1
    for j in range(0,i):
        if j == 0:
            print((12-2*i)*' ', end='')
        print(x, end=' ')
        x+=1
    print()

#PasswordTest

password = input('Enter your password: ')
req= [any(x.isupper() for x in password),any(x.islower() for x in password),
not all(x.isalnum() for x in password), len(password)>7,
any(x.isnumeric() for x in password)]
print('\nEntered password:\t', password)
if all(req):
    print('Verdict:\tValid Password')
else:
    print('Verdict:\tInvalid Password')

#LargestOccurenceCount

x = input('Enter positive integers separated by spaces (0 to quit): ')
y = [int(i) for i in x.split()]
num = []
for a in y:
    if a>0:
        num.append(a)
    elif a == 0 and num:
        print('\nValid inputs:\t', num)
        print('Largest value:\t', max(num))
        print('Occurrences:\t', num.count(max(num)), 'times')
        break