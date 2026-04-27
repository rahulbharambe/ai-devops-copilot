def detect_pattern(logs):
    if "NullPointerException" in logs:
        return "High frequency issue in UserService.java"
    return "No major pattern detected"
