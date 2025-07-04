from scapy.all import *

def detect_deauth(packet):
    if packet.haslayer(Dot11Deauth):
        print("[ALERT] Deauthentication Attack Detected!")
        print(f"Source MAC: {packet.addr2} -> Destination MAC: {packet.addr1}")

interface = input("Enter your Network Interface > ")
print(f"[INFO] Monitoring on interface: {interface}")

sniff(iface=interface, prn=detect_deauth, store=0)
