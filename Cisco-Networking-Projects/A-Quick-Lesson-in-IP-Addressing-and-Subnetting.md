<h1>A Quick Lesson in IP Addressing and Subnetting</h1>
<p>&nbsp;</p>
<p>Are you able to&nbsp;architech the solution for the following network? Check out the answer at the bottom of the page!</p>
<p style="text-align: center;"><img src="https://infotechaaron.wordpress.com/wp-content/uploads/2024/03/image-3.png" alt="" width="80%" height="80%" /></p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<h2 class="wp-block-heading has-text-align-center has-large-font-size" style="text-transform: uppercase;">A Quick Refresher in Binary</h2>
<h3 class="wp-block-heading has-text-align-center has-small-font-size" style="text-transform: uppercase; text-align: left;"><em>it&rsquo;s all About powers of 2</em></h3>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p style="text-align: center;"><img src="https://infotechaaron.wordpress.com/wp-content/uploads/2023/11/image-96.png" alt="" width="547" height="272" /></p>
<p style="text-align: center;">&nbsp;</p>
<p style="text-align: center;">&nbsp;</p>
<p style="text-align: center;"><img src="https://infotechaaron.wordpress.com/wp-content/uploads/2023/11/image-94.png" alt="" width="80%" height="80%" /></p>
<div class="wp-block-file aligncenter" style="text-align: center;"><a id="wp-block-file--media-f6490e5e-2cf2-4788-8668-840cb57e376b" href="https://infotechaaron.wordpress.com/wp-content/uploads/2023/11/binaryconversions-powerof2-practice.pdf" target="_blank" rel="noreferrer noopener">BinaryConversions&ndash;Powerof2&ndash;practice</a><a class="wp-block-file__button wp-element-button" href="https://infotechaaron.wordpress.com/wp-content/uploads/2023/11/binaryconversions-powerof2-practice.pdf" download="">Download</a></div>
<div class="wp-block-spacer" style="height: 22px;">&nbsp;</div>
<div class="wp-block-spacer" style="height: 22px;">&nbsp;</div>
<div class="wp-block-spacer" style="height: 22px;">&nbsp;</div>
<div class="wp-block-spacer" style="height: 22px;">&nbsp;</div>
<div class="wp-block-spacer" style="height: 22px;">&nbsp;</div>


<p>&nbsp;</p>
<p>&nbsp;</p>
<h2>IPv4 Address Classes</h2>
<p style="text-align: center;"><img src="https://infotechaaron.wordpress.com/wp-content/uploads/2023/11/image-99.png" alt="" width="80%" height="80%" /></p>
<p>&nbsp;</p>
<p style="text-align: center;"><img src="https://infotechaaron.wordpress.com/wp-content/uploads/2023/11/image-100.png" alt="" width="80%" height="80%" /></p>
<div class="wp-block-spacer" style="height: 19px;">&nbsp;</div>
<div class="wp-block-spacer" style="height: 19px;">&nbsp;</div>
<div class="wp-block-spacer" style="height: 19px;">&nbsp;</div>
<div class="wp-block-spacer" style="height: 19px;">&nbsp;</div>
<h2><strong>This is your end goal</strong> (don&rsquo;t freak out)</h2>
<p class="has-text-align-center has-x-small-font-size">The end goal of subnetting is to break larger networks into smaller subnetworks</p>
<ul class="wp-block-list">
<li class="has-x-small-font-size">In the diagram, you&rsquo;ve been given a Class C IP address of 192.168.1.0/24</li>
<li class="has-x-small-font-size">Now that only gives you one lousy network, which these days can cause many issues at the enterprise level (network congestion, security vulnerabilities, etc&hellip;)</li>
<li class="has-x-small-font-size">So let&rsquo;s divide this one network into more networks! Borrow those Host bits and quit your wining. Make it happen, do this elementary math and be about your day my guy/girl!</li>
</ul>
<p>&nbsp;</p>
<p style="text-align: center;"><img src="https://infotechaaron.wordpress.com/wp-content/uploads/2023/11/image-36.png" alt="" width="80%" height="80%" /></p>
<div class="wp-block-spacer" style="height: 22px;">&nbsp;</div>
<div class="wp-block-spacer" style="height: 22px;">&nbsp;</div>
<div class="wp-block-spacer" style="height: 22px;">&nbsp;</div>
<div class="wp-block-spacer" style="height: 22px;">&nbsp;</div>
<div class="wp-block-spacer" style="height: 22px;">&nbsp;</div>
<h2 class="wp-block-heading has-text-align-center has-small-font-size" style="text-transform: uppercase;">Cheat Sheet to help you remember the Prefix Length, Addresses, Mask and Subnets:</h2>
<p class="has-text-align-center has-x-small-font-size">&nbsp;</p>
<p class="has-text-align-center has-x-small-font-size" style="text-align: center;">&nbsp;</p>
<p class="has-text-align-center has-x-small-font-size" style="text-align: center;"><img src="https://infotechaaron.wordpress.com/wp-content/uploads/2024/03/image-10.png" alt="" width="80%" height="80%" /></p>
<p class="has-text-align-center has-x-small-font-size">&nbsp;</p>
<p style="text-align: center;">Don&rsquo;t forget to subtract 2 from usable addresses for Network and Broadcast addresses.</p>
<p class="has-text-align-center has-x-small-font-size" style="text-align: center;">&nbsp;</p>
<p class="has-text-align-center has-x-small-font-size" style="text-align: center;">&nbsp;</p>
<p class="has-text-align-center has-x-small-font-size" style="text-align: center;">&nbsp;</p>
<p class="has-text-align-center has-x-small-font-size" style="text-align: center;">&nbsp;</p>
<p class="has-text-align-center has-x-small-font-size" style="text-align: center;">&nbsp;</p>
<h2>Here&rsquo;s a good practice question for you:</h2>
<p class="has-x-small-font-size"><strong>Question:</strong> <em>Your router needs to be assigned the first valid host address of the 2nd subnet on network 192.168.4.0/28. What address would you assign?</em></p>
<p style="font-size: 0.7rem;">To determine the first valid host address of the 2nd subnet on the network 192.168.4.0/28, we need to understand the subnetting process and analyze the current network.</p>
<p style="font-size: 0.7rem;">The network address 192.168.4.0/28 has a subnet mask of 255.255.255.240. It&rsquo;s a Class C with a /28 mask (meaning that 4 bits were borrowed from the Host part). This means that the network is divided into subnets of 16 IP addresses each (including the network and broadcast addresses).</p>
<p style="font-size: 0.8rem;">We determined the number of subnets by using the formula:</p>
<p style="font-size: 0.8rem;">&nbsp;</p>
<div class="wp-block-group has-global-padding is-layout-constrained wp-block-group-is-layout-constrained">
<p class="has-text-align-center" style="font-size: 0.8rem; text-align: center;">2<sup>x</sup> = # of subnets <kbd>(x = </kbd># of borrowed bits)</p>
<p class="has-text-align-center" style="font-size: 0.8rem; text-align: center;"><strong>2<sup>4</sup> = 16 subnets</strong></p>
</div>
<div class="wp-block-spacer" style="height: 23px;">&nbsp;</div>
<div class="wp-block-spacer" style="height: 23px;">&nbsp;</div>
<div class="wp-block-spacer" style="height: 23px;">&nbsp;</div>
<p style="font-size: 0.8rem;">We determined the number of addresses per subnets by using the formula <em>(note that we did not subtract 2 for the Network/Broadcast addresses)</em>:</p>
<div class="wp-block-group has-global-padding is-layout-constrained wp-block-group-is-layout-constrained">
<p class="has-text-align-center" style="font-size: 0.8rem; text-align: center;">2<sup>n</sup> = # of hosts <kbd>(n = </kbd># of host bits)</p>
<p class="has-text-align-center" style="font-size: 0.8rem; text-align: center;"><strong>2<sup>4</sup> = 16 usable host addresses</strong></p>
</div>
<p style="font-size: 0.7rem;">&nbsp;</p>
<p style="font-size: 0.7rem;">To find the second subnet, we need to calculate the subnet address. Since each subnet contains 16 IP addresses, the first subnet will be 192.168.4.0/28, the second subnet will be 192.168.4.16/28, the third subnet will be 192.168.4.32/28, and so on.</p>
<p style="font-size: 0.7rem;">&nbsp;</p>
<p style="font-size: 0.7rem;">The <em><strong>first valid host address of the second subnet will be the first address within that subnet</strong></em>, <span style="text-decoration: underline;">excluding the network address and the broadcast address</span>. In this case, the second subnet is 192.168.4.16/28, so the first valid host address would be 192.168.4.17</p>
<p style="font-size: 0.7rem;">&nbsp;</p>
<p class="has-x-small-font-size"><strong>Answer:</strong> Therefore, you would assign the IP address 192.168.4.17 to your router as the first valid host address of the second subnet on the network 192.168.4.0/28.</p>
<p class="has-x-small-font-size">&nbsp;</p>
<p class="has-x-small-font-size">&nbsp;</p>
<p class="has-x-small-font-size">&nbsp;</p>
<h2 class="has-x-small-font-size">Here's another cool Subnetting Chart that breaks down IPv4 Class C addresses in a visually appealing way (at least to me):</h2>
<p class="has-x-small-font-size" style="text-align: center;"><img src="https://infotechaaron.wordpress.com/wp-content/uploads/2024/03/image-11.png" alt="" width="80%" height="80%" /></p>
<p class="has-x-small-font-size" style="text-align: center;">&nbsp;</p>
<p class="has-x-small-font-size" style="text-align: center;">&nbsp;</p>
<p class="has-x-small-font-size" style="text-align: center;">&nbsp;</p>
<p class="has-x-small-font-size" style="text-align: center;">&nbsp;</p>
<p class="has-x-small-font-size" style="text-align: center;">&nbsp;</p>
<h2 class="has-x-small-font-size" style="text-align: left;">Answer to the Subnetting riddle at the top of this page:</h2>
<p class="has-x-small-font-size" style="text-align: center;">&nbsp;</p>
<p class="has-x-small-font-size" style="text-align: center;"><img src="https://infotechaaron.wordpress.com/wp-content/uploads/2024/03/image-4.png" alt="" width="80%" height="80%" /></p>
