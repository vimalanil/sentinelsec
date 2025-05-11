from scanner import traffic_analyzer, storage_checker, tls_inspector, crypto_checker
from utils import report_generator
import os

def main():
    print("[*] SentinelSec - Sensitive Data Exposure Scanner\n")

    # Get user input for the target URL
    url = input("[+] Enter the target URL (e.g., https://example.com): ").strip()
    print(f"\n[*] Scanning target: {url}\n")
    
    # Traffic analysis
    traffic_issues = traffic_analyzer.analyze()
    
    # Storage inspection (localStorage, cookies)
    storage_issues = storage_checker.inspect()
    
    # TLS analysis
    tls_issues = tls_inspector.scan(url)
    
    # Crypto check (only ask for file if needed)
    code_file = input("[+] Enter the path to the code file for crypto check (or press Enter to skip): ").strip()
    crypto_issues = []
    if code_file:
        if os.path.isfile(code_file):  # Only attempt scan if file exists
            crypto_issues = crypto_checker.scan_code_file(code_file)
        else:
            print("[!] Error: The specified file does not exist.")
    else:
        print("[*] Skipping crypto check (no file provided)")

    # Consolidate all findings into the full report
    full_report = {
        "target_url": url,
        "traffic_issues": traffic_issues,
        "storage_issues": storage_issues,
        "tls_issues": tls_issues,
        "crypto_issues": crypto_issues
    }

    # Generate and save the report
    report_generator.generate(full_report)

if __name__ == "__main__":
    main()
