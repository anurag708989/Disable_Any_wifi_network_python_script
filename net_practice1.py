import scapy.all as scapy
import optparse

def arguments():
    parse = optparse.OptionParser()
    parse.add_option("-t","--targets",dest = "targetip",help = "Target ip")
    options,arguments = parse.parse_args()
    return options.targetip
def scan(ip):
    arp_request = scapy.ARP(pdst = ip)
    arp_broadcast =scapy.Ether(dst = "ff:ff:ff:ff:ff:ff")
    arp_and_broadcast = arp_broadcast/arp_request
    answered_list = scapy.srp(arp_and_broadcast,timeout = 2)[0]
    dict_list = []
    for element in answered_list:
        answered_dict =  {"ip":element[1].psrc,"mac":element[1].hwsrc}
        dict_list.append(answered_dict)
    return dict_list
def display_local_networks(answered_dictionary):
    for element in answered_dictionary:
        print(element["ip"] +"\t\t\t"+element["mac"])


answered_dict = scan(arguments())
display_local_networks(answered_dict)