f = open('C:\Users\lenae.stoner\Dropbox\Advent of Code\December 2016\Input\Day 7.txt')
puzzle =[]

for line in f:
    puzzle.append(line.strip())

test = ['abba[mnop]qrst', 'abcd[bddb]xyyx', 'aaaa[qwer]tyui', 'ioxxoj[asdfgh]zxcvbn']
test2 = ['aba[bab]xyz', 'xyx[xyx]xyx', 'aaa[kek]eke', 'zazbz[bzb]cdb']

def tls_support(ips):
    ips_supported = 0
    for ip in ips:
        ip = ip.replace('[', ']')
        ip = ip.split(']')
        has_abba = False
        is_invalid = False
        for section in range(len(ip)):
            brackets = section%2
            segment = ip[section]
            for char in range(3, len(segment)):
                if segment[char-1] + segment[char] == segment[char-2] + segment[char-3] and segment[char] != segment[char-1]:
                    if brackets == 1:
                        is_invalid = True
                    else:
                        has_abba = True
        if has_abba == True and is_invalid == False:
            ips_supported += 1
    return ips_supported

print tls_support(test)
print tls_support(puzzle)

def ssl_support(ips):
    ssl_supported = 0
    for ip in ips:
        ip = ip.replace('[', ']')
        ip = ip.split(']')
        aba_list = []
        bab_list = []
        supported = False
        for section in range(len(ip)):
            brackets = section%2
            segment = ip[section]
            for char in range(2, len(segment)):
                if segment[char] == segment[char - 2] and segment[char] != segment[char - 1]:
                    if brackets == 0:
                        aba_list.append(segment[char - 2:char + 1])
                    else:
                        bab_list.append(segment[char - 2:char + 1])
        for aba in aba_list:
            if aba[1] + aba[0] + aba[1] in bab_list:
                supported = True
        if supported == True:
            ssl_supported += 1
    return ssl_supported

print ssl_support(test2)
print ssl_support(puzzle)
