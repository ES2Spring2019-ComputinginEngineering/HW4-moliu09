# HOMEWORK 4 --- ES2
# Caesar Cipher

# FILL THESE COMMENTS IN
#*****************************************
# YOUR NAME: Mo Liu
# NUMBER OF HOURS TO COMPLETE: ~2
# YOUR COLLABORATION STATEMENT(s): I worked alone on this assignment.
#
#
#*****************************************

# For this assignment you are going to implement a Caesar Cipher
# A Caesar cipher works by shifting every letter in the alphabet by a set amount.
# For example the string 'abc', with a shift of 1, would become 'bcd'
# For more information: https://en.wikipedia.org/wiki/Caesar_cipher

# Decode the following messages and say what shift you used to do so.
# 1. 'sn ad, nq mns sn ad: sgzs hr sgd ptdrshnm:'
# 2. 'sg2 wg am tojcfwhs qzogg'
# 3. 'nwcz akwzm ivl amdmv gmiza iow'

# ****************Answers****************
# 1.Message: to be, or not to be: that is the question:
#   Shift Amt: 1
# 2.Message: es2 is my favorite class
#   Shift Amt: 12
# 3.Message: four score and seven years ago
#   Shift Amt: 18

# message: string to be encrypt
# shift: integer number of letters to shift by.
#   You can assume we will only test with integers between 0 and 25
#   However, you can write your function to work with negatives and numbers greater than 25 if you wish

import math
import time
message = input("What is your message?\n")
shift = int(input("How much do you want to shift the message?\n"))

#encrypting function
def encrypt(message, shift):
    string = ""
    for i in message:
        t = ord(i)
        if t >= 65 and t <= 90:
            t = t + 32
        if t >= 97 and t <= 122:
            t = t + shift
            if t > 122:
                t = 96 + (t - 122)
        string = string + chr(t)
    return string
print(encrypt(message, shift))

#automated decrypting function
prompt = input("Would you like to decrypt a message?\n")
if prompt == "yes":
    m = input("What would you like to decrypt?\n")
    s = 1
    while s < 26:
        number = str(s)
        print("amount shifted = " + number + ": " + encrypt(m, s))
        s = s + 1