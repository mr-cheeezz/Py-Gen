import string
import secrets

chrs = string.ascii_letters + string.digits + string.punctuation
nmbrs = string.digits

def generate_password(length):
    password_in_chrs = ''.join(secrets.choice(chrs) for _ in range(length))
    return password_in_chrs

def generate_pin(length):
    password_in_nmbrs = ''.join(secrets.choice(nmbrs) for _ in range(length))
    return password_in_nmbrs
