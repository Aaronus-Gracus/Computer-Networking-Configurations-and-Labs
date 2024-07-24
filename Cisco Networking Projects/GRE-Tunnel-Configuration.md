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



<div style="height:40px" aria-hidden="true" class="wp-block-spacer"></div>



<figure data-wp-context="{&quot;uploadedSrc&quot;:&quot;https:\/\/aaronguild.net\/wp-content\/uploads\/2024\/03\/image-45.png&quot;,&quot;figureClassNames&quot;:&quot;wp-block-image aligncenter size-full is-resized&quot;,&quot;figureStyles&quot;:null,&quot;imgClassNames&quot;:&quot;wp-image-3509&quot;,&quot;imgStyles&quot;:&quot;width:843px;height:auto&quot;,&quot;targetWidth&quot;:1051,&quot;targetHeight&quot;:660,&quot;scaleAttr&quot;:false,&quot;ariaLabel&quot;:&quot;Enlarge image&quot;,&quot;alt&quot;:&quot;&quot;}" data-wp-interactive="core/image" class="wp-block-image aligncenter size-full is-resized wp-lightbox-container"><img decoding="async" width="1051" height="660" data-wp-init="callbacks.setButtonStyles" data-wp-on--click="actions.showLightbox" data-wp-on--load="callbacks.setButtonStyles" data-wp-on-window--resize="callbacks.setButtonStyles" src="https://aaronguild.net/wp-content/uploads/2024/03/image-45.png" alt="" class="wp-image-3509" style="width:843px;height:auto" srcset="https://aaronguild.net/wp-content/uploads/2024/03/image-45.png 1051w, https://aaronguild.net/wp-content/uploads/2024/03/image-45-300x188.png 300w, https://aaronguild.net/wp-content/uploads/2024/03/image-45-1024x643.png 1024w, https://aaronguild.net/wp-content/uploads/2024/03/image-45-768x482.png 768w" sizes="(max-width: 1051px) 100vw, 1051px" /><button
			class="lightbox-trigger"
			type="button"
			aria-haspopup="dialog"
			aria-label="Enlarge image"
			data-wp-init="callbacks.initTriggerButton"
			data-wp-on--click="actions.showLightbox"
			data-wp-style--right="context.imageButtonRight"
			data-wp-style--top="context.imageButtonTop"
		>
			<svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" fill="none" viewBox="0 0 12 12">
				<path fill="#fff" d="M2 0a2 2 0 0 0-2 2v2h1.5V2a.5.5 0 0 1 .5-.5h2V0H2Zm2 10.5H2a.5.5 0 0 1-.5-.5V8H0v2a2 2 0 0 0 2 2h2v-1.5ZM8 12v-1.5h2a.5.5 0 0 0 .5-.5V8H12v2a2 2 0 0 1-2 2H8Zm2-12a2 2 0 0 1 2 2v2h-1.5V2a.5.5 0 0 0-.5-.5H8V0h2Z" />
			</svg>
		</button></figure>



<div style="height:100px" aria-hidden="true" class="wp-block-spacer"></div>



<p class="has-large-font-size"><strong><u>R1</u></strong></p>



<p class="has-x-small-font-size">To configure a GRE tunnel, we have to make a tunnel interface. This is not a physical interface of course, but a virtual interface, like a loopback interface:</p>



<p class="has-courier-prime-font-family">R1(config)#interface tunnel 0</p>



<figure class="wp-block-image size-full is-resized"><img decoding="async" width="850" height="563" src="https://aaronguild.net/wp-content/uploads/2024/03/image-46.png" alt="" class="wp-image-3512" style="width:568px;height:auto" srcset="https://aaronguild.net/wp-content/uploads/2024/03/image-46.png 850w, https://aaronguild.net/wp-content/uploads/2024/03/image-46-300x199.png 300w, https://aaronguild.net/wp-content/uploads/2024/03/image-46-768x509.png 768w" sizes="(max-width: 850px) 100vw, 850px" /></figure>



<p class="has-x-small-font-size">Okay, we&#8217;ve have created the tunnel interface.</p>



<p class="has-x-small-font-size">Now we have to specify 3 more items to complete the GRE configuration:</p>



<ol style="margin-bottom:0;margin-left:0" class="is-style-checkmark-list">
<li class="has-x-small-font-size"><em>Tunnel Source</em></li>



<li class="has-x-small-font-size"><em>Tunnel Destination</em></li>



<li class="has-x-small-font-size" style="margin-bottom:var(--wp--preset--spacing--60)"><em>IP address of the virtual tunnel itself</em></li>
</ol>



<p class="has-x-small-font-size"><span style="text-decoration: underline"><strong>Tunnel Source</strong></span>: specify which physical interface on R1 will be used for the tunnel. We should use the interface connected to the service provider, which is g0/0/0 :</p>



<p class="has-text-align-left has-courier-prime-font-family" style="margin-bottom:var(--wp--preset--spacing--60)">R1(config-if)#tunnel source g0/0/0</p>



<p class="has-x-small-font-size"><span style="text-decoration: underline">Tunnel Destination</span>: specify the IP address of the other end of the tunnel, so R2. So, enter R2&#8217;s WAN interface&#8217;s IP, 200.0.0.2 :</p>



<p class="has-text-align-left has-courier-prime-font-family" style="margin-bottom:var(--wp--preset--spacing--60)">R1(config-if)#tunnel destination 200.0.0.2</p>



<p class="has-x-small-font-size"><span style="text-decoration: underline">Virtual tunnel interface itself needs an IP address</span>:</p>



<p class="has-text-align-left has-courier-prime-font-family">R1(config-if)#ip address 192.168.1.1 255.255.255.252</p>



<div style="height:20px" aria-hidden="true" class="wp-block-spacer"></div>



<p class="has-x-small-font-size">Okay, that&#8217;s all the configuration needed on R1. Below is what we just configured above on R1:</p>



<figure class="wp-block-image size-full is-resized"><img loading="lazy" decoding="async" width="833" height="95" src="https://aaronguild.net/wp-content/uploads/2024/03/image-47.png" alt="" class="wp-image-3517" style="width:471px;height:auto" srcset="https://aaronguild.net/wp-content/uploads/2024/03/image-47.png 833w, https://aaronguild.net/wp-content/uploads/2024/03/image-47-300x34.png 300w, https://aaronguild.net/wp-content/uploads/2024/03/image-47-768x88.png 768w" sizes="(max-width: 833px) 100vw, 833px" /></figure>



<div style="height:25px" aria-hidden="true" class="wp-block-spacer"></div>



<p class="has-x-small-font-size">Let’s verify the virtual tunnel interface has been created:</p>



<figure class="wp-block-image size-full is-resized"><img loading="lazy" decoding="async" width="966" height="223" src="https://aaronguild.net/wp-content/uploads/2024/03/image-48.png" alt="" class="wp-image-3518" style="width:544px;height:auto" srcset="https://aaronguild.net/wp-content/uploads/2024/03/image-48.png 966w, https://aaronguild.net/wp-content/uploads/2024/03/image-48-300x69.png 300w, https://aaronguild.net/wp-content/uploads/2024/03/image-48-768x177.png 768w" sizes="(max-width: 966px) 100vw, 966px" /><figcaption class="wp-element-caption"><sub>Yes, there it is. It shows that the interface is in an up/down status. Why down? We’ll investigate shortly.</sub></figcaption></figure>



<p class="has-x-small-font-size">Let’s move on to R2 and configure the other side of the tunnel.</p>



<div style="height:25px" aria-hidden="true" class="wp-block-spacer"></div>



<p class="has-large-font-size"><strong><u>R2</u></strong></p>



<p class="has-x-small-font-size">Create the virtual tunnel Interface:</p>



<p class="has-courier-prime-font-family" style="margin-bottom:var(--wp--preset--spacing--60)">R2(config)#int tunnel 0</p>



<p class="has-x-small-font-size">Tunnel source (just like on R1, it will be g0/0/0):</p>



<p class="has-courier-prime-font-family" style="margin-bottom:var(--wp--preset--spacing--60)">R2(config-if)#tunnel source g0/0/0</p>



<p class="has-x-small-font-size">Tunnel destination (this time it will be the IP address of R1&#8217;s WAN interface, 100.0.0.2):</p>



<p class="has-courier-prime-font-family" style="margin-bottom:var(--wp--preset--spacing--60)">R2(config-if)#tunnel destination 100.0.0.2</p>



<p class="has-x-small-font-size">Finally, the IP address on the tunnel:</p>



<p class="has-courier-prime-font-family" style="margin-right:0;margin-bottom:var(--wp--preset--spacing--60);margin-left:0">R2(config-if)#ip address 192.168.1.2 255.255.255.252</p>



<p class="has-x-small-font-size">Let’s verify the virtual tunnel interface has been created:</p>



<p class="has-courier-prime-font-family">R2(config-if)#do show ip int br</p>



<figure class="wp-block-image size-full is-resized"><img loading="lazy" decoding="async" width="963" height="555" src="https://aaronguild.net/wp-content/uploads/2024/03/image-49.png" alt="" class="wp-image-3523" style="width:621px;height:auto" srcset="https://aaronguild.net/wp-content/uploads/2024/03/image-49.png 963w, https://aaronguild.net/wp-content/uploads/2024/03/image-49-300x173.png 300w, https://aaronguild.net/wp-content/uploads/2024/03/image-49-768x443.png 768w" sizes="(max-width: 963px) 100vw, 963px" /><figcaption class="wp-element-caption"><sub>Above is what we just configured on R2</sub></figcaption></figure>



<p class="has-x-small-font-size">Above, we see the tunnel interface is also showing an up/down status even though we’ve configured both sides. Why is that? Let me show you by issuing:</p>



<p class="has-courier-prime-font-family">R2(config-if)#do show ip route</p>



<figure class="wp-block-image size-full is-resized"><img loading="lazy" decoding="async" width="953" height="456" src="https://aaronguild.net/wp-content/uploads/2024/03/image-50.png" alt="" class="wp-image-3526" style="width:640px;height:auto" srcset="https://aaronguild.net/wp-content/uploads/2024/03/image-50.png 953w, https://aaronguild.net/wp-content/uploads/2024/03/image-50-300x144.png 300w, https://aaronguild.net/wp-content/uploads/2024/03/image-50-768x367.png 768w" sizes="(max-width: 953px) 100vw, 953px" /></figure>



<p class="has-x-small-font-size">As you can see, So R2 doesn&#8217;t have a connected route for its tunnel interface of course, because the interface is still down.<br>It has connected routes for its physical interfaces, but we&#8217;re missing a critical route.<br>R2 doesn&#8217;t know how to reach the IP address we specified as the tunnel destination, 100.0.0.2.<br>If R2 doesn&#8217;t know how to get to 100.0.0.2, it can&#8217;t build a GRE tunnel to 100.0.0.2.</p>



<p class="has-x-small-font-size">Let&#8217;s fix that:</p>



<p class="has-courier-prime-font-family" style="margin-bottom:var(--wp--preset--spacing--60)">R2(config-if)#exit</p>



<p class="has-x-small-font-size">Then I&#8217;ll just configure a default route:</p>



<p class="has-courier-prime-font-family" style="margin-bottom:var(--wp--preset--spacing--60)">R2(config)#ip route, 0.0.0.0 0.0.0.0 200.0.0.1</p>



<p class="has-x-small-font-size">After we enter a default route which goes to 100.0.0.2, the tunnel interface comes up.</p>



<p class="has-x-small-font-size">Let&#8217;s verify with:</p>



<p class="has-courier-prime-font-family">R2(config)#do show ip route</p>



<p class="has-x-small-font-size">Now we have the connected route for the tunnel in the route table:</p>



<figure class="wp-block-image size-full is-resized"><img loading="lazy" decoding="async" width="980" height="722" src="https://aaronguild.net/wp-content/uploads/2024/03/image-51.png" alt="" class="wp-image-3530" style="width:584px;height:auto" srcset="https://aaronguild.net/wp-content/uploads/2024/03/image-51.png 980w, https://aaronguild.net/wp-content/uploads/2024/03/image-51-300x221.png 300w, https://aaronguild.net/wp-content/uploads/2024/03/image-51-768x566.png 768w" sizes="(max-width: 980px) 100vw, 980px" /></figure>



<div style="height:25px" aria-hidden="true" class="wp-block-spacer"></div>



<p class="has-x-small-font-size">Let&#8217;s try to ping the R1 side:</p>



<figure data-wp-context="{&quot;uploadedSrc&quot;:&quot;https:\/\/aaronguild.net\/wp-content\/uploads\/2024\/03\/image-52.png&quot;,&quot;figureClassNames&quot;:&quot;wp-block-image size-full is-resized&quot;,&quot;figureStyles&quot;:null,&quot;imgClassNames&quot;:&quot;wp-image-3532&quot;,&quot;imgStyles&quot;:&quot;width:544px;height:auto&quot;,&quot;targetWidth&quot;:872,&quot;targetHeight&quot;:166,&quot;scaleAttr&quot;:false,&quot;ariaLabel&quot;:&quot;Enlarge image&quot;,&quot;alt&quot;:&quot;&quot;}" data-wp-interactive="core/image" class="wp-block-image size-full is-resized wp-lightbox-container"><img loading="lazy" decoding="async" width="872" height="166" data-wp-init="callbacks.setButtonStyles" data-wp-on--click="actions.showLightbox" data-wp-on--load="callbacks.setButtonStyles" data-wp-on-window--resize="callbacks.setButtonStyles" src="https://aaronguild.net/wp-content/uploads/2024/03/image-52.png" alt="" class="wp-image-3532" style="width:544px;height:auto" srcset="https://aaronguild.net/wp-content/uploads/2024/03/image-52.png 872w, https://aaronguild.net/wp-content/uploads/2024/03/image-52-300x57.png 300w, https://aaronguild.net/wp-content/uploads/2024/03/image-52-768x146.png 768w" sizes="(max-width: 872px) 100vw, 872px" /><button
			class="lightbox-trigger"
			type="button"
			aria-haspopup="dialog"
			aria-label="Enlarge image"
			data-wp-init="callbacks.initTriggerButton"
			data-wp-on--click="actions.showLightbox"
			data-wp-style--right="context.imageButtonRight"
			data-wp-style--top="context.imageButtonTop"
		>
			<svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" fill="none" viewBox="0 0 12 12">
				<path fill="#fff" d="M2 0a2 2 0 0 0-2 2v2h1.5V2a.5.5 0 0 1 .5-.5h2V0H2Zm2 10.5H2a.5.5 0 0 1-.5-.5V8H0v2a2 2 0 0 0 2 2h2v-1.5ZM8 12v-1.5h2a.5.5 0 0 0 .5-.5V8H12v2a2 2 0 0 1-2 2H8Zm2-12a2 2 0 0 1 2 2v2h-1.5V2a.5.5 0 0 0-.5-.5H8V0h2Z" />
			</svg>
		</button><figcaption class="wp-element-caption"><sub>The ping still isn&#8217;t working even though the interface is up and we have a route.<br>The reason for that is that we also have to configure a route on R1 to 200.0.0.2</sub></figcaption></figure>



<div style="height:39px" aria-hidden="true" class="wp-block-spacer"></div>



<p class="has-large-font-size"><strong><u>R1</u></strong></p>



<p class="has-x-small-font-size">Let&#8217;s check the routing table on R1:</p>



<figure data-wp-context="{&quot;uploadedSrc&quot;:&quot;https:\/\/aaronguild.net\/wp-content\/uploads\/2024\/03\/image-53.png&quot;,&quot;figureClassNames&quot;:&quot;wp-block-image size-full is-resized&quot;,&quot;figureStyles&quot;:null,&quot;imgClassNames&quot;:&quot;wp-image-3536&quot;,&quot;imgStyles&quot;:&quot;width:658px;height:auto&quot;,&quot;targetWidth&quot;:952,&quot;targetHeight&quot;:466,&quot;scaleAttr&quot;:false,&quot;ariaLabel&quot;:&quot;Enlarge image&quot;,&quot;alt&quot;:&quot;&quot;}" data-wp-interactive="core/image" class="wp-block-image size-full is-resized wp-lightbox-container"><img loading="lazy" decoding="async" width="952" height="466" data-wp-init="callbacks.setButtonStyles" data-wp-on--click="actions.showLightbox" data-wp-on--load="callbacks.setButtonStyles" data-wp-on-window--resize="callbacks.setButtonStyles" src="https://aaronguild.net/wp-content/uploads/2024/03/image-53.png" alt="" class="wp-image-3536" style="width:658px;height:auto" srcset="https://aaronguild.net/wp-content/uploads/2024/03/image-53.png 952w, https://aaronguild.net/wp-content/uploads/2024/03/image-53-300x147.png 300w, https://aaronguild.net/wp-content/uploads/2024/03/image-53-768x376.png 768w" sizes="(max-width: 952px) 100vw, 952px" /><button
			class="lightbox-trigger"
			type="button"
			aria-haspopup="dialog"
			aria-label="Enlarge image"
			data-wp-init="callbacks.initTriggerButton"
			data-wp-on--click="actions.showLightbox"
			data-wp-style--right="context.imageButtonRight"
			data-wp-style--top="context.imageButtonTop"
		>
			<svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" fill="none" viewBox="0 0 12 12">
				<path fill="#fff" d="M2 0a2 2 0 0 0-2 2v2h1.5V2a.5.5 0 0 1 .5-.5h2V0H2Zm2 10.5H2a.5.5 0 0 1-.5-.5V8H0v2a2 2 0 0 0 2 2h2v-1.5ZM8 12v-1.5h2a.5.5 0 0 0 .5-.5V8H12v2a2 2 0 0 1-2 2H8Zm2-12a2 2 0 0 1 2 2v2h-1.5V2a.5.5 0 0 0-.5-.5H8V0h2Z" />
			</svg>
		</button><figcaption class="wp-element-caption"><sub>As you can see, there’s only connected routes for its physical interfaces, so it doesn&#8217;t know how to get to the tunnel destination 200.0.0.2</sub></figcaption></figure>



<p class="has-x-small-font-size">Let’s give it a default route as well:</p>



<figure data-wp-context="{&quot;uploadedSrc&quot;:&quot;https:\/\/aaronguild.net\/wp-content\/uploads\/2024\/03\/image-54.png&quot;,&quot;figureClassNames&quot;:&quot;wp-block-image size-full is-resized&quot;,&quot;figureStyles&quot;:null,&quot;imgClassNames&quot;:&quot;wp-image-3538&quot;,&quot;imgStyles&quot;:&quot;width:597px;height:auto&quot;,&quot;targetWidth&quot;:966,&quot;targetHeight&quot;:316,&quot;scaleAttr&quot;:false,&quot;ariaLabel&quot;:&quot;Enlarge image&quot;,&quot;alt&quot;:&quot;&quot;}" data-wp-interactive="core/image" class="wp-block-image size-full is-resized wp-lightbox-container"><img loading="lazy" decoding="async" width="966" height="316" data-wp-init="callbacks.setButtonStyles" data-wp-on--click="actions.showLightbox" data-wp-on--load="callbacks.setButtonStyles" data-wp-on-window--resize="callbacks.setButtonStyles" src="https://aaronguild.net/wp-content/uploads/2024/03/image-54.png" alt="" class="wp-image-3538" style="width:597px;height:auto" srcset="https://aaronguild.net/wp-content/uploads/2024/03/image-54.png 966w, https://aaronguild.net/wp-content/uploads/2024/03/image-54-300x98.png 300w, https://aaronguild.net/wp-content/uploads/2024/03/image-54-768x251.png 768w" sizes="(max-width: 966px) 100vw, 966px" /><button
			class="lightbox-trigger"
			type="button"
			aria-haspopup="dialog"
			aria-label="Enlarge image"
			data-wp-init="callbacks.initTriggerButton"
			data-wp-on--click="actions.showLightbox"
			data-wp-style--right="context.imageButtonRight"
			data-wp-style--top="context.imageButtonTop"
		>
			<svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" fill="none" viewBox="0 0 12 12">
				<path fill="#fff" d="M2 0a2 2 0 0 0-2 2v2h1.5V2a.5.5 0 0 1 .5-.5h2V0H2Zm2 10.5H2a.5.5 0 0 1-.5-.5V8H0v2a2 2 0 0 0 2 2h2v-1.5ZM8 12v-1.5h2a.5.5 0 0 0 .5-.5V8H12v2a2 2 0 0 1-2 2H8Zm2-12a2 2 0 0 1 2 2v2h-1.5V2a.5.5 0 0 0-.5-.5H8V0h2Z" />
			</svg>
		</button><figcaption class="wp-element-caption"><sub>As usual, the first few pings might fail because the ARP process is a bit slow in Packet Tracer. But after ARP completes, they will succeed.</sub></figcaption></figure>



<div style="height:25px" aria-hidden="true" class="wp-block-spacer"></div>



<p class="has-x-small-font-size">So, although R1 and R2 aren&#8217;t directly connected, they will behave as if they are directly connected through the GRE tunnel.</p>



<p class="has-x-small-font-size">Let’s first look at a ping from R1 to R2 over the GRE tunnel in Simulation mode:</p>



<figure data-wp-context="{&quot;uploadedSrc&quot;:&quot;https:\/\/aaronguild.net\/wp-content\/uploads\/2024\/03\/image-58.png&quot;,&quot;figureClassNames&quot;:&quot;wp-block-image size-full is-resized&quot;,&quot;figureStyles&quot;:null,&quot;imgClassNames&quot;:&quot;wp-image-3545&quot;,&quot;imgStyles&quot;:&quot;width:801px;height:auto&quot;,&quot;targetWidth&quot;:935,&quot;targetHeight&quot;:770,&quot;scaleAttr&quot;:false,&quot;ariaLabel&quot;:&quot;Enlarge image&quot;,&quot;alt&quot;:&quot;&quot;}" data-wp-interactive="core/image" class="wp-block-image size-full is-resized wp-lightbox-container"><img loading="lazy" decoding="async" width="935" height="770" data-wp-init="callbacks.setButtonStyles" data-wp-on--click="actions.showLightbox" data-wp-on--load="callbacks.setButtonStyles" data-wp-on-window--resize="callbacks.setButtonStyles" src="https://aaronguild.net/wp-content/uploads/2024/03/image-58.png" alt="" class="wp-image-3545" style="width:801px;height:auto" srcset="https://aaronguild.net/wp-content/uploads/2024/03/image-58.png 935w, https://aaronguild.net/wp-content/uploads/2024/03/image-58-300x247.png 300w, https://aaronguild.net/wp-content/uploads/2024/03/image-58-768x632.png 768w" sizes="(max-width: 935px) 100vw, 935px" /><button
			class="lightbox-trigger"
			type="button"
			aria-haspopup="dialog"
			aria-label="Enlarge image"
			data-wp-init="callbacks.initTriggerButton"
			data-wp-on--click="actions.showLightbox"
			data-wp-style--right="context.imageButtonRight"
			data-wp-style--top="context.imageButtonTop"
		>
			<svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" fill="none" viewBox="0 0 12 12">
				<path fill="#fff" d="M2 0a2 2 0 0 0-2 2v2h1.5V2a.5.5 0 0 1 .5-.5h2V0H2Zm2 10.5H2a.5.5 0 0 1-.5-.5V8H0v2a2 2 0 0 0 2 2h2v-1.5ZM8 12v-1.5h2a.5.5 0 0 0 .5-.5V8H12v2a2 2 0 0 1-2 2H8Zm2-12a2 2 0 0 1 2 2v2h-1.5V2a.5.5 0 0 0-.5-.5H8V0h2Z" />
			</svg>
		</button></figure>



<div style="height:25px" aria-hidden="true" class="wp-block-spacer"></div>



<p class="has-x-small-font-size">From R1 in Simulation issue the following ping:</p>



<p class="has-courier-prime-font-family">R1(config)#do ping 192.168.1.2</p>



<p class="has-x-small-font-size">Then click on ICMP under Type in the right Simulation Panel to view the packet:</p>



<figure data-wp-context="{&quot;uploadedSrc&quot;:&quot;https:\/\/aaronguild.net\/wp-content\/uploads\/2024\/03\/image-57.png&quot;,&quot;figureClassNames&quot;:&quot;wp-block-image size-full is-resized&quot;,&quot;figureStyles&quot;:null,&quot;imgClassNames&quot;:&quot;wp-image-3544&quot;,&quot;imgStyles&quot;:&quot;width:815px;height:auto&quot;,&quot;targetWidth&quot;:1125,&quot;targetHeight&quot;:915,&quot;scaleAttr&quot;:false,&quot;ariaLabel&quot;:&quot;Enlarge image&quot;,&quot;alt&quot;:&quot;&quot;}" data-wp-interactive="core/image" class="wp-block-image size-full is-resized wp-lightbox-container"><img loading="lazy" decoding="async" width="1125" height="915" data-wp-init="callbacks.setButtonStyles" data-wp-on--click="actions.showLightbox" data-wp-on--load="callbacks.setButtonStyles" data-wp-on-window--resize="callbacks.setButtonStyles" src="https://aaronguild.net/wp-content/uploads/2024/03/image-57.png" alt="" class="wp-image-3544" style="width:815px;height:auto" srcset="https://aaronguild.net/wp-content/uploads/2024/03/image-57.png 1125w, https://aaronguild.net/wp-content/uploads/2024/03/image-57-300x244.png 300w, https://aaronguild.net/wp-content/uploads/2024/03/image-57-1024x833.png 1024w, https://aaronguild.net/wp-content/uploads/2024/03/image-57-768x625.png 768w" sizes="(max-width: 1125px) 100vw, 1125px" /><button
			class="lightbox-trigger"
			type="button"
			aria-haspopup="dialog"
			aria-label="Enlarge image"
			data-wp-init="callbacks.initTriggerButton"
			data-wp-on--click="actions.showLightbox"
			data-wp-style--right="context.imageButtonRight"
			data-wp-style--top="context.imageButtonTop"
		>
			<svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" fill="none" viewBox="0 0 12 12">
				<path fill="#fff" d="M2 0a2 2 0 0 0-2 2v2h1.5V2a.5.5 0 0 1 .5-.5h2V0H2Zm2 10.5H2a.5.5 0 0 1-.5-.5V8H0v2a2 2 0 0 0 2 2h2v-1.5ZM8 12v-1.5h2a.5.5 0 0 0 .5-.5V8H12v2a2 2 0 0 1-2 2H8Zm2-12a2 2 0 0 1 2 2v2h-1.5V2a.5.5 0 0 0-.5-.5H8V0h2Z" />
			</svg>
		</button></figure>



<div style="height:25px" aria-hidden="true" class="wp-block-spacer"></div>



<p class="has-x-small-font-size">Then a popup window will appear labeled PDU Information at Device: R1. Select Outbound PDU Details tab:</p>



<figure data-wp-context="{&quot;uploadedSrc&quot;:&quot;https:\/\/aaronguild.net\/wp-content\/uploads\/2024\/03\/image-59.png&quot;,&quot;figureClassNames&quot;:&quot;wp-block-image size-full is-resized&quot;,&quot;figureStyles&quot;:null,&quot;imgClassNames&quot;:&quot;wp-image-3547&quot;,&quot;imgStyles&quot;:&quot;width:663px;height:auto&quot;,&quot;targetWidth&quot;:847,&quot;targetHeight&quot;:847,&quot;scaleAttr&quot;:false,&quot;ariaLabel&quot;:&quot;Enlarge image&quot;,&quot;alt&quot;:&quot;&quot;}" data-wp-interactive="core/image" class="wp-block-image size-full is-resized wp-lightbox-container"><img loading="lazy" decoding="async" width="847" height="847" data-wp-init="callbacks.setButtonStyles" data-wp-on--click="actions.showLightbox" data-wp-on--load="callbacks.setButtonStyles" data-wp-on-window--resize="callbacks.setButtonStyles" src="https://aaronguild.net/wp-content/uploads/2024/03/image-59.png" alt="" class="wp-image-3547" style="width:663px;height:auto" srcset="https://aaronguild.net/wp-content/uploads/2024/03/image-59.png 847w, https://aaronguild.net/wp-content/uploads/2024/03/image-59-300x300.png 300w, https://aaronguild.net/wp-content/uploads/2024/03/image-59-150x150.png 150w, https://aaronguild.net/wp-content/uploads/2024/03/image-59-768x768.png 768w" sizes="(max-width: 847px) 100vw, 847px" /><button
			class="lightbox-trigger"
			type="button"
			aria-haspopup="dialog"
			aria-label="Enlarge image"
			data-wp-init="callbacks.initTriggerButton"
			data-wp-on--click="actions.showLightbox"
			data-wp-style--right="context.imageButtonRight"
			data-wp-style--top="context.imageButtonTop"
		>
			<svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" fill="none" viewBox="0 0 12 12">
				<path fill="#fff" d="M2 0a2 2 0 0 0-2 2v2h1.5V2a.5.5 0 0 1 .5-.5h2V0H2Zm2 10.5H2a.5.5 0 0 1-.5-.5V8H0v2a2 2 0 0 0 2 2h2v-1.5ZM8 12v-1.5h2a.5.5 0 0 0 .5-.5V8H12v2a2 2 0 0 1-2 2H8Zm2-12a2 2 0 0 1 2 2v2h-1.5V2a.5.5 0 0 0-.5-.5H8V0h2Z" />
			</svg>
		</button></figure>



<div style="height:25px" aria-hidden="true" class="wp-block-spacer"></div>



<p class="has-x-small-font-size">Scroll to bottom where we will see the ICMP message (the PING):</p>



<figure data-wp-context="{&quot;uploadedSrc&quot;:&quot;https:\/\/aaronguild.net\/wp-content\/uploads\/2024\/03\/image-60.png&quot;,&quot;figureClassNames&quot;:&quot;wp-block-image size-full is-resized&quot;,&quot;figureStyles&quot;:null,&quot;imgClassNames&quot;:&quot;wp-image-3548&quot;,&quot;imgStyles&quot;:&quot;width:656px;height:auto&quot;,&quot;targetWidth&quot;:833,&quot;targetHeight&quot;:298,&quot;scaleAttr&quot;:false,&quot;ariaLabel&quot;:&quot;Enlarge image&quot;,&quot;alt&quot;:&quot;&quot;}" data-wp-interactive="core/image" class="wp-block-image size-full is-resized wp-lightbox-container"><img loading="lazy" decoding="async" width="833" height="298" data-wp-init="callbacks.setButtonStyles" data-wp-on--click="actions.showLightbox" data-wp-on--load="callbacks.setButtonStyles" data-wp-on-window--resize="callbacks.setButtonStyles" src="https://aaronguild.net/wp-content/uploads/2024/03/image-60.png" alt="" class="wp-image-3548" style="width:656px;height:auto" srcset="https://aaronguild.net/wp-content/uploads/2024/03/image-60.png 833w, https://aaronguild.net/wp-content/uploads/2024/03/image-60-300x107.png 300w, https://aaronguild.net/wp-content/uploads/2024/03/image-60-768x275.png 768w" sizes="(max-width: 833px) 100vw, 833px" /><button
			class="lightbox-trigger"
			type="button"
			aria-haspopup="dialog"
			aria-label="Enlarge image"
			data-wp-init="callbacks.initTriggerButton"
			data-wp-on--click="actions.showLightbox"
			data-wp-style--right="context.imageButtonRight"
			data-wp-style--top="context.imageButtonTop"
		>
			<svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" fill="none" viewBox="0 0 12 12">
				<path fill="#fff" d="M2 0a2 2 0 0 0-2 2v2h1.5V2a.5.5 0 0 1 .5-.5h2V0H2Zm2 10.5H2a.5.5 0 0 1-.5-.5V8H0v2a2 2 0 0 0 2 2h2v-1.5ZM8 12v-1.5h2a.5.5 0 0 0 .5-.5V8H12v2a2 2 0 0 1-2 2H8Zm2-12a2 2 0 0 1 2 2v2h-1.5V2a.5.5 0 0 0-.5-.5H8V0h2Z" />
			</svg>
		</button></figure>



<div style="height:25px" aria-hidden="true" class="wp-block-spacer"></div>



<p class="has-x-small-font-size">Then above that we see that the ICMP is encapsulated with an IP Header, which shows the source 192.168.1.1 and destination 192.168.1.2. <br>These are the addresses of the tunnel interfaces:</p>



<figure data-wp-context="{&quot;uploadedSrc&quot;:&quot;https:\/\/aaronguild.net\/wp-content\/uploads\/2024\/03\/image-61.png&quot;,&quot;figureClassNames&quot;:&quot;wp-block-image size-full is-resized&quot;,&quot;figureStyles&quot;:null,&quot;imgClassNames&quot;:&quot;wp-image-3551&quot;,&quot;imgStyles&quot;:&quot;width:657px;height:auto&quot;,&quot;targetWidth&quot;:1031,&quot;targetHeight&quot;:520,&quot;scaleAttr&quot;:false,&quot;ariaLabel&quot;:&quot;Enlarge image&quot;,&quot;alt&quot;:&quot;&quot;}" data-wp-interactive="core/image" class="wp-block-image size-full is-resized wp-lightbox-container"><img loading="lazy" decoding="async" width="1031" height="520" data-wp-init="callbacks.setButtonStyles" data-wp-on--click="actions.showLightbox" data-wp-on--load="callbacks.setButtonStyles" data-wp-on-window--resize="callbacks.setButtonStyles" src="https://aaronguild.net/wp-content/uploads/2024/03/image-61.png" alt="" class="wp-image-3551" style="width:657px;height:auto" srcset="https://aaronguild.net/wp-content/uploads/2024/03/image-61.png 1031w, https://aaronguild.net/wp-content/uploads/2024/03/image-61-300x151.png 300w, https://aaronguild.net/wp-content/uploads/2024/03/image-61-1024x516.png 1024w, https://aaronguild.net/wp-content/uploads/2024/03/image-61-768x387.png 768w" sizes="(max-width: 1031px) 100vw, 1031px" /><button
			class="lightbox-trigger"
			type="button"
			aria-haspopup="dialog"
			aria-label="Enlarge image"
			data-wp-init="callbacks.initTriggerButton"
			data-wp-on--click="actions.showLightbox"
			data-wp-style--right="context.imageButtonRight"
			data-wp-style--top="context.imageButtonTop"
		>
			<svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" fill="none" viewBox="0 0 12 12">
				<path fill="#fff" d="M2 0a2 2 0 0 0-2 2v2h1.5V2a.5.5 0 0 1 .5-.5h2V0H2Zm2 10.5H2a.5.5 0 0 1-.5-.5V8H0v2a2 2 0 0 0 2 2h2v-1.5ZM8 12v-1.5h2a.5.5 0 0 0 .5-.5V8H12v2a2 2 0 0 1-2 2H8Zm2-12a2 2 0 0 1 2 2v2h-1.5V2a.5.5 0 0 0-.5-.5H8V0h2Z" />
			</svg>
		</button></figure>



<div style="height:25px" aria-hidden="true" class="wp-block-spacer"></div>



<p class="has-x-small-font-size">But still even on top of that, there is a GRE header, and on top of that, there is another IP header. In this outer IP header, the source IP is 100.0.0.2 (R1&#8217;s g0/0/0 interface), and the destination IP is 200.0.0.2 (R2&#8217;s g0/0/0 interface):</p>



<figure data-wp-context="{&quot;uploadedSrc&quot;:&quot;https:\/\/aaronguild.net\/wp-content\/uploads\/2024\/03\/image-62.png&quot;,&quot;figureClassNames&quot;:&quot;wp-block-image size-full is-resized&quot;,&quot;figureStyles&quot;:null,&quot;imgClassNames&quot;:&quot;wp-image-3554&quot;,&quot;imgStyles&quot;:&quot;width:661px;height:auto&quot;,&quot;targetWidth&quot;:1125,&quot;targetHeight&quot;:735,&quot;scaleAttr&quot;:false,&quot;ariaLabel&quot;:&quot;Enlarge image&quot;,&quot;alt&quot;:&quot;&quot;}" data-wp-interactive="core/image" class="wp-block-image size-full is-resized wp-lightbox-container"><img loading="lazy" decoding="async" width="1125" height="735" data-wp-init="callbacks.setButtonStyles" data-wp-on--click="actions.showLightbox" data-wp-on--load="callbacks.setButtonStyles" data-wp-on-window--resize="callbacks.setButtonStyles" src="https://aaronguild.net/wp-content/uploads/2024/03/image-62.png" alt="" class="wp-image-3554" style="width:661px;height:auto" srcset="https://aaronguild.net/wp-content/uploads/2024/03/image-62.png 1125w, https://aaronguild.net/wp-content/uploads/2024/03/image-62-300x196.png 300w, https://aaronguild.net/wp-content/uploads/2024/03/image-62-1024x669.png 1024w, https://aaronguild.net/wp-content/uploads/2024/03/image-62-768x502.png 768w" sizes="(max-width: 1125px) 100vw, 1125px" /><button
			class="lightbox-trigger"
			type="button"
			aria-haspopup="dialog"
			aria-label="Enlarge image"
			data-wp-init="callbacks.initTriggerButton"
			data-wp-on--click="actions.showLightbox"
			data-wp-style--right="context.imageButtonRight"
			data-wp-style--top="context.imageButtonTop"
		>
			<svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" fill="none" viewBox="0 0 12 12">
				<path fill="#fff" d="M2 0a2 2 0 0 0-2 2v2h1.5V2a.5.5 0 0 1 .5-.5h2V0H2Zm2 10.5H2a.5.5 0 0 1-.5-.5V8H0v2a2 2 0 0 0 2 2h2v-1.5ZM8 12v-1.5h2a.5.5 0 0 0 .5-.5V8H12v2a2 2 0 0 1-2 2H8Zm2-12a2 2 0 0 1 2 2v2h-1.5V2a.5.5 0 0 0-.5-.5H8V0h2Z" />
			</svg>
		</button></figure>



<div style="height:25px" aria-hidden="true" class="wp-block-spacer"></div>



<p class="has-x-small-font-size"><strong><u>NOTE</u></strong><br>The ping from R1 to R2 moves through the Service Provider Network as it would if the GRE tunnel was not configured. But as we have seen above, the communication is encapsulated several times over to create the GRE tunnel:</p>



<p class="has-x-small-font-size">First, PING goes to the SPR1 router. Second, the PING goes to the SPR2 router. Thirdly, the PING finally goes to R2.</p>



<figure data-wp-context="{&quot;uploadedSrc&quot;:&quot;https:\/\/aaronguild.net\/wp-content\/uploads\/2024\/03\/image-73.png&quot;,&quot;figureClassNames&quot;:&quot;wp-block-image size-full is-resized&quot;,&quot;figureStyles&quot;:null,&quot;imgClassNames&quot;:&quot;wp-image-3621&quot;,&quot;imgStyles&quot;:&quot;width:800px;height:auto&quot;,&quot;targetWidth&quot;:1052,&quot;targetHeight&quot;:575,&quot;scaleAttr&quot;:false,&quot;ariaLabel&quot;:&quot;Enlarge image&quot;,&quot;alt&quot;:&quot;&quot;}" data-wp-interactive="core/image" class="wp-block-image size-full is-resized wp-lightbox-container"><img loading="lazy" decoding="async" width="1052" height="575" data-wp-init="callbacks.setButtonStyles" data-wp-on--click="actions.showLightbox" data-wp-on--load="callbacks.setButtonStyles" data-wp-on-window--resize="callbacks.setButtonStyles" src="https://aaronguild.net/wp-content/uploads/2024/03/image-73.png" alt="" class="wp-image-3621" style="width:800px;height:auto" srcset="https://aaronguild.net/wp-content/uploads/2024/03/image-73.png 1052w, https://aaronguild.net/wp-content/uploads/2024/03/image-73-300x164.png 300w, https://aaronguild.net/wp-content/uploads/2024/03/image-73-1024x560.png 1024w, https://aaronguild.net/wp-content/uploads/2024/03/image-73-768x420.png 768w" sizes="(max-width: 1052px) 100vw, 1052px" /><button
			class="lightbox-trigger"
			type="button"
			aria-haspopup="dialog"
			aria-label="Enlarge image"
			data-wp-init="callbacks.initTriggerButton"
			data-wp-on--click="actions.showLightbox"
			data-wp-style--right="context.imageButtonRight"
			data-wp-style--top="context.imageButtonTop"
		>
			<svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" fill="none" viewBox="0 0 12 12">
				<path fill="#fff" d="M2 0a2 2 0 0 0-2 2v2h1.5V2a.5.5 0 0 1 .5-.5h2V0H2Zm2 10.5H2a.5.5 0 0 1-.5-.5V8H0v2a2 2 0 0 0 2 2h2v-1.5ZM8 12v-1.5h2a.5.5 0 0 0 .5-.5V8H12v2a2 2 0 0 1-2 2H8Zm2-12a2 2 0 0 1 2 2v2h-1.5V2a.5.5 0 0 0-.5-.5H8V0h2Z" />
			</svg>
		</button></figure>



<p class="has-x-small-font-size">Then the PING will take the same path back a ping echo reply.</p>



<div style="height:48px" aria-hidden="true" class="wp-block-spacer"></div>



<p><strong>The second part of this lab is to “Configure OSPF on the tunnel interfaces of R1 and R2, to allow PC1 and PC2 to communicate.</strong></p>



<p class="has-x-small-font-size">First let&#8217;s send a ping from PC1 to PC2 to show that they cannot communicate yet:</p>



<figure data-wp-context="{&quot;uploadedSrc&quot;:&quot;https:\/\/aaronguild.net\/wp-content\/uploads\/2024\/03\/image-65.png&quot;,&quot;figureClassNames&quot;:&quot;wp-block-image size-full is-resized&quot;,&quot;figureStyles&quot;:null,&quot;imgClassNames&quot;:&quot;wp-image-3562&quot;,&quot;imgStyles&quot;:&quot;width:581px;height:auto&quot;,&quot;targetWidth&quot;:1083,&quot;targetHeight&quot;:631,&quot;scaleAttr&quot;:false,&quot;ariaLabel&quot;:&quot;Enlarge image&quot;,&quot;alt&quot;:&quot;&quot;}" data-wp-interactive="core/image" class="wp-block-image size-full is-resized wp-lightbox-container"><img loading="lazy" decoding="async" width="1083" height="631" data-wp-init="callbacks.setButtonStyles" data-wp-on--click="actions.showLightbox" data-wp-on--load="callbacks.setButtonStyles" data-wp-on-window--resize="callbacks.setButtonStyles" src="https://aaronguild.net/wp-content/uploads/2024/03/image-65.png" alt="" class="wp-image-3562" style="width:581px;height:auto" srcset="https://aaronguild.net/wp-content/uploads/2024/03/image-65.png 1083w, https://aaronguild.net/wp-content/uploads/2024/03/image-65-300x175.png 300w, https://aaronguild.net/wp-content/uploads/2024/03/image-65-1024x597.png 1024w, https://aaronguild.net/wp-content/uploads/2024/03/image-65-768x447.png 768w" sizes="(max-width: 1083px) 100vw, 1083px" /><button
			class="lightbox-trigger"
			type="button"
			aria-haspopup="dialog"
			aria-label="Enlarge image"
			data-wp-init="callbacks.initTriggerButton"
			data-wp-on--click="actions.showLightbox"
			data-wp-style--right="context.imageButtonRight"
			data-wp-style--top="context.imageButtonTop"
		>
			<svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" fill="none" viewBox="0 0 12 12">
				<path fill="#fff" d="M2 0a2 2 0 0 0-2 2v2h1.5V2a.5.5 0 0 1 .5-.5h2V0H2Zm2 10.5H2a.5.5 0 0 1-.5-.5V8H0v2a2 2 0 0 0 2 2h2v-1.5ZM8 12v-1.5h2a.5.5 0 0 0 .5-.5V8H12v2a2 2 0 0 1-2 2H8Zm2-12a2 2 0 0 1 2 2v2h-1.5V2a.5.5 0 0 0-.5-.5H8V0h2Z" />
			</svg>
		</button></figure>



<p class="has-x-small-font-size">As you can see the ping’s timed out and didn’t work. But when R1 and R2 become OSPF neighbors, they will learn each other&#8217;s routes, and PC1 and PC2 will be able to communicate over the GRE tunnel.</p>



<p class="has-x-small-font-size">Let’s do that by enabling OSPF on R1 first by entering OSPF mode:</p>



<p class="has-courier-prime-font-family">R1(config)#router ospf 1<br></p>



<p class="has-x-small-font-size"><br>The following network command enables OSPF on the Tunnel0 interface:</p>



<p class="has-courier-prime-font-family">R1(config-router)#network 192.168.1.1 0.0.0.0 area 0<br></p>



<p class="has-x-small-font-size"><br>The following network command enables OSPF on the g0/0/0 interface.</p>



<p class="has-courier-prime-font-family">R1(config-router)#network 10.0.1.1 0.0.0.0 area 0<br><br></p>



<p class="has-x-small-font-size">And we’ll make g0/0 a passive interface since there are no neighbors connected to it:</p>



<p class="has-courier-prime-font-family">R1(config-router)#passive-interface g0/0<br><br></p>



<p class="has-x-small-font-size">Below are the OSPF commands we just configured:</p>



<figure data-wp-context="{&quot;uploadedSrc&quot;:&quot;https:\/\/aaronguild.net\/wp-content\/uploads\/2024\/03\/image-66.png&quot;,&quot;figureClassNames&quot;:&quot;wp-block-image size-full is-resized&quot;,&quot;figureStyles&quot;:null,&quot;imgClassNames&quot;:&quot;wp-image-3565&quot;,&quot;imgStyles&quot;:&quot;width:570px;height:auto&quot;,&quot;targetWidth&quot;:864,&quot;targetHeight&quot;:220,&quot;scaleAttr&quot;:false,&quot;ariaLabel&quot;:&quot;Enlarge image&quot;,&quot;alt&quot;:&quot;&quot;}" data-wp-interactive="core/image" class="wp-block-image size-full is-resized wp-lightbox-container"><img loading="lazy" decoding="async" width="864" height="220" data-wp-init="callbacks.setButtonStyles" data-wp-on--click="actions.showLightbox" data-wp-on--load="callbacks.setButtonStyles" data-wp-on-window--resize="callbacks.setButtonStyles" src="https://aaronguild.net/wp-content/uploads/2024/03/image-66.png" alt="" class="wp-image-3565" style="width:570px;height:auto" srcset="https://aaronguild.net/wp-content/uploads/2024/03/image-66.png 864w, https://aaronguild.net/wp-content/uploads/2024/03/image-66-300x76.png 300w, https://aaronguild.net/wp-content/uploads/2024/03/image-66-768x196.png 768w" sizes="(max-width: 864px) 100vw, 864px" /><button
			class="lightbox-trigger"
			type="button"
			aria-haspopup="dialog"
			aria-label="Enlarge image"
			data-wp-init="callbacks.initTriggerButton"
			data-wp-on--click="actions.showLightbox"
			data-wp-style--right="context.imageButtonRight"
			data-wp-style--top="context.imageButtonTop"
		>
			<svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" fill="none" viewBox="0 0 12 12">
				<path fill="#fff" d="M2 0a2 2 0 0 0-2 2v2h1.5V2a.5.5 0 0 1 .5-.5h2V0H2Zm2 10.5H2a.5.5 0 0 1-.5-.5V8H0v2a2 2 0 0 0 2 2h2v-1.5ZM8 12v-1.5h2a.5.5 0 0 0 .5-.5V8H12v2a2 2 0 0 1-2 2H8Zm2-12a2 2 0 0 1 2 2v2h-1.5V2a.5.5 0 0 0-.5-.5H8V0h2Z" />
			</svg>
		</button></figure>



<div style="height:36px" aria-hidden="true" class="wp-block-spacer"></div>



<p class="has-x-small-font-size">Now let’s do the same to R2:</p>



<figure data-wp-context="{&quot;uploadedSrc&quot;:&quot;https:\/\/aaronguild.net\/wp-content\/uploads\/2024\/03\/image-67.png&quot;,&quot;figureClassNames&quot;:&quot;wp-block-image size-full is-resized&quot;,&quot;figureStyles&quot;:null,&quot;imgClassNames&quot;:&quot;wp-image-3569&quot;,&quot;imgStyles&quot;:&quot;width:621px;height:auto&quot;,&quot;targetWidth&quot;:977,&quot;targetHeight&quot;:225,&quot;scaleAttr&quot;:false,&quot;ariaLabel&quot;:&quot;Enlarge image&quot;,&quot;alt&quot;:&quot;&quot;}" data-wp-interactive="core/image" class="wp-block-image size-full is-resized wp-lightbox-container"><img loading="lazy" decoding="async" width="977" height="225" data-wp-init="callbacks.setButtonStyles" data-wp-on--click="actions.showLightbox" data-wp-on--load="callbacks.setButtonStyles" data-wp-on-window--resize="callbacks.setButtonStyles" src="https://aaronguild.net/wp-content/uploads/2024/03/image-67.png" alt="" class="wp-image-3569" style="width:621px;height:auto" srcset="https://aaronguild.net/wp-content/uploads/2024/03/image-67.png 977w, https://aaronguild.net/wp-content/uploads/2024/03/image-67-300x69.png 300w, https://aaronguild.net/wp-content/uploads/2024/03/image-67-768x177.png 768w" sizes="(max-width: 977px) 100vw, 977px" /><button
			class="lightbox-trigger"
			type="button"
			aria-haspopup="dialog"
			aria-label="Enlarge image"
			data-wp-init="callbacks.initTriggerButton"
			data-wp-on--click="actions.showLightbox"
			data-wp-style--right="context.imageButtonRight"
			data-wp-style--top="context.imageButtonTop"
		>
			<svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" fill="none" viewBox="0 0 12 12">
				<path fill="#fff" d="M2 0a2 2 0 0 0-2 2v2h1.5V2a.5.5 0 0 1 .5-.5h2V0H2Zm2 10.5H2a.5.5 0 0 1-.5-.5V8H0v2a2 2 0 0 0 2 2h2v-1.5ZM8 12v-1.5h2a.5.5 0 0 0 .5-.5V8H12v2a2 2 0 0 1-2 2H8Zm2-12a2 2 0 0 1 2 2v2h-1.5V2a.5.5 0 0 0-.5-.5H8V0h2Z" />
			</svg>
		</button><figcaption class="wp-element-caption"><sub>As highlighted above, you can see R1 and R2 have become OSPF neighbors. So fast that it messed up my second network command I was typing lol. I should’ve have enabled the logging synchronous, which eliminates those typing errors.</sub></figcaption></figure>



<div style="height:31px" aria-hidden="true" class="wp-block-spacer"></div>



<p class="has-x-small-font-size">Let’s check the routes on R2 with the <em>do show ip route</em> command:</p>



<figure data-wp-context="{&quot;uploadedSrc&quot;:&quot;https:\/\/aaronguild.net\/wp-content\/uploads\/2024\/03\/image-68.png&quot;,&quot;figureClassNames&quot;:&quot;wp-block-image size-full is-resized&quot;,&quot;figureStyles&quot;:null,&quot;imgClassNames&quot;:&quot;wp-image-3571&quot;,&quot;imgStyles&quot;:&quot;width:578px;height:auto&quot;,&quot;targetWidth&quot;:952,&quot;targetHeight&quot;:586,&quot;scaleAttr&quot;:false,&quot;ariaLabel&quot;:&quot;Enlarge image&quot;,&quot;alt&quot;:&quot;&quot;}" data-wp-interactive="core/image" class="wp-block-image size-full is-resized wp-lightbox-container"><img loading="lazy" decoding="async" width="952" height="586" data-wp-init="callbacks.setButtonStyles" data-wp-on--click="actions.showLightbox" data-wp-on--load="callbacks.setButtonStyles" data-wp-on-window--resize="callbacks.setButtonStyles" src="https://aaronguild.net/wp-content/uploads/2024/03/image-68.png" alt="" class="wp-image-3571" style="width:578px;height:auto" srcset="https://aaronguild.net/wp-content/uploads/2024/03/image-68.png 952w, https://aaronguild.net/wp-content/uploads/2024/03/image-68-300x185.png 300w, https://aaronguild.net/wp-content/uploads/2024/03/image-68-768x473.png 768w" sizes="(max-width: 952px) 100vw, 952px" /><button
			class="lightbox-trigger"
			type="button"
			aria-haspopup="dialog"
			aria-label="Enlarge image"
			data-wp-init="callbacks.initTriggerButton"
			data-wp-on--click="actions.showLightbox"
			data-wp-style--right="context.imageButtonRight"
			data-wp-style--top="context.imageButtonTop"
		>
			<svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" fill="none" viewBox="0 0 12 12">
				<path fill="#fff" d="M2 0a2 2 0 0 0-2 2v2h1.5V2a.5.5 0 0 1 .5-.5h2V0H2Zm2 10.5H2a.5.5 0 0 1-.5-.5V8H0v2a2 2 0 0 0 2 2h2v-1.5ZM8 12v-1.5h2a.5.5 0 0 0 .5-.5V8H12v2a2 2 0 0 1-2 2H8Zm2-12a2 2 0 0 1 2 2v2h-1.5V2a.5.5 0 0 0-.5-.5H8V0h2Z" />
			</svg>
		</button><figcaption class="wp-element-caption"><sub>Okay, it learned a route to 10.0.1.0/24, R1&#8217;s LAN, via the Tunnel0 interface.</sub></figcaption></figure>



<div style="height:31px" aria-hidden="true" class="wp-block-spacer"></div>



<p class="has-x-small-font-size">Let’s check the routes on R1 as well:</p>



<figure data-wp-context="{&quot;uploadedSrc&quot;:&quot;https:\/\/aaronguild.net\/wp-content\/uploads\/2024\/03\/image-69.png&quot;,&quot;figureClassNames&quot;:&quot;wp-block-image size-full is-resized&quot;,&quot;figureStyles&quot;:null,&quot;imgClassNames&quot;:&quot;wp-image-3573&quot;,&quot;imgStyles&quot;:&quot;width:620px;height:auto&quot;,&quot;targetWidth&quot;:947,&quot;targetHeight&quot;:584,&quot;scaleAttr&quot;:false,&quot;ariaLabel&quot;:&quot;Enlarge image&quot;,&quot;alt&quot;:&quot;&quot;}" data-wp-interactive="core/image" class="wp-block-image size-full is-resized wp-lightbox-container"><img loading="lazy" decoding="async" width="947" height="584" data-wp-init="callbacks.setButtonStyles" data-wp-on--click="actions.showLightbox" data-wp-on--load="callbacks.setButtonStyles" data-wp-on-window--resize="callbacks.setButtonStyles" src="https://aaronguild.net/wp-content/uploads/2024/03/image-69.png" alt="" class="wp-image-3573" style="width:620px;height:auto" srcset="https://aaronguild.net/wp-content/uploads/2024/03/image-69.png 947w, https://aaronguild.net/wp-content/uploads/2024/03/image-69-300x185.png 300w, https://aaronguild.net/wp-content/uploads/2024/03/image-69-768x474.png 768w" sizes="(max-width: 947px) 100vw, 947px" /><button
			class="lightbox-trigger"
			type="button"
			aria-haspopup="dialog"
			aria-label="Enlarge image"
			data-wp-init="callbacks.initTriggerButton"
			data-wp-on--click="actions.showLightbox"
			data-wp-style--right="context.imageButtonRight"
			data-wp-style--top="context.imageButtonTop"
		>
			<svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" fill="none" viewBox="0 0 12 12">
				<path fill="#fff" d="M2 0a2 2 0 0 0-2 2v2h1.5V2a.5.5 0 0 1 .5-.5h2V0H2Zm2 10.5H2a.5.5 0 0 1-.5-.5V8H0v2a2 2 0 0 0 2 2h2v-1.5ZM8 12v-1.5h2a.5.5 0 0 0 .5-.5V8H12v2a2 2 0 0 1-2 2H8Zm2-12a2 2 0 0 1 2 2v2h-1.5V2a.5.5 0 0 0-.5-.5H8V0h2Z" />
			</svg>
		</button><figcaption class="wp-element-caption"><sub>Okay, it learned a route to 10.0.2.0/24 via the Tunnel0 interface.</sub></figcaption></figure>



<div style="height:31px" aria-hidden="true" class="wp-block-spacer"></div>



<p class="has-x-small-font-size">Now let’s try that same ping again from PC1 to PC2:</p>



<figure data-wp-context="{&quot;uploadedSrc&quot;:&quot;https:\/\/aaronguild.net\/wp-content\/uploads\/2024\/03\/image-70.png&quot;,&quot;figureClassNames&quot;:&quot;wp-block-image size-full is-resized&quot;,&quot;figureStyles&quot;:null,&quot;imgClassNames&quot;:&quot;wp-image-3575&quot;,&quot;imgStyles&quot;:&quot;width:532px;height:auto&quot;,&quot;targetWidth&quot;:847,&quot;targetHeight&quot;:345,&quot;scaleAttr&quot;:false,&quot;ariaLabel&quot;:&quot;Enlarge image&quot;,&quot;alt&quot;:&quot;&quot;}" data-wp-interactive="core/image" class="wp-block-image size-full is-resized wp-lightbox-container"><img loading="lazy" decoding="async" width="847" height="345" data-wp-init="callbacks.setButtonStyles" data-wp-on--click="actions.showLightbox" data-wp-on--load="callbacks.setButtonStyles" data-wp-on-window--resize="callbacks.setButtonStyles" src="https://aaronguild.net/wp-content/uploads/2024/03/image-70.png" alt="" class="wp-image-3575" style="width:532px;height:auto" srcset="https://aaronguild.net/wp-content/uploads/2024/03/image-70.png 847w, https://aaronguild.net/wp-content/uploads/2024/03/image-70-300x122.png 300w, https://aaronguild.net/wp-content/uploads/2024/03/image-70-768x313.png 768w" sizes="(max-width: 847px) 100vw, 847px" /><button
			class="lightbox-trigger"
			type="button"
			aria-haspopup="dialog"
			aria-label="Enlarge image"
			data-wp-init="callbacks.initTriggerButton"
			data-wp-on--click="actions.showLightbox"
			data-wp-style--right="context.imageButtonRight"
			data-wp-style--top="context.imageButtonTop"
		>
			<svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" fill="none" viewBox="0 0 12 12">
				<path fill="#fff" d="M2 0a2 2 0 0 0-2 2v2h1.5V2a.5.5 0 0 1 .5-.5h2V0H2Zm2 10.5H2a.5.5 0 0 1-.5-.5V8H0v2a2 2 0 0 0 2 2h2v-1.5ZM8 12v-1.5h2a.5.5 0 0 0 .5-.5V8H12v2a2 2 0 0 1-2 2H8Zm2-12a2 2 0 0 1 2 2v2h-1.5V2a.5.5 0 0 0-.5-.5H8V0h2Z" />
			</svg>
		</button><figcaption class="wp-element-caption"><sub>One or two pings might fail, but after that, they will work. R1 will encapsulate the packet from PC1 using GRE and send it over the tunnel to R2.</sub></figcaption></figure>



<div style="height:33px" aria-hidden="true" class="wp-block-spacer"></div>



<figure data-wp-context="{&quot;uploadedSrc&quot;:&quot;https:\/\/aaronguild.net\/wp-content\/uploads\/2024\/03\/image-64.png&quot;,&quot;figureClassNames&quot;:&quot;wp-block-image size-full is-resized&quot;,&quot;figureStyles&quot;:null,&quot;imgClassNames&quot;:&quot;wp-image-3559&quot;,&quot;imgStyles&quot;:&quot;width:856px;height:auto&quot;,&quot;targetWidth&quot;:1125,&quot;targetHeight&quot;:617,&quot;scaleAttr&quot;:false,&quot;ariaLabel&quot;:&quot;Enlarge image&quot;,&quot;alt&quot;:&quot;&quot;}" data-wp-interactive="core/image" class="wp-block-image size-full is-resized wp-lightbox-container"><img loading="lazy" decoding="async" width="1125" height="617" data-wp-init="callbacks.setButtonStyles" data-wp-on--click="actions.showLightbox" data-wp-on--load="callbacks.setButtonStyles" data-wp-on-window--resize="callbacks.setButtonStyles" src="https://aaronguild.net/wp-content/uploads/2024/03/image-64.png" alt="" class="wp-image-3559" style="width:856px;height:auto" srcset="https://aaronguild.net/wp-content/uploads/2024/03/image-64.png 1125w, https://aaronguild.net/wp-content/uploads/2024/03/image-64-300x165.png 300w, https://aaronguild.net/wp-content/uploads/2024/03/image-64-1024x562.png 1024w, https://aaronguild.net/wp-content/uploads/2024/03/image-64-768x421.png 768w" sizes="(max-width: 1125px) 100vw, 1125px" /><button
			class="lightbox-trigger"
			type="button"
			aria-haspopup="dialog"
			aria-label="Enlarge image"
			data-wp-init="callbacks.initTriggerButton"
			data-wp-on--click="actions.showLightbox"
			data-wp-style--right="context.imageButtonRight"
			data-wp-style--top="context.imageButtonTop"
		>
			<svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" fill="none" viewBox="0 0 12 12">
				<path fill="#fff" d="M2 0a2 2 0 0 0-2 2v2h1.5V2a.5.5 0 0 1 .5-.5h2V0H2Zm2 10.5H2a.5.5 0 0 1-.5-.5V8H0v2a2 2 0 0 0 2 2h2v-1.5ZM8 12v-1.5h2a.5.5 0 0 0 .5-.5V8H12v2a2 2 0 0 1-2 2H8Zm2-12a2 2 0 0 1 2 2v2h-1.5V2a.5.5 0 0 0-.5-.5H8V0h2Z" />
			</svg>
		</button></figure>



<p>In this lab I&#8217;ve shown how to create a GRE tunnel between two routers and activate OSPF on the tunnel.</p>
