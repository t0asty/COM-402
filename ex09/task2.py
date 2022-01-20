import requests
import json
from phe import paillier
import numpy as np

PRECISION = 2**(-16)
EXPONENT = -8

def query_pred(li, keys):
    if len(li) != 10:
        raise ValueError
    pub_key, priv_key = keys
    encrypted = [pub_key.encrypt(x, precision=PRECISION).ciphertext() for x in li]
    response = requests.post('http://localhost:8000/prediction', json={'pub_key_n': pub_key.n, 'enc_feature_vector': encrypted})
    
    y_enc = response.json()['enc_prediction']

    encrypted = paillier.EncryptedNumber(pub_key, y_enc, EXPONENT)
    return priv_key.decrypt(encrypted)


# only create keys once
keys = paillier.generate_paillier_keypair()

print("Attacking bias") # pass only 0s
bias = query_pred([0]*10, keys)

weights = []
for i in range(10):
    print("Attacking weight {}".format(i), end="\r")
    # create vector [0,0,..,1,..,0,0]
    vector = np.zeros(10)
    vector[i] = 1
    # receive w_1 + b, deduce bias
    y = query_pred(vector, keys) - bias
    weights.append(y) # save the bias
# tada, you have the bias and weights!
print("\nWeights: {}\nbias: {}".format(weights, bias))
