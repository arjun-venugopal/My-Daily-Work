"1. Write a Python Program to print hollow diamond patterns?"
'''
* * * * * * * * 
* * *     * * * 
* *         * * 
*             * 
*             * 
* *         * * 
* * *     * * * 
* * * * * * * *
'''


for i in range(4, 0, -1):
    print("* " * i + "  " * (4 - i) * 2 + "* " * i)
for i in range(1, 4 + 1):
    print("* " * i + "  " * (4 - i) * 2 + "* " * i)



n = 4
for i in range (n, 0, -1):
    for j in range (i, 0, -1):
        print("* ", end="")
    for j in range (2 * (n - i)):
        print("  ", end="")
    for j in range (i, 0, -1):
        print("* ", end="")
    print()

for i in range (n):
    for j in range (i + 1):
        print("* ", end="")
    for j in range (2 * (n - i-1)):
        print("  ", end="")
    for j in range (i+1):
        print("* ", end="")
    print()


#---------------------------------------------------------------

'''
2. Write a Python program to generate and 
print a list of the first and last 5 elements where 
the values are square numbers between 1 and 30 (both included)?
'''

list = []
for i in range(1, 31):
    list.append(i**2)
print(list[:5])
print(list[-5:])


#---------------------------------------------------------------

"""
3. Write a Python program to convert a month name to a number of days.
 Sample Output:  Input the name of Month: February                                       
No. of days: 28/29 days
"""

month_name = input("Input the name of Month: ")

if month_name == "February":
    print("No. of days: 28/29 days")  
elif month_name in ("April", "June", "September", "November"):
    print("No. of days: 30 days")  
elif month_name in ("January", "March", "May", "July", "August", "October", "December"):
    print("No. of days: 31 days")  
else:
    print("Wrong month name") 


#---------------------------------------------------------------

"""
4. Write a Python program to print the alphabet pattern 'A' ? 5 Mark Each
Expected Output:

  ***                                                                   
 *   *                                                                  
 *   *                                                                  
 *****                                                                  
 *   *                                                                  
 *   *                                                                  
 *   *

"""

for i in range (7):
    for j in range (7):
        if ((j == 1 or j == 5) and (i not in [0])) or (i in [0,3] and 1<j<5) :
            print("* ", end="")
        else:
            print("  ", end="")
    print()


#---------------------------------------------------------------

"""
5. Python program to reverse each word in a sentence
"""

sentence = input("Input a sentence: ")
words = (sentence.split()[::-1])
reverse = " ".join(words)
print(reverse)


#---------------------------------------------------------------

"""
6. Write a Python program to find numbers between 100 and 400 (both included)
where each digit of a number is an even number. 
The numbers obtained should be printed in a comma-separated sequence.
"""

even = []
for i in range(100, 401):
    s = str(i)
    if (int(s[0]) % 2 == 0) and (int(s[1]) % 2 == 0) and (int(s[2]) % 2 == 0):
        even.append(s)
print(",".join(even))
        
    
#---------------------------------------------------------------

"""
7. Write a Python program that iterates the integers from 1 to 50. 
For multiples of three print "Fizz" instead of the number and for multiples of five print "Buzz".
For numbers that are multiples of three and five, print "FizzBuzz"?
"""

for i in range (1, 51):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)


#---------------------------------------------------------------

"""
8. Write a Python program to find the second smallest number in a list?
"""

list = [10, 20, 4, 45, 99]
list.sort()
print(list[1])

