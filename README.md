# MQTT Network Attack Dataset

## Overview
This dataset contains captured network traffic from an MQTT-based environment, including both **benign** and **attack** scenarios.  
It was designed for research in network intrusion detection, anomaly detection, and traffic classification, especially in IoT systems using the MQTT protocol.

The dataset includes labeled records with relevant fields from TCP/IP and MQTT layers, as well as application-specific payloads, enabling deep analysis of both network- and message-level characteristics.

---

## File Information
- **Format:** CSV (Comma-Separated Values)  
- **Total rows:** 10,490  
- **Total columns:** 28  
- **Encoding:** UTF-8  

---

## Column Descriptions

| Column                  | Description |
|-------------------------|-------------|
| `frame.time_relative`   | Relative timestamp of the packet in seconds since the start of the capture. |
| `ip.src`                | Source IP address of the packet. |
| `ip.dst`                | Destination IP address of the packet. |
| `tcp.len`               | TCP payload length in bytes. |
| `tcp.flags_ack`         | Boolean (`True`/`False`) indicating if the TCP ACK flag is set. |
| `tcp.flags_syn`         | Boolean indicating if the TCP SYN flag is set (connection initiation). |
| `tcp.flags_fin`         | Boolean indicating if the TCP FIN flag is set (connection termination). |
| `tcp.flags_urg`         | Boolean indicating if the TCP URG flag is set (urgent pointer significant). |
| `tcp.flags_ae`          | Boolean for an additional extended TCP flag (implementation-specific). |
| `tcp.flags_cwr`         | Boolean indicating if the TCP CWR flag is set (Congestion Window Reduced). |
| `tcp.flags_push`        | Boolean indicating if the TCP PSH flag is set (push function). |
| `tcp.flags_res`         | Boolean for reserved TCP bits. |
| `tcp.flags_reset`       | Boolean indicating if the TCP RST flag is set (connection reset). |
| `tcp.flags_ece`         | Boolean indicating if the TCP ECE flag is set (ECN-Echo). |
| `tcp.flags_str`         | Human-readable string representation of all TCP flags set. |
| `tcp.time_delta`        | Time difference in seconds between this packet and the previous packet. |
| `mqtt.msgtype`          | MQTT message type as an integer (e.g., 1 = CONNECT, 2 = CONNACK, 3 = PUBLISH, 14 = DISCONNECT). |
| `mqtt.dupflag`          | Boolean indicating if the MQTT DUP flag is set (duplicate message). |
| `mqtt.hdrflags`         | MQTT header flags in hexadecimal notation. |
| `mqtt.len`              | Remaining length field in the MQTT fixed header. |
| `mqtt.msg`              | Raw MQTT payload, often in JSON format with sensor readings or control messages. |
| `mqtt.qos`              | Quality of Service (QoS) level for the MQTT message (0, 1, or 2). |
| `mqtt.msgid`            | MQTT message identifier (only present for QoS > 0). |
| `velocidade`            | Extracted from the MQTT payload, represents speed (units depend on context, usually km/h). |
| `angulo`                | Extracted from the MQTT payload, represents angle or steering position (degrees). |
| `vbat`                  | Extracted from the MQTT payload, represents battery voltage. |
| `attack_label`          | Final classification: `'legitimate'` for benign traffic, or attack type (`'dos'`, `'malformed'`, `'falsedata'`). |

---

## Labels
- **legitimate** → Normal traffic, no malicious activity detected.  
- **dos** → Denial of Service attack traffic.  
- **malformed** → MQTT messages crafted with protocol violations or incorrect structure.  
- **falsedata** → MQTT messages containing fabricated or unrealistic sensor values.  

---

## Special Notes
- Rule enforced: **If `ip.src` or `ip.dst` = `10.42.0.201`, then `attack_label` ≠ `legitimate`**.  
- Attacks are marked using MQTT PUBLISH messages with the format:
  - `"START:<attack_type>"` → Beginning of the attack window.
  - `"END:<attack_type>"` → End of the attack window.
- A typical attack session follows this sequence:
  1. CONNECT (`mqtt.msgtype` = 1)  
  2. CONNACK (`mqtt.msgtype` = 2)  
  3. PUBLISH (`mqtt.msgtype` = 3) — including START/END markers  
  4. DISCONNECT (`mqtt.msgtype` = 14)  

---
