from netfilterqueue import NetfilterQueue
from scapy.all import *

def print_and_accept(pkt):
    msg_bytes = pkt.get_payload()
    msg_bytes2 = [b for b in msg_bytes]
    ip = IP(pkt.get_payload())
    if ip.haslayer("Raw"):
        tcpPayload = ip["Raw"].load
        print(tcpPayload[0], tcpPayload[1])
        if tcpPayload[0] == 0x16 and tcpPayload[1] == 0x03:
            if (tcpPayload[46] == 0x00 and tcpPayload[47] == 0x35):
                msg_bytes2[113] = 0x2F
    pkt.set_payload(bytes(msg_bytes2))
    pkt.accept()

nfqueue = NetfilterQueue()
nfqueue.bind(1, print_and_accept)
try:
    nfqueue.run()
except KeyboardInterrupt:
    print('')

nfqueue.unbind()