import scapy.all as scapy
import optparse

def scan(ip):
    arp_request  = scapy.ARP(pdst = ip)
    mac_address = scapy.Ether(dst = "ff:ff:ff:ff:ff:ff")
    arp_and_mac = arp_request/mac_address
    answered_list= scapy.srp(arp_and_mac,timeout =1)[0]
    answered_dic_list = []
    for i in answered_list:
        print(i)

scan("192.168.0.1/24")

