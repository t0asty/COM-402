#!/usr/bin/env python

import asyncio
import websockets
from hashlib import sha256
from os import urandom

EMAIL = "your.email@epfl.ch"
PASSWORD = "correct horse battery staple"
H = sha256
N = int("EEAF0AB9ADB38DD69C33F80AFA8FC5E86072618775FF3C0B9EA2314C9C256576D674DF7496EA81D3383B4813D692C6E0E0D5D8E250B98BE48E495C1D6089DAD15DC7D7B46154D6B6CE8EF4AD69B15D4982559B297BCF1885C529F566660E57EC68EDBC3C05726CC02FD4CBF4976EAA9AFD5138FE8376435B9FC61D2FC0EB06E3", 16)
g = 2

def randomInt(n_bytes):
    random_data = urandom(n_bytes)
    return int.from_bytes(random_data, byteorder='big')


async def main():
    async with websockets.connect("ws://127.0.0.1:5000/") as websocket:
        U = EMAIL
        U_utf8 = U.encode()
        await websocket.send(U_utf8)

        salt_utf8 = await websocket.recv()
        salt = int(salt_utf8, 16)
        a = randomInt(32)
        A = pow(g, a, N)
        A_utf8 = format(A, "x").encode()
        await websocket.send(A_utf8)

        B_utf8 = await websocket.recv()
        B = int(salt_utf8, 16)
        h = H()
        h.update(A_utf8)
        h.update(B_utf8.encode())
        u_utf8 = h.hexdigest()
        u = int(u_utf8, 16)
        h = H()
        h.update(U_utf8)
        h.update(":".encode())
        h.update(PASSWORD.encode())
        x_1 = h.hexdigest()
        h = H()
        h.update(salt_utf8.encode())
        h.update(x_1.encode())
        x_utf8 = h.hexdigest()
        x = int(x_utf8, 16)
        S = pow(B - pow(g, x), a + (u*x), N)
        S_utf8 = format(S, "x").encode()

        h = H()
        h.update(A_utf8)
        h.update(B_utf8.encode())
        h.update(S_utf8)
        res = h.hexdigest()
        print(res)
        await websocket.send(res.encode())


asyncio.run(main())

