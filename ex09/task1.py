import requests
import json
from phe import paillier

PRECISION = 2**(-16)
EXPONENT = -8

def query_pred(li):
    if len(li) != 10:
        raise ValueError
    pub_key, priv_key = paillier.generate_paillier_keypair(n_length=2048)
    encrypted = [pub_key.encrypt(x, precision=PRECISION).ciphertext() for x in li]
    response = requests.post('http://localhost:8000/prediction', json={'pub_key_n': pub_key.n, 'enc_feature_vector': encrypted})
    
    y_enc = response.json()['enc_prediction']

    encrypted = paillier.EncryptedNumber(pub_key, y_enc, EXPONENT)
    return priv_key.decrypt(encrypted)

print(query_pred([0.48555949, 0.29289251, 0.63463107,
                                  0.41933057, 0.78672205, 0.58910837,
                                  0.00739207, 0.31390802, 0.37037496,
                                  0.3375726 ]))

assert 2**(-16) > abs(query_pred([0.48555949, 0.29289251, 0.63463107,
                                  0.41933057, 0.78672205, 0.58910837,
                                  0.00739207, 0.31390802, 0.37037496,
                                  0.3375726 ]) - 0.44812144746653826)