import sys
def encryptdecrypt(c, m):
    if c == 1:
        return ''.join(format(ord(char), '08b') for char in m)
    elif c == -1:
        return ''.join(chr(int(m[i:i+8], 2)) for i in range(0, len(m), 8))
    
x = int(input())
m = sys.stdin.read().strip()
result = encryptdecrypt(x, m)
print(result)