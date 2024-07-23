<h1>GRE Tunnel Configuration</h1>

### YouTube Demonstration - coming soon!
<!-- ### [YouTube Demonstration](https://youtu.be/7eJexJVCqJo) -->

<h2>Description</h2>
<p>In this lab, I’ll show you how to configure a GRE tunnel between two routers. Then we will configure OSPF on the tunnel interfaces of R1 and R2, to allow PC1 in Office A to communicate with PC2 in Office B. You can follow along by downloading this&nbsp;<a href="https://1drv.ms/u/s!AgcNOlrpw6UkhPAb7v4KGKXRxWG0_g?e=h5oNJw" target="_blank" rel="noreferrer noopener">GRE Tunnels Packet Tracer File</a>&nbsp;and opening it in&nbsp;<a href="https://skillsforall.com/resources/lab-downloads?courseLang=en-US" target="_blank" rel="noreferrer noopener">Cisco’s Free Packet Tracer Simulator</a>&nbsp;(<em>create a free account, enroll in one of the free courses and download the free software</em>).</p>
<br />


<h2>Languages and Programs Used</h2>

- <b>Cisco IOS</b> 
- <b>Cisco Packet Tracer</b>

<h2>Configuration walk-through:</h2>

<p align="center">
Launch Cisco Packet Tracer: <br/>
<img src="https://i.imgur.com/ALXYSw5.png" height="80%" width="80%" alt="GRE Config Cisco Packet Tracer"/>
<br />

<b>R1</b>

To configure a GRE tunnel, we have to make a tunnel interface. This is not a physical interface of course, but a virtual interface, like a loopback interface:

R1(config)#interface tunnel 0

<p align="center">
<img src="https://i.imgur.com/qjRTEj2.png" height="70%" width="70%" alt="GRE Config Cisco Packet Tracer"/>
<br />

Okay, we’ve have created the tunnel interface.

Now we have to specify 3 more items to complete the GRE configuration:
- Tunnel Source
- Tunnel Destination
- IP address of the virtual tunnel itself

<b>Tunnel Source:</b> specify which physical interface on R1 will be used for the tunnel. We should use the interface connected to the service provider, which is g0/0/0 :

R1(config-if)#tunnel source g0/0/0

<b>Tunnel Destination:</b> specify the IP address of the other end of the tunnel, so R2. So, enter R2’s WAN interface’s IP, 200.0.0.2 :

R1(config-if)#tunnel destination 200.0.0.2

Virtual tunnel interface itself needs an IP address:

R1(config-if)#ip address 192.168.1.1 255.255.255.252

Okay, that’s all the configuration needed on R1. Below is what we just configured above on R1:
