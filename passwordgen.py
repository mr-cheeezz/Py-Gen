import string, secrets

nmbr = "0123456789"

length = input("Choose your pin length: ")

pin = ''.join(secrets.choice(nmbr) for i in range(int(length)))

print('PIN: ' + pin)