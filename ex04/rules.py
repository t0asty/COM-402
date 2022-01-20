from hashlib import sha256
from itertools import permutations

sha_keys = set(
    [
"2e41f7133fd134335f566736c03cc02621a03a4d21954c3bec6a1f2807e87b8a",
"7987d2f5f930524a31e0716314c2710c89ae849b4e51a563be67c82344bcc8da",
"076f8c265a856303ac6ae57539140e88a3cbce2a2197b872ba6894132ccf92fb",
"b1ea522fd21e8fe242136488428b8604b83acea430d6fcd36159973f48b1102e",
"3992b888e772681224099302a5eeb6f8cf27530f7510f0cce1f26e79fdf8ea21",
"2326e90c0d2e7073d578976d120a4071f83ce6b7bc89c16ecb215d99b3d51a29b",
"69398301262810bdf542150a2c1b81ffe0e1282856058a0e26bda91512cfdc4",
"4fbee71939b9a46db36a3b0feb3d04668692fa020d30909c12b6e00c2d902c31",
"55c5a78379afce32da9d633ffe6a7a58fa06f9bbe66ba82af61838be400d624e",
"5106610b8ac6bc9da787a89bf577e888bce9c07e09e6caaf780d2288c3ec1f0c"
    ]
)

def capit(stri):
    return stri.title()

def leetize_e(stri):
    return stri.replace('e', '3')

def leetize_o(stri):
    return stri.replace('o', '0')

def leetize_i(stri):
    return stri.replace('i', '1')

leetizers = set([leetize_e, leetize_i, leetize_o, capit])


with open('with_help.txt', 'r', encoding='latin-1') as f:
    for pw in f.readlines():
        pw = pw.replace('\n','')
        for i in range(5):
            if i == 0:
                pw_candidate = pw
                m = sha256()
                m.update(pw_candidate.encode())
                hashcode = m.hexdigest()
                if hashcode in sha_keys:
                    print(hashcode + ": " + pw_candidate)
            else:
                for comb in permutations(leetizers, i):
                    comb = list(comb)
                    pw_candidate = pw
                    for f in comb:
                        pw_candidate = f(pw_candidate)
                        if pw_candidate == '1M0nj1tas':
                            print(pw_candidate)
                    m = sha256()
                    m.update(pw_candidate.encode())
                    hashcode = m.hexdigest()
                    if hashcode in sha_keys:
                        print(hashcode + ": " + pw_candidate)

