import ssl
import socket

def scan(domain):
    print(f"Checking TLS for: {domain}")
    try:
        context = ssl.create_default_context()
        with socket.create_connection((domain.replace("https://", ""), 443)) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as ssock:
                tls_version = ssock.version()
                print("TLS version used:", tls_version)
                if tls_version in ["TLSv1", "TLSv1.1"]:
                    return [f"[!] Weak TLS version detected: {tls_version}"]
                else:
                    return [f"[+] Secure TLS version in use: {tls_version}"]
    except Exception as e:
        return [f"[!] TLS check failed: {str(e)}"]
