__author__ = "Neil"
__time__ = "2018/5/27 15:23"
from scapy.all import *

stars = lambda n: "*" * n

def print(packet):
    return "\n".join((
        stars(40) + "PACKET" + stars(40),
        "\n".join(packet.sprintf("{Raw:%Raw.load%}").split(r"\r\n")),
        stars(90)))

sniff(iface='at0',prn=GET_print, filter="tcp port 80")