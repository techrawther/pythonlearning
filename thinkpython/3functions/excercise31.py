# Write a function named right_justify that takes a string named s as a parameter
# and prints the string with enough leading spaces so that the last letter of the string
# is in column 70 of the display:

def right_justify(s):
     stringlength = (len(s))
     fillength = 70 - stringlength
     print(fillength)
     print(" " * fillength + s)

right_justify('something')