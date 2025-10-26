# 🧠 Threat Intelligence Feed Processor

## 👨‍💻 Author
**Karthik Reddy Morapally**

---

## 📘 Project Objective
This project checks IP addresses from a log file and identifies which ones are **malicious** using a small local threat intelligence database.

---

## ⚙️ Tools Used
- Python 3  
- SQLite Database  
- Text File (access.log)

---

## 🧩 How It Works
1. The script (`threat_checker.py`) creates a small local database of malicious IPs.  
2. It generates a fake log file (`access.log`) containing IP addresses.  
3. The script checks every IP in the log file.  
4. It prints “ALERT” if the IP is malicious, or “OK” if it’s safe.

---

## 🖥️ How to Run
### 1️⃣ Install Python
Make sure Python 3 is installed.  
To check, run this command in terminal or PowerShell:
python --version

shell
Copy code

### 2️⃣ Run the script
python threat_checker.py

yaml
Copy code

---

## ✅ Expected Output
=== Threat Intelligence Feed Processor ===
Fake log file created: access.log
[OK] Safe IP: 192.168.1.1
[ALERT] Bad IP found: 185.191.171.12 (Phishing)
[OK] Safe IP: 8.8.8.8
[ALERT] Bad IP found: 206.189.123.45 (Malware)
=== Done ===

yaml
Copy code

---

## 📊 Output Screenshot
(Attach your terminal screenshot here if you want)

---

## 🏁 Project Outcome
This project shows how **cybersecurity analysts** use threat intelligence to detect **malicious IPs** from log files.

---
This repository contains:
- `threat_checker.py` → Main Python script  
- `access.log` → Sample log file  
- `threat_intel.db` → SQLite threat database  
- `report.pdf` → Final project report
