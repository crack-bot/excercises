#variables
# write a program that displays several numbers
# num1 = 4
# num2 = 6
# print(num1)
# print(num2)
# make a program that solve and shows the summation
# x = 50
# y = 20
# z = x+y
# print(z)
# x = 64 + 32
# print(x)
# strings
# write a program to print out ur fav celebrity name
# name = "katrina kappor"
# print(name)
# try to print the word lucky inside s
# s = "you are lucky"
# print(s[7:])
#try to print the day,month,year in the form today is 2/2/2026
# cal_time = "today is 2/2/2026"
# print(cal_time[9:])
# try the replace program
# s = "joy"
# p = s.replace("joy", "faith")
# print(p)
# find out if te find() is case sensitive
# p = "joy"
# s = p.find("y")# yes it is case sensitive
# print(s)

# user = input('title of a movie: ')
# y = user.find("thieves")
# print(y)

# join sting method
# name = "_"
# s = name.join(("j", "o", "y"))
# print(s)
# words = ["i", "am", "a", "baby", "girl", "for", "life"]
# sentence = " ".join(words)
# print(sentence)

#spilt
# a = "word! earth america canada"
# b = a.split("!")
# print(b)

# random numbers
# import random as r
# for i in range(3):
#     print(r.random())

#
# user = int(input("enter any number: "))
# if user == value:
#    print("valid number")
# else:
#     print("invalid number")
import random as r
numList = range(1, 100)
result = r.choices(numList, k=100)
print(result)
freq = 0
count = 0
index = 0

for i in range(1, 100):
    freq = result.count(i)
    print(f"{i}'s:  {freq}")

    if freq > count:
       count = freq
       index = i


mostFreq = result[index]
print(mostFreq)
print(" the number appeared ", count, "time in the list")









