from scapy.all import *
def http_header(packet):
        http_packet=str(packet)
        print(packet)
sniff(iface='at0', prn=http_header, filter="tcp port 80")