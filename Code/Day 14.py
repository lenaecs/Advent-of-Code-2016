import hashlib

def password_decoder(salt):
    count = 0
    keys = 0
    hash_dict = {}
    for i in range(1002):
        md5_hash = hashlib.md5()
        md5_hash.update((salt + str(i)))
        hash = md5_hash.hexdigest()
        for j in range(2016):
            md5_hash = hashlib.md5()
            md5_hash.update(hash)
            hash = md5_hash.hexdigest()
        hash_dict[i] = hash
    while keys < 64:
        count += 1
        found_seq = False
        for char in range(len(hash_dict[count]) -2):
            hash = hash_dict[count]
            if hash[char] == hash[char + 1] and hash[char] == hash[char + 2] and found_seq == False:
                rep_char = hash[char]
                found_seq = True
                found_hash = False
                for next_hash in range(1000):
                    hash2 = hash_dict[count + next_hash + 1]
                    for char2 in range(len(hash2) - 4):
                        if (hash2[char2] == rep_char and hash2[char2 + 1] == rep_char and
                            hash2[char2 + 2] == rep_char and hash2[char2 + 3] == rep_char
                            and hash2[char2 + 4] == rep_char) and found_hash == False:
                            keys += 1
                            found_hash = True
        md5_hash = hashlib.md5()
        md5_hash.update((salt + str(count + 1001)))
        hash = md5_hash.hexdigest()
        for j in range(2016):
            md5_hash = hashlib.md5()
            md5_hash.update(hash)
            hash = md5_hash.hexdigest()
        hash_dict[count + 1001] = hash
    return count

print(password_decoder('yjdafjpo'))