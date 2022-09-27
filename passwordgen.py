import cgi
from operator import length_hint
import string, secrets

chrs = string.ascii_letters + string.digits + string.printable
nmbrs = string.digits

choose = input("Do you want to generate a password or a pin: ")
length = input("Choose your password/pin length: ")

password_in_chrs = ''.join(secrets.choice(chrs) for i in range(int(length)))
password_in_nmbrs = ''.join(secrets.choice(nmbrs) for i in range(int(length)))

if choose == "password":
    print(password_in_chrs)

if choose == "pin":
    print(password_in_nmbrs)