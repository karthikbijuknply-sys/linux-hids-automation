import re
import time
import os
from datetime import datetime

# Global state tracking database for malicious authentication metrics
ATTACK_TRACKER = {}

def get_risk_level(count):
    """Evaluates security posturing based on attack velocity thresholds."""
    if count >= 10:
        return "HIGH", "🚨"
    elif count >= 5:
        return "MEDIUM", "⚠️"
    else:
        return "LOW", "ℹ️"

def print_alert(ip, count):
    """Generates real-time, high-visibility console alert telemetry."""
    risk_level, emoji = get_risk_level(count)
    print("=" * 60)
    print(f"{emoji}  THREAT DETECTED  {emoji}")
    print("=" * 60)
    print(f"IP Address     : {ip}")
    print(f"Failed Attempts: {count}")
    print(f"Risk Level     : {risk_level}")
    print(f"Time           : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)
    print()

def generate_incident_report():
    """Compiles attack data and flushes a forensic audit log to report.txt."""
    try:
        with open("report.txt", "w", encoding="utf-8") as f:
            f.write("====================================\n")
            f.write("     LINUX DETECTION ENGINE REPORT\n")
            f.write("====================================\n")
            f.write(f"Generated At: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Total Suspicious IPs Monitored: {len(ATTACK_TRACKER)}\n\n")
            
            for ip, count in ATTACK_TRACKER.items():
                risk_level, _ = get_risk_level(count)
                f.write(f"Attacker IP     : {ip}\n")
                f.write(f"Failed Attempts : {count}\n")
                f.write(f"Risk Level      : {risk_level}\n")
                f.write("-" * 50 + "\n")
            
            f.write("\n=== End of Report ===\n")
            print("💾 Forensic incident report successfully written to -> report.txt")
    except Exception as e:
        print(f"❌ Critical Failure: Unable to write report.txt: {e}")

def parse_and_track_line(line, ip_regex):
    """Inspects log entries via Regex and updates persistent security states."""
    if "Failed password" in line:
        match = ip_regex.search(line)
        if match:
            ip = match.group()
            
            # Increment tracking metrics per unique source IP address
            ATTACK_TRACKER[ip] = ATTACK_TRACKER.get(ip, 0) + 1
            
            # Fire console security alert triggers
            print_alert(ip, ATTACK_TRACKER[ip])
            return True
    return False

def run_demonstration_engine(log_path):
    """Executes baseline ingestion of fake demo logs, then transitions to live tracking."""
    print(f"🎯 Target Log Collector Bound To: {log_path}\n")
    
    if not os.path.exists(log_path):
        print(f"❌ Error: Target file '{log_path}' missing. Please verify directory nesting.")
        return

    # Compile optimized Regex pattern matching schema for IPv4 extraction
    ip_regex = re.compile(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}")

    # Phase 1: Ingest and process existing simulated logs for demonstration validation
    print("🚀 PHASE 1: Executing Simulated Log Demonstration Ingestion...")
    print("-" * 60)
    
    new_data_found = False
    with open(log_path, "r", encoding="utf-8") as f:
        for line in f:
            if parse_and_track_line(line, ip_regex):
                new_data_found = True
        
        # Compile and generate report.txt immediately following baseline scan
        if new_data_found:
            generate_incident_report()
        else:
            print("ℹ️ Demonstration notice: logs/auth.log contained no brute-force failure strings.")

        print("-" * 60)
        print("🟢 PHASE 2: Transitioning to Persistent Active Monitoring.")
        print("Listening for incoming host anomalies... Press Ctrl+C to stop.")

        # Phase 2: Live tail streaming simulation loop monitoring for added lines
        try:
            while True:
                line = f.readline()
                
                # If no new line is generated, rest thread to protect host processing resources
                if not line:
                    time.sleep(1)
                    continue

                # Process newly appended line telemetry and rewrite report.txt state
                if parse_and_track_line(line, ip_regex):
                    generate_incident_report()

        except KeyboardInterrupt:
            print("\n🛑 Security platform shutdown sequence initiated by root administrator.")

def main():
    print("=============================================================")
    print("  Linux Detection Engine — Real-Time HIDS Platform Ingest    ")
    print("=============================================================")
    print("Initializing demonstration testing sequence...\n")
    
    target_log = "logs/auth.log"
    run_demonstration_engine(target_log)

if __name__ == "__main__":
    main()
