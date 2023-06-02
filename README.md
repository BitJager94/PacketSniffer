# GitHub Documentation: Stream Sniffer

## Introduction

The Stream Sniffer is a Python script that allows you to intercept and analyze network packets. It can capture outgoing TCP and UDP packets, extract relevant information from them, and display details such as source IP, destination IP, source port, destination port, protocol, and packet summary. Additionally, it provides the ability to track and visualize the number of packets sent to each IP address.

## Prerequisites

Before using the Stream Sniffer, make sure you have the following dependencies installed:

- Python 3.x
- `requests` library
- `scapy` library
- `colorama` library
- `matplotlib` library
- `keyboard` library

You can install these dependencies using the following command:

```shell
pip install requests scapy colorama matplotlib keyboard
```

## Usage

To use the Stream Sniffer, follow the steps below:

1. Import the necessary libraries:

```python
import requests
from scapy.all import *
from colorama import Fore, Style
import matplotlib.pyplot as plt
import keyboard
```

2. Define the `StreamSniffer` class:

```python
class StreamSniffer:
    # ...
```

3. Implement the constructor method of the `StreamSniffer` class:

```python
    def __init__(self):
        # ...
```

4. Implement the `key_listener` method to listen for the "Esc" key press:

```python
    def key_listener(self, event):
        # ...
```

5. Implement the `draw_line_chart` method to visualize the packet counts:

```python
    def draw_line_chart(self):
        # ...
```

6. Implement the `intercept_request` method to intercept and analyze network packets:

```python
    def intercept_request(self, packet):
        # ...
```

7. Implement the `start_interception` method to start capturing packets:

```python
    def start_interception(self):
        # ...
```

8. Implement the `stop_interception` method to stop capturing packets and display the packet count chart:

```python
    def stop_interception(self):
        # ...
```

9. Handle exceptions and start the packet interception:

```python
try:
    interceptor = StreamSniffer()
    interceptor.start_interception()
except KeyboardInterrupt:
    pass
```

10. Run the script and press the "Esc" key to stop capturing packets and display the packet count chart.

## Example

Here's an example of how to use the Stream Sniffer:

```python
# Example usage

python PacketSniffer.py
```

## Conclusion

The Stream Sniffer script provides a convenient way to intercept and analyze network packets, extract relevant information, and visualize packet counts. You can customize the script further based on your specific requirements. Happy packet sniffing!