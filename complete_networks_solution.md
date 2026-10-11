## Section - A (Very Short Answer Questions — 3 Marks Each, All 5 Mandatory)

### Q1. Describe the various components of Data Communication.
**Answer:**
1. **Message:** The data/information being exchanged (text, audio, video).
2. **Sender:** Device originating the message (PC, smartphone).
3. **Receiver:** Destination device receiving the message.
4. **Transmission Medium:** Physical communication channel (twisted pair, fiber optic, radio waves).
5. **Protocol:** A governing set of formal communication rules agreed upon by devices.

---

### Q2. Define Bandwidth and Network Congestion.
**Answer:**
- **Bandwidth:** The maximum rate of data transfer across a given path (bits per second or Hertz).
- **Network Congestion:** Occurs when transmitted traffic exceeds available channel/router buffer capacity, causing packet queuing delays and loss.

---

### Q3. Distinguish between MAC Address and IP Address.
**Answer:**
- **MAC Address:** 48-bit permanent physical hardware address burnt into the NIC at Data Link Layer (Layer 2).
- **IP Address:** 32-bit (IPv4) or 128-bit (IPv6) logical network address assigned dynamically or statically at Network Layer (Layer 3).

---

### Q4. Differentiate between a Hub and a Switch.
**Answer:**
- **Hub:** Layer 1 (Physical layer) device. Broadcasts incoming frames to all ports. Shared collision domain.
- **Switch:** Layer 2 (Data Link layer) device. Inspects destination MAC address and forwards frames selectively. Separate collision domain per port.

---

### Q5. What is Subnetting? Give an example.
**Answer:**
Subnetting divides a large network into smaller, manageable subnets.
- *Example:* Network `192.168.1.0/24` with subnet mask `255.255.255.192` (`/26`) creates 4 subnets with 62 usable host IPs each (`.1-.62`, `.65-.126`, `.129-.190`, `.193-.254`).

---

## Section - B (Short Answer Questions — 7.5 Marks Each, Attempt Any Two)

### Q6. Describe the role of the Transport Layer in the OSI Model.
**Answer:**
Provides end-to-end, process-to-process delivery:
1. Port Addressing (e.g., HTTP: 80, DNS: 53)
2. Segmentation and Reassembly of messages
3. Connection establishment and termination (TCP)
4. Flow control via sliding window
5. Error control via checksums and retransmissions

---

### Q7. Explain Network Topologies (Star, Mesh, Bus, Ring) with diagrams.
**Answer:**
- **Star:** Nodes connect to central switch/hub. Easy to install and isolate faults.
- **Mesh:** Every node connects to every other node via dedicated point-to-point links (n(n-1)/2 links). High redundancy and fault tolerance.
- **Bus:** Nodes share a single central backbone cable with terminators.
- **Ring:** Nodes connect in a circular daisy chain. Tokens regulate transmission.

---

### Q8. Explain Congestion Control Algorithms (Leaky Bucket and Token Bucket).
**Answer:**
- **Leaky Bucket:** Discards bursts exceeding bucket size and transmits packets at a strictly uniform constant rate.
- **Token Bucket:** Accumulates tokens up to capacity C at rate r. Allows regulated bursts while bounding average rate.

---

## Section - C (Long Answer Questions — 15 Marks Each, Attempt Any Three)

### Q9. Explain the TCP Three-Way Handshake with a diagram.
**Answer:**
1. **SYN:** Client sends `SYN = 1`, `Seq = X`.
2. **SYN-ACK:** Server sends `SYN = 1`, `ACK = 1`, `Seq = Y`, `Ack_Num = X + 1`.
3. **ACK:** Client sends `ACK = 1`, `Seq = X + 1`, `Ack_Num = Y + 1`.
The connection is established and full-duplex data transfer begins.

---

### Q10. Draw and explain the 7 Layers of the ISO/OSI Reference Model.
**Answer:**
1. **Physical:** Raw bit transmission over physical media.
2. **Data Link:** Node-to-node frame delivery, MAC addressing, CRC error detection.
3. **Network:** Logical addressing (IP), path routing, packet forwarding.
4. **Transport:** End-to-end process delivery, TCP/UDP segmentation, flow control.
5. **Session:** Dialogue control, session checkpoint synchronization.
6. **Presentation:** Encryption, data compression, format translation.
7. **Application:** User services (HTTP, FTP, SMTP, DNS).

---

### Q11. Explain Shannon Capacity Theorem with an example.
**Answer:**
Channel capacity formula: `C = B * log2(1 + S/N)`
For Bandwidth B = 3000 Hz and SNR = 3162 (35 dB):
`C = 3000 * log2(3163) = 3000 * 11.628 = 34,884 bps = 34.88 kbps`

---

### Q12. Explain CSMA/CD in Ethernet and compare with CSMA/CA.
**Answer:**
- **CSMA/CD (Wired Ethernet 802.3):** Listens before transmitting; if collision detected while transmitting, immediately aborts, broadcasts jam signal, and waits a random binary exponential backoff duration.
- **CSMA/CA (Wireless Wi-Fi 802.11):** Collisions cannot be detected easily in wireless; uses RTS/CTS handshake and Inter-Frame Spacing (IFS) to avoid collisions before transmitting.

---

### Q13. Compare Circuit Switching, Packet Switching, and Message Switching.
**Answer:**
- **Circuit Switching:** Dedicated physical circuit setup before transfer; constant bandwidth (telephone network).
- **Packet Switching:** Packets routed dynamically; optimal bandwidth utilization (Internet IP).
- **Message Switching:** Entire message stored and forwarded; high delay (telegraph).
