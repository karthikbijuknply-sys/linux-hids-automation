# main.py - Simple HIDS with Continuous Monitoring
import re
import time
from datetime import datetime

def get_risk_level(count):
    if count >= 10:
        return "HIGH", "🚨"
    elif count >= 5:
        return "MEDIUM", "⚠️"
    else:
        return "LOW", "ℹ️"

def print_alert(ip, count):
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

def reports(attempts):
    """Save report to report.txt"""
    try:
        with open("report.txt", "w", encoding="utf-8") as f:
            f.write("====================================\n")
            f.write("     LINUX THREAT HUNTER REPORT\n")
            f.write("====================================\n")
            f.write(f"Generated At: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Total Suspicious IPs: {len(attempts)}\n\n")
            
            for ip, count in attempts.items():
                risk_level, _ = get_risk_level(count)
                f.write(f"Attacker IP     : {ip}\n")
                f.write(f"Failed Attempts : {count}\n")
                f.write(f"Risk Level      : {risk_level}\n")
                f.write("-" * 50 + "\n")
            
            f.write("\n=== End of Report ===\n")
            print("✅ Report saved to report.txt")
    except Exception as e:
        print(f"❌ Could not save report: {e}")
def analyze_logs():
    """Analyze the log file once"""
    try:
        with open("logs/auth.log", "r", encoding="utf-8") as f:
            lines = f.readlines()

        attempts = {}

        for line in lines:
            line = line.strip()
            if "Failed password" in line:
                match = re.search(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", line)
                if match:
                    ip = match.group()
                    attempts[ip] = attempts.get(ip, 0) + 1

        return attempts

    except Exception as e:
        print(f"Error reading log: {e}")
        return {}

def main():
    print("=== Simple HIDS Continuous Monitoring Started ===\n")
    print("Press Ctrl + C to stop monitoring\n")

    while True:   # This creates the continuous loop
        print(f"\n🔄 Checking logs at {datetime.now().strftime('%H:%M:%S')}...")

        attempts = analyze_logs()

        if attempts:
            print("🔊 GENERATING ALERTS...\n")
            for ip, count in attempts.items():
                print_alert(ip, count)
            reports(attempts)     
        else:
            print("✅ No suspicious activity detected.")

        print(f"Next check in 30 seconds... (Press Ctrl+C to stop)")
        time.sleep(30)   # Wait 30 seconds before next check

if __name__ == "__main__":
    main()
