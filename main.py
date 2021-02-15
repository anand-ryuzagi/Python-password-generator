import string
import random
alphabet_string_lower = string.ascii_lowercase
list_lower = list(alphabet_string_lower)

alphabet_string_upper = string.ascii_uppercase
list_upper = list(alphabet_string_upper)

number = string.digits

special_characters = ['@','!','-','#','$','&']

pass_len = int(input("enter the password length you want: "))

s = []
s.extend(alphabet_string_upper)
s.extend(number)
s.extend(special_characters)
s.extend(alphabet_string_lower)

random.shuffle(s)
# print(s)

print("Your Password is: ")
print("".join(s[0:pass_len]))
