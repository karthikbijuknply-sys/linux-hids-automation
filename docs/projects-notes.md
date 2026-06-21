# Project Notes – Linux Threat Hunter

## Project Objective

Design and develop a Python-based security monitoring tool capable of detecting potential SSH brute-force attacks through the analysis of Linux authentication logs.

The project focuses on improving visibility into authentication-related security events and automating the identification of suspicious login activity.

---

## Security Problem

SSH services are frequently targeted by attackers attempting to gain unauthorized access through repeated password guessing attempts.

Manually reviewing authentication logs can be time-consuming and inefficient. This project explores how basic security automation can be used to identify suspicious authentication patterns and generate alerts for further investigation.

---

## Detection Workflow

```text
Authentication Logs
        │
        ▼
 Log File Analysis
        │
        ▼
 Failed Login Detection
        │
        ▼
 IP Address Extraction
        │
        ▼
 Attempt Aggregation
        │
        ▼
 Risk Classification
        │
        ▼
 Alert & Report Generation
```

---

## Concepts Applied

### Linux Log Analysis

Analyzed Linux authentication log entries to identify failed SSH login attempts and authentication-related events.

### Regular Expressions (Regex)

Implemented Regex pattern matching to extract IPv4 addresses from log entries.

### Threat Detection Logic

Developed logic to identify potentially malicious login activity based on repeated failed authentication attempts.

### Risk-Based Alerting

Implemented a simple severity model that classifies activity as LOW, MEDIUM, or HIGH risk based on the number of failed attempts.

### Security Monitoring

Created a continuous monitoring process that repeatedly analyzes log data and reports suspicious activity.

### Incident Reporting

Generated structured alerts and reports to assist with documenting detected security events.

---

## Technical Challenges

### Log Parsing

Designed logic to process authentication logs and identify relevant security events.

### Data Extraction

Implemented reliable extraction of source IP addresses from unstructured log entries.

### Threat Classification

Created a risk classification model that converts raw event counts into meaningful alert levels.

### Continuous Monitoring

Developed a monitoring loop capable of repeatedly analyzing log data at scheduled intervals.

---

## Key Learning Outcomes

* Linux authentication log analysis
* SSH brute-force attack detection
* Security event monitoring
* Python scripting for cybersecurity
* Regex-based pattern matching
* Risk-based alert generation
* Incident reporting fundamentals

---

## Future Enhancements

* Username extraction and profiling
* Time-window attack velocity analysis
* Email and webhook notifications
* Automated IP blocking using UFW/IPTables
* Database-backed event storage
* Security dashboard visualization
* Real-time log streaming
* SIEM integration
* Cloud-based log monitoring

---

## Project Outcome

Successfully developed a Python-based security monitoring solution capable of identifying suspicious SSH authentication activity and generating actionable security alerts.

Project Status: Completed ✅
