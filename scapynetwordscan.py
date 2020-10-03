import scapy.all as scapy
import optparse

def network_parse():
    parse = optparse.OptionParser()
    parse.add_option("--t","--targets",dest ="ipaddress",help="ip address or iprange")
    options,arguments = parse.parse_args()
    if not options.ipaddress:
        parse.error("[+] enter ip address or ip ranges for ex 192.168.0.1/24")
    else:
        return options.ipaddress
def scan(ip):
    arp_request = scapy.ARP(pdst = ip)
    #arp_request.show()
    #print(arp_request.summary())
    #scapy.ls(scapy.ARP()) #for listing options
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    #broadcast.show()
    #scapy.ls(scapy.Ether()) //for listing options for Ether such as mac destination
    arp_request_broadcast = broadcast/arp_request
    #arp_request_broadcast.show()
    answered_list= scapy.srp(arp_request_broadcast,timeout=1,verbose = False)[0]#it is somewhat similar to ping command so thats why used timeout option
    print("target ip \t\t|\t\t  mac address")
    answered_dic_list = []
    for i in answered_list:
        answered_dic = {"ip" : i[1].psrc ,"mac" : i[1].hwsrc}
        #print(i[1].psrc +"\t\t|\t\t"+ i[1].hwsrc )
        answered_dic_list.append(answered_dic)
    return answered_dic_list
def ansdict(answered_listdict):
    for element in answered_listdict:
        print(element["ip"] +"\t\t\t"+element["mac"])
def main():
    network_ips = network_parse()
    anweredlist_dict = scan(network_ips)
    ansdict(anweredlist_dict)
main()