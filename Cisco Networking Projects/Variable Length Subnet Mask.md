<h1>Variable Length Subnet Mask</h1>

### YouTube Demonstration - coming soon!
<!-- ### [YouTube Demonstration](https://youtu.be/7eJexJVCqJo) -->

<h2>Description</h2>
In the lab below, I’ve taken the 192.168.5.0 /24 network and broken it down into 5 smaller variable length subnets. Each subnet has the required number of host IP addresses. The network has been broken down as follows:
<br />
- LAN2 is the largest subnetwork which requires 64 host IP addresses and has been given a /25 subnet mask.
- LAN1 is the second largest subnetwork which needs only 45 host IP addresses and has been given a /26 subnet mask.
- I then continued to subnet LAN3 and LAN4.
- Finally, the point-to-point network between R1 and R2 only requires 2 host IP addresses and has been given a /30 subnet mask.

<h2>Languages and Programs Used</h2>

- <b>Cisco IOS</b> 
- <b>Cisco Packet Tracer</b>

<h2>Configuration walk-through:</h2>

<p align="center">
Launch Cisco Packet Tracer: <br/>
<img src="https://i.imgur.com/UbAkoIp.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
