import requests
from scapy.all import *
from colorama import Fore, Style
import matplotlib.pyplot as plt
import keyboard



packet_counts = {}
key_pressed = False


class StreamSniffer:
    # def __init__(self, base_url):
    #     self.base_url = base_url

    def __init__(self):
        print('Press Esc To Stop And Show The Graph')
        keyboard.on_press(self.key_listener)

    def key_listener(self, event):
        if event.name == 'esc':
            global key_pressed
            key_pressed = True
    

    def draw_line_chart(self):
        global packet_counts

        ips = list(packet_counts.keys())
        counts = list(packet_counts.values())

        plt.figure(figsize=(10, 6))
        plt.plot(ips, counts, marker='o', linestyle='-', color='b')
        plt.xlabel('IP Address')
        plt.ylabel('Packet Count')
        plt.title('Number of Packets Sent to Each IP')
        plt.xticks(rotation='vertical')
        plt.tight_layout()
        plt.show()



    def intercept_request(self, packet):
       
        global packet_counts
        global key_pressed
    
        if packet.haslayer(TCP) and packet.haslayer(IP):
            # Extract the relevant fields from the packet
            src_ip = packet[IP].src
            dst_ip = packet[IP].dst
            src_port = packet[TCP].sport
            dst_port = packet[TCP].dport
            payload = str(packet[TCP].payload)


            # Check if it's an outgoing HTTP request
            if packet.haslayer(TCP):  # Check if packet is a TCP packet
                src_port = packet[TCP].sport
                dst_port = packet[TCP].dport
                print(f"Source IP: {src_ip}  -->  Destination IP: {dst_ip}")
                print(f"Source Port: {src_port}  -->  Destination Port: {dst_port}")
                print(f"Protocol: TCP")

                
            elif packet.haslayer(UDP):  # Check if packet is a UDP packet
                src_port = packet[UDP].sport
                dst_port = packet[UDP].dport
                print(f"Source IP: {src_ip}  -->  Destination IP: {dst_ip}")
                print(f"Source Port: {src_port}  -->  Destination Port: {dst_port}")
                print(f"Protocol: UDP")
            else:
                print(f"Source IP: {src_ip}  -->  Destination IP: {dst_ip}")
                print(f"Protocol: {protocol}")

            try:
                dst_hostname = socket.gethostbyaddr(dst_ip)[0]
            except socket.herror:
                dst_hostname = dst_ip

            if dst_hostname == "google.com":
                print(f"{Fore.RED}Packet Destination: {dst_ip}{Style.RESET_ALL}")
                print(f"destination url is: {dst_hostname}")
            else:
                print(f"{Fore.GREEN}Packet Destination: {dst_ip}")
                print(f"destination url is: {dst_hostname}")


            
            print(f"Packet Summary: {packet.summary()}")
            print("------------------------------------------")

            if dst_ip in packet_counts:
                packet_counts[dst_ip] += 1
            else:
                packet_counts[dst_ip] = 1
            

            if (key_pressed == True):
                # Stop packet capturing if ESC key is pressed
                print(f"{Fore.RED}Stopping packet capturing...")
                self.stop_interception()

        

    def start_interception(self):
        # Start sniffing packets
        # sniff(filter='tcp', prn=self.intercept_request)
        sniff(prn=self.intercept_request)

        # You can also specify additional parameters for sniffing, such as `iface` to select a network interface,
        # `count` to specify the number of packets to sniff, or `timeout` to set a duration for sniffing.
    def stop_interception(self):
        self.draw_line_chart()
        raise KeyboardInterrupt()
# Example usage

try:
    interceptor = StreamSniffer()
    interceptor.start_interception()
except KeyboardInterrupt:
    pass
