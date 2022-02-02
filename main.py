print("-----1-----")
#Variables are pieces in you code to store and oganize data
#In python, varriables normally have one of a few types

#int variables hold integers
x = 5
y = 20
age = 11

#float variables hold decimal numbers
version = 2.1
temperature = 39.3 
score = 93.2

#str variables hold strings of characters
#IMPORTANT: when setting the value of a string, use quotes around the contents
#otherwise, you could cause an error, and your code may not function as intended
#for most purposes, a string is basically just a word
alphabet = "abcdefghijklmnopqrstuvwxyz"
name = "Walker"
day = "Monday"

# bool variables hold a boolean value, or more simply put, true or false
married = False
tired = True
correct = True

#One common way of accessing the data within a variable is to use the print() function
#To use print something, type print, followed by parenthesis containing what you
#would like to print
print(x)
print(name)
print(age)
print(tired)
#it is good programming ettiqite to name your variables something descriptive
# x is not that descriptive, but name is, this makes it easier to find sepcific variables in your code, and makes it esier to understand
print("-----2-----")
#run this code and look a the first three lines of the output
#You can see that each of  the print statements prints the contents of its corresponding variable

#you can use variables to set the value of other 
#variables
z = x + y
a = z / 2

print(z)
print(a)

#notice that changing the values of x and y dont change the value of z

x = 1
y = 2
print(z)

#you can perform concatonation to strings
#concatonation is a fancy way of saying you can add the words
#use the plus symbol (+)

n = name + day
print(n)

print("-----3-----")

#Finally, lists can be used to store multiple pieces of data in one "container"

#for lists, use [] brackets
#as we will see later, lists can be changed, added to, and subtracted from
classes = ["Physics", "Calculus", "Computer Science"]
grades = [99, 96.6, 87.5]

#lists have multiple elements as seen above, but when you print the list
print(classes)
#you can see that all of the parts are printed
#if you want a specific element, you need its index, or position in the list
#IMPORTANT: all lists start at 0!!!!!! meaning that the first element has an index of 0

#so to print each class as it's own, use [] again after the list name with the index inside

print(classes[0])
print(classes[1])
print(classes[2])

#As Im sure you noticed, I am just typing in the file to write the instructions, but how does the computer know when something is code or words?
#the answer is #
#placing a hashtag before a line of code tells the computer to skip it, this is called a comment
#commenting can be useful for explaining what your code is doing without having to be there next to someone reading it

#time for you to try some stuff yourself
print("\n-On your own-")

#create and integer variable called my_age and store your age in it


#Create a list of strings with your first and last name


#print your last name using the list above


#