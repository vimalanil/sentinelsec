import re

def scan_code_file(path):
    print(f"Scanning {path} for weak crypto...")
    with open(path, 'r') as file:
        code = file.read()

    weak_algos = ["md5", "sha1", "des", "rc4"]
    found = []

    for algo in weak_algos:
        if re.search(rf'\b{algo}\b', code.lower()):
            found.append(f"[!] Weak algorithm used: {algo.upper()}")
    
    return found
