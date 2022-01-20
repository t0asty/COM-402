import string
from hashlib import sha256
from itertools import permutations

sha_keys = set(
    [
"962642e330bd50792f647c1bf71895c5990be4ebf6b3ca60332befd732aed56c",
"8eef79d547f7a6d6a79329be3c7035f8e377f9e629cd9756936ec233969a45a3",
"e71067887d50ce854545afdd75d10fa80b841b98bb13272cf4be7ef0619c7dab",
"889a22781ef9b72b7689d9982bb3e22d31b6d7cc04db7571178a4496dc5ee128",
"6a16f9c6d9542a55c1560c65f25540672db6b6e121a6ba91ee5745dabdc4f208",
"2317603823a03507c8d7b2970229ee267d22192b8bb8760bb5fcef2cf4c09edf",
"c6c51f8a7319a7d0985babe1b6e4f5c329403d082e05e83d7b9d0bf55876ecdc",
"c01304fc36655dd37b5aa8ca96d34382ed9248b87650fffcd6ec70c9342bf451",
"cff39d9be689f0fc7725a43c3bdc7f5be012c840b9db9b547e6e3c454a076fc8",
"662ab7be194cee762494c6d725f29ef6321519035bfb15817e84342829728891"
    ]
)

hexdigits = set([x.lower() for x in list(string.hexdigits)])

def capit(stri):
    return stri.title()

def leetize_e(stri):
    return stri.replace('e', '3')

def leetize_o(stri):
    return stri.replace('o', '0')

def leetize_i(stri):
    return stri.replace('i', '1')

leetizers = set([leetize_e, leetize_i, leetize_o, capit])


with open('with_help3.txt', 'r', encoding='latin-1') as f:
    for pw in f.readlines():
        pw = pw.replace('\n','')
        for a in hexdigits:
            for b in hexdigits:
                pw_candidate = pw
                salt = a + b
                # print(salt)
                pw_candidate += str(salt)
                # print(pw_candidate)
                m = sha256()
                m.update(pw_candidate.encode())
                hashcode = m.hexdigest()
                if hashcode in sha_keys:
                    print(hashcode + ": " + pw_candidate)