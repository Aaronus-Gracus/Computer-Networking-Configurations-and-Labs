<h1>SSH Configuration on a Cisco Switch</h1>

 ### [YouTube Demonstration](https://youtu.be/7eJexJVCqJo)

<h2>Description</h2>
<p>In this lab, we’ll configure SSH on a Cisco switch for remote access. <strong>SSH (Secure Shell)</strong>&nbsp;is a cryptographic network protocol that ensures secure communication over an otherwise unsecured network. SSH was designed to replace insecure protocols like&nbsp;<strong>Telnet</strong>&nbsp;and other remote Unix shell protocols. You can follow along by downloading this <a href="https://1drv.ms/u/s!AgcNOlrpw6UkhPJ6sEofDveQaUs84g?e=t3uZIo" target="_blank" rel="noreferrer noopener">SSH Config Packet Tracer File</a> and opening it in&nbsp;<a href="https://skillsforall.com/resources/lab-downloads?courseLang=en-US" target="_blank" rel="noreferrer noopener">Cisco’s Free Packet Tracer Simulator</a>&nbsp;(<em>create a free account, enroll in one of the free courses and download the free software</em>).</p>
<br />


<h2>Languages and Programs Used</h2>

- <b>Cisco IOS</b> 
- <b>Cisco Packet Tracer</b>

<h2>Configuration walk-through:</h2>


Launch Packet Tracer:  <br/>
<img src="https://i.imgur.com/m0Oz6ps.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
First we need to connect Laptop1 to SW2 via a console cable: <br/>
<img src="https://i.imgur.com/m62TRiW.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
Now make the connection by clicking on Laptop1 and selecting the RS 232 port:  <br/>
<img src="https://i.imgur.com/ASC1oQU.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
Next click on SW2 and select the Console port:  <br/>
<img src="https://i.imgur.com/DpSq3mC.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
Click on Laptop1 and open the Desktop tab. From there open the Terminal connection:  <br/>
<img src="https://i.imgur.com/WMDTyF0.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
Leave the Terminal Configuration screen at their defaults and hit OK:  <br/>
<img src="https://i.imgur.com/XmQbJs2.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
If you’ve followed the previous steps correctly, you should see information about SW2:  <br/>
<img src="https://i.imgur.com/gPsNWCw.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
Click in the Terminal > press Enter > issue the enable command:  <br/>
<img src="https://i.imgur.com/7nqcpls.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
<br />
Now you’re ready to actually start the SSH configuration process. Use the below commands to correctly finish the lab:  <br/>
<img src="https://i.imgur.com/FStU5Nj.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
Test the configuration by connecting to SW2 via SSH from PC1 > Desktop > Command Prompt:  <br/>
<img src="https://i.imgur.com/hf0WOEw.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
In PC1s command prompt issue the following command:  <br/>
<br/>
ssh -l aaron 192.168.2.253 <br/>
<br/>
Enter the password: ccna <br/>
<img src="https://i.imgur.com/3RCxc19.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
And it works! You’re now remotely connected to SW2 over the Secure Shell protocol.  <br/>
</p>


