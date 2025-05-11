import json

def generate(report_data, output_file="sentinelsec_report.json"):
    print("\n[*] Generating report...")
    with open(output_file, 'w') as f:
        json.dump(report_data, f, indent=4)
    print(f"[+] Report saved to {output_file}")
