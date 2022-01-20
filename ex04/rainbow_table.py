from hashlib import sha256

lookup_chars = {x: chr(x+97) for x in range(26)}
lookup_chars.update({x + 26: str(x) for x in range(10)})

table_rows = 1000
table_cols = 1000

def reduce(hash, col=0, pw_len=8, num_chars=36):
    num = int(hash, base=16) + col
    res = list()

    while len(res) < pw_len:
        res.append(lookup_chars[num % num_chars])
        num = num // num_chars

    return ''.join(res)

rainbow_table = dict()
for row in range(table_rows):
    p_0 = reduce(sha256(str(row).encode()).hexdigest())
    p_i = p_0
    for col in range(table_cols):
        p_i = reduce(sha256(p_i.encode()).hexdigest(), col=col)
    rainbow_table[sha256(p_i.encode()).hexdigest()] = p_0

print(rainbow_table)