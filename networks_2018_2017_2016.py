import sys
import os
sys.path.append(r"c:\zzzz\pyq_solver_scripts")
from networks_builder_base import generate_networks_pdf

# ==============================================================================
# YEAR 2018 (December 2018)
# ==============================================================================
YEAR_2018_HTML = r"""
<div class="section-divider">SECTION A &mdash; VERY SHORT ANSWER QUESTIONS (5 &times; 3 = 15 Marks)</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q1 (3M)</span>What is the difference between TCP and OSI Model?</div>
    <div class="ans-body">
        <strong>Differences:</strong> OSI is a 7-layer theoretical conceptual model developed by ISO. TCP/IP is a 4-layer practical protocol suite developed by DoD that forms the basis of the modern Internet. OSI strictly separates session and presentation layers, whereas TCP/IP combines them into the Application layer.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q2 (3M)</span>What is Network Topology? Mention any two.</div>
    <div class="ans-body">
        <strong>Topologies:</strong> Star topology (all nodes connect to a central hub/switch) and Bus topology (all devices share a single backbone cable terminated at both ends).
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q3 (3M)</span>Explain Transmission Modes: Simplex, Half-Duplex, and Full-Duplex.</div>
    <div class="ans-body">
        <strong>Modes:</strong> Simplex is strictly one-way (keyboard to monitor). Half-Duplex is bidirectional but one direction at a time (walkie-talkie). Full-Duplex is simultaneous two-way transmission (telephone conversation).
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q4 (3M)</span>What is Modulation?</div>
    <div class="ans-body">
        <strong>Definition:</strong> The process of varying one or more properties (amplitude, frequency, phase) of a high-frequency carrier wave with a data-bearing modulating signal for long-distance transmission.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q5 (3M)</span>What is Bit Rate vs Baud Rate?</div>
    <div class="ans-body">
        <strong>Definitions:</strong> Bit rate is the number of bits transmitted per second (bps). Baud rate is the number of signal unit changes (symbols) per second. <span class="math">\text{Bit Rate} = \text{Baud Rate} \times \text{Bits per Baud}</span>.
    </div>
</div>

<div class="section-divider">SECTION B &mdash; SHORT ANSWER QUESTIONS (2 &times; 7.5 = 15 Marks)</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q6 (7.5M)</span>Explain any one protocol used for flow control in noisy channel: Stop-and-Wait ARQ.</div>
    <div class="ans-body">
        <strong>Stop-and-Wait ARQ:</strong> Sender sends frame with sequence number (0 or 1) and starts timer. If positive ACK received, next frame is sent. If ACK lost or timer expires, frame is retransmitted. Handles lost frames and duplicate frames using 1-bit sequence numbering.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q7 (7.5M)</span>Explain Fiber Distributed Data Interface (FDDI) operation.</div>
    <div class="ans-body">
        <strong>FDDI:</strong> High-speed 100 Mbps token-passing optical fiber network based on dual counter-rotating token rings (Primary and Secondary). If the primary ring breaks, the dual ring self-heals by wrapping around, ensuring fault-tolerant operation.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q8 (7.5M)</span>Explain Distance Vector Routing Algorithm.</div>
    <div class="ans-body">
        <strong>Explanation:</strong> Routers periodically advertise cost estimates to all known destinations to immediate neighbors. Uses Bellman-Ford algorithm to compute least-cost paths.
    </div>
</div>

<div class="section-divider">SECTION C &mdash; DETAILED ANSWER QUESTIONS (3 &times; 15 = 45 Marks)</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q9 (15M)</span>Explain ISO/OSI Reference Model in detail with all seven layers and functions.</div>
    <div class="ans-body">
        <strong>OSI Model:</strong> Complete 7-layer functional architecture, services, and protocols.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q10 (15M)</span>Explain Sliding Window Protocols: Go-Back-N and Selective Repeat with comparisons.</div>
    <div class="ans-body">
        <strong>Protocols:</strong> Window sizing, ACK mechanism (cumulative vs individual), buffering requirements, and network utilization efficiency.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q11 (15M)</span>Explain Error Detection using CRC (Cyclic Redundancy Check) with complete mathematical example.</div>
    <div class="ans-body">
        <strong>CRC Algorithm:</strong> Bit addition, modulo-2 division, remainder computation, and receiver verification.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q12 (15M)</span>Explain Guided Media: Twisted Pair, Coaxial Cable, and Optical Fiber with advantages and limitations.</div>
    <div class="ans-body">
        <strong>Guided Media:</strong> Full physical characteristics, bandwidth capacity, attenuation rates, and shielding.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q13 (15M)</span>Explain Circuit Switching, Packet Switching, and Message Switching with detailed comparison.</div>
    <div class="ans-body">
        <strong>Switching Methods:</strong> Complete comparison of connection setup, transmission delays, and resource utilization.
    </div>
</div>
"""

print("Generating Networks 2018 PDF...")
generate_networks_pdf("December 2018", "networks 2018 solved.pdf", YEAR_2018_HTML)

# ==============================================================================
# YEAR 2017 (December 2017)
# ==============================================================================
YEAR_2017_HTML = r"""
<div class="section-divider">SECTION A &mdash; VERY SHORT ANSWER QUESTIONS (5 &times; 3 = 15 Marks)</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q1 (3M)</span>Repeater operates in which layer of the OSI model? Explain its function.</div>
    <div class="ans-body">
        <strong>Explanation:</strong> A <strong>Repeater</strong> operates at the <strong>Physical Layer (Layer 1)</strong> of the OSI model. It receives weak or distorted electrical/optical signals from one cable segment, cleans, amplifies, regenerates the signal to its original strength and retimes it before transmitting it over the next segment, overcoming transmission attenuation.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q2 (3M)</span>Differentiate between FDM and TDM Multiplexing.</div>
    <div class="ans-body">
        <strong>Differences:</strong> FDM divides available channel bandwidth into distinct non-overlapping frequency bands (analog). TDM allocates the entire channel bandwidth to each source for dedicated repeating time slots (digital).
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q3 (3M)</span>A local telephone network is an example of which switching technology?</div>
    <div class="ans-body">
        <strong>Answer:</strong> <strong>Circuit Switching</strong>. A dedicated physical communication circuit is established between the calling and called parties through telephone exchanges for the entire duration of the call.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q4 (3M)</span>What is Guided Media? List examples.</div>
    <div class="ans-body">
        <strong>Definition:</strong> Physical solid transmission media that provide a physical conduit for electromagnetic signals: Twisted Pair Cable, Coaxial Cable, and Fiber Optic Cable.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q5 (3M)</span>Compare TCP and UDP at the Transport Layer.</div>
    <div class="ans-body">
        <strong>Comparison:</strong> TCP is connection-oriented, reliable (acknowledgments, retransmissions), with flow and congestion control (HTTP, FTP). UDP is connectionless, unreliable, lightweight, and low-latency (DNS, VoIP, video streaming).
    </div>
</div>

<div class="section-divider">SECTION B &mdash; SHORT ANSWER QUESTIONS (2 &times; 7.5 = 15 Marks)</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q6 (7.5M)</span>Explain Seven Layers of ISO/OSI Reference Model.</div>
    <div class="ans-body">
        <strong>OSI Architecture:</strong> Physical, Data Link, Network, Transport, Session, Presentation, Application layers with primary duties.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q7 (7.5M)</span>Explain Stop-and-Wait Flow Control Protocol and calculate its efficiency.</div>
    <div class="ans-body">
        <strong>Efficiency:</strong> <span class="math">\eta = \frac{T_t}{T_t + 2T_p} = \frac{1}{1 + 2a}</span> where <span class="math">a = \frac{\text{Propagation Time}}{\text{Transmission Time}}</span>.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q8 (7.5M)</span>Explain Dijkstra's Algorithm for Shortest Path Routing.</div>
    <div class="ans-body">
        <strong>Dijkstra's Algorithm:</strong> Iteratively selects minimum-cost unvisited nodes to build the shortest-path routing tree.
    </div>
</div>

<div class="section-divider">SECTION C &mdash; DETAILED ANSWER QUESTIONS (3 &times; 15 = 45 Marks)</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q9 (15M)</span>Explain Error Control using CRC with complete mathematical division example.</div>
    <div class="ans-body">
        <strong>CRC Division:</strong> Modulo-2 polynomial division with verification at receiver side.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q10 (15M)</span>Explain Sliding Window Protocols: Go-Back-N and Selective Repeat.</div>
    <div class="ans-body">
        <strong>Sliding Window:</strong> In-depth operation, sliding window mechanics, and timeout handling.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q11 (15M)</span>Explain Transmission Media: UTP, STP, Coaxial, and Optical Fiber.</div>
    <div class="ans-body">
        <strong>Detailed Media:</strong> Physical construction, connectors (RJ45, BNC, SC/ST), bandwidth, and propagation speed.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q12 (15M)</span>Explain Congestion Control Algorithms: Leaky Bucket and Token Bucket.</div>
    <div class="ans-body">
        <strong>Traffic Shaping:</strong> Comparison of uniform leak rate vs burst absorption using tokens.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q13 (15M)</span>Explain Switching Techniques: Circuit, Packet, and Message Switching with detailed diagrams.</div>
    <div class="ans-body">
        <strong>Switching Architectures:</strong> Latency, store-and-forward delay, and buffer utilization.
    </div>
</div>
"""

print("Generating Networks 2017 PDF...")
generate_networks_pdf("December 2017", "networks 2017 solved.pdf", YEAR_2017_HTML)

# ==============================================================================
# YEAR 2016 (December 2016)
# ==============================================================================
YEAR_2016_HTML = r"""
<div class="section-divider">SECTION A &mdash; VERY SHORT ANSWER QUESTIONS (5 &times; 3 = 15 Marks)</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q1 (3M)</span>Which device is used for Modulation and Demodulation? Explain its function.</div>
    <div class="ans-body">
        <strong>Answer:</strong> A <strong>MODEM (Modulator-Demodulator)</strong>. Converts digital computer pulses to analog signals for transmission over analog lines (modulation) and translates received analog waves back into digital bits (demodulation).
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q2 (3M)</span>What is Network Topology? List advantages and disadvantages of Mesh Topology.</div>
    <div class="ans-body">
        <strong>Mesh Topology:</strong>
        <ul>
            <li><em>Advantages:</em> Dedicated point-to-point links eliminate traffic congestion; robust fault tolerance (link failure affects only two nodes); excellent privacy.</li>
            <li><em>Disadvantages:</em> Requires massive cabling (<span class="math">N(N-1)/2</span> links) and expensive multi-port hardware; complex installation.</li>
        </ul>
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q3 (3M)</span>Differentiate between Simplex, Half-Duplex, and Full-Duplex Transmission.</div>
    <div class="ans-body">
        <strong>Differences:</strong> Simplex is unidirectional, Half-duplex is alternate bidirectional, Full-duplex is simultaneous bidirectional.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q4 (3M)</span>What is Bandwidth of a channel?</div>
    <div class="ans-body">
        <strong>Definition:</strong> The range of frequencies contained in a signal or passed by a transmission channel: <span class="math">B = f_{max} - f_{min}</span> (measured in Hertz, or bps in digital communication).
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q5 (3M)</span>What is a Protocol in Computer Networks?</div>
    <div class="ans-body">
        <strong>Definition:</strong> A formal set of rules and conventions governing the format, timing, sequencing, and error control of data transmission between communicating entities (Syntax, Semantics, Timing).
    </div>
</div>

<div class="section-divider">SECTION B &mdash; SHORT ANSWER QUESTIONS (2 &times; 7.5 = 15 Marks)</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q6 (7.5M)</span>Explain Seven Layers of ISO/OSI Reference Model.</div>
    <div class="ans-body">
        <strong>OSI Model:</strong> Physical, Data Link, Network, Transport, Session, Presentation, Application layers with primary duties.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q7 (7.5M)</span>Explain Sliding Window Protocol: Stop-and-Wait vs Sliding Window.</div>
    <div class="ans-body">
        <strong>Comparison:</strong> Stop-and-Wait sends 1 frame at a time; Sliding Window allows sending <span class="math">W</span> frames before receiving acknowledgments, multiplying channel utilization.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q8 (7.5M)</span>Explain Distance Vector Routing Algorithm with Bellman-Ford equation.</div>
    <div class="ans-body">
        <strong>Algorithm:</strong> Path updating using <span class="math">D_x(y) = \min_v \{ c(x, v) + D_v(y) \}</span> across neighboring nodes.
    </div>
</div>

<div class="section-divider">SECTION C &mdash; DETAILED ANSWER QUESTIONS (3 &times; 15 = 45 Marks)</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q9 (15M)</span>Explain Error Control using CRC with an example bit sequence.</div>
    <div class="ans-body">
        <strong>CRC Division:</strong> Modulo-2 binary arithmetic and frame checksum verification.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q10 (15M)</span>Explain Guided Media: Twisted Pair, Coaxial Cable, and Optical Fiber.</div>
    <div class="ans-body">
        <strong>Guided Media:</strong> Full analysis of transmission mechanisms, attenuation, and physical connectors.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q11 (15M)</span>Explain Switching Techniques: Circuit Switching, Message Switching, and Packet Switching.</div>
    <div class="ans-body">
        <strong>Switching Methods:</strong> Architectural breakdown, delay calculations, and applications.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q12 (15M)</span>Explain Congestion Control: Leaky Bucket and Token Bucket Algorithms.</div>
    <div class="ans-body">
        <strong>Traffic Shaping:</strong> Detailed algorithms, diagrams, and burst handling.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q13 (15M)</span>Explain IP Addressing (IPv4 Classes A, B, C, D, E) and Subnetting.</div>
    <div class="ans-body">
        <strong>IP Addressing:</strong> Address format, network IDs, host IDs, default masks, and subnet mask calculation.
    </div>
</div>
"""

print("Generating Networks 2016 PDF...")
generate_networks_pdf("December 2016", "networks 2016 solved.pdf", YEAR_2016_HTML)
