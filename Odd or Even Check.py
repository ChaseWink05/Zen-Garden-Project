'''1. Make an empty list and assign a variable to it
   2. Make a loop that asks the user to input 5 random numbers
   3. Add those numbers to the list
   4. Use Booleans operators to set a range for the numbers
   5. Set a range for the even numbers and then use the else function to print out its odd
   6. Use print function to print out the even numbers '''
'''odd = 0
even = 0
for i in range(5):
    x = int(input('What are the numbers?'))
    if x % 2 == 0:
        print('even')
        even = even+1
    else:
        print('odd')
        odd = odd+1
        break
print(even)
print(odd)'''

# Wrtie a program using the while loop that prompts the user to enter their password and keeps asking until the correcty password is enterned
'''password = 'HotDOG'
user_input =''
while user_input != password:
    user_input = input('Enter the password:')

print('Access granted')'''
# Modify the program to print 'wrong attempt try again if it dosen't match, prints the number of attemps too
'''password = 'HotDOG'
user_input =''
attempts = 0           #Assigning variables to use in the while loop
while user_input != password:           #Setting condition to make the while loop know when to stop
    attempts += 1
    user_input = input('Enter the password:')    #Adding to attempts every time the loop runs, the user inputs guessing the password
    print('You entered the wrong. Try again')


print('Access granted')                 #Print the statements
print('The number of attempts are', attempts)'''

# Find the smallest number in the list
'''numbers = [3, 4, 7, 1, 10]
smallest_number = numbers[0]
for num in numbers:
    if num < smallest_number:
        smallest_number = num
print('The smallest value in the list is', smallest_number)'''
# Find the average of numbers inputed
'''repetition = 0
sum = 0
while repetition < 5:
    num = float(input('Enter a number'))
    sum += num
    repetition += 1
average = sum/5
print('The average for the numbers inputed is', average)'''
# Write a python program that continues printing "Mighty Baynans" , till user types in 'stop'
'''print("Type stop to stop Mighty Bayans from displaying")
while True:
    user_input = input("Mighty Bayans")
    if user_input == 'stop':
        break'''


def factorial_recursive(n):
    n * factorial_recursive(n - 1)

factorial_recursive(5)


