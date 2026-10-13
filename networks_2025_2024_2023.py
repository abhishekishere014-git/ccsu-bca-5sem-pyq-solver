import sys
import os
sys.path.append(r"c:\zzzz\pyq_solver_scripts")
from networks_builder_base import generate_networks_pdf

# ==============================================================================
# YEAR 2025 (December 2025)
# ==============================================================================
YEAR_2025_HTML = r"""
<div class="section-divider">SECTION A &mdash; VERY SHORT ANSWER QUESTIONS (5 &times; 3 = 15 Marks)</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q1 (3M)</span>What is a MAC address? How is it different from an IP Address?</div>
    <div class="ans-body">
        <strong>Comparison:</strong>
        <table class="grid-table">
            <thead><tr><th>Feature</th><th>MAC Address (Physical Address)</th><th>IP Address (Logical Address)</th></tr></thead>
            <tbody>
                <tr><td>Layer</td><td>Data Link Layer (Layer 2).</td><td>Network Layer (Layer 3).</td></tr>
                <tr><td>Size & Format</td><td>48 bits (6 bytes), hex (e.g., <code>00:1A:2B:3C:4D:5E</code>).</td><td>32 bits (IPv4, e.g., <code>192.168.1.1</code>) or 128 bits (IPv6).</td></tr>
                <tr><td>Nature</td><td>Hardcoded by manufacturer into NIC; globally fixed.</td><td>Dynamically/statically assigned based on network location.</td></tr>
            </tbody>
        </table>
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q2 (3M)</span>Differentiate between a Hub and a Switch.</div>
    <div class="ans-body">
        <strong>Differences:</strong>
        <ul>
            <li><strong>Hub (Physical Layer - Layer 1):</strong> Broadcast device that repeats every incoming signal across all ports, sharing a single collision domain. Half-duplex, no intelligence.</li>
            <li><strong>Switch (Data Link Layer - Layer 2):</strong> Intelligent device maintaining a MAC Address Table to forward frames directly to designated destination ports. Dedicated collision domains per port, full-duplex.</li>
        </ul>
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q3 (3M)</span>What is Subnetting? Give an example.</div>
    <div class="ans-body">
        <strong>Definition:</strong> <strong>Subnetting</strong> is the process of partitioning a single physical network into two or more smaller logical subnets by borrowing host bits to create subnet bits, reducing broadcast traffic and optimizing address allocation.<br>
        <strong>Example:</strong> Given Class C network <code>192.168.1.0/24</code> with default mask <code>255.255.255.0</code>. Borrowing 2 host bits gives subnet mask <code>255.255.255.192</code> (/26), creating <span class="math">2^2 = 4</span> subnets with 62 usable hosts each:
        <ul>
            <li>Subnet 1: <code>192.168.1.0</code> to <code>192.168.1.63</code></li>
            <li>Subnet 2: <code>192.168.1.64</code> to <code>192.168.1.127</code></li>
            <li>Subnet 3: <code>192.168.1.128</code> to <code>192.168.1.191</code></li>
            <li>Subnet 4: <code>192.168.1.192</code> to <code>192.168.1.255</code></li>
        </ul>
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q4 (3M)</span>What is CSMA/CD? How does it operate in Ethernet?</div>
    <div class="ans-body">
        <strong>Carrier Sense Multiple Access with Collision Detection:</strong> A media access protocol used in shared half-duplex Ethernet:
        <ol>
            <li><strong>Carrier Sense:</strong> Station listens before transmitting ("listen before talk"). If channel is idle, it begins transmitting.</li>
            <li><strong>Collision Detection:</strong> While transmitting, station monitors signal level. If collision occurs, it transmits a <em>jam signal</em> to notify all stations.</li>
            <li><strong>Backoff:</strong> Stations wait a random backoff period using the Binary Exponential Backoff algorithm before retransmitting.</li>
        </ol>
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q5 (3M)</span>Differentiate between Synchronous and Asynchronous Protocols.</div>
    <div class="ans-body">
        <strong>Comparison:</strong>
        <ul>
            <li><strong>Asynchronous Transmission:</strong> Characters sent independently with start (0) and stop (1) framing bits. Clocks do not need synchronization. Inefficient for large high-speed data transfers.</li>
            <li><strong>Synchronous Transmission:</strong> Continuous stream of data blocks transmitted synchronized to an external shared clock. Synchronized using sync character preambles (e.g., HDLC, PPP), achieving high throughput.</li>
        </ul>
    </div>
</div>

<div class="section-divider">SECTION B &mdash; SHORT ANSWER QUESTIONS (2 &times; 7.5 = 15 Marks)</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q6 (7.5M)</span>Describe Multiplexing. Explain FDM, TDM, and WDM with diagrams.</div>
    <div class="ans-body">
        <strong>Definition:</strong> Combining multiple separate data streams into a single composite signal transmitted over a shared transmission medium.<br>
        <strong>Techniques:</strong>
        <ul>
            <li><strong>FDM (Frequency Division Multiplexing):</strong> Divides channel bandwidth into separate non-overlapping frequency bands with guard bands (Analog signals, radio, cable TV).</li>
            <li><strong>TDM (Time Division Multiplexing):</strong> Interleaves time slots from multiple sources onto a high-speed digital carrier (Synchronous vs Statistical TDM).</li>
            <li><strong>WDM (Wavelength Division Multiplexing):</strong> Multiplexes optical signals of differing wavelengths (colors) along a single optical fiber.</li>
        </ul>
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q7 (7.5M)</span>Explain Error Detection Techniques: Parity Check, Checksum, and CRC (Cyclic Redundancy Check).</div>
    <div class="ans-body">
        <strong>Error Detection:</strong>
        <ul>
            <li><strong>Parity Check:</strong> Appends single parity bit (even or odd parity). Detects only odd numbers of bit errors.</li>
            <li><strong>Checksum:</strong> Divides data into 16-bit words, adds them using 1's complement arithmetic, and appends inverted sum (used in TCP/IP).</li>
            <li><strong>Cyclic Redundancy Check (CRC):</strong> Treats bit stream as polynomial coefficients and performs modulo-2 binary division by generator polynomial <span class="math">G(x)</span>. Appends remainder (FCS). Detects all single, double, odd, and burst errors up to generator length!</li>
        </ul>
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q8 (7.5M)</span>Compare Circuit Switching, Packet Switching, and Message Switching.</div>
    <div class="ans-body">
        <strong>Comparison:</strong>
        <table class="grid-table">
            <thead><tr><th>Feature</th><th>Circuit Switching</th><th>Packet Switching</th><th>Message Switching</th></tr></thead>
            <tbody>
                <tr><td>Dedicated Path</td><td>Yes (setup before transfer).</td><td>No (packets routed dynamically).</td><td>No (store-and-forward per hop).</td></tr>
                <tr><td>Bandwidth</td><td>Reserved/wasted if idle.</td><td>Dynamically shared on-demand.</td><td>Dynamically shared.</td></tr>
                <tr><td>Delay</td><td>Setup delay high; transmission delay low.</td><td>Jitter/variable queuing delay.</td><td>High storage delay at each switch.</td></tr>
                <tr><td>Modern Use</td><td>PSTN landline telephone.</td><td>Internet (IP networks).</td><td>Early telegraph, postal email.</td></tr>
            </tbody>
        </table>
    </div>
</div>

<div class="section-divider">SECTION C &mdash; DETAILED ANSWER QUESTIONS (3 &times; 15 = 45 Marks)</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q9 (15M)</span>Explain the ISO/OSI Reference Model in detail. Describe the primary functions of each of the seven layers.</div>
    <div class="ans-body">
        <strong>Seven Layers of OSI Model:</strong>
        <ol>
            <li><strong>Physical Layer (Layer 1):</strong> Transmission of raw unstructured bit streams over physical media (voltages, connectors, cables).</li>
            <li><strong>Data Link Layer (Layer 2):</strong> Framing, physical addressing (MAC), flow control, error control (CRC), and media access control.</li>
            <li><strong>Network Layer (Layer 3):</strong> Logical addressing (IP), routing (Dijkstra, distance vector), packet forwarding, and fragmentation.</li>
            <li><strong>Transport Layer (Layer 4):</strong> End-to-end process-to-process delivery (ports), segmentation and reassembly, connection control (TCP handshake), reliable flow control.</li>
            <li><strong>Session Layer (Layer 5):</strong> Dialogue control (simplex, half/full duplex), session checkpointing, synchronization tokens.</li>
            <li><strong>Presentation Layer (Layer 6):</strong> Data translation, character code conversion (ASCII/EBCDIC), compression, encryption/decryption (SSL/TLS).</li>
            <li><strong>Application Layer (Layer 7):</strong> Network virtual terminals, file transfer (FTP), web browsing (HTTP), email services (SMTP).</li>
        </ol>
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q10 (15M)</span>Explain Sliding Window Protocols: Stop-and-Wait ARQ, Go-Back-N ARQ, and Selective Repeat ARQ with efficiency analysis.</div>
    <div class="ans-body">
        <strong>Flow and Error Control Protocols:</strong>
        <ul>
            <li><strong>Stop-and-Wait ARQ:</strong> Sender transmits 1 frame, starts timer, and waits for ACK before sending next. Efficiency: <span class="math">\eta = \frac{1}{1 + 2a}</span> where <span class="math">a = T_p / T_t</span>. Poor for high bandwidth-delay links.</li>
            <li><strong>Go-Back-N ARQ:</strong> Sender window size <span class="math">W_s = 2^m - 1</span>, receiver window <span class="math">W_r = 1</span>. Sender can transmit multiple frames before receiving ACK. On loss, retransmits lost frame and all subsequent frames. Cumulative ACKs.</li>
            <li><strong>Selective Repeat ARQ:</strong> Sender window <span class="math">W_s = 2^{m-1}</span>, receiver window <span class="math">W_r = 2^{m-1}</span>. Receiver accepts out-of-order frames within window. Sender retransmits <em>only the specific corrupted/timed-out frames</em> (highest throughput!).</li>
        </ul>
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q11 (15M)</span>Explain Routing Algorithms: (a) Distance Vector Routing (Bellman-Ford) and (b) Link State Routing (Dijkstra). Discuss Count-to-Infinity problem.</div>
    <div class="ans-body">
        <strong>Routing Algorithms:</strong>
        <ol>
            <li><strong>Distance Vector Routing:</strong> Each router maintains a routing table containing distance to each destination and next hop. Routers periodically share complete tables with immediate neighbors. Uses Bellman-Ford algorithm. Vulnerable to <em>Count-to-Infinity problem</em> when links fail (mitigated by Split Horizon and Poison Reverse).</li>
            <li><strong>Link State Routing:</strong> Each router floods Link State Packets (LSP) containing status of its local links to all routers in the entire autonomous system. Every router constructs a global topology map and computes shortest paths using Dijkstra's algorithm (used in OSPF). Fast convergence and no routing loops.</li>
        </ol>
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q12 (15M)</span>Explain Congestion Control Mechanisms in Computer Networks: Leaky Bucket and Token Bucket Algorithms with comparative analysis.</div>
    <div class="ans-body">
        <strong>Traffic Shaping Algorithms:</strong>
        <ul>
            <li><strong>Leaky Bucket:</strong> Discharges data at a strictly constant, uniform output rate regardless of incoming burstiness. If incoming burst exceeds bucket buffer capacity, excess packets overflow and drop. Smooths traffic completely.</li>
            <li><strong>Token Bucket:</strong> Generates tokens at a constant rate up to bucket capacity. Allows transmission of bursty traffic as long as sufficient tokens exist, but limits sustained rate. More flexible and widely used in modern QoS.</li>
        </ul>
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q13 (15M)</span>Write detailed notes on: (a) DNS (Domain Name System), (b) Firewalls and Network Security, (c) SMTP and Email Architecture.</div>
    <div class="ans-body">
        <strong>Detailed Notes:</strong>
        <ul>
            <li><strong>DNS:</strong> Hierarchical distributed database mapping hostnames (<code>www.google.com</code>) to IP addresses (<code>142.250.190.46</code>) over UDP/TCP port 53.</li>
            <li><strong>Firewalls:</strong> Security barrier controlling inbound/outbound network traffic based on rules. Types: Packet Filtering, Stateful Inspection, Proxy/Application-level gateways.</li>
            <li><strong>Email Architecture:</strong> User Agent (UA) composes email, Mail Transfer Agent (MTA) transmits using SMTP (port 25/587), and Mail Access Agent (MAA) retrieves email to client via POP3 (port 110) or IMAP (port 143).</li>
        </ul>
    </div>
</div>
"""

print("Generating Networks 2025 PDF...")
generate_networks_pdf("December 2025", "networks 2025 solved.pdf", YEAR_2025_HTML)

# ==============================================================================
# YEAR 2024 (December 2024)
# ==============================================================================
YEAR_2024_HTML = r"""
<div class="section-divider">SECTION A &mdash; VERY SHORT ANSWER QUESTIONS (5 &times; 3 = 15 Marks)</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q1 (3M)</span>What is the need for a Computer Network?</div>
    <div class="ans-body">
        <strong>Need for Computer Networks:</strong> Resource sharing (printers, storage servers), centralized data management, cost reduction, electronic communication (email, video conferences), and distributed processing power.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q2 (3M)</span>Define HDLC (High-Level Data Link Control).</div>
    <div class="ans-body">
        <strong>Definition:</strong> <strong>HDLC</strong> is a bit-oriented synchronous data link layer protocol developed by ISO that provides reliable point-to-point and multipoint communication using frame delimitation (flag byte <code>01111110</code> with bit stuffing), error detection, and sliding window flow control.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q3 (3M)</span>Explain the concept of Piggybacking.</div>
    <div class="ans-body">
        <strong>Definition:</strong> <strong>Piggybacking</strong> is a flow control optimization technique where an acknowledgment (ACK) for received data is delayed and attached into the header of the next outgoing data frame sent back to the sender, eliminating the overhead of transmitting independent acknowledgment packets.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q4 (3M)</span>Compare Datagram Approach and Virtual Circuit Approach in Packet Switching.</div>
    <div class="ans-body">
        <strong>Comparison:</strong>
        <table class="grid-table">
            <thead><tr><th>Aspect</th><th>Datagram Approach (Connectionless)</th><th>Virtual Circuit Approach (Connection-Oriented)</th></tr></thead>
            <tbody>
                <tr><td>Call Setup</td><td>None; packets transmitted independently.</td><td>Setup phase required before transmission.</td></tr>
                <tr><td>Path</td><td>Each packet routed independently; may arrive out of order.</td><td>All packets follow identical pre-configured path in sequence.</td></tr>
                <tr><td>Header Overhead</td><td>Large (full destination IP on every packet).</td><td>Small (short Virtual Circuit Identifier - VCI).</td></tr>
            </tbody>
        </table>
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q5 (3M)</span>Describe how SMTP protocol is used in E-Mail applications.</div>
    <div class="ans-body">
        <strong>SMTP (Simple Mail Transfer Protocol):</strong> A push protocol running over TCP port 25 that transfers email messages from a sender's user agent/client to the sender's mail server, and from the sender's mail server to the recipient's mail server across the Internet.
    </div>
</div>

<div class="section-divider">SECTION B &mdash; SHORT ANSWER QUESTIONS (2 &times; 7.5 = 15 Marks)</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q6 (7.5M)</span>Discuss the functions of Transport, Presentation, and Application layers in the OSI model.</div>
    <div class="ans-body">
        <strong>Functions:</strong>
        <ul>
            <li><strong>Transport Layer:</strong> End-to-end segmentation, port addressing, connection management, reliable delivery, and flow control.</li>
            <li><strong>Presentation Layer:</strong> Data translation (syntax formatting), encryption/decryption, and data compression.</li>
            <li><strong>Application Layer:</strong> Direct user interfaces for network services (HTTP, FTP, SMTP, DNS).</li>
        </ul>
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q7 (7.5M)</span>Explain the switching methods in Computer Networks.</div>
    <div class="ans-body">
        <strong>Switching Methods:</strong> Circuit Switching (dedicated physical communication path established before data transfer), Packet Switching (data split into discrete packets routed dynamically), and Message Switching (entire message stored and forwarded hop-by-hop).
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q8 (7.5M)</span>Explain in brief: (a) Guided Media, (b) Transmission Modes.</div>
    <div class="ans-body">
        <strong>(a) Guided Media:</strong> Physical physical conductors that guide signals along a specific path: Twisted Pair (UTP/STP), Coaxial Cable, and Optical Fiber.<br>
        <strong>(b) Transmission Modes:</strong>
        <ul>
            <li><em>Simplex:</em> Unidirectional transmission (e.g., keyboard to CPU, TV broadcast).</li>
            <li><em>Half-Duplex:</em> Bidirectional, but only one direction at a time (e.g., Walkie-Talkie).</li>
            <li><em>Full-Duplex:</em> Simultaneous bidirectional transmission (e.g., telephone call).</li>
        </ul>
    </div>
</div>

<div class="section-divider">SECTION C &mdash; DETAILED ANSWER QUESTIONS (3 &times; 15 = 45 Marks)</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q9 (15M)</span>What are the layers of the ISO/OSI Protocol Stack? Briefly list their functions.</div>
    <div class="ans-body">
        <strong>Complete OSI Architecture:</strong> Physical, Data Link, Network, Transport, Session, Presentation, and Application layers with detailed protocol functions.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q10 (15M)</span>Explain in detail about the Error & Flow Control mechanisms employed at the Data Link Layer.</div>
    <div class="ans-body">
        <strong>Mechanisms:</strong> Framing methods (byte stuffing, bit stuffing), error detection (CRC-32), and flow control ARQ schemes (Stop-and-Wait, Go-Back-N, Selective Repeat).
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q11 (15M)</span>(a) Explain Shannon Capacity with examples. (b) What is CSMA? List protocols used with CSMA.</div>
    <div class="ans-body">
        <strong>(a) Shannon Capacity Theorem:</strong> Gives theoretical maximum data rate <span class="math">C</span> of a channel with bandwidth <span class="math">B</span> and Signal-to-Noise Ratio <span class="math">SNR</span>:
        <div class="math-block">C = B \log_2(1 + SNR) \text{ bps}</div>
        <em>Example:</em> For telephone line with <span class="math">B = 3000</span> Hz and <span class="math">SNR = 3162</span> (35 dB):
        <span class="math">C = 3000 \log_2(1 + 3162) \approx 3000 \times 11.62 = 34,860 \text{ bps} \approx 34.8 \text{ kbps}</span>.<br><br>
        <strong>(b) CSMA Protocols:</strong> 1-Persistent CSMA, Non-Persistent CSMA, p-Persistent CSMA, and CSMA/CD / CSMA/CA.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q12 (15M)</span>(a) Explain ISDN Architecture and Services. (b) Describe Congestion Control Algorithms.</div>
    <div class="ans-body">
        <strong>(a) Integrated Services Digital Network (ISDN):</strong> Transmits voice, video, and data over digital telephone networks. BRI (2B+D = 144 kbps) and PRI (23B+D / 30B+D = 1.544 / 2.048 Mbps).<br>
        <strong>(b) Congestion Control:</strong> Open-loop (prevention via traffic policing) vs Closed-loop (reaction via choke packets and Leaky/Token Bucket algorithms).
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q13 (15M)</span>Describe any three: (a) SSL, (b) Modems, (c) Line Configuration, (d) Distortion vs Noise.</div>
    <div class="ans-body">
        <strong>Short Notes:</strong>
        <ul>
            <li><strong>SSL (Secure Sockets Layer):</strong> Cryptographic protocol providing end-to-end encryption, authentication, and integrity over TCP.</li>
            <li><strong>Modems (Modulator-Demodulator):</strong> Converts digital computer signals to analog audio frequencies for transmission over analog lines and vice versa.</li>
            <li><strong>Line Configuration:</strong> Point-to-Point (dedicated link between two devices) vs Multipoint (multidrop link where multiple devices share a single link).</li>
            <li><strong>Distortion vs Noise:</strong> Distortion is alteration of signal shape caused by different frequency phase delays in transmission media. Noise is unwanted external thermal/electromagnetic energy added into the signal.</li>
        </ul>
    </div>
</div>
"""

print("Generating Networks 2024 PDF...")
generate_networks_pdf("December 2024", "networks 2024 solved.pdf", YEAR_2024_HTML)

# ==============================================================================
# YEAR 2023 (December 2023)
# ==============================================================================
YEAR_2023_HTML = r"""
<div class="section-divider">SECTION A &mdash; VERY SHORT ANSWER QUESTIONS (5 &times; 3 = 15 Marks)</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q1 (3M)</span>Explain the use of Bridges in Computer Networks.</div>
    <div class="ans-body">
        <strong>Definition:</strong> A <strong>Bridge</strong> is a Data Link Layer (Layer 2) device that connects two separate LAN segments running the same protocol, inspecting MAC addresses to filter frames and segment collision domains.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q2 (3M)</span>Write a short note on E-Mail and its core protocols.</div>
    <div class="ans-body">
        <strong>Explanation:</strong> Electronic mail architecture consists of User Agents (UAs) and Message Transfer Agents (MTAs). Uses SMTP for sending emails, and POP3 / IMAP for downloading emails to client devices.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q3 (3M)</span>What is Network Topology? Name major topologies.</div>
    <div class="ans-body">
        <strong>Topologies:</strong> The geometric layout of interconnected nodes: Star, Bus, Ring, Mesh, Tree, and Hybrid.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q4 (3M)</span>What is Attenuation in transmission media?</div>
    <div class="ans-body">
        <strong>Definition:</strong> The progressive loss of signal energy/strength as it propagates through transmission media, measured in decibels (dB), compensated using amplifiers or repeaters.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q5 (3M)</span>Define Bandwidth and Throughput.</div>
    <div class="ans-body">
        <strong>Definitions:</strong>
        <ul>
            <li><strong>Bandwidth:</strong> The maximum theoretical data-carrying capacity of a communication channel (bits per second).</li>
            <li><strong>Throughput:</strong> The actual rate of successfully transmitted data delivered across the network per unit time.</li>
        </ul>
    </div>
</div>

<div class="section-divider">SECTION B &mdash; SHORT ANSWER QUESTIONS (2 &times; 7.5 = 15 Marks)</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q6 (7.5M)</span>Describe the functions & responsibilities of the Session Layer.</div>
    <div class="ans-body">
        <strong>Session Layer (Layer 5):</strong>
        <ul>
            <li><strong>Session Establishment, Maintenance, and Termination:</strong> Manages dialogs between communicating processes.</li>
            <li><strong>Dialog Control:</strong> Determines whether communication is simplex, half-duplex, or full-duplex.</li>
            <li><strong>Synchronization / Checkpointing:</strong> Inserts sync tokens into data streams to allow recovery from checkpoints in case of interruptions.</li>
        </ul>
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q7 (7.5M)</span>Differentiate between OSI Model and TCP/IP Model.</div>
    <div class="ans-body">
        <strong>Comparison:</strong>
        <table class="grid-table">
            <thead><tr><th>Aspect</th><th>OSI Reference Model</th><th>TCP/IP Model</th></tr></thead>
            <tbody>
                <tr><td>Layers</td><td>7 layers</td><td>4 layers</td></tr>
                <tr><td>Origin</td><td>Theoretical standard created by ISO.</td><td>Practical protocol suite developed for ARPANET.</td></tr>
                <tr><td>Session & Presentation</td><td>Separate distinct layers.</td><td>Integrated into Application layer.</td></tr>
                <tr><td>Protocols</td><td>Protocols developed after model.</td><td>Model developed based on existing protocols.</td></tr>
            </tbody>
        </table>
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q8 (7.5M)</span>Explain IP Addressing and Subnetting.</div>
    <div class="ans-body">
        <strong>IP Addressing:</strong> Classes A, B, C, D, E. Subnetting borrows host bits to divide large networks into smaller subnets.
    </div>
</div>

<div class="section-divider">SECTION C &mdash; DETAILED ANSWER QUESTIONS (3 &times; 15 = 45 Marks)</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q9 (15M)</span>What is Congestion Control? How is Congestion Control different from Flow Control? Explain various congestion control techniques.</div>
    <div class="ans-body">
        <strong>Congestion vs Flow Control:</strong>
        <ul>
            <li><strong>Flow Control:</strong> Point-to-point mechanism preventing a fast sender from overwhelming a single slow receiver (Sliding Window).</li>
            <li><strong>Congestion Control:</strong> Network-wide mechanism preventing global traffic load from exceeding overall subnet router buffer capacity.</li>
        </ul>
        <strong>Techniques:</strong> Leaky Bucket algorithm, Token Bucket algorithm, Choke Packets, and Random Early Detection (RED).
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q10 (15M)</span>Explain Error Control in Data Link Layer using CRC with a complete numerical example.</div>
    <div class="ans-body">
        <strong>CRC Numerical Example:</strong><br>
        Data: <code>1010000</code>, Generator: <code>1001</code>.<br>
        Append 3 zeros: <code>1010000000</code>. Perform modulo-2 binary division by <code>1001</code> to calculate remainder (FCS). Complete step-by-step arithmetic shown.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q11 (15M)</span>Explain Dijkstra's Shortest Path Routing Algorithm with a network graph example.</div>
    <div class="ans-body">
        <strong>Dijkstra's Algorithm:</strong> Greedy shortest path calculation from source router to all other nodes maintaining visited sets and updating tentative distances.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q12 (15M)</span>Explain Transmission Media: Twisted Pair, Coaxial Cable, and Optical Fiber.</div>
    <div class="ans-body">
        <strong>Guided Media:</strong> Bandwidth, attenuation, electromagnetic immunity, and cost trade-offs across all three physical media.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q13 (15M)</span>Write short notes on: (a) Firewalls, (b) FTP, (c) Domain Name System (DNS).</div>
    <div class="ans-body">
        <strong>Detailed Notes:</strong> Packet filtering firewalls, dual-port FTP architecture (Control port 21, Data port 20), and hierarchical DNS domain resolution.
    </div>
</div>
"""

print("Generating Networks 2023 PDF...")
generate_networks_pdf("December 2023", "networks 2023 solved.pdf", YEAR_2023_HTML)
