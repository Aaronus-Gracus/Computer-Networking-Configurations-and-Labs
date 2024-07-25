<h1>HSRP Configuration on Cisco Routers</h1>

 ### YouTube Demonstration - Coming Soon!

<h2>Description</h2>
<p>In this lab, we’ll configure HSRP on two Cisco routers. <strong>HSRP (Hot Standby Router Protocol)</strong>&nbsp;is a&nbsp;<strong>Cisco proprietary redundancy protocol</strong>&nbsp;used to establish a fault-tolerant default gateway in computer networking. Basically, multiple routers share a Virtual IP address (VIP). If there is a failure in one router, the other immediately and transparently takes over as the default gateway. You can follow along by downloading this&nbsp;<a href="https://1drv.ms/u/s!AgcNOlrpw6UkhPAgi7XHsXnE_I-ghw?e=P0V6Sh" target="_blank" rel="noreferrer noopener">HSRP Packet Tracer File</a>&nbsp;and opening it in&nbsp;<a href="https://skillsforall.com/resources/lab-downloads?courseLang=en-US" target="_blank" rel="noreferrer noopener">Cisco’s Free Packet Tracer Simulator</a>&nbsp;(<em>create a free account, enroll in one of the free courses and download the free software</em>). </p>
<br />


<h2>Languages and Programs Used</h2>

- <b>Cisco IOS</b> 
- <b>Cisco Packet Tracer</b>

<h2>Configuration walk-through:</h2>
<br />
<br />
Launch Packet Tracer &nbsp;<a href="https://1drv.ms/u/s!AgcNOlrpw6UkhPAgi7XHsXnE_I-ghw?e=P0V6Sh" target="_blank" rel="noreferrer noopener">File</a>&nbsp  
<br/>
<p align="center">
<img src="https://i.imgur.com/nc557rX.png" height="80%" width="80%" alt="HSRP"/>
<br /></p>
<br />
<br />
<ol>
<li class="has-medium-font-size"><strong>Ping external server 8.8.8.8 from PC1/PC2.</strong>
<ul>
<li class="has-medium-font-size"><strong>What is the default gateway configured as?</strong></li>
</ul>
</li>
</ol>
<p align="center">
<br/>
<img src="https://i.imgur.com/BrVIYw8.png" height="80%" width="80%" alt="HSRP"/>
<br /></p>
<br />
<p class="has-x-small-font-size"><em>Currently both PC1 and PC2 are using 10.0.1.253 (R1) as their default gateway.<br>(8.8.8.8 is just a virtual loopback interface on R3)</em></p>
<br />
<br />
<br />
<br />
Let’s also run a traceroute from PC1 to 8.8.8.8 just to verify the ping does indeed pass through 10.0.1.253 (R1) on its way to 8.8.8.8:
<br />
<p align="center">
<br/>
<img src="https://i.imgur.com/4fv6nWK.png" height="80%" width="80%" alt="HSRP"/>
<br />
Yes it does pass through R1 on its way to 8.8.8.8 (R3).</p>
<br />
<br />
<br />
<ol start="2">
<li class="has-medium-font-size"><strong>Configure HSRPv2 on R1/R2.</strong>
<ul>
<li class="has-medium-font-size"><strong>Raise R1’s priority above the default </strong>(<em>making R1 the Active router</em>)</li>
<li class="has-medium-font-size"><strong>Lower R2’s priority below the default </strong>(<em>making R2 the Standby router</em>).</li>
<li class="has-medium-font-size"><strong>Enable preemption.</strong></li>
</ul>
</li>
</ol>


<p class="has-large-font-size"><strong><span style="text-decoration: underline">R1</span></strong></p>



<pre class="wp-block-preformatted">R1#<strong>conf t</strong><br>Enter configuration commands, one per line.  End with CNTL/Z.<br>R1(config)#<strong>int g0/0</strong><br>R1(config-if)#<strong>standby version 2</strong><br>R1(config-if)#<br>R1(config-if)#<strong>standby ?</strong><br>  &lt;0-4095&gt;  group number<br>  ip        Enable HSRP and set the virtual IP address<br>  ipv6      Enable HSRP IPv6<br>  preempt   Overthrow lower priority Active routers<br>  priority  Priority level<br>  timers    Hello and hold timers<br>  track     Priority Tracking<br>  version   HSRP version<br><br>R1(config-if)#<strong>standby 1 ip 10.0.1.254</strong><br>%HSRP-6-STATECHANGE: GigabitEthernet0/0 Grp 1 state Init -&gt; Init<br><br>R1(config-if)#<strong>standby 1 priority 200</strong><br>%HSRP-6-STATECHANGE: GigabitEthernet0/0 Grp 1 state Speak -&gt; Standby<br><br>%HSRP-6-STATECHANGE: GigabitEthernet0/0 Grp 1 state Standby -&gt; Active<br><br>R1(config-if)#<strong>standby 1 preempt</strong><br></pre>



<p class="has-x-small-font-size"><strong>NOTE:</strong> <em>The HSRP version number MUST match on BOTH routers involved in the HSRP configuration. If we were not to change R2 to HSRP version 2, we would receive &#8220;DUPLICATE ADDRESS 10.0.1.254&#8221; error messages. Both routers think they are the Active router if there is a version mismatch. In Packet Tracer, the HSRP version defaults to version 1. </em></p>



<div style="height:100px" aria-hidden="true" class="wp-block-spacer"></div>



<p class="has-large-font-size"><strong><span style="text-decoration: underline">R</span>2</strong></p>



<pre class="wp-block-preformatted">R2(config)#<strong>int g0/0</strong><br>R2(config-if)#<strong>standby version 2</strong><br>R2(config-if)#<strong>standby 1 ip 10.0.1.254</strong><br>R2(config-if)#<br>%HSRP-6-STATECHANGE: GigabitEthernet0/0 Grp 1 state Init -&gt; Init<br><br>R2(config-if)#<strong>standby 1 priority 50</strong><br>R2(config-if)#<br>%HSRP-6-STATECHANGE: GigabitEthernet0/0 Grp 1 state Speak -&gt; Standby</pre>



<div style="height:50px" aria-hidden="true" class="wp-block-spacer"></div>



<p class="has-x-small-font-size">So, we just configured R2 with the exact same configuration, but with the lower priority of 50. <br>This ensures R1 will be the Active router. Now let&#8217;s verify what we just configured:</p>



<pre class="wp-block-preformatted">R2(config-if)#<strong>do show standby</strong><br>GigabitEthernet0/0 - Group 1 (version 2)<br>  <mark style="background-color:#f3ef90" class="has-inline-color">State is Standby</mark><br>    5 state changes, last state change 00:02:14<br>  Virtual IP address is 10.0.1.254<br>  Active virtual MAC address is 0000.0C9F.F001<br>    Local virtual MAC address is 0000.0C9F.F001 (v2 default)<br>  Hello time 3 sec, hold time 10 sec<br>    Next hello sent in 1.818 secs<br>  Preemption disabled<br>  <mark style="background-color:#f3ef90" class="has-inline-color">Active router is 10.0.1.253</mark><br>  Standby router is local<br>  Priority 50 (configured 50)<br>  Group name is hsrp-Gig0/0-1 (default)</pre>



<div style="height:20px" aria-hidden="true" class="wp-block-spacer"></div>



<p style="font-size:clamp(0.875rem, 0.875rem + ((1vw - 0.2rem) * 0.042), 0.9rem);"><em><strong>Notice the highlights above:</strong><br> &#8211; R2 is the Standby router<br> &#8211; The Active router is 10.0.1.253 (R1)</em></p>



<div style="height:100px" aria-hidden="true" class="wp-block-spacer"></div>



<ol start="3">
<li class="has-medium-font-size"><strong>Configure the VIP as the default gateway of PC1/PC2.</strong>
<ul>
<li class="has-medium-font-size"><strong>Ping 8.8.8.8 from the PCs. Check the PCs&#8217; ARP table.</strong></li>



<li class="has-medium-font-size"><strong>What MAC address is mapped to the VIP?</strong></li>
</ul>
</li>
</ol>



<p>Click on both PCs &gt; Config Tab &gt; In the Default Gateway enter 10.0.1.254</p>


<br />
<p align="center">
<br/>
<img src="https://i.imgur.com/aTcaH0T.png" height="80%" width="80%" alt="HSRP"/>
<br /></p>
<br />
<br />



<div style="height:100px" aria-hidden="true" class="wp-block-spacer"></div>



<p class="has-x-small-font-size">Now ping 8.8.8.8 from one of the PCs:</p>



<br />
<p align="center">
<br/>
<img src="https://i.imgur.com/jdCHkx2.png" height="80%" width="80%" alt="HSRP"/>
<br /></p>
<p class="has-x-small-font-size"><em>The ping works. Now check the PCs arp table with the <strong>arp -a</strong> command. <br>Notice the HSRP version 2 virtual MAC address highlighted in blue.</em></p>



<div style="height:50px" aria-hidden="true" class="wp-block-spacer"></div>



<div style="height:0px" aria-hidden="true" class="wp-block-spacer"></div>



<p class="has-x-small-font-size">Next issue a traceroute to 8.8.8.8 and notice that the first hop is NOT the virtual gateway by R1s G0/0 interface. <br>The traceroute tool is useful to verify that the correct Active router is being used:</p>




<br />
<p align="center">
<br/>
<img src="https://i.imgur.com/rsePgQm.png" height="80%" width="80%" alt="HSRP"/>
<br /></p>
<br />
<br />



<div style="height:100px" aria-hidden="true" class="wp-block-spacer"></div>



<ol start="4">
<li class="has-medium-font-size"><strong>Turn off R1 (save the config first!).</strong>
<ul>
<li class="has-medium-font-size"><strong>Ping from PC1 to 8.8.8.8 again.</strong></li>



<li class="has-medium-font-size"><strong>Is R2 used as the default gateway?</strong></li>
</ul>
</li>
</ol>



<p class="has-x-small-font-size">Go to R1 and save the configuration using the <strong>write</strong> command from privileged exec mode:</p>


<br />
<p align="center">
<br/>
<img src="https://i.imgur.com/aI8wPjs.png" height="80%" width="80%" alt="HSRP"/>
<br /></p>
<br />
<br />



<p class="has-vivid-red-color has-text-color has-link-color has-x-small-font-size wp-elements-1f165b5ef9fc56c22f4db0060e2d3046"><em><strong>Make sure you save the config before restarting R1, because all of the configuration we&#8217;ve done will be erased!</strong></em></p>



<div style="height:40px" aria-hidden="true" class="wp-block-spacer"></div>



<p class="has-x-small-font-size">Press the Power button in R1s Physical Tab:</p>




<br />
<p align="center">
<br/>
<img src="https://i.imgur.com/8Qf8HrR.png" height="80%" width="80%" alt="HSRP"/>
<br /></p>
<br />
<br />



<div style="height:53px" aria-hidden="true" class="wp-block-spacer"></div>



<p class="has-x-small-font-size">Ping from PC1 to 8.8.8.8 again, followed by a traceroute:</p>




<br />
<p align="center">
<br/>
<img src="https://i.imgur.com/XvHdMxx.png" height="80%" width="80%" alt="HSRP"/>
<br /></p>


<p class="has-x-small-font-size">The ping still works to R3s loopback interface 8.8.8.8 and the traceroute shows that R2 has taken over the responsibility of Default Gateway (Active router).</p>



<div style="height:95px" aria-hidden="true" class="wp-block-spacer"></div>



<ol start="5">
<li class="has-medium-font-size"><strong>Turn on R1 again.</strong>
<ul>
<li class="has-medium-font-size"><strong>Ping from PC1 to 8.8.8.8 again.</strong></li>



<li class="has-medium-font-size"><strong>Does R1 become the active router again?</strong></li>
</ul>
</li>
</ol>



<br />
<p align="center">
<br/>
<img src="https://i.imgur.com/d2rsXyX.png" height="80%" width="80%" alt="HSRP"/>
<br /></p>
<br />
<br />


<div style="height:53px" aria-hidden="true" class="wp-block-spacer"></div>



<p class="has-x-small-font-size">Ping from PC1 to 8.8.8.8 again, followed by a traceroute:</p>



<br />
<p align="center">
<br/>
<img src="https://i.imgur.com/HRB02YR.png" width="80%" alt="HSRP"/>
<br /></p>




<p class="has-x-small-font-size">As shown above in the traceroute, when R1 comes back online it takes back the Active router role and is the Default Gateway again. <strong>How is this so?</strong> <br>Because earlier we gave it a higher priority than R2 and we enabled preemption:</p>



<p class="has-courier-prime-font-family">R1(config-if)#<strong>standby 1 priority 200</strong><br>R1(config-if)#<strong>standby 1 preempt</strong></p>



<div style="height:24px" aria-hidden="true" class="wp-block-spacer"></div>



<ol class="has-x-small-font-size">
<li><strong>Purpose of Preemption</strong>:
<ul>
<li><strong>HSRP preemption</strong> allows a standby router with a <strong>higher priority</strong> to <strong>immediately become the active router</strong> in an HSRP group.</li>



<li>By default, when the active router goes down, the standby router with the <strong>highest priority</strong> takes over as the active router.<br></li>
</ul>
</li>



<li><strong>How It Works</strong>:
<ul>
<li>When a router with a <strong>higher priority</strong> becomes available, it sends a <strong>“Coup” message</strong> to the network.</li>



<li>The <strong>lower-priority active router</strong> receives this message and transitions to the <strong>“Speak” state</strong>.</li>



<li>The active router then sends a <strong>“resign” message</strong>, signaling its readiness to relinquish the active role.</li>



<li>The router with higher priority assumes the active role immediately.</li>
</ul>
</li>
</ol>
