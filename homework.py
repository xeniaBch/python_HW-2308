# task 1
print("Python " * 100)

# task2
a, b = map(int, input('Enter goods price ').split())
c, d = map(int, input('Enter how much you have paid ').split())
cash = (c * 100 + d) - (a * 100 + b)
e = cash // 100
f = cash % 100
print('You receive cash', e, 'euro', f, 'cents')

# Second level
# task 1
print('Enter your name please')
name = input()
print('Hello, ' + name + '!')

# task2
number = int(input('Please enter integer number '))
print('The next number for the number', number, 'is', number + 1, '.')
print('The previous number for the number', number, 'is', number - 1, '.')
