# Regexes to detect sensitive data patterns
patterns = {
    "credit_card": r"(?:\d[ -]*?){13,16}",
    "email": r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+",
    "password_hint": r"(?i)(password|pwd)[^:]*[:=][^\n]+"
}
