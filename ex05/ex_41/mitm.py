from netfilterqueue import NetfilterQueue
from scapy.all import *

def print_and_accept(pkt):
    ip = str(IP(pkt.get_payload()))
    if 'pwd ---' in ip or 'cc ---' in ip:
        print(ip)
    pkt.accept()

nfqueue = NetfilterQueue()
nfqueue.bind(1, print_and_accept)
try:
    nfqueue.run()
except KeyboardInterrupt:
    print('')

nfqueue.unbind()