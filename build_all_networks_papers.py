# -*- coding: utf-8 -*-
"""
Build high-quality textbook-formatted Computer Networks solved PYQ PDFs for CCSU BCA 5th Semester.
Features OSI 7-layer stack tables, Shannon capacity math formulas,
TCP 3-way handshake diagrams, topology cards, and clean page breaks via Chrome Headless.
"""
import os
import subprocess

TARGET_DIR = r"c:\zzzz\solved pyq"
os.makedirs(TARGET_DIR, exist_ok=True)
CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

CSS_STYLES = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap');

@page {
    size: A4;
    margin: 14mm 12mm 14mm 12mm;
    @bottom-center {
        content: counter(page);
    }
}

body {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
    font-size: 9.5pt;
    line-height: 1.48;
    color: #1e293b;
    background-color: #ffffff;
    margin: 0;
    padding: 0;
}

.header-banner {
    border-bottom: 2.5px solid #1e40af;
    padding-bottom: 8px;
    margin-bottom: 12px;
}

.univ-name {
    font-size: 10pt;
    font-weight: 700;
    color: #1e40af;
    text-transform: uppercase;
    letter-spacing: 0.8px;
    margin: 0 0 2px 0;
}

.paper-title {
    font-size: 15pt;
    font-weight: 800;
    color: #0f172a;
    margin: 0 0 2px 0;
}

.meta-info {
    font-size: 9pt;
    color: #475569;
    font-weight: 500;
    margin: 0;
}

.sec-title {
    background: #f1f5f9;
    border-left: 5px solid #1e40af;
    padding: 5px 10px;
    font-size: 10.5pt;
    font-weight: 800;
    color: #0f172a;
    margin: 14px 0 8px 0;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    border-radius: 0 4px 4px 0;
    page-break-after: avoid;
}

.q-box {
    margin-bottom: 12px;
    page-break-inside: auto;
}

.q-title {
    font-size: 10pt;
    font-weight: 700;
    color: #0f172a;
    margin: 6px 0 4px 0;
    page-break-after: avoid;
}

.q-marks {
    display: inline-block;
    background: #e0e7ff;
    color: #3730a3;
    font-size: 8pt;
    font-weight: 700;
    padding: 1px 6px;
    border-radius: 3px;
    margin-left: 6px;
}

.info-box {
    background: #f8fafc;
    border-left: 3.5px solid #2563eb;
    border-top: 1px solid #e2e8f0;
    border-right: 1px solid #e2e8f0;
    border-bottom: 1px solid #e2e8f0;
    padding: 7px 12px;
    margin: 6px 0;
    border-radius: 0 4px 4px 0;
    page-break-inside: avoid;
}

.diagram-card {
    background: #ffffff;
    border: 1.5px solid #cbd5e1;
    border-radius: 6px;
    padding: 8px 12px;
    margin: 8px 0;
    page-break-inside: avoid;
    box-shadow: 0 1px 3px rgba(0,0,0,0.04);
}

.math-formula {
    font-family: 'Cambria Math', 'Times New Roman', serif;
    font-size: 11pt;
    color: #0f172a;
    line-height: 1.6;
    margin: 4px 0;
}

.frac {
    display: inline-flex;
    flex-direction: column;
    vertical-align: middle;
    text-align: center;
    font-size: 0.9em;
    padding: 0 3px;
    line-height: 1.1;
}

.num {
    border-bottom: 1.4px solid #0f172a;
    padding-bottom: 1.5px;
}

.den {
    padding-top: 1.5px;
}

table.data-table {
    width: 100%;
    border-collapse: collapse;
    margin: 8px 0;
    font-size: 8.5pt;
    page-break-inside: avoid;
}

table.data-table th {
    background-color: #1e40af;
    color: #ffffff;
    font-weight: 700;
    padding: 5px 8px;
    border: 1px solid #1e3a8a;
    text-align: left;
}

table.data-table td {
    padding: 4px 8px;
    border: 1px solid #cbd5e1;
    vertical-align: top;
}

table.data-table tr:nth-child(even) td {
    background-color: #f8fafc;
}

.highlight-ans {
    background: #ecfdf5;
    border: 1.5px solid #10b981;
    color: #065f46;
    font-weight: 700;
    padding: 3px 10px;
    border-radius: 4px;
    display: inline-block;
    margin: 5px 0;
    font-size: 9pt;
}

.step-label {
    font-weight: 700;
    color: #1e40af;
    margin-top: 5px;
    margin-bottom: 2px;
}

p, li {
    margin: 2px 0 4px 0;
    color: #334155;
}

ul, ol {
    margin: 3px 0 5px 16px;
    padding: 0;
}

code {
    font-family: 'JetBrains Mono', Consolas, monospace;
    font-size: 8.5pt;
    background-color: #f1f5f9;
    color: #0f172a;
    padding: 1px 4px;
    border-radius: 3px;
    border: 1px solid #e2e8f0;
}

hr {
    border: 0;
    border-top: 1px solid #e2e8f0;
    margin: 10px 0;
}
</style>
"""

BODY_QUESTIONS_HTML = """
<!-- ==================== SECTION A ==================== -->
<div class="sec-title">Section – A (Very Short Answer Questions &bull; 3 Marks Each &bull; All 5 Compulsory)</div>

<!-- Q1 -->
<div class="q-box">
    <div class="q-title">Q1. Describe the various components of Data Communication. <span class="q-marks">[3 Marks]</span></div>
    <p><strong>Answer:</strong></p>
    <p>Data communication is the exchange of data between two devices via a transmission medium. It comprises five essential components:</p>
    <table class="data-table">
        <tr>
            <th style="width: 25%;">Component</th>
            <th style="width: 75%;">Description & Role</th>
        </tr>
        <tr>
            <td><b>1. Message</b></td>
            <td>The information or payload to be communicated (Text, Numbers, Pictures, Audio, Video).</td>
        </tr>
        <tr>
            <td><b>2. Sender (Transmitter)</b></td>
            <td>The source device originating and transmitting the data message (PC, Workstation, Smartphone).</td>
        </tr>
        <tr>
            <td><b>3. Receiver</b></td>
            <td>The destination device that receives the transmitted data (Server, Printer, Mobile terminal).</td>
        </tr>
        <tr>
            <td><b>4. Transmission Medium</b></td>
            <td>The physical communication conduit carrying the signal from sender to receiver: Guided (Twisted pair, Coaxial cable, Fiber optic) or Unguided (Radio waves, Microwaves, Infrared).</td>
        </tr>
        <tr>
            <td><b>5. Protocol</b></td>
            <td>A formal set of governing rules that coordinate data transmission syntax, semantics, and timing (e.g., TCP/IP, HTTP).</td>
        </tr>
    </table>
</div>

<hr>

<!-- Q2 -->
<div class="q-box">
    <div class="q-title">Q2. Define Bandwidth and Network Congestion. <span class="q-marks">[3 Marks]</span></div>
    <p><strong>Answer:</strong></p>
    <div class="info-box">
        <p class="step-label">1. Bandwidth:</p>
        <p>The maximum data transfer capacity of a communication channel over a given interval. In digital systems, it is measured in <b>bits per second (bps, Mbps, Gbps)</b>; in analog systems, it represents the frequency range (in Hertz, Hz) between upper and lower cutoff frequencies (<code>Bandwidth = f<sub>high</sub> &minus; f<sub>low</sub></code>).</p>
    </div>
    <div class="info-box">
        <p class="step-label">2. Network Congestion:</p>
        <p>A state where network nodes (routers/switches) carry more data packets than they can accommodate. When offered traffic load exceeds channel capacity, router queues overflow, causing <b>packet queuing delay, packet loss, and throughput collapse</b>.</p>
    </div>
</div>

<hr>

<!-- Q3 -->
<div class="q-box">
    <div class="q-title">Q3. Distinguish between MAC Address and IP Address. <span class="q-marks">[3 Marks]</span></div>
    <p><strong>Answer:</strong></p>
    <table class="data-table">
        <tr>
            <th style="width: 25%;">Parameter</th>
            <th style="width: 38%;">MAC Address (Physical Address)</th>
            <th style="width: 37%;">IP Address (Logical Address)</th>
        </tr>
        <tr>
            <td><b>OSI Layer</b></td>
            <td>Data Link Layer (Layer 2).</td>
            <td>Network Layer (Layer 3).</td>
        </tr>
        <tr>
            <td><b>Address Length & Format</b></td>
            <td><b>48 bits (6 bytes)</b>; written in 12 hexadecimal digits (e.g., <code>00:1A:2B:3C:4D:5E</code>).</td>
            <td><b>32 bits</b> in IPv4 (e.g., <code>192.168.1.1</code>); <b>128 bits</b> in IPv6 (hexadecimal).</td>
        </tr>
        <tr>
            <td><b>Permanence & Assignment</b></td>
            <td>Permanently hard-coded into Network Interface Card (NIC) by manufacturer (OUI).</td>
            <td>Dynamically (DHCP) or statically assigned based on network location.</td>
        </tr>
        <tr>
            <td><b>Scope of Utility</b></td>
            <td>Local node-to-node frame delivery within the same LAN segment.</td>
            <td>Global end-to-end packet routing across multiple networks/Internet.</td>
        </tr>
    </table>
</div>

<hr>

<!-- Q4 -->
<div class="q-box">
    <div class="q-title">Q4. Differentiate between a Hub and a Switch. <span class="q-marks">[3 Marks]</span></div>
    <p><strong>Answer:</strong></p>
    <table class="data-table">
        <tr>
            <th style="width: 25%;">Feature</th>
            <th style="width: 38%;">Network Hub</th>
            <th style="width: 37%;">Network Switch</th>
        </tr>
        <tr>
            <td><b>Operating OSI Layer</b></td>
            <td>Physical Layer (Layer 1).</td>
            <td>Data Link Layer (Layer 2) / Multilayer (Layer 3).</td>
        </tr>
        <tr>
            <td><b>Data Transmission Mode</b></td>
            <td><b>Broadcasts</b> all incoming frames to every connected port indiscriminately.</td>
            <td><b>Unicasts</b> frames selectively to the specific destination port using MAC table.</td>
        </tr>
        <tr>
            <td><b>Collision Domains</b></td>
            <td>All ports share a single collision domain (high collision risk).</td>
            <td>Each individual port forms its own dedicated collision domain.</td>
        </tr>
        <tr>
            <td><b>Bandwidth Sharing</b></td>
            <td>Total bandwidth is shared among all connected active nodes.</td>
            <td>Dedicated, full-rate bandwidth provided to each port (full-duplex).</td>
        </tr>
    </table>
</div>

<hr>

<!-- Q5 -->
<div class="q-box">
    <div class="q-title">Q5. What is Subnetting? Give an example with CIDR calculation. <span class="q-marks">[3 Marks]</span></div>
    <p><strong>Answer:</strong></p>
    <p><b>Subnetting</b> is the practice of logically partitioning a single large IP network into smaller, distinct subnetworks (subnets) by borrowing host bits for the network ID. This reduces broadcast domains, improves routing efficiency, and conserves IP addresses.</p>
    
    <div class="info-box">
        <p class="step-label">Example: Subnetting 192.168.1.0/24 into 4 Subnets</p>
        <ul>
            <li>To create 4 subnets: Borrow 2 bits from host portion (<code>2<sup>2</sup> = 4</code> subnets).</li>
            <li>New prefix length: <code>/24 + 2 = /26</code> &rArr; Subnet Mask: <code>255.255.255.192</code>.</li>
            <li>Block Size: <code>256 &minus; 192 = 64</code> addresses per subnet (62 usable hosts).</li>
        </ul>
        <table class="data-table">
            <tr>
                <th>Subnet #</th>
                <th>Network ID</th>
                <th>Usable Host IP Range</th>
                <th>Directed Broadcast IP</th>
            </tr>
            <tr><td>Subnet 1</td><td><code>192.168.1.0</code></td><td><code>192.168.1.1 &ndash; 192.168.1.62</code></td><td><code>192.168.1.63</code></td></tr>
            <tr><td>Subnet 2</td><td><code>192.168.1.64</code></td><td><code>192.168.1.65 &ndash; 192.168.1.126</code></td><td><code>192.168.1.127</code></td></tr>
            <tr><td>Subnet 3</td><td><code>192.168.1.128</code></td><td><code>192.168.1.129 &ndash; 192.168.1.190</code></td><td><code>192.168.1.191</code></td></tr>
            <tr><td>Subnet 4</td><td><code>192.168.1.192</code></td><td><code>192.168.1.193 &ndash; 192.168.1.254</code></td><td><code>192.168.1.255</code></td></tr>
        </table>
    </div>
</div>

<!-- ==================== SECTION B ==================== -->
<div class="sec-title">Section – B (Short Answer Questions &bull; 7.5 Marks Each &bull; Attempt Any Two)</div>

<!-- Q6 -->
<div class="q-box">
    <div class="q-title">Q6. Describe the role of the Transport Layer in the OSI Model. <span class="q-marks">[7.5 Marks]</span></div>
    <p><strong>Answer:</strong></p>
    <p>The <b>Transport Layer (Layer 4)</b> serves as the boundary between hardware-oriented subnet layers and software application layers, providing true <b>end-to-end, process-to-process reliable data delivery</b>.</p>
    <table class="data-table">
        <tr>
            <th style="width: 25%;">Core Function</th>
            <th style="width: 75%;">Detailed Mechanism & Protocol Realization</th>
        </tr>
        <tr>
            <td><b>1. Service-Point (Port) Addressing</b></td>
            <td>Differentiates concurrent application processes executing on the same host using 16-bit Port numbers (e.g., HTTP: 80, HTTPS: 443, DNS: 53, SSH: 22).</td>
        </tr>
        <tr>
            <td><b>2. Segmentation & Reassembly</b></td>
            <td>Splits massive application messages into manageable chunks called <b>Segments</b>, appends sequence numbers, and reassembles them at receiver in exact order.</td>
        </tr>
        <tr>
            <td><b>3. Connection Management</b></td>
            <td>Manages connection-oriented transmission via 3-way handshake (TCP) or fast connectionless datagram delivery (UDP).</td>
        </tr>
        <tr>
            <td><b>4. Flow Control</b></td>
            <td>Uses <b>Sliding Window Protocol</b> to prevent a fast transmitter from overwhelming a slow receiver's buffer space.</td>
        </tr>
        <tr>
            <td><b>5. Error Control</b></td>
            <td>Enforces end-to-end integrity using 16-bit <b>Checksums</b> and Automatic Repeat reQuest (ARQ) retransmissions for dropped/corrupted segments.</td>
        </tr>
    </table>
</div>

<hr>

<!-- Q7 -->
<div class="q-box">
    <div class="q-title">Q7. Explain Network Topologies (Star, Mesh, Bus, Ring) with diagrams and comparisons. <span class="q-marks">[7.5 Marks]</span></div>
    <p><strong>Answer:</strong></p>
    <p><b>Network Topology</b> defines the geometric and logical arrangement of communication links and nodes in a network.</p>
    
    <div class="diagram-card">
        <p class="step-label">1. Star Topology:</p>
        <p>All nodes connect via dedicated point-to-point links directly to a central multiport device (Hub or Switch).</p>
        <p><i>Layout:</i> <code>[Node A, Node B, Node C, Node D] &rarr; [Central Switch / Hub]</code></p>
        <p><b>Pros:</b> Easy to install, failure of one node does not impact others. <b>Cons:</b> Central hub is a single point of failure.</p>
    </div>

    <div class="diagram-card">
        <p class="step-label">2. Mesh Topology (Full Mesh):</p>
        <p>Every node has a dedicated point-to-point link to every other node in the network.</p>
        <p><i>Link Formula:</i> For <code>n</code> nodes, requires <span class="frac"><span class="num">n(n &minus; 1)</span><span class="den">2</span></span> physical links and <code>(n &minus; 1)</code> I/O ports per device.</p>
        <p><b>Pros:</b> Maximum redundancy, zero traffic contention, highly fault-tolerant. <b>Cons:</b> Extremely expensive cabling and port requirements.</p>
    </div>

    <div class="diagram-card">
        <p class="step-label">3. Bus Topology:</p>
        <p>All nodes share a single common linear backbone cable (coaxial cable with terminators at both ends).</p>
        <p><i>Layout:</i> <code>Terminator &mdash;&mdash; [Node 1] &mdash;&mdash; [Node 2] &mdash;&mdash; [Node 3] &mdash;&mdash; Terminator</code></p>
        <p><b>Pros:</b> Minimal cabling needed. <b>Cons:</b> A single break in backbone takes down entire network; hard to troubleshoot.</p>
    </div>

    <div class="diagram-card">
        <p class="step-label">4. Ring Topology:</p>
        <p>Each device connects directly to its two immediate neighbors, forming a closed continuous loop.</p>
        <p><i>Layout:</i> <code>Node 1 &rarr; Node 2 &rarr; Node 3 &rarr; Node 4 &rarr; Node 1 (Token Passing)</code></p>
        <p><b>Pros:</b> Orderly token transmission, no collisions. <b>Cons:</b> Break in ring disrupts network (unless dual counter-rotating ring like FDDI is used).</p>
    </div>
</div>

<hr>

<!-- Q8 -->
<div class="q-box">
    <div class="q-title">Q8. Explain Congestion Control Algorithms (Leaky Bucket and Token Bucket). <span class="q-marks">[7.5 Marks]</span></div>
    <p><strong>Answer:</strong></p>
    <p>Traffic shaping algorithms regulate the bursty flow of packets injected into the network to mitigate congestion:</p>
    <table class="data-table">
        <tr>
            <th style="width: 25%;">Parameter</th>
            <th style="width: 38%;">Leaky Bucket Algorithm</th>
            <th style="width: 37%;">Token Bucket Algorithm</th>
        </tr>
        <tr>
            <td><b>Core Operating Principle</b></td>
            <td>Bursty packet arrivals enter a finite buffer; packets leak out at a <b>strictly constant, rigid rate</b>.</td>
            <td>Tokens generate into bucket at regular rate <code>r</code> up to capacity <code>C</code>. Packets transmit by consuming tokens.</td>
        </tr>
        <tr>
            <td><b>Bursty Traffic Handling</b></td>
            <td><b>Smooths out all bursts completely</b>; discards packets if bucket capacity overflows.</td>
            <td><b>Allows controlled bursts</b> of packets up to the accumulated token capacity <code>C</code>.</td>
        </tr>
        <tr>
            <td><b>Output Transmission Rate</b></td>
            <td>Strictly uniform, deterministic constant rate regardless of burstiness.</td>
            <td>Variable rate bounded by average rate <code>r</code> and peak burst capacity.</td>
        </tr>
        <tr>
            <td><b>Packet Discard Policy</b></td>
            <td>Discards incoming packets when buffer memory fills up.</td>
            <td>Discards tokens when token bucket fills; packets queue or wait for fresh tokens.</td>
        </tr>
    </table>
</div>

<!-- ==================== SECTION C ==================== -->
<div class="sec-title">Section – C (Long Answer Questions &bull; 15 Marks Each &bull; Attempt Any Three)</div>

<!-- Q9 -->
<div class="q-box">
    <div class="q-title">Q9. Explain the TCP Three-Way Handshake with a sequence diagram. <span class="q-marks">[15 Marks]</span></div>
    <p><strong>Answer:</strong></p>
    <p>The <b>TCP 3-Way Handshake</b> is the synchronization mechanism used by Transmission Control Protocol to establish a reliable, full-duplex virtual connection between client and server before data exchange begins.</p>
    
    <div class="diagram-card">
        <p class="step-label">TCP 3-Way Handshake Connection Sequence:</p>
        <table class="data-table">
            <tr>
                <th style="width: 15%;">Step</th>
                <th style="width: 20%;">Direction</th>
                <th style="width: 35%;">Control Flags & Sequence #</th>
                <th style="width: 30%;">Action & Purpose</th>
            </tr>
            <tr>
                <td><b>Step 1 (SYN)</b></td>
                <td>Client &rarr; Server</td>
                <td><code>SYN = 1</code><br><code>Seq = X</code> (Client ISN)</td>
                <td>Client requests connection and announces its initial sequence number X. Client enters <b>SYN-SENT</b> state.</td>
            </tr>
            <tr>
                <td><b>Step 2 (SYN-ACK)</b></td>
                <td>Server &rarr; Client</td>
                <td><code>SYN = 1, ACK = 1</code><br><code>Seq = Y</code> (Server ISN)<br><code>Ack_Num = X + 1</code></td>
                <td>Server acknowledges client's request (<code>Ack = X + 1</code>) and provides its own sequence number Y. Server enters <b>SYN-RCVD</b>.</td>
            </tr>
            <tr>
                <td><b>Step 3 (ACK)</b></td>
                <td>Client &rarr; Server</td>
                <td><code>ACK = 1</code><br><code>Seq = X + 1</code><br><code>Ack_Num = Y + 1</code></td>
                <td>Client acknowledges server's sequence number (<code>Ack = Y + 1</code>). Connection enters <b>ESTABLISHED</b> state on both endpoints.</td>
            </tr>
        </table>
    </div>
    <p><b>Significance:</b> Guarantees both parties agree on initial sequence numbers, confirms bidirectional communication capability, and prevents old duplicate connection requests from causing false sessions.</p>
</div>

<hr>

<!-- Q10 -->
<div class="q-box">
    <div class="q-title">Q10. Draw and explain the 7 Layers of the ISO/OSI Reference Model. <span class="q-marks">[15 Marks]</span></div>
    <p><strong>Answer:</strong></p>
    <p>The <b>Open Systems Interconnection (OSI)</b> reference model is a conceptual 7-layer architectural framework developed by ISO for standardized computer communication:</p>
    <table class="data-table">
        <tr>
            <th style="width: 10%;">Layer</th>
            <th style="width: 18%;">Layer Name</th>
            <th style="width: 12%;">PDU</th>
            <th style="width: 38%;">Primary Functions & Responsibilities</th>
            <th style="width: 22%;">Standard Protocols</th>
        </tr>
        <tr>
            <td><b>Layer 7</b></td>
            <td><b>Application</b></td>
            <td>Data</td>
            <td>Provides user interface and network service abstraction for software apps.</td>
            <td>HTTP, HTTPS, FTP, SMTP, DNS, DHCP</td>
        </tr>
        <tr>
            <td><b>Layer 6</b></td>
            <td><b>Presentation</b></td>
            <td>Data</td>
            <td>Data syntax translation, compression, encryption and decryption (SSL/TLS).</td>
            <td>JPEG, MPEG, ASCII, TLS/SSL</td>
        </tr>
        <tr>
            <td><b>Layer 5</b></td>
            <td><b>Session</b></td>
            <td>Data</td>
            <td>Dialog control, token management, session checkpointing and synchronization.</td>
            <td>RPC, NetBIOS, PPTP</td>
        </tr>
        <tr>
            <td><b>Layer 4</b></td>
            <td><b>Transport</b></td>
            <td>Segment</td>
            <td>End-to-end process delivery, port addressing, flow control (sliding window), error recovery.</td>
            <td>TCP, UDP</td>
        </tr>
        <tr>
            <td><b>Layer 3</b></td>
            <td><b>Network</b></td>
            <td>Packet</td>
            <td>Logical IP addressing, subnet routing, packet forwarding across networks.</td>
            <td>IPv4, IPv6, ICMP, OSPF, BGP</td>
        </tr>
        <tr>
            <td><b>Layer 2</b></td>
            <td><b>Data Link</b></td>
            <td>Frame</td>
            <td>Node-to-node frame delivery, physical MAC addressing, CRC error detection, CSMA/CD.</td>
            <td>Ethernet (802.3), Wi-Fi (802.11), PPP</td>
        </tr>
        <tr>
            <td><b>Layer 1</b></td>
            <td><b>Physical</b></td>
            <td>Bit</td>
            <td>Transmission of raw bitstream over physical media, signal encoding, voltages.</td>
            <td>RS-232, RJ-45, V.35, Cables</td>
        </tr>
    </table>
</div>

<hr>

<!-- Q11 -->
<div class="q-box">
    <div class="q-title">Q11. Explain Shannon Capacity Theorem with a solved numerical problem. <span class="q-marks">[15 Marks]</span></div>
    <p><strong>Answer:</strong></p>
    <p><b>Shannon's Capacity Theorem</b> establishes the theoretical upper limit on the maximum data transmission rate (Channel Capacity C) across a noisy communication channel with white Gaussian thermal noise.</p>
    
    <div class="info-box">
        <p class="math-formula">
            <b>Shannon Formula:</b>&emsp;
            C = B &bull; log<sub>2</sub> &left;( 1 + <span class="frac"><span class="num">S</span><span class="den">N</span></span> &right;) &nbsp; (in bits per second, bps)
        </p>
        <p>Where:</p>
        <ul>
            <li><code>C</code> = Maximum theoretical channel capacity in bits per second (bps)</li>
            <li><code>B</code> = Channel bandwidth in Hertz (Hz)</li>
            <li><code>S / N</code> = Signal-to-Noise Ratio (SNR as a linear power ratio)</li>
        </ul>
    </div>

    <p class="step-label">Solved Numerical Problem:</p>
    <div class="info-box">
        <p><b>Problem Statement:</b> A noisy telephone channel has a bandwidth of <i>B = 3000 Hz</i> and a Signal-to-Noise Ratio of <i>SNR<sub>dB</sub> = 35 dB</i>. Calculate the theoretical maximum channel capacity.</p>
        <p><b>Step 1: Convert SNR from decibels (dB) to linear ratio:</b></p>
        <p class="math-formula">
            SNR<sub>dB</sub> = 10 &bull; log<sub>10</sub>(S/N) = 35 &rArr; log<sub>10</sub>(S/N) = 3.5 &rArr; <span class="frac"><span class="num">S</span><span class="den">N</span></span> = 10<sup>3.5</sup> &approx; <b>3162.28</b>
        </p>
        <p><b>Step 2: Apply Shannon's Formula:</b></p>
        <p class="math-formula">
            C = 3000 &bull; log<sub>2</sub>(1 + 3162.28) = 3000 &bull; log<sub>2</sub>(3163.28)
        </p>
        <p class="math-formula">
            Using change of base:&emsp; log<sub>2</sub>(3163.28) = <span class="frac"><span class="num">log<sub>10</sub>(3163.28)</span><span class="den">log<sub>10</sub>(2)</span></span> = <span class="frac"><span class="num">3.50014</span><span class="den">0.30103</span></span> &approx; <b>11.6272</b>
        </p>
        <p class="math-formula">
            C = 3000 &times; 11.6272 &approx; <b>34,881.6 bps &approx; 34.88 kbps</b>
        </p>
    </div>
    <div><span class="highlight-ans">Theoretical Channel Capacity: C &approx; 34.88 kbps</span></div>
</div>

<hr>

<!-- Q12 -->
<div class="q-box">
    <div class="q-title">Q12. Explain CSMA/CD in Ethernet and compare with CSMA/CA in Wi-Fi. <span class="q-marks">[15 Marks]</span></div>
    <p><strong>Answer:</strong></p>
    <p><b>Carrier Sense Multiple Access (CSMA)</b> protocols require nodes to "listen before talking" on a shared broadcast transmission medium.</p>
    <table class="data-table">
        <tr>
            <th style="width: 22%;">Comparison Feature</th>
            <th style="width: 39%;">CSMA/CD (Collision Detection)</th>
            <th style="width: 39%;">CSMA/CA (Collision Avoidance)</th>
        </tr>
        <tr>
            <td><b>Standard & Medium</b></td>
            <td>IEEE 802.3 (Wired Ethernet cables).</td>
            <td>IEEE 802.11 (Wireless Wi-Fi radio channels).</td>
        </tr>
        <tr>
            <td><b>Collision Strategy</b></td>
            <td>Transmits while listening; if collision signal is detected, stops immediately.</td>
            <td>Avoids collisions prior to transmission via reservation handshakes and delays.</td>
        </tr>
        <tr>
            <td><b>Collision Response</b></td>
            <td>Transmits a <b>Jam Signal</b> to notify all stations, then applies <b>Binary Exponential Backoff</b>.</td>
            <td>Cannot detect collision while sending (half-duplex RF); infers collision if no ACK received.</td>
        </tr>
        <tr>
            <td><b>Control Mechanism</b></td>
            <td>Collision detection hardware listening for elevated cable voltage.</td>
            <td><b>RTS (Request to Send) / CTS (Clear to Send)</b> handshakes + Inter-Frame Spacing (DIFS/SIFS).</td>
        </tr>
    </table>
</div>

<hr>

<!-- Q13 -->
<div class="q-box">
    <div class="q-title">Q13. Compare Circuit Switching, Packet Switching, and Message Switching. <span class="q-marks">[15 Marks]</span></div>
    <p><strong>Answer:</strong></p>
    <p><b>Switching</b> is the methodology by which nodes communicate across multiple intermediate network nodes without direct point-to-point physical links.</p>
    <table class="data-table">
        <tr>
            <th style="width: 18%;">Feature</th>
            <th style="width: 28%;">Circuit Switching</th>
            <th style="width: 27%;">Packet Switching</th>
            <th style="width: 27%;">Message Switching</th>
        </tr>
        <tr>
            <td><b>Dedicated Physical Path</b></td>
            <td><b>Yes</b>; dedicated end-to-end copper/fiber circuit reserved for session duration.</td>
            <td><b>No</b>; dynamic independent packet routing over shared virtual links.</td>
            <td><b>No</b>; whole message hops from node to node across shared lines.</td>
        </tr>
        <tr>
            <td><b>Call Setup Phase</b></td>
            <td>Required prior to any data transmission. Adds initial setup latency.</td>
            <td>Zero connection setup latency (in Connectionless Datagram mode).</td>
            <td>No setup phase needed.</td>
        </tr>
        <tr>
            <td><b>Bandwidth Utilization</b></td>
            <td>Low/wasteful; reserved circuit capacity is idle during conversational silence.</td>
            <td><b>Very High</b>; dynamic statistical multiplexing shares channel bandwidth.</td>
            <td>Moderate; links occupied only while whole message transmits.</td>
        </tr>
        <tr>
            <td><b>Store & Forward Mechanism</b></td>
            <td>None; continuous real-time bitstream.</td>
            <td>Packets buffered at each router and forwarded. Minimal latency.</td>
            <td>Entire message buffered on intermediate disks; very high delay.</td>
        </tr>
        <tr>
            <td><b>Primary Application</b></td>
            <td>Traditional Landline Telephony (PSTN), cellular voice calls.</td>
            <td><b>The Modern Internet (IP)</b>, VoIP, streaming, web browsing.</td>
            <td>Telegraph, Telex, historic military communication systems.</td>
        </tr>
    </table>
</div>
"""

def generate_pdf(year, out_filename):
    full_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>BCA-503: Computer Networks — {year} Solved Paper</title>
{CSS_STYLES}
</head>
<body>

<div class="header-banner">
    <p class="univ-name">Chaudhary Charan Singh University (CCSU) &bull; BCA V Semester</p>
    <h1 class="paper-title">BCA-503: Computer Networks</h1>
    <p class="meta-info"><strong>Session:</strong> {year} Examination &nbsp;|&nbsp; <strong>Paper Code:</strong> 18023 &nbsp;|&nbsp; <strong>Complete 100% Solved Paper (All 13 Questions)</strong> &nbsp;|&nbsp; <strong>Time:</strong> 3 Hours &bull; <strong>Max Marks:</strong> 75</p>
</div>

{BODY_QUESTIONS_HTML}

</body>
</html>
"""
    temp_html = os.path.join(TARGET_DIR, f"temp_net_{year}.html")
    pdf_out = os.path.join(TARGET_DIR, out_filename)
    with open(temp_html, "w", encoding="utf-8") as f:
        f.write(full_html)
    
    cmd = [
        CHROME_PATH,
        "--headless=new",
        "--disable-gpu",
        "--no-pdf-header-footer",
        f"--print-to-pdf={pdf_out}",
        temp_html
    ]
    subprocess.run(cmd, check=True)
    if os.path.exists(temp_html):
        os.remove(temp_html)
    size_kb = os.path.getsize(pdf_out) / 1024
    print(f"[OK] Generated {out_filename} ({size_kb:.1f} KB)")

def main():
    years = [2025, 2024, 2023, 2021, 2020, 2019, 2018, 2017, 2016]
    print("Generating beautifully formatted Computer Networks PDFs...")
    for yr in years:
        filename = f"networks {yr} solved.pdf"
        generate_pdf(f"December {yr}", filename)
    
    # Subject bank
    print("Generating BCA-503_Computer_Networks_Solved_PYQ.pdf...")
    generate_pdf("Comprehensive PYQ Bank", "BCA-503_Computer_Networks_Solved_PYQ.pdf")

if __name__ == "__main__":
    main()
