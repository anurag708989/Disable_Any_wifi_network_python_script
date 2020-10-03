import scapy.all as scapy
import optparse



def arguments():
    parse = optparse.OptionParser()
    parse.add_option("-i","--ipaddress",dest="ipaddr",help="[+] Target ip or ip range ")
    (options,arguments) = parse.parse_args()
    if not options.ipaddr:
        parse.error("[+] Enter ip address  -i or --ipaddress")
    else:
        return options.ipaddr
def scan(ip):
    arp_request = scapy.ARP(pdst = ip) #send arp request that who has <target-ip> says <ip-fromsenderdevice >
    broadcast_request = scapy.Ether(dst = "ff:ff:ff:ff:ff:ff")#broadcast arp_request to all ips
    arp_broadcast = broadcast_request/arp_request #combining two variables into one we can see summary by print(arp_broadcast.summary())
    answered_list = scapy.srp(arp_broadcast , timeout = 1,verbose = False)[0]
    answered_dic_list = []#making a list of dictionary containing mac and ip
    for element in answered_list:
        demo_answer_dic = {"ip":element[1].psrc ,"mac": element[1].src}
        answered_dic_list.append(demo_answer_dic)

    return answered_dic_list


def main():
    ip_address = arguments()
    print(ip_address)
    network_list = scan(ip_address)
    print("Target IP:\t\t\tTarget Mac:")
    for element in network_list:
        print(element["ip"] + "\t\t\t" + element["mac"])

main()