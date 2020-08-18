import binascii
lines =[]

f = open("output.txt", "r")
for line in f.readlines():
    lines.append(line)
flag = ""
for i in range(len(lines[0]) - 1):
    ones = 0
    zeros = 0
    for j in range(256):
        if(lines[j][i] == '1'):
            ones += 1
        else :
            zeros += 1
    if(zeros > ones):
        flag += '1'
    else:
        flag += '0'
   


flag_int = int(flag, 2)


print(bytes.fromhex(hex(int(flag, 2))[2:]).decode())