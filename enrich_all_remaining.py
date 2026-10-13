# Comprehensive Expansion Answers for Remaining Questions in Java, Networks, and DBMS

ALL_ADDITIONAL_ENRICHMENTS = {
    # ==================== JAVA ====================
    "table formatting and validation": """
<p><strong>Answer:</strong></p>
<p>Web forms collect user input and submit data to server-side scripts. Table-based styling ensures clean alignment of labels and input fields, while JavaScript provides client-side validation before HTTP submission.</p>
<div class=\"code-box\">&lt;!DOCTYPE html&gt;
&lt;html&gt;
&lt;head&gt;
    &lt;title&gt;Validated User Registration Form&lt;/title&gt;
    &lt;script&gt;
        function validateForm() {
            var name = document.forms[\"regForm\"][\"uname\"].value;
            var email = document.forms[\"regForm\"][\"email\"].value;
            var pass = document.forms[\"regForm\"][\"pwd\"].value;
            var mobile = document.forms[\"regForm\"][\"mob\"].value;

            if (name.trim() == \"\") {
                alert(\"Validation Error: Full Name is required!\");
                return false;
            }
            if (email.indexOf(\"@\") == -1 || email.indexOf(\".\") == -1) {
                alert(\"Validation Error: Enter a valid email address!\");
                return false;
            }
            if (pass.length &lt; 6) {
                alert(\"Validation Error: Password must be at least 6 characters long!\");
                return false;
            }
            if (!/^[0-9]{10}$/.test(mobile)) {
                alert(\"Validation Error: Mobile number must be exactly 10 digits!\");
                return false;
            }
            alert(\"Validation Succeeded: Submitting data to server...\");
            return true;
        }
    &lt;/script&gt;
&lt;/head&gt;
&lt;body style=\"font-family:Arial, sans-serif; background:#f8fafc; padding:30px;\"&gt;
    &lt;div style=\"max-width:550px; margin:auto; background:white; padding:25px; border-radius:8px; border:1px solid #cbd5e1;\"&gt;
        &lt;h2 style=\"text-align:center; color:#1e3a8a;\"&gt;Student Portal Registration&lt;/h2&gt;
        &lt;form name=\"regForm\" action=\"RegisterServlet\" method=\"POST\" onsubmit=\"return validateForm()\"&gt;
            &lt;table cellpadding=\"8\" cellspacing=\"0\" style=\"width:100%;\"&gt;
                &lt;tr&gt;
                    &lt;td&gt;&lt;b&gt;Username:&lt;/b&gt;&lt;/td&gt;
                    &lt;td&gt;&lt;input type=\"text\" name=\"uname\" style=\"width:100%; padding:6px;\"&gt;&lt;/td&gt;
                &lt;/tr&gt;
                &lt;tr&gt;
                    &lt;td&gt;&lt;b&gt;Email Address:&lt;/b&gt;&lt;/td&gt;
                    &lt;td&gt;&lt;input type=\"text\" name=\"email\" style=\"width:100%; padding:6px;\"&gt;&lt;/td&gt;
                &lt;/tr&gt;
                &lt;tr&gt;
                    &lt;td&gt;&lt;b&gt;Password:&lt;/b&gt;&lt;/td&gt;
                    &lt;td&gt;&lt;input type=\"password\" name=\"pwd\" style=\"width:100%; padding:6px;\"&gt;&lt;/td&gt;
                &lt;/tr&gt;
                &lt;tr&gt;
                    &lt;td&gt;&lt;b&gt;Mobile (10 digits):&lt;/b&gt;&lt;/td&gt;
                    &lt;td&gt;&lt;input type=\"text\" name=\"mob\" style=\"width:100%; padding:6px;\"&gt;&lt;/td&gt;
                &lt;/tr&gt;
                &lt;tr&gt;
                    &lt;td&gt;&lt;b&gt;Gender:&lt;/b&gt;&lt;/td&gt;
                    &lt;td&gt;
                        &lt;input type=\"radio\" name=\"gender\" value=\"Male\" checked&gt; Male
                        &lt;input type=\"radio\" name=\"gender\" value=\"Female\" style=\"margin-left:15px;\"&gt; Female
                    &lt;/td&gt;
                &lt;/tr&gt;
                &lt;tr&gt;
                    &lt;td colspan=\"2\" style=\"text-align:center; padding-top:15px;\"&gt;
                        &lt;input type=\"submit\" value=\"Register Now\" style=\"background:#2563eb; color:white; padding:8px 20px; border:none; border-radius:4px; font-weight:bold; cursor:pointer;\"&gt;
                        &lt;input type=\"reset\" value=\"Clear Form\" style=\"background:#64748b; color:white; padding:8px 15px; border:none; border-radius:4px; margin-left:10px; cursor:pointer;\"&gt;
                    &lt;/td&gt;
                &lt;/tr&gt;
            &lt;/table&gt;
        &lt;/form&gt;
    &lt;/div&gt;
&lt;/body&gt;
&lt;/html&gt;</div>
""",

    "responsive institutional web page": """
<p><strong>Answer:</strong></p>
<p>A responsive institutional web page adapts dynamically across desktops, tablets, and smartphones using modern CSS Media Queries and flexible layouts.</p>
<div class=\"code-box\">&lt;!DOCTYPE html&gt;
&lt;html lang=\"en\"&gt;
&lt;head&gt;
    &lt;meta charset=\"UTF-8\"&gt;
    &lt;meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\"&gt;
    &lt;title&gt;Chaudhary Charan Singh University &bull; Dept of Computer Applications&lt;/title&gt;
    &lt;style&gt;
        * { box-sizing: border-box; margin: 0; padding: 0; font-family: 'Segoe UI', Tahoma, sans-serif; }
        header { background: #1e3a8a; color: white; padding: 20px; text-align: center; }
        nav { background: #0f172a; display: flex; justify-content: center; flex-wrap: wrap; }
        nav a { color: #f8fafc; padding: 12px 20px; text-decoration: none; font-weight: 600; font-size: 14px; }
        nav a:hover { background: #2563eb; }
        .hero { background: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.6)), url('campus.jpg') center/cover; color: white; text-align: center; padding: 60px 20px; }
        .container { max-width: 1100px; margin: 30px auto; padding: 0 15px; display: grid; grid-template-columns: 2fr 1fr; gap: 25px; }
        .card { background: white; padding: 20px; border-radius: 8px; box-shadow: 0 2px 6px rgba(0,0,0,0.08); }
        footer { background: #0f172a; color: #94a3b8; text-align: center; padding: 20px; margin-top: 40px; font-size: 13px; }
        /* Media Query for Mobile Responsive Screen */
        @media (max-width: 768px) {
            .container { grid-template-columns: 1fr; }
            nav { flex-direction: column; text-align: center; }
        }
    &lt;/style&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;header&gt;
        &lt;h1&gt;Chaudhary Charan Singh University, Meerut&lt;/h1&gt;
        &lt;p&gt;Faculty of Engineering &amp; Technology &bull; BCA Department&lt;/p&gt;
    &lt;/header&gt;
    &lt;nav&gt;
        &lt;a href=\"#\"&gt;Home&lt;/a&gt;
        &lt;a href=\"#\"&gt;Academics&lt;/a&gt;
        &lt;a href=\"#\"&gt;Examinations&lt;/a&gt;
        &lt;a href=\"#\"&gt;PYQ Bank&lt;/a&gt;
        &lt;a href=\"#\"&gt;Contact Us&lt;/a&gt;
    &lt;/nav&gt;
    &lt;div class=\"hero\"&gt;
        &lt;h2&gt;Excellence in Computer Science &amp; Applications&lt;/h2&gt;
        &lt;p&gt;Empowering students with industry-standard programming and analytical skills.&lt;/p&gt;
    &lt;/div&gt;
    &lt;div class=\"container\"&gt;
        &lt;main class=\"card\"&gt;
            &lt;h3 style=\"color:#1e3a8a; margin-bottom:10px;\"&gt;About BCA Programme&lt;/h3&gt;
            &lt;p&gt;The 3-Year Bachelor of Computer Applications curriculum encompasses Data Structures, DBMS, Java, Computer Networks, and Numerical Analysis to build cutting-edge software engineering capabilities.&lt;/p&gt;
        &lt;/main&gt;
        &lt;aside class=\"card\"&gt;
            &lt;h3 style=\"color:#dc2626; margin-bottom:10px;\"&gt;Notice Board&lt;/h3&gt;
            &lt;ul style=\"padding-left:18px; line-height:1.6; font-size:13px;\"&gt;
                &lt;li&gt;5th Sem Examination Schedule Released.&lt;/li&gt;
                &lt;li&gt;Solved PYQs uploaded to student portal.&lt;/li&gt;
                &lt;li&gt;Project viva submissions due next week.&lt;/li&gt;
            &lt;/ul&gt;
        &lt;/aside&gt;
    &lt;/div&gt;
    &lt;footer&gt;
        &lt;p&gt;&amp;copy; CCS University BCA Portal. All Rights Reserved.&lt;/p&gt;
    &lt;/footer&gt;
&lt;/body&gt;
&lt;/html&gt;</div>
""",

    "define constructor in java": """
<p><strong>Answer:</strong></p>
<p>A <b>Constructor</b> in Java is a special member method invoked automatically by the runtime when an object is instantiated using the <code>new</code> operator. Its primary role is to initialize instance variables and allocate required memory resources.</p>
<div class=\"info-box\">
    <p><b>Core Characteristics of Constructors:</b></p>
    <ul>
        <li><b>Same Name as Class:</b> Must bear the exact identifier of the enclosing class.</li>
        <li><b>No Return Type:</b> Does not return any value; must never declare a return type (not even <code>void</code>).</li>
        <li><b>Automatic Invocation:</b> Triggered implicitly upon object creation: <code>Student s = new Student();</code></li>
        <li><b>Default Constructor:</b> If no constructor is defined by the developer, the Java compiler automatically synthesizes a default no-argument constructor.</li>
        <li><b>Cannot be static, abstract, or final:</b> Constructors belong to object instantiation and cannot be inherited or made static.</li>
    </ul>
</div>
""",

    # ==================== NETWORKS ====================
    "what is the need for a computer network": """
<p><strong>Answer:</strong></p>
<p>A <b>Computer Network</b> is an interconnected collection of autonomous computers and peripherals capable of exchanging information and sharing resources.</p>
<div class=\"info-box\">
    <p><b>Five Fundamental Needs & Advantages:</b></p>
    <ol>
        <li><b>Hardware Resource Sharing:</b> High-cost hardware peripherals such as network printers, scanners, and multi-terabyte NAS storage servers are shared across hundreds of workstations.</li>
        <li><b>Data & Software Centralization:</b> Centralized database servers (e.g., banking cores) ensure data consistency, centralized backups, and eliminate data silos.</li>
        <li><b>Fast & Global Communication:</b> Facilitates instant real-time collaboration through E-Mail, VoIP, video conferencing, and messaging protocols.</li>
        <li><b>High Reliability & Redundancy:</b> Alternative routing paths ensure that if one server fails, backup servers maintain business continuity.</li>
        <li><b>Cost Reduction:</b> Eliminates redundant hardware purchases and software licenses through multi-user enterprise servers.</li>
    </ol>
</div>
""",

    "define hdlc (high-level data link control)": """
<p><strong>Answer:</strong></p>
<p><b>HDLC (High-Level Data Link Control)</b> is a bit-oriented synchronous Data Link Layer protocol developed by ISO (ISO 3309) providing reliable point-to-point and multipoint communication.</p>
<div class=\"info-box\">
    <p><b>Standard HDLC Frame Structure:</b></p>
    <table class=\"data-table\">
        <tr><th>Flag (8 bits)</th><th>Address (8 bits)</th><th>Control (8/16 bits)</th><th>Information (Variable)</th><th>FCS / CRC (16/32 bits)</th><th>Flag (8 bits)</th></tr>
        <tr><td><code>01111110</code></td><td>Station Address</td><td>Frame type &amp; Sequence</td><td>Network Layer Payload</td><td>CRC Error Checksum</td><td><code>01111110</code></td></tr>
    </table>
    <p><b>Three Frame Types:</b></p>
    <ul>
        <li><b>I-Frame (Information):</b> Carries user payload data and piggybacked ACKs.</li>
        <li><b>S-Frame (Supervisory):</b> Carries flow/error control signals (RR, RNR, REJ).</li>
        <li><b>U-Frame (Unnumbered):</b> Carries link setup, disconnection, and mode setting commands (SABM, DISC).</li>
    </ul>
    <p><b>Bit Stuffing:</b> To prevent premature flag detection within data, HDLC inserts a '0' bit whenever five consecutive '1' bits appear in the payload.</p>
</div>
""",

    "concept of piggybacking": """
<p><strong>Answer:</strong></p>
<p><b>Piggybacking</b> is an optimization technique used in bidirectional sliding window protocols where positive acknowledgment (ACK) bits for received frames are attached onto an outgoing outgoing data frame rather than transmitting a dedicated ACK frame.</p>
<div class=\"info-box\">
    <p><b>Operational Mechanism & Benefits:</b></p>
    <ul>
        <li>When Station A receives a data frame from Station B, instead of immediately sending a separate small ACK packet (which incurs full 20-byte IP header + 14-byte Ethernet header overhead), it waits briefly until its own application layer generates an outgoing data packet for Station B.</li>
        <li>The ACK sequence number is then placed into the header of that outgoing data frame.</li>
        <li><b>Significantly Reduces Bandwidth Consumption:</b> Saves link channel capacity by cutting packet framing overhead in half.</li>
        <li><i>Timer Precaution:</i> If no outgoing data frame is generated within a predetermined timeout period (ACK delay timer), a standalone ACK frame is dispatched to prevent retransmission timeouts at the sender.</li>
    </ul>
</div>
""",

    "how smtp protocol is used in e-mail": """
<p><strong>Answer:</strong></p>
<p><b>Simple Mail Transfer Protocol (SMTP)</b> is an application-layer, push-based protocol operating over TCP port 25 (or port 587 with TLS) used to deliver email messages across the Internet.</p>
<div class=\"info-box\">
    <p><b>SMTP Roles & Architecture:</b></p>
    <ul>
        <li><b>Push Protocol:</b> SMTP is strictly used by the sending Mail User Agent (MUA) to push email to the sender's Mail Transfer Agent (MTA) server, and from the sender MTA to the receiver's MTA server.</li>
        <li><i>Pull Limitation:</i> SMTP <b>cannot pull</b> email messages from a mailbox down to a client device; retrieval requires pull protocols such as <b>POP3 (Port 110)</b> or <b>IMAP (Port 143)</b>.</li>
    </ul>
    <p><b>Key SMTP Commands:</b> <code>HELO / EHLO</code> (handshake), <code>MAIL FROM:</code> (sender identity), <code>RCPT TO:</code> (recipient address), <code>DATA</code> (message body and headers), <code>QUIT</code> (session termination).</p>
</div>
""",

    "explain the use of bridges in computer networks": """
<p><strong>Answer:</strong></p>
<p>A <b>Bridge</b> is an internetworking device operating at the <b>Data Link Layer (Layer 2)</b> of the OSI model that connects and filters traffic between two separate LAN segments sharing identical protocols.</p>
<div class=\"info-box\">
    <p><b>Core Functions & Mechanism:</b></p>
    <ol>
        <li><b>Collision Domain Segmentation:</b> Splits a large collision domain into two smaller, isolated collision domains, dramatically reducing packet collisions.</li>
        <li><b>MAC Address Filtering:</b> Inspects the destination MAC address of incoming frames using an internal forwarding table. If sender and receiver reside on the same segment, the frame is filtered (blocked) from crossing over.</li>
        <li><b>Transparent Learning:</b> Dynamically inspects source MAC addresses of passing frames to build and update its bridge forwarding table.</li>
        <li><b>Spanning Tree Protocol (STP):</b> Eliminates broadcast storms and packet loops in redundant multi-bridge topologies.</li>
    </ol>
</div>
""",

    "write a short note on e-mail and its core protocols": """
<p><strong>Answer:</strong></p>
<p><b>Electronic Mail (E-Mail)</b> is a store-and-forward transmission system allowing digital messages and attachments to be exchanged globally between networked hosts.</p>
<table class=\"data-table\">
    <tr><th>Protocol</th><th>Port</th><th>Role / Nature</th><th>Key Distinction</th></tr>
    <tr><td><b>SMTP (Simple Mail Transfer Protocol)</b></td><td>25 / 587</td><td><b>Push Protocol:</b> Sends email from sender client to sender server, and relays between intermediate mail servers.</td><td>Outbound delivery only; cannot retrieve from server mailbox.</td></tr>
    <tr><td><b>POP3 (Post Office Protocol v3)</b></td><td>110 / 995</td><td><b>Pull Protocol:</b> Downloads email messages from server to local client disk and deletes from server by default.</td><td>Offline access; changes on local device not synchronized to server.</td></tr>
    <tr><td><b>IMAP (Internet Message Access Protocol)</b></td><td>143 / 993</td><td><b>Pull & Sync Protocol:</b> Manages messages directly on the central mail server. Folders, read status, and drafts sync across all devices.</td><td>Real-time two-way synchronization for multiple client devices (phones, laptops).</td></tr>
</table>
""",

    "define bandwidth and throughput": """
<p><strong>Answer:</strong></p>
<table class=\"data-table\">
    <tr><th>Metric</th><th>Bandwidth</th><th>Throughput</th></tr>
    <tr><td><b>Definition</b></td><td>The theoretical maximum theoretical data carrying capacity of a transmission medium.</td><td>The actual rate of successful data delivery achieved across the link under real network conditions.</td></tr>
    <tr><td><b>Nature</b></td><td>Theoretical peak ceiling (potential).</td><td>Practical measured performance (reality).</td></tr>
    <tr><td><b>Unit</b></td><td>Bits per second (bps, Mbps, Gbps) or Hertz (Hz).</td><td>Bits per second (bps, Mbps) or Packets per sec.</td></tr>
    <tr><td><b>Factors Influencing</b></td><td>Physical cable characteristics, channel frequency spectrum.</td><td>Network congestion, packet collisions, processing overhead, protocol headers, retransmissions.</td></tr>
    <tr><td><b>Analogy</b></td><td>The width of a highway (e.g., 6 lanes).</td><td>The actual number of cars passing per minute during rush hour.</td></tr>
</table>
""",

    "four channels, each with 100-khz bandwidth": """
<p><strong>Answer:</strong></p>
<p><b>Given Problem:</b> Four channels, each with 100-kHz bandwidth, are multiplexed together using Frequency Division Multiplexing (FDM). Guard bands of 10 kHz are required between adjacent channels. Find the minimum link bandwidth.</p>
<div class=\"info-box\">
    <p><b>Step-by-Step Calculation:</b></p>
    <ul>
        <li>Number of channels: <i>N = 4</i></li>
        <li>Bandwidth per channel: <i>B = 100 kHz</i></li>
        <li>Total bandwidth for 4 channels: <code>4 &times; 100 kHz = 400 kHz</code></li>
        <li>Number of guard bands between <i>N</i> channels: <code>N - 1 = 4 - 1 = 3 guard bands</code></li>
        <li>Bandwidth per guard band: <i>10 kHz</i></li>
        <li>Total guard band bandwidth: <code>3 &times; 10 kHz = 30 kHz</code></li>
    </ul>
    <p><b>Minimum Link Bandwidth Required:</b></p>
    <p><code>Total Bandwidth = (N &times; B) + [(N - 1) &times; Guard Band] = 400 kHz + 30 kHz = <b>430 kHz</b></code> &check;</p>
</div>
""",

    "point-to-point protocol (ppp)": """
<p><strong>Answer:</strong></p>
<p><b>PPP (Point-to-Point Protocol)</b> is a standard Data Link Layer protocol (RFC 1661) used to establish a direct connection between two networking nodes over dial-up, serial, or broadband links.</p>
<div class=\"info-box\">
    <p><b>Three Primary Components of PPP:</b></p>
    <ol>
        <li><b>Framing Method:</b> HDLC-like framing mechanism providing unambiguous frame delimitation and 16/32-bit CRC error detection.</li>
        <li><b>LCP (Link Control Protocol):</b> Establishes, configures, tests data link quality, negotiates options (packet sizes), and gracefully terminates the point-to-point connection.</li>
        <li><b>NCP (Network Control Protocols):</b> A family of protocols that negotiates network layer protocols (e.g., IPCP negotiates dynamic IP addresses for IPv4).</li>
    </ol>
    <p><b>Authentication Support:</b> PPP supports robust authentication via <b>PAP (Password Authentication Protocol)</b> and <b>CHAP (Challenge Handshake Authentication Protocol)</b>.</p>
</div>
""",

    "differentiate between lan, man, and wan": """
<p><strong>Answer:</strong></p>
<table class=\"data-table\">
    <tr><th>Parameter</th><th>LAN (Local Area Network)</th><th>MAN (Metropolitan Area Network)</th><th>WAN (Wide Area Network)</th></tr>
    <tr><td><b>Geographical Span</b></td><td>Confined to small area (single room, office, building, campus: &le; 1 km).</td><td>Spans an entire city or metropolitan town (&le; 50 km).</td><td>Spans entire countries, continents, or the globe (&gt; 100 km).</td></tr>
    <tr><td><b>Ownership</b></td><td>Privately owned by single organization/individual.</td><td>Public or private enterprise (Cable TV provider, Telecom).</td><td>Distributed, collective ownership (Telecom consortiums, ISPs).</td></tr>
    <tr><td><b>Data Transfer Rate</b></td><td><b>Highest:</b> 1 Gbps to 10 Gbps.</td><td>Moderate: 100 Mbps to 1 Gbps.</td><td>Lowest: 10 Mbps to 1 Gbps across long-haul undersea fibers.</td></tr>
    <tr><td><b>Error Rate & Delay</b></td><td>Lowest error rates; sub-millisecond delay.</td><td>Moderate error rates and propagation delay.</td><td>Highest error rates; significant propagation delay (50-200 ms).</td></tr>
    <tr><td><b>Technology Example</b></td><td>Ethernet (IEEE 802.3), Wi-Fi (802.11).</td><td>FDDI, Cable TV Networks, Metro Ethernet.</td><td><b>The Global Internet</b>, ATM, Satellite Links.</td></tr>
</table>
""",

    "collision domain vs broadcast domain": """
<p><strong>Answer:</strong></p>
<table class=\"data-table\">
    <tr><th>Feature</th><th>Collision Domain</th><th>Broadcast Domain</th></tr>
    <tr><td><b>Definition</b></td><td>A network segment where simultaneous transmissions from two stations result in an electrical signal packet collision.</td><td>A network segment where a broadcast packet sent by one station is received by all other stations in that segment.</td></tr>
    <tr><td><b>Delimited By</b></td><td>Separated and broken up by <b>Switches, Bridges, and Routers</b> (Hubs do not break collision domains).</td><td>Separated and broken up <b>ONLY by Routers and VLANs</b> (Hubs and Switches forward broadcasts).</td></tr>
    <tr><td><b>OSI Layer</b></td><td>Data Link Layer (Layer 2) / Physical Layer (Layer 1).</td><td>Network Layer (Layer 3).</td></tr>
    <tr><td><b>Switch Behavior</b></td><td>Each individual switch port forms an isolated collision domain.</td><td>All ports on a switch belong to a single default broadcast domain.</td></tr>
</table>
""",

    "differentiate between bridges and repeaters": """
<p><strong>Answer:</strong></p>
<table class=\"data-table\">
    <tr><th>Feature</th><th>Repeater</th><th>Bridge</th></tr>
    <tr><td><b>OSI Layer</b></td><td>Operates strictly at the <b>Physical Layer (Layer 1)</b>.</td><td>Operates at the <b>Data Link Layer (Layer 2)</b>.</td></tr>
    <tr><td><b>Functionality</b></td><td>Amplifies, regenerates, and retimes electrical/optical signals to overcome cable attenuation.</td><td>Inspects MAC addresses, filters frames, and forwards traffic across network segments.</td></tr>
    <tr><td><b>Intelligence</b></td><td>Zero intelligence; cannot inspect packet headers or MAC addresses.</td><td>Intelligent; maintains dynamic MAC Address Table (CAM) in memory.</td></tr>
    <tr><td><b>Collision Domain</b></td><td>Extends the single collision domain (does not break it).</td><td><b>Divides collision domains</b> into separate segments.</td></tr>
    <tr><td><b>Data Unit Handled</b></td><td>Individual electrical bits (0s and 1s).</td><td>Frames (packets with MAC addresses and CRC).</td></tr>
</table>
""",

    "services provided by the transport layer": """
<p><strong>Answer:</strong></p>
<p>The <b>Transport Layer (Layer 4)</b> is the core of the OSI architecture providing transparent, logical, end-to-end communication between application processes running on distinct hosts.</p>
<div class=\"info-box\">
    <p><b>Five Core Services:</b></p>
    <ol>
        <li><b>Port Addressing (Service Point Addressing):</b> Identifies specific communicating software processes using 16-bit Port Numbers (e.g., Port 80 for HTTP, Port 22 for SSH).</li>
        <li><b>Segmentation and Reassembly:</b> Divides large application messages into smaller numbered segments at sender, and accurately reconstructs them at receiver.</li>
        <li><b>Connection Management:</b> Provides either reliable connection-oriented transport (TCP 3-Way Handshake) or fast connectionless transport (UDP).</li>
        <li><b>Flow Control:</b> Regulates data transmission speed using Sliding Window buffers to prevent fast senders from overwhelming slow receivers.</li>
        <li><b>Error Control & Recovery:</b> Verifies end-to-end data integrity via Checksums and initiates retransmissions for lost or damaged segments.</li>
    </ol>
</div>
""",

    "shannon capacity theorem": """
<p><strong>Answer:</strong></p>
<p><b>Shannon's Channel Capacity Theorem</b> establishes the absolute theoretical upper limit on the maximum data rate (in bits per second) that can be transmitted over a noisy analog communication channel without uncorrectable errors.</p>
<div class=\"info-box\">
    <p><b>Shannon's Formula:</b></p>
    <p style=\"font-size:1.1rem; font-weight:bold; color:#1e40af; text-align:center;\">C = B &times; log<sub>2</sub>(1 + SNR)</p>
    <ul>
        <li><b>C:</b> Channel Capacity in bits per second (bps).</li>
        <li><b>B:</b> Channel Bandwidth in Hertz (Hz).</li>
        <li><b>SNR:</b> Signal-to-Noise Ratio (linear power ratio: <i>P<sub>signal</sub> / P<sub>noise</sub></i>).</li>
    </ul>
    <p><i>Note on SNR:</i> If SNR is given in decibels (dB): <code>SNR<sub>dB</sub> = 10 &times; log<sub>10</sub>(SNR)</code>. For example, a 30 dB SNR corresponds to linear SNR = 1000.</p>
</div>
""",

    "bit rate vs baud rate": """
<p><strong>Answer:</strong></p>
<table class=\"data-table\">
    <tr><th>Feature</th><th>Bit Rate</th><th>Baud Rate (Modulation Rate)</th></tr>
    <tr><td><b>Definition</b></td><td>The total number of binary data bits (0s and 1s) transmitted per second.</td><td>The total number of signal units or voltage state transitions (symbols) per second.</td></tr>
    <tr><td><b>Unit</b></td><td>Bits per second (bps, kbps, Mbps).</td><td>Baud (or symbols/second).</td></tr>
    <tr><td><b>Relationship Formula</b></td><td colspan=\"2\" style=\"text-align:center;\"><b>Bit Rate = Baud Rate &times; N</b> &nbsp; (where <i>N = log<sub>2</sub> M</i> is bits encoded per signal element)</td></tr>
    <tr><td><b>Example</b></td><td colspan=\"2\">In 16-QAM modulation, each signal symbol represents <i>log<sub>2</sub>(16) = 4 bits</i>. If Baud Rate is 1000 Baud, the Bit Rate is: <code>1000 &times; 4 = 4000 bps</code>.</td></tr>
</table>
""",

    # ==================== DBMS ====================
    "given tables: play(playcode, playname, dirnum)": """
<p><strong>Answer:</strong></p>
<p><b>Given Relational Schema:</b></p>
<ul>
    <li><code>PLAY(<u>PlayCode</u>, PlayName, DirNum)</code> &mdash; DirNum is Foreign Key referencing DIRECTOR</li>
    <li><code>DIRECTOR(<u>DirNum</u>, DirName, DirDOB)</code> &mdash; DirNum is Primary Key</li>
</ul>
<div class=\"info-box\">
    <p class=\"step-label\">(i) Display all Director names and their respective Date of Birth:</p>
    <div class=\"code-box\">SELECT DirName, DirDOB FROM DIRECTOR;</div>

    <p class=\"step-label\">(ii) Display all Play names directed by director named 'Christopher Nolan':</p>
    <div class=\"code-box\">SELECT P.PlayName 
FROM PLAY P 
JOIN DIRECTOR D ON P.DirNum = D.DirNum 
WHERE D.DirName = 'Christopher Nolan';</div>

    <p class=\"step-label\">(iii) Count total number of plays directed by each Director:</p>
    <div class=\"code-box\">SELECT D.DirName, COUNT(P.PlayCode) AS TotalPlays 
FROM DIRECTOR D 
LEFT JOIN PLAY P ON D.DirNum = P.DirNum 
GROUP BY D.DirNum, D.DirName;</div>

    <p class=\"step-label\">(iv) Find director names who have directed more than 2 plays:</p>
    <div class=\"code-box\">SELECT D.DirName 
FROM DIRECTOR D 
JOIN PLAY P ON D.DirNum = P.DirNum 
GROUP BY D.DirNum, D.DirName 
HAVING COUNT(P.PlayCode) &gt; 2;</div>
</div>
""",

    "given tables: dept(deptno, dname, loc)": """
<p><strong>Answer:</strong></p>
<p><b>Given Relational Schema:</b></p>
<ul>
    <li><code>DEPT(<u>Deptno</u>, Dname, Loc)</code></li>
    <li><code>PROJECT(<u>Projno</u>, Deptno, Projname)</code> &mdash; Deptno references DEPT</li>
</ul>
<div class=\"info-box\">
    <p class=\"step-label\">(i) Display all project names handled by the 'Research' department:</p>
    <div class=\"code-box\">SELECT P.Projname 
FROM PROJECT P 
JOIN DEPT D ON P.Deptno = D.Deptno 
WHERE D.Dname = 'Research';</div>

    <p class=\"step-label\">(ii) List department names situated in location 'Delhi' with their project counts:</p>
    <div class=\"code-box\">SELECT D.Dname, COUNT(P.Projno) AS ProjectCount 
FROM DEPT D 
LEFT JOIN PROJECT P ON D.Deptno = P.Deptno 
WHERE D.Loc = 'Delhi' 
GROUP BY D.Deptno, D.Dname;</div>

    <p class=\"step-label\">(iii) Find departments that have zero active projects assigned:</p>
    <div class=\"code-box\">SELECT D.Deptno, D.Dname 
FROM DEPT D 
WHERE D.Deptno NOT IN (SELECT DISTINCT Deptno FROM PROJECT WHERE Deptno IS NOT NULL);</div>

    <p class=\"step-label\">(iv) Insert a new Project 'AI Assistant' under Deptno 10:</p>
    <div class=\"code-box\">INSERT INTO PROJECT (Projno, Deptno, Projname) 
VALUES ('PRJ99', 10, 'AI Assistant');</div>
</div>
""",

    "deadlock detection and prevention methods in dbms": """
<p><strong>Answer:</strong></p>
<p>A <b>Deadlock</b> is a condition where two or more transactions are in a simultaneous circular wait state, each holding locks that the other requires to proceed.</p>
<div class=\"info-box\">
    <p class=\"step-label\">1. Deadlock Prevention Strategies (Timestamp-Based):</p>
    <ul>
        <li><b>Wait-Die Scheme (Non-Preemptive):</b> If older transaction <i>T<sub>i</sub></i> requests a lock held by younger <i>T<sub>j</sub></i>, <i>T<sub>i</sub></i> is allowed to <b>wait</b>. If younger requests from older, younger <b>dies</b> (aborts and restarts with original timestamp).</li>
        <li><b>Wound-Wait Scheme (Preemptive):</b> If older requests from younger, older <b>wounds</b> (preempts/aborts) younger. If younger requests from older, younger is allowed to <b>wait</b>.</li>
    </ul>
    <p class=\"step-label\">2. Deadlock Detection & Recovery:</p>
    <ul>
        <li><b>Wait-For Graph (WFG):</b> Directed graph where nodes represent active transactions. Directed edge <i>T<sub>1</sub> &rarr; T<sub>2</sub></i> indicates <i>T<sub>1</sub></i> is waiting for <i>T<sub>2</sub></i>. A <b>cycle in the WFG signals a deadlock</b>.</li>
        <li><b>Deadlock Recovery:</b> Pick a victim transaction based on lowest rollback cost, abort it, release its locks, and restart it.</li>
    </ul>
</div>
""",

    "differentiate between association and aggregation": """
<p><strong>Answer:</strong></p>
<table class=\"data-table\">
    <tr><th>Feature</th><th>Association</th><th>Aggregation</th></tr>
    <tr><td><b>Concept</b></td><td>A generic structural relationship between two independent classes (\"knows-a\" relationship).</td><td>A specialized form of association representing a whole-part relationship (\"has-a\" relationship).</td></tr>
    <tr><td><b>Ownership & Lifetime</b></td><td>Both objects have independent lifecycles; neither owns the other.</td><td>The parent (\"whole\") contains the child (\"part\"), but the child can exist independently of the parent.</td></tr>
    <tr><td><b>Tightness of Coupling</b></td><td>Loose coupling.</td><td>Moderate coupling (weaker than Composition where parent death destroys children).</td></tr>
    <tr><td><b>Real-World Example</b></td><td><b>Teacher and Student:</b> A Teacher associates with a Student, but both exist independently.</td><td><b>Department and Teacher:</b> A Department aggregates Teachers. If Department closes, Teachers still exist.</td></tr>
</table>
""",

    "what is rdbms": """
<p><strong>Answer:</strong></p>
<p>A <b>Relational Database Management System (RDBMS)</b> is a database system founded on E.F. Codd's Relational Model (1970) where data is structured into two-dimensional tables (relations) consisting of rows (tuples) and columns (attributes).</p>
<div class=\"info-box\">
    <p><b>Core Pillars of RDBMS:</b></p>
    <ul>
        <li><b>Relational Integrity:</b> Enforces Entity Integrity (Primary Keys cannot be null) and Referential Integrity (Foreign Keys).</li>
        <li><b>SQL Interface:</b> Standardized declarative language for DDL, DML, and DCL commands.</li>
        <li><b>Full ACID Compliance:</b> Guarantees Atomicity, Consistency, Isolation, and Durability across concurrent transactions.</li>
        <li><b>Commercial Examples:</b> Oracle Database, Microsoft SQL Server, MySQL, PostgreSQL, SQLite.</li>
    </ul>
</div>
""",

    "what is a weak entity set": """
<p><strong>Answer:</strong></p>
<p>A <b>Weak Entity Set</b> is an entity set that does not possess sufficient attributes to form a Primary Key of its own. It is existentially dependent on a parent <b>Identifying (Owner) Entity Set</b>.</p>
<div class=\"info-box\">
    <p><b>Identification & Diagrammatic Representation:</b></p>
    <ul>
        <li><b>Discriminator (Partial Key):</b> The set of attributes that distinguishes weak entities belonging to the same owner entity. Underlined with a <b>dashed / dotted line</b>.</li>
        <li><b>Primary Key Composition:</b> Formed by combining the <b>Primary Key of the Identifying Entity + Discriminator</b>.</li>
        <li><b>ER Diagram Notation:</b>
            <ul>
                <li>Weak Entity Box: <b>Double Rectangle</b>.</li>
                <li>Identifying Relationship: <b>Double Diamond</b>.</li>
                <li>Total Participation: <b>Double Line</b>.</li>
            </ul>
        </li>
        <li><i>Example:</i> <code>DEPENDENT(<u>EmpID</u>, <u>DepName</u>, Age, Relation)</code> where <code>EmpID</code> is borrowed from <code>EMPLOYEE</code>.</li>
    </ul>
</div>
""",

    "natural join and theta join": """
<p><strong>Answer:</strong></p>
<table class=\"data-table\">
    <tr><th>Feature</th><th>Theta Join (&theta;-Join)</th><th>Natural Join (&bowtie;)</th></tr>
    <tr><td><b>Join Condition</b></td><td>Allows arbitrary comparison operators (<code>=</code>, <code>&lt;</code>, <code>&gt;</code>, <code>&le;</code>, <code>&ge;</code>, <code>&ne;</code>).</td><td>Strictly tests equality (<code>=</code>) on attributes sharing identical names.</td></tr>
    <tr><td><b>Duplicate Columns</b></td><td>Retains both common columns in the output relation (redundant columns).</td><td><b>Automatically eliminates duplicate columns</b>; retains only one instance of shared attributes.</td></tr>
    <tr><td><b>Syntax & Notation</b></td><td><code>R &bowtie;<sub>R.A &theta; S.B</sub> S</code></td><td><code>R &bowtie; S</code> (no explicit condition required).</td></tr>
    <tr><td><b>Relational Equivalence</b></td><td>Equivalent to Cartesian Product followed by Selection: <code>&sigma;<sub>Predicate</sub> (R &times; S)</code>.</td><td>Equivalent to Equi-Join followed by Projection removing duplicate attribute.</td></tr>
</table>
""",

    "commit and rollback commands in sql": """
<p><strong>Answer:</strong></p>
<p><code>COMMIT</code> and <code>ROLLBACK</code> are Transaction Control Language (TCL) commands that preserve the ACID properties of database transactions:</p>
<table class=\"data-table\">
    <tr><th>Command</th><th>Syntax</th><th>Operational Behavior</th></tr>
    <tr><td><b>COMMIT</b></td><td><code>COMMIT;</code></td><td>Permanently saves all changes made by the transaction to disk. Once committed, changes are durable and cannot be undone. Releases all held locks.</td></tr>
    <tr><td><b>ROLLBACK</b></td><td><code>ROLLBACK;</code><br><code>ROLLBACK TO savepoint_name;</code></td><td>Cancels all uncommitted modifications made by the active transaction, restoring the database back to its last clean committed state.</td></tr>
</table>
""",

    "what do you understand by hashing": """
<p><strong>Answer:</strong></p>
<p><b>Hashing</b> is an effective file organization and indexing technique that uses a mathematical algorithm (hash function <code>h(k)</code>) to compute direct physical block addresses from search key values.</p>
<div class=\"info-box\">
    <p><b>Key Concepts:</b></p>
    <ul>
        <li><b>Hash Function:</b> <code>h(Key) = Address</code>. Desirable properties: uniform distribution and random dispersion to avoid hotspots.</li>
        <li><b>Collision:</b> Occurs when two distinct keys hash to the same bucket address: <code>h(k<sub>1</sub>) = h(k<sub>2</sub>)</code>.</li>
        <li><b>Collision Resolution Methods:</b>
            <ol>
                <li><b>Open Addressing (Linear Probing):</b> Searches sequentially for the next available bucket.</li>
                <li><b>Chaining (Overflow Buckets):</b> Maintains a linked list of overflow disk blocks attached to the bucket.</li>
            </ol>
        </li>
        <li><b>Pros:</b> Constant time access <i>O(1)</i> for equality searches (<code>WHERE ID = 101</code>).</li>
    </ul>
</div>
""",

    "data redundancy": """
<p><strong>Answer:</strong></p>
<p><b>Data Redundancy</b> refers to the unnecessary duplication of the same piece of information across multiple files or tables in a database system.</p>
<div class=\"info-box\">
    <p><b>Major Problems Caused by Redundancy:</b></p>
    <ol>
        <li><b>Wasted Storage:</b> Storing identical department names and manager addresses thousands of times squanders disk space.</li>
        <li><b>Data Inconsistency:</b> If duplicate data is modified in one place but missed in another, conflicting records result.</li>
        <li><b>Operational Anomalies:</b> Causes Insertion, Deletion, and Update anomalies in relational tables.</li>
    </ol>
    <p><b>Elimination:</b> Controlled and eliminated through the process of <b>Relational Normalization (1NF through BCNF)</b>.</p>
</div>
""",

    "relational data model": """
<p><strong>Answer:</strong></p>
<p>Proposed by Dr. Edgar F. Codd in 1970, the <b>Relational Data Model</b> represents data in the form of mathematical two-dimensional tables called <b>Relations</b>.</p>
<div class=\"info-box\">
    <p><b>Fundamental Components:</b></p>
    <ul>
        <li><b>Relation (Table):</b> A set of rows representing an entity set.</li>
        <li><b>Tuple (Row):</b> A single record representing an individual entity instance.</li>
        <li><b>Attribute (Column):</b> A named field representing a property of the relation.</li>
        <li><b>Domain:</b> The set of all permissible atomic values for an attribute.</li>
        <li><b>Degree (Arity):</b> Total count of attributes (columns) in a relation.</li>
        <li><b>Cardinality:</b> Total count of tuples (rows) in a relation.</li>
    </ul>
</div>
"""
}
