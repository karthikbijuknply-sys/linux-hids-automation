# Linux Threat Hunter – SSH Brute-Force Detection & Incident Reporting System

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge\&logo=python)
![Linux](https://img.shields.io/badge/Linux-Ubuntu-orange?style=for-the-badge\&logo=linux)
![Cybersecurity](https://img.shields.io/badge/Cybersecurity-Project-red?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)

## Overview

Linux Threat Hunter is a Python-based security monitoring tool designed to detect potential SSH brute-force attacks by analyzing Linux authentication logs.

The system continuously monitors authentication events, identifies failed login attempts, extracts source IP addresses using Regular Expressions (Regex), performs threat tracking, assigns risk severity levels, generates security alerts, and creates incident reports for security analysis.

This project was developed to gain hands-on experience in Linux security operations, log analysis, threat detection, and cybersecurity automation.

---

## Key Features

* Continuous log monitoring
* SSH brute-force attack detection
* Authentication log analysis
* Regex-based IP extraction
* Failed login attempt aggregation
* Risk severity classification
* Automated threat alerting
* Incident report generation
* Security monitoring automation

---

## Technology Stack

| Technology | Purpose                            |
| ---------- | ---------------------------------- |
| Python 3   | Core application development       |
| Linux      | Authentication log source          |
| Regex      | Pattern matching and IP extraction |
| auth.log   | Security event source              |
| Datetime   | Timestamp generation               |
| Time       | Continuous monitoring              |

---

## Detection Workflow

```text
Linux Authentication Logs
           │
           ▼
     Log Analysis
           │
           ▼
 Failed Login Detection
           │
           ▼
   Source IP Extraction
           │
           ▼
 Failed Attempt Tracking
           │
           ▼
 Risk Severity Analysis
           │
           ▼
 Alert & Report Generation
```

---

## Risk Classification Matrix

| Failed Attempts | Severity  | Action              |
| --------------- | --------- | ------------------- |
| 1 – 4           | 🟢 LOW    | Monitor Activity    |
| 5 – 9           | 🟡 MEDIUM | Investigate Source  |
| 10+             | 🔴 HIGH   | Immediate Attention |

---

## Sample Alert

```text
============================================================
🚨  THREAT DETECTED  🚨
============================================================
IP Address     : 185.220.101.4
Failed Attempts: 12
Risk Level     : HIGH
Time           : 2026-06-21 14:05:32
============================================================
```

---

## Project Structure

```text
hids-project/
├── main.py
├── README.md
├── logs/
│   └── auth.log
├── docs/
│   └── project-notes.md
├── screenshots/
├── report.txt
```

---

## Skills Demonstrated

* Python Programming
* Linux Fundamentals
* Cybersecurity Fundamentals
* Security Monitoring
* Threat Detection
* Log Analysis
* Regular Expressions (Regex)
* Incident Reporting
* Security Automation
* Problem Solving

---

## Learning Outcomes

Through this project, I gained practical experience in:

* Linux authentication log analysis
* SSH brute-force attack detection
* Threat monitoring and alert generation
* Regex-based data extraction
* Security event investigation
* Python-based security automation
* Incident reporting workflows

---

## Future Improvements

* Username extraction from authentication logs
* Time-window attack velocity analysis
* Email alert notifications
* Automated IP blocking using UFW/IPTables
* SQLite database integration
* Dashboard visualization
* Real-time log streaming
* Cloud-based log monitoring
* SIEM integration

---

## Project Status

✅ Completed

## Author

Karthik B

Aspiring Cybersecurity & Cloud Security Professional
