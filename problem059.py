import sys

def verify_char(c):
    if c > 127:
        return False
    if c < 32:
        return False
    if c > 90 and c < 97:
        return False
    return True

def decrypt(data, key):
    resp = []

    for d1, d2, d3 in zip(data[0::3], data[1::3], data[2::3]):
        c1 = d1 ^ key[0]
        c2 = d2 ^ key[1]
        c3 = d3 ^ key[2]

        if verify_char(c1) and verify_char(c2) and verify_char(c3):
            resp.extend([c1, c2, c3])
        else:
            return None

    return resp

with open("p059_cipher.txt", 'r') as f:
    # Read file, remove newline
    row = f.readline().replace("\n","")
    
    # Split to list and convert to int
    data = [int(i) for i in row.split(",")]

    # Pad with two byte
    data.extend([0,0])

# Key is three low case chars
# 0x61 = a
# 0x7A = z
for k1 in range(0x61, 0x7B):
    for k2 in range(0x61, 0x7B):
        for k3 in range(0x61, 0x7B):
            decoded = decrypt(data, (k1, k2, k3))

            if decoded:
                sum = 0
                sys.stdout.write("Key: ") 
                print(k1, k2, k3)
                print("Cleartext:")
                # Remove padding
                for c in decoded[:-2]:
                    sys.stdout.write(chr(c))
                    sum += c
                print("\nASCII sum: " + str(sum))
                exit(0)

print(len(data))
