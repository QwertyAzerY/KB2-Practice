def rotate(a):
    rotated = tuple(zip(*a[::-1])) # Python 3
    return rotated

def apply_cipher(cipher,chars):
    res = ''
    for i in range(4):
        for j in range(4):
            if cipher[i][j]==1:
                res=res+str(chars[i][j])
    return res

n = 4
m = 4
cipher = [0] * n
for i in range(n):
    cipher[i] = [0] * m

for i in range(4):
    a =input()
    for j in range(4):
        if a[j] == 'X':
            cipher[i][j]=1

result = ''

chars = [0] * n
for i in range(n):
    chars[i] = [0] * m

for i in range(4):  
    chars[i] = input()

for i in range(4):  
    result = result+apply_cipher(cipher,chars)
    cipher=rotate(cipher)


print(result)
