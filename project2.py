import random
import string

pass_len = 12
charValue = string.ascii_letters + string.punctuation + string.digits

password = ""
for i in range(pass_len):
    password = password + random.choice(charValue)


print(password)

