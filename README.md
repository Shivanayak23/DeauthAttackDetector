# Deauthentication Attack Detector for Wi-Fi

🔒 A real-time deauthentication attack detection tool that monitors 802.11 Wi-Fi traffic to detect and alert users of malicious disconnect attempts using Python and Scapy.

## 📌 Features

- Detects deauthentication (DoS) attacks in real-time
- Logs attacker and victim MAC addresses
- Runs on monitor mode-enabled interfaces
- Lightweight and easy to deploy on Kali Linux

## 🎯 Objective

To develop a Python-based intrusion detection system that detects Wi-Fi deauth attacks using packet sniffing and alerts the user in real-time.

## 🛠 Requirements

- Python 3.x  
- Scapy  
- Kali Linux  
- Wi-Fi adapter supporting monitor mode (e.g., Alfa AWUS036NHA)

## ⚙️ Setup Instructions

```bash
sudo apt update
sudo apt install python3-venv
python3 -m venv deauth_env
source deauth_env/bin/activate
pip install -r requirements.txt
