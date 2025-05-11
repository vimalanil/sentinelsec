# SentinelSec 🛡️  
**Sensitive Data Exposure Detection Tool (OWASP A3 Focus)**

SentinelSec is a Python-based tool designed to detect and report sensitive data exposure vulnerabilities in web applications. It scans for plaintext sensitive data, weak cryptographic usage, insecure storage, and outdated TLS/SSL configurations.

---

## 🔍 Features

- **Traffic Analysis** – Detects sensitive data like passwords, credit card numbers, etc., exposed in plaintext HTTP traffic.
- **Storage Inspection** – Analyzes browser cookies and local storage for unsafe data.
- **TLS/SSL Checker** – Validates TLS usage and identifies outdated/insecure versions.
- **Cryptographic Scanner** – Detects usage of weak algorithms like MD5 or SHA1 in codebases.
- **Report Generation** – Produces readable reports in JSON format with remediation suggestions.

---

## 🧪 Technologies Used

- Python 3
- Cryptography Library
- OpenSSL
- Requests
- Custom Regex
- Burp Suite (optional integration via API)

---

## 📂 Project Structure

```
sentinelsec/
├── main.py                  # Entry point
├── scanner/
│   ├── traffic_analyzer.py
│   ├── storage_checker.py
│   ├── tls_inspector.py
│   ├── crypto_checker.py
├── utils/
│   ├── regex_patterns.py
│   ├── report_generator.py
├── requirements.txt
├── README.md
```

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/vimalanil/sentinelsec.git
cd sentinelsec
```

### 2. Set Up a Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Tool
```bash
python3 main.py
```

---

## 📝 Sample Usage

```
[*] SentinelSec - Sensitive Data Exposure Scanner

[+] Enter the target URL (e.g., https://example.com): https://example.com

[*] Scanning target: https://example.com
Analyzing network traffic for sensitive data...
Inspecting local storage and cookies...
Checking TLS for: https://example.com
[+] Enter the path to the code file for crypto check (e.g., script.py): myapp.py
```

---

## 🛠️ Future Enhancements

- Browser automation with Selenium for real-time DOM inspection
- Integration with Burp Suite for deeper traffic interception
- Dashboard for viewing scan history and analytics

---

## 📄 License

This project is licensed under the MIT License.

---

## 🤝 Contributing

Feel free to fork the repo, raise issues, or submit pull requests.

---

## 👨‍💻 Author

- **Vimal Anil**  
  📧 vimalanil4442@gmail.com  
  🌐 [github.com/vimalanil](https://github.com/vimalanil)
