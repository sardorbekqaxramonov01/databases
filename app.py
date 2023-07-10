# my_list = [10,25,12,40,62,73]

# for i in my_list:
#     second_num = i % 10
#     first_num = int((i - second_num) / 10)

#     if (first_num + second_num) % 2 == 0:
#         print(i)





# n = int (input ("Enter a number: "))

# factorial = 1

# if n >= 1:

#     for i in range (1, n+1):

#                     factorial = factorial *i

# print ("Factorial of the given number is: ", factorial)








# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)

# number  = int(input("Enter a number: "))
# factorial_number = factorial(number)
# print("The factorial of", number, "is", factorial_number)







import sqlite3

connect = sqlite3.connect("words.sqlite3")
cursor = connect.cursor()

cursor.execute("SELECT * FROM WORDS_LIST")
data = cursor.fetchall()

def full_data():
    return data

connect.commit()

connect.close()