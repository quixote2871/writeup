hex_list = [(hex(i)[2:].zfill(2).upper()) for i in range(256)]

with open('encfile', 'r') as f:
    et = f.read()

plain_list = []
for i in range(0, len(et), 2):
    index = hex_list.index(et[i:i+2])
    hex_b = hex_list[(index-128)%len(hex_list)]
    plain_list.append(hex_b)

plain_list = bytes.fromhex(''.join(plain_list))

with open('flag.png', 'wb') as f:
    f.write(plain_list)
