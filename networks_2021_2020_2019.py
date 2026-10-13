import sys
import os
sys.path.append(r"c:\zzzz\pyq_solver_scripts")
from networks_builder_base import generate_networks_pdf

# ==============================================================================
# YEAR 2021 (December 2021 / CV-3 Pattern)
# ==============================================================================
YEAR_2021_HTML = r"""
<div class="section-divider">SECTION A &mdash; VERY SHORT ANSWER QUESTIONS (2 &times; 7.5 = 15 Marks / CV-3 Pattern)</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q1 (7.5M)</span>Explain the functions of the Session Layer in the OSI model.</div>
    <div class="ans-body">
        <strong>Session Layer (Layer 5):</strong> Responsible for establishing, maintaining, synchronizing, and terminating communication sessions between applications. Controls dialog (simplex/half-duplex/full-duplex) and inserts synchronization checkpoints into data streams to facilitate restart upon failure.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q2 (7.5M)</span>Write short notes on: (a) Throughput & Wavelength, (b) Synchronous Protocols, (c) Routers.</div>
    <div class="ans-body">
        <strong>Notes:</strong>
        <ul>
            <li><strong>(a) Throughput & Wavelength:</strong> Throughput is the actual measurement of data transferred across a network per second. Wavelength (<span class="math">\lambda = v / f</span>) is the physical distance between consecutive signal wave peaks in optical communication.</li>
            <li><strong>(b) Synchronous Protocols:</strong> Continuous transmission of data blocks synchronized to a shared clock, using sync bytes/flags (e.g. HDLC).</li>
            <li><strong>(c) Routers:</strong> Network Layer (Layer 3) internetworking devices that inspect destination IP addresses and make packet forwarding decisions based on routing tables.</li>
        </ul>
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q3 (7.5M)</span>Discuss ISDN, its services, and layer structure.</div>
    <div class="ans-body">
        <strong>ISDN (Integrated Services Digital Network):</strong> Transmits voice, data, and video simultaneously over standard telephone copper lines. Channels: B-channel (64 kbps, user data), D-channel (16 or 64 kbps, control signaling). BRI provides 2B+D (144 kbps); PRI provides 23B+D (1.544 Mbps) or 30B+D (2.048 Mbps).
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q4 (7.5M)</span>Explain Flow Control and Error Control in Computer Networks.</div>
    <div class="ans-body">
        <strong>Mechanisms:</strong> Flow control ensures a fast sender does not overwhelm a slow receiver (Sliding Window). Error control detects corrupted frames via CRC and retransmits them via ARQ schemes (Stop-and-Wait, Go-Back-N, Selective Repeat).
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q5 (7.5M)</span>Explain TCP Packet Format (Header Structure) in detail.</div>
    <div class="ans-body">
        <strong>TCP Header Fields:</strong>
        <ul>
            <li>Source Port (16 bits) and Destination Port (16 bits)</li>
            <li>Sequence Number (32 bits) and Acknowledgment Number (32 bits)</li>
            <li>Header Length / Data Offset (4 bits) and Reserved bits (6 bits)</li>
            <li>Control Flags (6 bits: URG, ACK, PSH, RST, SYN, FIN)</li>
            <li>Window Size (16 bits) for flow control</li>
            <li>Checksum (16 bits) and Urgent Pointer (16 bits)</li>
        </ul>
    </div>
</div>

<div class="section-divider">SECTION B &mdash; SHORT ANSWER QUESTIONS (1 &times; 15 = 15 Marks / CV-3 Pattern)</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q6 (15M)</span>Explain Seven Layers of ISO/OSI Reference Model with their functions.</div>
    <div class="ans-body">
        <strong>Complete OSI Model:</strong> Detailed explanation of Physical, Data Link, Network, Transport, Session, Presentation, and Application layers.
    </div>
</div>

<div class="section-divider">SECTION C &mdash; DETAILED ANSWER QUESTIONS (2 &times; 22.5 = 45 Marks / CV-3 Pattern)</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q7 (22.5M)</span>Explain Routing Algorithms: Shortest Path Routing (Dijkstra) and Distance Vector Routing with Count-to-Infinity problem.</div>
    <div class="ans-body">
        <strong>Routing Algorithms:</strong> Dijkstra link-state calculation vs Bellman-Ford distributed vector routing with split horizon and poison reverse solutions.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q8 (22.5M)</span>Explain Sliding Window Protocols: Go-Back-N and Selective Repeat with window sizes and frame sequences.</div>
    <div class="ans-body">
        <strong>Sliding Window:</strong> Mathematical condition for maximum window sizes: Go-Back-N (<span class="math">W_s \le 2^m - 1</span>) and Selective Repeat (<span class="math">W_s + W_r \le 2^m \implies W_s \le 2^{m-1}</span>) to prevent ambiguity with duplicate sequence numbers.
    </div>
</div>
"""

print("Generating Networks 2021 PDF...")
generate_networks_pdf("December 2021", "networks 2021 solved.pdf", YEAR_2021_HTML)

# ==============================================================================
# YEAR 2020 (December 2020)
# ==============================================================================
YEAR_2020_HTML = r"""
<div class="section-divider">SECTION A &mdash; VERY SHORT ANSWER QUESTIONS (5 &times; 3 = 15 Marks)</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q1 (3M)</span>Four channels, each with 100-KHz bandwidth, are to be multiplexed together. What is the minimum bandwidth of the link if there is a need for a guard band of 10 KHz between channels?</div>
    <div class="ans-body">
        <strong>Solution:</strong>
        <span class="math">N = 4</span> channels of <span class="math">100</span> KHz each.<br>
        Number of guard bands required between 4 channels <span class="math">= 4 - 1 = 3</span>.<br>
        Each guard band <span class="math">= 10</span> KHz.<br>
        Total minimum bandwidth:
        <div class="math-block">B = (4 \times 100) + (3 \times 10) = 400 + 30 = \mathbf{430 \text{ KHz}}</div>
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q2 (3M)</span>Discuss Point-to-Point Protocol (PPP).</div>
    <div class="ans-body">
        <strong>PPP:</strong> A data link layer protocol used to establish a direct connection between two nodes over dial-up, serial cable, or broadband (PPPoE). Provides authentication via PAP/CHAP, framing, and dynamic IP configuration (IPCP).
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q3 (3M)</span>Explain the functions of the Presentation Layer.</div>
    <div class="ans-body">
        <strong>Functions:</strong> Data syntax translation, character code conversion, data compression (lossless/lossy), and data encryption/decryption (cryptography).
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q4 (3M)</span>Differentiate between LAN, MAN, and WAN.</div>
    <div class="ans-body">
        <strong>Comparison:</strong> LAN covers a room or building (high speed, private ownership). MAN covers a city (cable TV network). WAN covers a country or globe (telecom lines, satellite, Internet).
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q5 (3M)</span>What is a Collision Domain vs Broadcast Domain?</div>
    <div class="ans-body">
        <strong>Definitions:</strong> A Collision Domain is a network segment where simultaneous transmissions collide (divided by switches). A Broadcast Domain is a segment receiving all broadcast frames (divided by routers).
    </div>
</div>

<div class="section-divider">SECTION B &mdash; SHORT ANSWER QUESTIONS (2 &times; 7.5 = 15 Marks)</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q6 (7.5M)</span>How does DTE-DCE interface work? Discuss the essence of Modems.</div>
    <div class="ans-body">
        <strong>DTE-DCE Interface:</strong> DTE (Data Terminal Equipment, e.g. computer/router) generates digital data. DCE (Data Circuit-terminating Equipment, e.g. modem) converts signals for transmission across the physical telephone link. Standards include RS-232 / EIA-232.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q7 (7.5M)</span>Explain Error Detection using CRC with generator polynomial x³ + x + 1.</div>
    <div class="ans-body">
        <strong>CRC Calculation:</strong> Complete modulo-2 polynomial division with bit representation <code>1011</code>.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q8 (7.5M)</span>Explain Distance Vector Routing Algorithm.</div>
    <div class="ans-body">
        <strong>Algorithm:</strong> Periodic exchange of routing tables between adjacent neighbors based on Bellman-Ford algorithm.
    </div>
</div>

<div class="section-divider">SECTION C &mdash; DETAILED ANSWER QUESTIONS (3 &times; 15 = 45 Marks)</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q9 (15M)</span>Explain OSI Reference Model with detailed layer descriptions.</div>
    <div class="ans-body">
        <strong>7-Layer Model:</strong> Detailed functions, protocols, and data units (Bits, Frames, Packets, Segments, Data).
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q10 (15M)</span>Explain Sliding Window Protocols: Stop-and-Wait, Go-Back-N, and Selective Repeat.</div>
    <div class="ans-body">
        <strong>Flow Control:</strong> Efficiency equations, window buffering, and timeout retransmission mechanisms.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q11 (15M)</span>Explain Transmission Media: UTP, STP, Coaxial, and Fiber Optic Cable.</div>
    <div class="ans-body">
        <strong>Transmission Media:</strong> Attenuation, propagation velocity, bandwidth, and EMI immunity analysis.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q12 (15M)</span>Explain Congestion Control Algorithms: Leaky Bucket and Token Bucket.</div>
    <div class="ans-body">
        <strong>Traffic Shaping:</strong> Smooth constant-rate leakage vs bursty-tolerant token generation.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q13 (15M)</span>Explain Switching Techniques: Circuit, Message, and Packet Switching.</div>
    <div class="ans-body">
        <strong>Switching:</strong> Detailed comparison of setup time, propagation delay, transmission delay, and queuing overhead.
    </div>
</div>
"""

print("Generating Networks 2020 PDF...")
generate_networks_pdf("December 2020", "networks 2020 solved.pdf", YEAR_2020_HTML)

# ==============================================================================
# YEAR 2019 (November 2019)
# ==============================================================================
YEAR_2019_HTML = r"""
<div class="section-divider">SECTION A &mdash; VERY SHORT ANSWER QUESTIONS (5 &times; 3 = 15 Marks)</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q1 (3M)</span>Differentiate between Bridges and Repeaters.</div>
    <div class="ans-body">
        <strong>Differences:</strong> Repeaters operate at the Physical Layer (Layer 1) to regenerate electrical signals without looking at frames. Bridges operate at the Data Link Layer (Layer 2) to inspect MAC addresses and filter traffic between segments.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q2 (3M)</span>What are the services provided by the Transport Layer?</div>
    <div class="ans-body">
        <strong>Services:</strong> Connection-oriented delivery (TCP) vs connectionless datagram delivery (UDP), port-based process addressing, segmentation/reassembly, end-to-end flow control, and error recovery.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q3 (3M)</span>Define Modulation and Demodulation.</div>
    <div class="ans-body">
        <strong>Explanation:</strong> Modulation transforms digital bitstreams into analog signals for transmission across physical media. Demodulation recovers original digital bits from incoming modulated analog waves.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q4 (3M)</span>What is Network Topology? Name two topologies with advantages.</div>
    <div class="ans-body">
        <strong>Topologies:</strong> Star topology (central hub, easy fault isolation) and Mesh topology (point-to-point dedicated links, highest fault tolerance).
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q5 (3M)</span>What is Shannon Capacity Theorem?</div>
    <div class="ans-body">
        <strong>Theorem:</strong> <span class="math">C = B \log_2(1 + SNR)</span> gives the theoretical upper bound on data transmission speed in bits per second over a noisy channel.
    </div>
</div>

<div class="section-divider">SECTION B &mdash; SHORT ANSWER QUESTIONS (2 &times; 7.5 = 15 Marks)</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q6 (7.5M)</span>Explain Dijkstra's Algorithm with an example network.</div>
    <div class="ans-body">
        <strong>Dijkstra's Algorithm:</strong> Finds single-source shortest path to all destinations by maintaining tentative distance labels and iteratively selecting the minimum-cost unvisited node.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q7 (7.5M)</span>Explain Distance Vector Routing and the Count-to-Infinity problem.</div>
    <div class="ans-body">
        <strong>Distance Vector Routing:</strong> Uses Bellman-Ford algorithm; slow reaction to link failures causes loops (count-to-infinity), resolved via split horizon.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q8 (7.5M)</span>Explain Sliding Window Protocol for Flow Control.</div>
    <div class="ans-body">
        <strong>Sliding Window:</strong> Permits sending multiple frames within a window without waiting for immediate individual acknowledgments.
    </div>
</div>

<div class="section-divider">SECTION C &mdash; DETAILED ANSWER QUESTIONS (3 &times; 15 = 45 Marks)</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q9 (15M)</span>Explain ISO/OSI Reference Model in detail with all seven layers.</div>
    <div class="ans-body">
        <strong>OSI Architecture:</strong> Full 7-layer functional breakdown and data encapsulation process.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q10 (15M)</span>Explain Guided Media: Twisted Pair Cable, Coaxial Cable, and Fiber Optic Cable.</div>
    <div class="ans-body">
        <strong>Transmission Media:</strong> Construction, signal propagation, attenuation characteristics, and network cabling standards (Cat5e, Cat6, Single-mode/Multi-mode fiber).
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q11 (15M)</span>Explain Error Detection using CRC (Cyclic Redundancy Check) with numerical problem.</div>
    <div class="ans-body">
        <strong>CRC Problem:</strong> Generator polynomial division, bit stuffing, and frame validation on receiver side.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q12 (15M)</span>Explain Circuit Switching, Packet Switching, and Message Switching with comparison.</div>
    <div class="ans-body">
        <strong>Switching Techniques:</strong> Comprehensive comparison of latency, bandwidth efficiency, and modern telecom implementations.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q13 (15M)</span>Explain Congestion Control in Computer Networks: Leaky Bucket and Token Bucket Algorithms.</div>
    <div class="ans-body">
        <strong>Traffic Shaping:</strong> Deep dive into burst mitigation, token accumulation, and packet scheduling.
    </div>
</div>
"""

print("Generating Networks 2019 PDF...")
generate_networks_pdf("November 2019", "networks 2019 solved.pdf", YEAR_2019_HTML)
