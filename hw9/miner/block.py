from hashlib import sha256
import json
from base64 import b64encode, b64decode
from miner.block import Block

class Block:
    def __init__(self, data, previous):
        self.data = data
        self.previous_hash = previous

    def hash(self):
        m = sha256()
        m.update(self.data)
        m.update(self.previous_hash)
        return m.hexdigest()

    def encode(self):
        return json.dumps({'data': b64encode(self.data), 'previous': self.previous_hash.hex()}).encode('utf-8')

    @staticmethod
    def decode(b):
        param_dic = json.loads(b.decode('utf-8'))
        return Block(b64decode(param_dic['data']), bytes.fromhex(param_dic['previous']))