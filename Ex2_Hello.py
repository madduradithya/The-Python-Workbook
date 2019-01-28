#Exercise 2: Hello
#Write a program that asks the user to enter his or her name. The program should
#respond with a message that says hello to the user, using his or her name.
nameoftheuser = input("Please enter your name: ")
if not nameoftheuser or nameoftheuser.isspace():
    print("No name was entered or spaces were entered")
else:
    print("Hello, " + nameoftheuser + "!")
