import hashlib

def password_decoder(door):
    password = ''
    count = 0
    while len(password) < 8:
        hash = 'XXXXX'
        while hash[0:5] != '00000':
            count += 1
            md5_hash = hashlib.md5()
            md5_hash.update((door + str(count)))
            hash = md5_hash.hexdigest()
        password = password + str(hash[5])
    return password

# print password_decoder('uqwqemis')

def second_password_decoder(door):
    password = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    count = 0
    while ' ' in password:
        hash = 'XXXXX'
        while hash[0:5] != '00000':
            count += 1
            md5_hash = hashlib.md5()
            md5_hash.update((door + str(count)))
            hash = md5_hash.hexdigest()
        if hash[5] in '01234567':
            pos = int(hash[5])
            if password[pos] == ' ':
                password[pos] = hash[6]
        print password
    password_str = ''
    for item in password:
        password_str += item
    return password_str

print second_password_decoder('uqwqemis')