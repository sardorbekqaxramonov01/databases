# import sqlite3

# connect = sqlite3.connect("words.db")

# cursor = connect.cursor()



# # connect.execute('''
# # CREATE TABLE WORDS_LIST(
# #          ENG TEXT NOT NULL,
# #          RU  TEXT NOT NULL,
# #          UZ  TEXT NOT NULL
# #         );
# #          ''')

# # ENG = input("Name: ")
# # RU = input("Company: ")
# # UZ = input("Email address: ")

# # connect.execute(f"INSERT INTO WORDS_LIST(ENG,RU,UZ) VALUES ('{ENG}', '{RU}', '{UZ}');")

# cursor.execute("SELECT * FROM WORDS_LIST")

# data = cursor.fetchall

# for i in data:
#     print(i)

# connect.commit()

# print("Done!")

# connect.close()







# import sqlite3

# connect = sqlite3.connect("words.db")

# cursor = connect.cursor()

# cursor.execute("SELECT * FROM personal_info")

# data = cursor.fetchall()

# for i in data:
#     print(i)

# connect.commit()

# print("Done!")

# connect.close()








import sqlite3
from deep_translator import GoogleTranslator

ENG = input("English word: ")

translated = GoogleTranslator(source='auto', target='uz').translate(ENG)
translate = GoogleTranslator(source='auto', target='ru').translate(ENG)

connect = sqlite3.connect("words.sqlite3")

cursor = connect.cursor()

# connect.execute('''
# CREATE TABLE WORDS_LIST(
#           ENG TEXT NOT NULL,
#           RU  TEXT NOT NULL,
#           UZ  TEXT NOT NULL
#         );
#           ''')


RU = translate
UZ = translated

connect.execute(f"INSERT INTO WORDS_LIST(ENG,RU,UZ) VALUES ('{ENG}', '{RU}', '{UZ}');")

# data = cursor.fetchall()

# for i in data:
#     print(i)

connect.commit()

print("Done!")

connect.close()





# import app

# data = app.full_data()

# counter = 0
# while counter < len(data):
#     print(f"ENG: {data[counter][0]}")
#     e = input("RU: ")
#     i = input("UZ: ")
#     if i == data[counter][2]:
#         print("Good")
#     elif e == data[counter][1]:
#         print("Good")
#     else:
#         with open("done.txt", "a") as f:
#             f.write(data[counter][0])
#             f.write("\n")
#             f.write(data[counter][1])
#             f.write("\n")
#             f.write(data[counter][2])
#             f.write("\n")
#     counter += 1