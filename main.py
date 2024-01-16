"""
Task:

Write a Python function that takes in a single string as an argument, checks that it meets the criteria below and displays whether or not the string is a valid address.

assume that an email address must meet these criteria:

a: contain an @ symbol
b: contain atleat 1 .
c: have a lenght greater than 9 characters
"""


def email(email):
  if "@" in email:
    email = email.split("@")
    if "." in email[1]:
      print("Your email contains a . after the @ symbol")
      if len(email[0]) >= 8:
        print("Your email is longer than 8 characters")
        if "." in email[1]:
          print("Your email has a good format")
        else:
          print("Please have a '.' before the @ symbol ")
      else:
        print("Please make your email longer than 8 characters")
  else:
    print("Make sure you include the @ symbol")


print("email checker")

emailIn = input("Please enter your email address: ")

email(emailIn)
