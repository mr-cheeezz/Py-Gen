import random

lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "0123456789"
symbols = "@#$%^&*/\?"

letter_types = lower_case + upper_case + number + symbols
pass_length = "12" #change to length of password

password = "".join(random.sample(letter_types, pass_length))

print("Your password is:")