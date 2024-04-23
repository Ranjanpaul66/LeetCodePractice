def compress(s):
    n = len(s)
    new_s = ''
    count = 1
    for i in range(n-1):
        if s[i] == s[i+1]:
            count +=1
        else:
            new_s = new_s + s[i] + str(count)
            count = 1
    return new_s

compress("aabbccaaaafffeiii")
# result = a2b2c2a4f3e1i3